# OSC RIC Installation (H Relase

## Environment
Operating Sytem: Ubuntu 20.04


## Initial prerequisite

### Java 11 Installation
```sh
sudo apt-get install openjdk-11-jdk -y
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/
export PATH=$PATH:$JAVA_HOME/bin
java -version
```
### Maven Installation
```sh
sudo apt install maven -y
```
### Docker Installation
```sh
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get install docker-ce docker-ce-cli containerd.io -y
sudo docker run hello-world
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
```
### Basic tools installation
```sh
apt-get update
apt-get install -y git vim curl net-tools openssh-server python3-pip nfs-common
```
## Kubernetes and Helm Installation
>**Important:** Need to do it as root
>
>```sh
>sudo su
>```
>Then enter password
### Download RIC Source Code from OSC website
```sh
CD ~
git clone https://gerrit.o-ran-sc.org/r/ric-plt/ric-dep
```

### Modify the k8s instalation shell script

#### Adjust the docker and kube version
```sh
KUBEV="1.28.11"
KUBECNIV="0.7.5"
HELMV="3.14.4"
DOCKERV="20.10.21"
```
#### Change the kubernetes package GPG and url
From:
```sh
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
echo 'deb http://apt.kubernetes.io/ kubernetes-xenial main' > /etc/apt/sources.list.d/kubernetes.list
```
To:
```
mkdir /etc/apt/keyrings
echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.28/deb/ /" | sudo tee /etc/apt/sources.list.d/kubernetes.list
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.28/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
```

**Full script used in this installation:**
```sh
#!/bin/bash -x
#
################################################################################
#   Copyright (c) 2019 AT&T Intellectual Property.                             #
#   Copyright (c) 2022 Nokia.                                                  #
#                                                                              #
#   Licensed under the Apache License, Version 2.0 (the "License");            #
#   you may not use this file except in compliance with the License.           #
#   You may obtain a copy of the License at                                    #
#                                                                              #
#       http://www.apache.org/licenses/LICENSE-2.0                             #
#                                                                              #
#   Unless required by applicable law or agreed to in writing, software        #
#   distributed under the License is distributed on an "AS IS" BASIS,          #
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.   #
#   See the License for the specific language governing permissions and        #
#   limitations under the License.                                             #
################################################################################


usage() {
    echo "Usage: $0 [ -k <k8s version> -d <docker version> -e <helm version> -c <cni-version>" 1>&2;

    echo "k:    kubernetes version" 1>&2;
    echo "c:    kubernetes CNI  version" 1>&2;
    echo "d:    docker version" 1>&2;
    echo "e:    helm version" 1>&2;
    exit 1;
}


wait_for_pods_running () {
  NS="$2"
  CMD="kubectl get pods --all-namespaces "
  if [ "$NS" != "all-namespaces" ]; then
    CMD="kubectl get pods -n $2 "
  fi
  KEYWORD="Running"
  if [ "$#" == "3" ]; then
    KEYWORD="${3}.*Running"
  fi

  CMD2="$CMD | grep \"$KEYWORD\" | wc -l"
  NUMPODS=$(eval "$CMD2")
  echo "waiting for $NUMPODS/$1 pods running in namespace [$NS] with keyword [$KEYWORD]"
  while [  $NUMPODS -lt $1 ]; do
    sleep 5
    NUMPODS=$(eval "$CMD2")
    echo "> waiting for $NUMPODS/$1 pods running in namespace [$NS] with keyword [$KEYWORD]"
  done 
}


start_ipv6_if () {
  IPv6IF="$1"
  if ifconfig -a $IPv6IF; then
    echo "" >> /etc/network/interfaces.d/50-cloud-init.cfg
    echo "allow-hotplug ${IPv6IF}" >> /etc/network/interfaces.d/50-cloud-init.cfg
    echo "iface ${IPv6IF} inet6 auto" >> /etc/network/interfaces.d/50-cloud-init.cfg
    ifconfig ${IPv6IF} up
  fi
}

KUBEV="1.28.11"
KUBECNIV="0.7.5"
HELMV="3.14.4"
DOCKERV="20.10.21"

echo running ${0}
while getopts ":k:d:e:n:c" o; do
    case "${o}" in
    e)	
       HELMV=${OPTARG}
        ;;
    d)
       DOCKERV=${OPTARG}
        ;;
    k)
       KUBEV=${OPTARG}
       ;;
    c)
       KUBECNIV=${OPTARG}
       ;;
    *)
       usage
       ;;
    esac
done

if [[ ${HELMV} == 2.* ]]; then
  echo "helm 2 ("${HELMV}")not supported anymore" 
  exit -1
fi

set -x
export DEBIAN_FRONTEND=noninteractive
echo "$(hostname -I) $(hostname)" >> /etc/hosts
printenv

IPV6IF=""

rm -rf /opt/config
mkdir -p /opt/config
echo "" > /opt/config/docker_version.txt
echo "1.16.0" > /opt/config/k8s_version.txt
echo "0.7.5" > /opt/config/k8s_cni_version.txt
echo "3.14.4" > /opt/config/helm_version.txt
echo "$(hostname -I)" > /opt/config/host_private_ip_addr.txt
echo "$(curl ifconfig.co)" > /opt/config/k8s_mst_floating_ip_addr.txt
echo "$(hostname -I)" > /opt/config/k8s_mst_private_ip_addr.txt
echo "__mtu__" > /opt/config/mtu.txt
echo "__cinder_volume_id__" > /opt/config/cinder_volume_id.txt
echo "$(hostname)" > /opt/config/stack_name.txt

ISAUX='false'
if [[ $(cat /opt/config/stack_name.txt) == *aux* ]]; then
  ISAUX='true'
fi

modprobe -- ip_vs
modprobe -- ip_vs_rr
modprobe -- ip_vs_wrr
modprobe -- ip_vs_sh
modprobe -- nf_conntrack_ipv4
modprobe -- nf_conntrack_ipv6
modprobe -- nf_conntrack_proto_sctp

if [ ! -z "$IPV6IF" ]; then
  start_ipv6_if $IPV6IF
fi

SWAPFILES=$(grep swap /etc/fstab | sed '/^[ \t]*#/ d' | sed 's/[\t ]/ /g' | tr -s " " | cut -f1 -d' ')
if [ ! -z $SWAPFILES ]; then
  for SWAPFILE in $SWAPFILES
  do
    if [ ! -z $SWAPFILE ]; then
      echo "disabling swap file $SWAPFILE"
      if [[ $SWAPFILE == UUID* ]]; then
        UUID=$(echo $SWAPFILE | cut -f2 -d'=')
        swapoff -U $UUID
      else
        swapoff $SWAPFILE
      fi
      sed -i "\%$SWAPFILE%d" /etc/fstab
    fi
  done
fi


echo "### Docker version  = "${DOCKERV}
echo "### k8s version     = "${KUBEV}
echo "### helm version    = "${HELMV}
echo "### k8s cni version = "${KUBECNIV}

#KUBEVERSION="${KUBEV}-00"
CNIVERSION="${KUBECNIV}-00"
DOCKERVERSION="${DOCKERV}"

UBUNTU_RELEASE=$(lsb_release -r | sed 's/^[a-zA-Z:\t ]\+//g')
if [[ ${UBUNTU_RELEASE} == 16.* ]]; then
  echo "Installing on Ubuntu $UBUNTU_RELEASE (Xenial Xerus) host"
  if [ ! -z "${DOCKERV}" ]; then
    DOCKERVERSION="${DOCKERV}-0ubuntu1~16.04.5"
  fi
elif [[ ${UBUNTU_RELEASE} == 18.* ]]; then
  echo "Installing on Ubuntu $UBUNTU_RELEASE (Bionic Beaver)"
  if [ ! -z "${DOCKERV}" ]; then
    DOCKERVERSION="${DOCKERV}-0ubuntu1~18.04.4"
  fi
elif [[ ${UBUNTU_RELEASE} == 20.* ]]; then
  echo "Installing on Ubuntu $UBUNTU_RELEASE (Focal Fossal)"
  if [ ! -z "${DOCKERV}" ]; then
    DOCKERVERSION="${DOCKERV}-0ubuntu1~20.04.2"  # 20.10.21-0ubuntu1~20.04.2
  fi
else
  echo "Unsupported Ubuntu release ($UBUNTU_RELEASE) detected.  Exit."
fi

echo "docker version to use = "${DOCKERVERSION}

#curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
#echo 'deb http://apt.kubernetes.io/ kubernetes-xenial main' > /etc/apt/sources.list.d/kubernetes.list

mkdir /etc/apt/keyrings
echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.28/deb/ /" | sudo tee /etc/apt/sources.list.d/kubernetes.list
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.28/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

mkdir -p /etc/apt/apt.conf.d
echo "APT::Acquire::Retries \"3\";" > /etc/apt/apt.conf.d/80-retries

apt-get update
RES=$(apt-get install -y  curl jq netcat make ipset moreutils 2>&1)
if [[ $RES == */var/lib/dpkg/lock* ]]; then
  echo "Fail to get dpkg lock.  Wait for any other package installation"
  echo "process to finish, then rerun this script"
  exit -1
fi

APTOPTS="--allow-downgrades --allow-change-held-packages --allow-unauthenticated --ignore-hold "

for PKG in kubeadm docker.io; do
  INSTALLED_VERSION=$(dpkg --list |grep ${PKG} |tr -s " " |cut -f3 -d ' ')
  if [ ! -z ${INSTALLED_VERSION} ]; then
    if [ "${PKG}" == "kubeadm" ]; then
      kubeadm reset -f
      rm -rf ~/.kube
      apt-get -y $APTOPTS remove kubeadm kubelet kubectl kubernetes-cni
    else
      apt-get -y $APTOPTS remove "${PKG}"
    fi
  fi
done
apt-get -y autoremove

if [ -z ${DOCKERVERSION} ]; then
  apt-get install -y $APTOPTS docker.io
else
  apt-get install -y $APTOPTS docker.io=${DOCKERVERSION}
fi
cat > /etc/docker/daemon.json <<EOF
{
  "exec-opts": ["native.cgroupdriver=systemd"],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m"
  },
  "storage-driver": "overlay2"
}
EOF
mkdir -p /etc/systemd/system/docker.service.d
systemctl enable docker.service
systemctl daemon-reload
systemctl restart docker

if [ -z ${CNIVERSION} ]; then
  apt-get install -y $APTOPTS kubernetes-cni
else
  apt-get install -y $APTOPTS kubernetes-cni=${CNIVERSION}
fi

if [ -z ${KUBEVERSION} ]; then
  apt-get install -y $APTOPTS kubeadm kubelet kubectl
else
  apt-get install -y $APTOPTS kubeadm=${KUBEVERSION} kubelet=${KUBEVERSION} kubectl=${KUBEVERSION}
fi

apt-mark hold docker.io kubernetes-cni kubelet kubeadm kubectl


kubeadm config images pull --kubernetes-version=${KUBEV}


NODETYPE="master"
if [ "$NODETYPE" == "master" ]; then

  if [[ ${KUBEV} == 1.13.* ]]; then
    cat <<EOF >/root/config.yaml
apiVersion: kubeadm.k8s.io/v1alpha3
kubernetesVersion: v${KUBEV}
kind: ClusterConfiguration
apiServerExtraArgs:
  feature-gates: SCTPSupport=true
networking:
  dnsDomain: cluster.local
  podSubnet: 10.244.0.0/16
  serviceSubnet: 10.96.0.0/12
---
apiVersion: kubeproxy.config.k8s.io/v1alpha1
kind: KubeProxyConfiguration
mode: ipvs
EOF

  elif [[ ${KUBEV} == 1.14.* ]]; then
    cat <<EOF >/root/config.yaml
apiVersion: kubeadm.k8s.io/v1beta1
kubernetesVersion: v${KUBEV}
kind: ClusterConfiguration
apiServerExtraArgs:
  feature-gates: SCTPSupport=true
networking:
  dnsDomain: cluster.local
  podSubnet: 10.244.0.0/16
  serviceSubnet: 10.96.0.0/12
---
apiVersion: kubeproxy.config.k8s.io/v1alpha1
kind: KubeProxyConfiguration
mode: ipvs
EOF
  elif [[ ${KUBEV} == 1.15.* ]] || [[ ${KUBEV} == 1.16.* ]] || [[ ${KUBEV} == 1.18.* ]]; then
    cat <<EOF >/root/config.yaml
apiVersion: kubeadm.k8s.io/v1beta2
kubernetesVersion: v${KUBEV}
kind: ClusterConfiguration
apiServer:
  extraArgs:
    feature-gates: SCTPSupport=true
networking:
  dnsDomain: cluster.local
  podSubnet: 10.244.0.0/16
  serviceSubnet: 10.96.0.0/12
---
apiVersion: kubeproxy.config.k8s.io/v1alpha1
kind: KubeProxyConfiguration
mode: ipvs
EOF
  elif [[ ${KUBEV} == 1.28.* ]] ; then
    echo "Do Nothing for now."
    else
    echo "Unsupported Kubernetes version requested.  Bail."
    exit
  fi

  cat <<EOF > /root/rbac-config.yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: tiller
  namespace: kube-system
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: tiller
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
  - kind: ServiceAccount
    name: tiller
    namespace: kube-system
EOF

if [[ ${KUBEV} == 1.28.11 ]]; then
  kubeadm init --pod-network-cidr=10.244.0.0/16
  mkdir -p /run/flannel
cat <<EOF > /run/flannel/subnet.env
FLANNEL_NETWORK=10.244.0.0/16
FLANNEL_SUBNET=10.244.0.1/24
FLANNEL_MTU=1450
FLANNEL_IPMASQ=true
EOF
else  
  kubeadm init --config /root/config.yaml
fi

  cd /root
  rm -rf .kube
  mkdir -p .kube
  cp -i /etc/kubernetes/admin.conf /root/.kube/config
  chown root:root /root/.kube/config
  export KUBECONFIG=/root/.kube/config
  echo "KUBECONFIG=${KUBECONFIG}" >> /etc/environment

  kubectl get pods --all-namespaces

if [[ ${KUBEV} == 1.28.11 ]]; then
  kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
else
  # we refer to version 0.18.1 because later versions use namespace kube-flannel instead of kube-system TODO
  kubectl apply -f "https://raw.githubusercontent.com/flannel-io/flannel/v0.18.1/Documentation/kube-flannel.yml"
fi

if [[ ${KUBEV} == 1.28.11 ]]; then
  wait_for_pods_running 7 kube-system
  wait_for_pods_running 1 kube-flannel
  kubectl taint nodes --all node-role.kubernetes.io/control-plane:NoSchedule-
else
  wait_for_pods_running 8 kube-system
  kubectl taint nodes --all node-role.kubernetes.io/master-
fi


  HELMV=$(cat /opt/config/helm_version.txt)
  HELMVERSION=${HELMV}
  if [ ! -e helm-v${HELMVERSION}-linux-amd64.tar.gz ]; then
    wget https://get.helm.sh/helm-v${HELMVERSION}-linux-amd64.tar.gz
  fi
  cd /root && rm -rf Helm && mkdir Helm && cd Helm
  tar -xvf ../helm-v${HELMVERSION}-linux-amd64.tar.gz
  mv linux-amd64/helm /usr/local/bin/helm

  cd /root

  rm -rf /root/.helm
#  if [[ ${KUBEV} == 1.16.* ]]; then
#    if [[ ${HELMVERSION} == 2.* ]]; then
#       helm init --service-account tiller --override spec.selector.matchLabels.'name'='tiller',spec.selector.matchLabels.'app'='helm' --output yaml > /tmp/helm-init.yaml
#       sed 's@apiVersion: extensions/v1beta1@apiVersion: apps/v1@' /tmp/helm-init.yaml > /tmp/helm-init-patched.yaml
#       kubectl apply -f /tmp/helm-init-patched.yaml
#    fi
#  else
#    if [[ ${HELMVERSION} == 2.* ]]; then
#       helm init --service-account tiller
#    fi
#  fi
#  if [[ ${HELMVERSION} == 2.* ]]; then
#     helm init -c
#     export HELM_HOME="$(pwd)/.helm"
#     echo "HELM_HOME=${HELM_HOME}" >> /etc/environment
#  fi

  while ! helm version; do
    echo "Waiting for Helm to be ready"
    sleep 15
  done

  echo "Preparing a master node (lower ID) for using local FS for PV"
  PV_NODE_NAME=$(kubectl get nodes |grep master | cut -f1 -d' ' | sort | head -1)
  kubectl label --overwrite nodes $PV_NODE_NAME local-storage=enable
  if [ "$PV_NODE_NAME" == "$(hostname)" ]; then
    mkdir -p /opt/data/dashboard-data
  fi

  echo "Done with master node setup"
fi


if [[ ! -z "" && ! -z "" ]]; then 
  echo " " >> /etc/hosts
fi
if [[ ! -z "" && ! -z "" ]]; then 
  echo " " >> /etc/hosts
fi
if [[ ! -z "" && ! -z "helm.ricinfra.local" ]]; then 
  echo " helm.ricinfra.local" >> /etc/hosts
fi

if [[ "1" -gt "100" ]]; then
  cat <<EOF >/etc/ca-certificates/update.d/helm.crt

EOF
fi

if [[ "1" -gt "100" ]]; then
  mkdir -p /etc/docker/certs.d/:
  cat <<EOF >/etc/docker/ca.crt

EOF
  cp /etc/docker/ca.crt /etc/docker/certs.d/:/ca.crt

  service docker restart
  systemctl enable docker.service
  docker login -u  -p  :
  docker pull :/whoami:0.0.1
fi
```

### Run the installation script inside ric-dep/bin/
```sh
sudo ./install_k8s_and_helm.sh
sudo ./install_common_templates_to_helm.sh
sudo ./setup-ric-common-template
```

## RIC Installation
### Edit Deployment Config
#### xApp Manager
```
nano ric-dep/helm/appmgr/resources/appmgr.yaml
```
Change the log level to 4
```yaml
#...

"xapp":
  #Namespace to install xAPPs
  "namespace": __XAPP_NAMESPACE__
  "tarDir": "/tmp"
  "schema": "descriptors/schema.json"
  "config": "config/config-file.json"
  "tmpConfig": "/tmp/config-file.json"
"loglevel" :  4
```

#### A1 Mediator
1. Change loglevel.txt
    
    ```sh
    nano ric-dep/helm/a1mediator/templates/config.yaml
    ```

    ```yaml
    data:
        local.rt: |
            newrt|start
            mse|20010|SUBID|service-ricxapp-admctrl-rmr.{{ include "common.namespace.xapp" . }}:4563
            rte|20011|{{ include "common.servicename.a1mediator.rmr" . }}.{{ include "common.namespace.platform" . }}:{{ include "common.serviceport.a1mediator.rmr.data" . }}
            rte|20012|{{ include "common.servicename.a1mediator.rmr" . }}.{{ include "common.namespace.platform" . }}:{{ include "common.serviceport.a1mediator.rmr.data" . }}
            newrt|end
        #=============THIS ONE==========================
        loglevel.txt: |
                log-level: {{ .Values.a1mediator.loglevel }} 
        #===============================================
    ```

2. Change loglevel
    ```sh
    nano ric-dep/helm/a1mediator/values.yaml
    ```
    ```yaml
    a1mediator:
    replicaCount: 1
    imagePullPolicy: IfNotPresent
    image:
        name: ric-plt-a1
        tag: 2.5.0
        registry: "nexus3.o-ran-sc.org:10002/o-ran-sc"
    ...
    ...
    rmr_timeout_config:
        a1_rcv_retry_times: 20
        ins_del_no_resp_ttl: 5
        ins_del_resp_ttl: 10
    #==================THIS ONE=====================
    loglevel: "DEBUG"
    #===============================================
    ```

3. Add ENV for A1EI
    ```sh
    nano ric-dep/helm/a1mediator/templates/env.yaml
    ```
    ```yaml
    data:
        RMR_RTG_SVC: {{ include "common.serviceport.a1mediator.rmr.route" . | quote }}
        PYTHONUNBUFFERED: "1"
        A1_RMR_RETRY_TIMES: "{{ .Values.a1mediator.rmr_timeout_config.a1_rcv_retry_times }}"
        # this sets the source field in messages from a1 to point back to a1s service name, rather than it's random pod name
        # In my private testing, this is needed! however it wasn't here in it/dep. If routing doesn't work, possibly add this back.
        RMR_SRC_ID: {{ include "common.servicename.a1mediator.rmr" . }}.{{ include "common.namespace.platform" . }}
        INSTANCE_DELETE_NO_RESP_TTL: "{{ .Values.a1mediator.rmr_timeout_config.ins_del_no_resp_ttl }}"
        INSTANCE_DELETE_RESP_TTL: "{{ .Values.a1mediator.rmr_timeout_config.ins_del_resp_ttl }}"
        CONFIG_MAP_NAME: "/opt/route/loglevel.txt"
        #===========================THIS ONE===========================
        ECS_SERVICE_HOST: {{ .Values.a1mediator.a1ei.ecs_ip_port }}
        #==============================================================
    ```
4. Edit values.yaml
    ```sh
    nano ric-dep/helm/a1mediator/values.yaml
    ```
    ```yaml
    a1mediator:
    replicaCount: 1
    imagePullPolicy: IfNotPresent
    image:
        name: ric-plt-a1
        tag: 2.5.0
        registry: "nexus3.o-ran-sc.org:10002/o-ran-sc"

    # Service ports are now defined in
    # ric-common/Common-Template/helm/ric-common/templates/_ports.tpl file.
    # If need to change a service port, make the code change necessary, then
    # update the _ports.tpl file with the new port number.

    # these are ENV variables that A1 takes; see docs
    rmr_timeout_config:
        a1_rcv_retry_times: 20
        ins_del_no_resp_ttl: 5
        ins_del_resp_ttl: 10
    loglevel: "DEBUG"
    #====================THIS oNE==============================
    a1ei:
        ecs_ip_port: "http://<ecs_host>:<ecs_port>"
    #==========================================================

    ```
#### E2 Termination
1. Change loglevel to debug
    ```sh
    nano ric-dep/helm/e2term/values.yaml
    ```
    ```yaml
    health:
        liveness:
        command: "ip=`hostname -i`;export RMR_SRC_ID=$ip;/opt/e2/rmr_probe -h $ip"
        initialDelaySeconds: 10
        periodSeconds: 10
        enabled: true

        readiness:
        command: "ip=`hostname -i`;export RMR_SRC_ID=$ip;/opt/e2/rmr_probe -h $ip"
        initialDelaySeconds: 120
        periodSeconds: 60
        enabled: true
    #===============THIS oNE=======================
    loglevel: 4
    #==============================================
    common_env_variables:
    ConfigMapName: "/etc/config/log-level"
    ServiceName: "RIC_E2_TERM"
    ```
2. Modify container deployment
   ```sh
   nano ric-dep/helm/e2term/templates/deployment.yaml
   ```
   ```yaml
   spec:
      hostname: {{ include "common.name.e2term" $topCtx }}-{{ $key }}
      hostNetwork: {{ .hostnetworkmode }}
      dnsPolicy: ClusterFirstWithHostNet
      imagePullSecrets:
        - name: {{ include "common.dockerregistry.credential" $imagectx }}
      {{- with .nodeselector }}
      nodeSelector: {{ toYaml . | trim | nindent 8 -}}
      {{- end }}
      containers:
      #================================THIS ONE=======================================
        - name: {{ include "common.containername.e2term" $topCtx }}
          image: {{ include "common.dockerregistry.url" $imagectx }}/{{ .image.name }}:{{ .image.tag }}
          imagePullPolicy: {{ include "common.dockerregistry.pullpolicy" $pullpolicyctx }}
      #===============================================================================
          volumeMounts:
          - mountPath: "{{ $common_env.ConfigMapName }}"
            name: local-router-file
            subPath: log-level
           #...
            #...
    ```
3. Add log-level section
    ```sh
    nano ric-dep/helm/e2term/templates/configmap.yaml
    ```
    ```yaml
        apiVersion: v1
    kind: ConfigMap
    metadata:
    name: {{ include "common.configmapname.e2term" $topCtx }}-router-configmap
    namespace: {{ include "common.namespace.platform" $topCtx }}
    data:
    #====================HERE=================================
    log-level: |
        {{- if hasKey .Values "loglevel" }}
        log-level: {{ .Values.loglevel }}
        {{- else }}
        log-level: 1
        {{- end }}
    #====================HERE=================================

    rmr_verbose: |
        0
    router.txt: |
        newrt|start
        rte|1080|{{ include "common.servicename.e2mgr.rmr" $topCtx }}.{{ include "common.namespace.platform" $topCtx }}:{{ include "common.serviceport.e2mgr.rmr.data" $topCtx }}
        rte|1090|
    {{- $frist := true -}}
    {{- range keys .Values.e2term -}}
    {{- if $frist -}}
    {{- $frist = false -}}
    {{- else -}}
    ;
    ```
#### Subscription Manager

1. Change log level

    ```sh
    nano ric-dep/helm/e2term/templates/configmap.yaml
    ```
    ```yaml
    data:
    # FQDN and port info of rtmgr
    submgrcfg: |
        "local":
        "host": ":8080"
        #============================THIS ONE===========================
        "logger":
            "level": 4
        #===============================================================

        "rmr":
            "protPort" : "tcp:4560"
            "maxSize": 8192
            "numWorkers": 1
    ```
2. Add new port for subscription in service file
   
     ```sh
    nano ric-dep/helm/submgr/templates/service-http.yaml
    ```
    ```yaml
    spec:
    selector:
        app: {{ include "common.namespace.platform" . }}-{{ include "common.name.submgr" . }}
        release: {{ .Release.Name }}
    clusterIP: None
    ports:
    - name: http
        port: {{ include "common.serviceport.submgr.http" . }}
        protocol: TCP
        targetPort: http
    #========================HERE==============================
    - name: subscription
        port: 8088
        protocol: TCP
        targetPort: 8088
    #==========================================================

    ```
3. Add new port for subscription in deployment file
    ```sh
    nano ric-dep/helm/submgr/templates/deployment.yaml
    ```
    ```yaml
      containers:
        - name: {{ include "common.containername.submgr" . }}
          image: {{ include "common.dockerregistry.url" $imagectx }}/{{ .Values.submgr.image.name }}:{{ .Values.submgr.image.tag }}
          imagePullPolicy: {{ include "common.dockerregistry.pullpolicy" $pullpolicyctx }}
          command: ["/submgr"]
          args: ["-f", "/cfg/submgr-config.yaml"]
          envFrom:
            - configMapRef:
                name: {{ include "common.configmapname.submgr" . }}-env
            - configMapRef:
                name: {{ include "common.configmapname.dbaas" . }}-appconfig
          ports:
            - name: http
              containerPort: {{ include "common.serviceport.submgr.http" . }}
              protocol: TCP
            - name: rmrroute
              containerPort: {{ include "common.serviceport.submgr.rmr.route" . }}
              protocol: TCP
            - name: rmrdata
              containerPort: {{ include "common.serviceport.submgr.rmr.data" . }}
              protocol: TCP
            #==========================HERE==============================
            - name: subscription
              containerPort: 8088
              protocol: TCP
            #============================================================

          volumeMounts:
            - name: config-volume
              mountPath: /cfg
          livenessProbe:
            httpGet:
              path: ric/v1/health/alive
              port: 8080
            initialDelaySeconds: 5
            periodSeconds: 15
          readinessProbe:
            httpGet:
              path: ric/v1/health/ready
              port: 8080
    ```

#### Routing Manager
1. Routing path config
    ```sh
    nano ric-dep/helm/rtmgr/templates/config.yaml
    ```
    ```yaml
       "messagetypes": [
          "RIC_HEALTH_CHECK_REQ=100",
          "RIC_HEALTH_CHECK_RESP=101",
          "RIC_ALARM=110",
          "RIC_ALARM_QUERY=111",
          "RIC_SCTP_CONNECTION_FAILURE=1080",
          "E2_TERM_INIT=1100",
          "E2_TERM_KEEP_ALIVE_REQ=1101",
          "E2_TERM_KEEP_ALIVE_RESP=1102",
          "RIC_SCTP_CLEAR_ALL=1090",
          "RAN_CONNECTED=1200",
          "RAN_RESTARTED=1210",
          "RAN_RECONFIGURED=1220",
          "RIC_ENB_LOAD_INFORMATION=10020",
          "RIC_SN_STATUS_TRANSFER=10040",
          "RIC_UE_CONTEXT_RELEASE=10050",
          "RIC_X2_SETUP_REQ=10060",
          "RIC_X2_SETUP_RESP=10061",
          "RIC_X2_SETUP_FAILURE=10062",
          "RIC_X2_RESET=10070",
          "RIC_X2_RESET_RESP=10071",
          "RIC_ENB_CONF_UPDATE=10080",
          "RIC_ENB_CONF_UPDATE_ACK=10081",
          "RIC_ENB_CONF_UPDATE_FAILURE=10082",
          "RIC_RES_STATUS_REQ=10090",
          "RIC_RES_STATUS_RESP=10091",
          "RIC_RES_STATUS_FAILURE=10092",
          "RIC_SGNB_ADDITION_REQ=10270",
          "RIC_SGNB_ADDITION_ACK=10271",
          "RIC_SGNB_ADDITION_REJECT=10272",
          "RIC_SGNB_RECONF_COMPLETE=10280",
          "RIC_SGNB_MOD_REQUEST=10290",
          "RIC_SGNB_MOD_REQUEST_ACK=10291",
          "RIC_SGNB_MOD_REQUEST_REJ=10292",
          "RIC_SGNB_MOD_REQUIRED=10300",
          "RIC_SGNB_MOD_CONFIRM=10301",
          "RIC_SGNB_MOD_REFUSE=10302",
          "RIC_SGNB_RELEASE_REQUEST=10310",
          "RIC_SGNB_RELEASE_REQUEST_ACK=10311",
          "RIC_SGNB_RELEASE_REQUIRED=10320",
          "RIC_SGNB_RELEASE_CONFIRM=10321",
          "RIC_RRC_TRANSFER=10350",
          "RIC_ENDC_X2_SETUP_REQ=10360",
          "RIC_ENDC_X2_SETUP_RESP=10361",
          "RIC_ENDC_X2_SETUP_FAILURE=10362",
          "RIC_ENDC_CONF_UPDATE=10370",
          "RIC_ENDC_CONF_UPDATE_ACK=10371",
          "RIC_ENDC_CONF_UPDATE_FAILURE=10372",
          "RIC_SECONDARY_RAT_DATA_USAGE_REPORT=10380",
          "RIC_E2_SETUP_REQ=12001",
          "RIC_E2_SETUP_RESP=12002",
          "RIC_E2_SETUP_FAILURE=12003",
          "RIC_ERROR_INDICATION=12007",
          "RIC_SUB_REQ=12010",
          "RIC_SUB_RESP=12011",
          "RIC_SUB_FAILURE=12012",
          "RIC_SUB_DEL_REQ=12020",
          "RIC_SUB_DEL_RESP=12021",
          "RIC_SUB_DEL_FAILURE=12022",
          "RIC_SUB_DEL_REQUIRED=12023",
          "RIC_CONTROL_REQ=12040",
          "RIC_CONTROL_ACK=12041",
          "RIC_CONTROL_FAILURE=12042",
          "RIC_INDICATION=12050",
          "A1_POLICY_REQ=20010",
          "A1_POLICY_RESP=20011",
          "A1_POLICY_QUERY=20012",
          "TS_UE_LIST=30000",
          "TS_QOE_PRED_REQ=30001",
          "TS_QOE_PREDICTION=30002",
          "TS_ANOMALY_UPDATE=30003",
          "TS_ANOMALY_ACK=30004",
          "MC_REPORT=30010",
          "DCAPTERM_RTPM_RMR_MSGTYPE=33001",
          "DCAPTERM_GEO_RMR_MSGTYPE=33002",
          "RIC_SERVICE_UPDATE=12030",
          "RIC_SERVICE_UPDATE_ACK=12031",
          "RIC_SERVICE_UPDATE_FAILURE=12032",
          "RIC_E2NODE_CONFIG_UPDATE=12070",
          "RIC_E2NODE_CONFIG_UPDATE_ACK==12071",
          "RIC_E2NODE_CONFIG_UPDATE_FAILURE=12072",
          "RIC_E2_RESET_REQ=12004",
          "RIC_E2_RESET_RESP=12005",
          #========================ADD THIS===========================
          "A1_EI_QUERY_ALL=20013",
          "A1_EI_QUERY_ALL_RESP=20014",
          "A1_EI_CREATE_JOB=20015",
          "A1_EI_CREATE_JOB_RESP=20016",
          "A1_EI_DATA_DELIVERY=20017",
          #========================ADD THIS===========================
          ]
    ```

    ```yaml
       "PlatformRoutes": [
         { 'messagetype': 'RIC_SUB_REQ', 'senderendpoint': 'SUBMAN', 'subscriptionid': -1, 'endpoint': '', 'meid': '%meid'},
         { 'messagetype': 'RIC_SUB_DEL_REQ', 'senderendpoint': 'SUBMAN', 'subscriptionid': -1,'endpoint': '', 'meid': '%meid'},
         { 'messagetype': 'RIC_SUB_RESP', 'senderendpoint': '', 'subscriptionid': -1, 'endpoint': 'SUBMAN', 'meid': ''},
         { 'messagetype': 'RIC_SUB_DEL_RESP', 'senderendpoint': '', 'subscriptionid': -1, 'endpoint': 'SUBMAN', 'meid': ''},
         { 'messagetype': 'RIC_SUB_FAILURE', 'senderendpoint': '', 'subscriptionid': -1, 'endpoint': 'SUBMAN', 'meid': ''},
         { 'messagetype': 'RIC_SUB_DEL_FAILURE', 'senderendpoint': '', 'subscriptionid': -1, 'endpoint': 'SUBMAN', 'meid': ''},
         { 'messagetype': 'RIC_SUB_DEL_REQUIRED', 'senderendpoint': '', 'subscriptionid': -1, 'endpoint': 'SUBMAN', 'meid': ''},
         { 'messagetype': 'RIC_X2_SETUP_REQ', 'senderendpoint': 'E2MAN', 'subscriptionid': -1, 'endpoint': '', 'meid': '%meid'},
         { 'messagetype': 'RIC_X2_RESET', 'senderendpoint': 'E2MAN', 'subscriptionid': -1, 'endpoint': '', 'meid': '%meid'},
         { 'messagetype': 'RIC_X2_RESET_RESP', 'senderendpoint': 'E2MAN', 'subscriptionid': -1, 'endpoint': '', 'meid': '%meid'},
         { 'messagetype': 'RIC_ENDC_X2_SETUP_REQ', 'senderendpoint': 'E2MAN', 'subscriptionid': -1, 'endpoint': '', 'meid': '%meid'},
         { 'messagetype': 'RIC_ENB_CONF_UPDATE_ACK', 'senderendpoint': 'E2MAN', 'subscriptionid': -1, 'endpoint': '', 'meid': '%meid'},
         { 'messagetype': 'RIC_ENB_CONF_UPDATE_FAILURE', 'senderendpoint': 'E2MAN', 'subscriptionid': -1, 'endpoint': '', 'meid': '%meid'},
         { 'messagetype': 'RIC_ENDC_CONF_UPDATE_ACK', 'senderendpoint': 'E2MAN', 'subscriptionid': -1, 'endpoint': '', 'meid': '%meid'},
         { 'messagetype': 'RIC_ENDC_CONF_UPDATE_FAILURE', 'senderendpoint': 'E2MAN', 'subscriptionid': -1, 'endpoint': '', 'meid': '%meid'},
         { 'messagetype': 'RIC_E2_SETUP_REQ', 'senderendpoint': '', 'subscriptionid': -1, 'endpoint': 'E2MAN', 'meid': ''},
         { 'messagetype': 'E2_TERM_INIT', 'senderendpoint': '', 'subscriptionid': -1, 'endpoint': 'E2MAN', 'meid': ''},
         { 'messagetype': 'RIC_X2_SETUP_RESP', 'senderendpoint': '', 'subscriptionid': -1, 'endpoint': 'E2MAN', 'meid': ''},
         { 'messagetype': 'RIC_X2_SETUP_FAILURE', 'senderendpoint': '', 'subscriptionid': -1, 'endpoint': 'E2MAN', 'meid': ''},
         { 'messagetype': 'RIC_X2_RESET', 'senderendpoint': '', 'subscriptionid': -1, 'endpoint': 'E2MAN', 'meid': ''},
         { 'messagetype': 'RIC_X2_RESET_RESP', 'senderendpoint': '', 'subscriptionid': -1, 'endpoint': 'E2MAN', 'meid': ''},
         { 'messagetype': 'RIC_ENDC_X2_SETUP_RESP', 'senderendpoint': '', 'subscriptionid': -1, 'endpoint': 'E2MAN', 'meid': ''},
         { 'messagetype': 'RIC_ENDC_X2_SETUP_FAILURE', 'senderendpoint': '', 'subscriptionid': -1, 'endpoint': 'E2MAN', 'meid': ''},
         { 'messagetype': 'RIC_ENDC_CONF_UPDATE', 'senderendpoint': '', 'subscriptionid': -1, 'endpoint': 'E2MAN', 'meid': ''},
         { 'messagetype': 'RIC_SCTP_CONNECTION_FAILURE', 'senderendpoint': '', 'subscriptionid': -1, 'endpoint': 'E2MAN', 'meid': ''},
         { 'messagetype': 'RIC_ERROR_INDICATION', 'senderendpoint': '', 'subscriptionid': -1, 'endpoint': 'E2MAN', 'meid': ''},
         { 'messagetype': 'RIC_ENB_CONF_UPDATE', 'senderendpoint': '', 'subscriptionid': -1, 'endpoint': 'E2MAN', 'meid': ''},
         { 'messagetype': 'RIC_ENB_LOAD_INFORMATION', 'senderendpoint': '', 'subscriptionid': -1, 'endpoint': 'E2MAN', 'meid': ''},
         { 'messagetype': 'E2_TERM_KEEP_ALIVE_RESP', 'senderendpoint': '', 'subscriptionid': -1, 'endpoint': 'E2MAN', 'meid': ''},
         { 'messagetype': 'A1_POLICY_QUERY', 'senderendpoint': '', 'subscriptionid': -1, 'endpoint': 'A1MEDIATOR', 'meid': ''},
         { 'messagetype': 'A1_POLICY_RESP', 'senderendpoint': '', 'subscriptionid': -1, 'endpoint': 'A1MEDIATOR', 'meid': ''},
         { 'messagetype': 'RIC_SERVICE_UPDATE', 'senderendpoint': '', 'subscriptionid': -1, 'endpoint': 'E2MAN', 'meid': ''},
         { 'messagetype': 'RIC_E2NODE_CONFIG_UPDATE', 'senderendpoint': '', 'subscriptionid': -1, 'endpoint': 'E2MAN', 'meid': ''},
         { 'messagetype': 'RIC_E2_RESET_REQ', 'senderendpoint': '', 'subscriptionid': -1, 'endpoint': 'E2MAN', 'meid': ''},
         #==============================ADD THIS========================================
         { 'messagetype': 'A1_EI_QUERY_ALL','senderendpoint': '', 'subscriptionid': -1, 'endpoint': 'A1MEDIATOR', 'meid': ''},
         { 'messagetype': 'A1_EI_CREATE_JOB','senderendpoint': '', 'subscriptionid': -1, 'endpoint': 'A1MEDIATOR', 'meid': ''},
         #==============================ADD THIS========================================
         ]
    ```

#### Alarm Manager
1. Change controls.promAlertManager.address
    ```sh
    nano ric-dep/helm/alarmmanager/templates/configmap.yaml
    ```
    ```yaml
      "controls": {
        "promAlertManager": {
        #=========================HERE==============================
          "address": "r4-infrastructure-prometheus-alertmanager:80",
        #===========================================================
          "baseUrl": "api/v2",
          "schemes": "http",
          "alertInterval": 30000
        },
        "maxActiveAlarms": 5000,
        "maxAlarmHistory": 20000,
        "alarmInfoPvFile": "/mnt/pv-ricplt-alarmmanager/alarminfo.json"
      }
    ```
2. Add liveness and readiness probe
   ```sh
   nano ric-dep/helm/alarmmanager/templates/deployment.yaml
   ```
   ```yaml
    spec:
      hostname: {{ include "common.name.alarmmanager" . }}
      imagePullSecrets:
        - name: {{ include "common.dockerregistry.credential" $imagectx }}
      serviceAccountName: {{ include "common.serviceaccountname.alarmmanager" . }}
      containers:
        - name: {{ include "common.containername.alarmmanager" . }}
          image: {{ include "common.dockerregistry.url" $imagectx }}/{{ .Values.alarmmanager.image.name }}:{{ $imagetag }}
          imagePullPolicy: {{ include "common.dockerregistry.pullpolicy" $pullpolicyctx }}
          #================================HERE==============================
          readinessProbe:
            failureThreshold: 3
            httpGet:
              path: ric/v1/health/ready
              port: 8080
              scheme: HTTP
            initialDelaySeconds: 5
            periodSeconds: 15
          livenessProbe:
            failureThreshold: 3
            httpGet:
              path: ric/v1/health/alive
              port: 8080
              scheme: HTTP
            initialDelaySeconds: 5
            periodSeconds: 15
          #==================================================================
   ```

#### O1 Mediator
1. Add livenessProbe and readinessProbe：
    ```sh
    nano ric-dep/helm/o1mediator/templates/deployment.yaml
    ```
    ```yaml
    spec:
      hostname: {{ include "common.name.o1mediator" . }}
      imagePullSecrets:
        - name: {{ include "common.dockerregistry.credential" $imagectx }}
      serviceAccountName: {{ include "common.serviceaccountname.o1mediator" . }}
      containers:
        - name: {{ include "common.containername.o1mediator" . }}
          image: {{ include "common.dockerregistry.url" $imagectx }}/{{ .Values.o1mediator.image.name }}:{{ .Values.o1mediator.image.tag }}
          imagePullPolicy: {{ include "common.dockerregistry.pullpolicy" $pullpolicyctx }}
          #===================================HERE===================================
          livenessProbe:
            failureThreshold: 3
            httpGet:
              path: ric/v1/health/alive
              port: 8080
              scheme: HTTP
            initialDelaySeconds: 5
            periodSeconds: 15
            successThreshold: 1
            timeoutSeconds: 1
          readinessProbe:
            failureThreshold: 3
            httpGet:
              path: ric/v1/health/ready
              port: 8080
              scheme: HTTP
          #===================================HERE===================================
            initialDelaySeconds: 5
            periodSeconds: 15
            successThreshold: 1
            timeoutSeconds: 1
    ```

### Install nfs for InfluxDB
```sh
kubectl create ns ricinfra
helm repo add stable https://charts.helm.sh/stable
helm install nfs-release-1 stable/nfs-server-provisioner --namespace ricinfra
kubectl patch storageclass nfs -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
sudo apt install nfs-common
```
### Modify installation script to include influxdb and jaegeradapter
```sh
nano ric-dep/bin/install
```
```sh
IS_INFLUX_PERSIST=$( kubectl get storageclass nfs 2>/dev/null | awk '{print $1}' | grep nfs)
if [[ ${LIST_OF_COMPONENTS} == *"influxdb"* ]]; then
	if [ -z "$IS_INFLUX_PERSIST" ]; then
        	echo  "nfs storage does not exist, create PersistentVolume through the storage class for the influxdb database"
        	LIST_OF_COMPONENTS=$(echo "$LIST_OF_COMPONENTS" | sed "s/influxdb//")
            echo "skipping influxdb component"
	else
        	echo "nfs storage exist"
        fi
fi

# replace the dbaasha with dbaas1 if deploying non HA DBaaS
#====================================================HERE=============================
COMPONENTS="infrastructure dbaas appmgr rtmgr e2mgr e2term a1mediator submgr vespamgr o1mediator alarmmanager influxdb jaegeradapter $LIST_OF_COMPONENTS"
#=====================================================================================


echo "Deploying RIC infra components [$COMPONENTS]"
if [[ ${COMPONENTS} != *"influxdb"* ]]; then
        OPTIONAL_COMPONENTS="influxdb"
fi
if [[ ${COMPONENTS} != *"jaegeradapter"* ]]; then
        OPTIONAL_COMPONENTS={"$OPTIONAL_COMPONENTS jaegeradapter"}
fi
if [ ! -z "$OPTIONAL_COMPONENTS" ]; then
        echo "Note that the following optional components are NOT being deployed: $OPTIONAL_COMPONENTS. To deploy them add them with -c to the default component list of the install command"
fi

```
### Modify RIC Platform and RIC AUX IP
```sh
nano ric-dep/RECIPE_EXAMPLE/example_recipe_oran_f_release.yaml
```
```yaml
common:
  releasePrefix: r4
# If a local docker registry is used, please specify it using the following option
#  localregistry: nexus3.o-ran-sc.org:10004

# Change the overall image pull policy using the following option
#  pullpolicy: IfNotPresent

# Change the namespaces using the following options
#  namespace:
#    aux: ricaux
#    platform: ricplt
#    xapp: ricxapp
#    infra: ricinfra

# ricip should be the ingress controller listening IP for the platform cluster
# auxip should be the ingress controller listening IP for the AUX cluster
#==========================================HERE========================================
extsvcplt:
  ricip: "<your ip here>"
  auxip: "<your ip here>"
#==========================================HERE========================================

```

### RIC Deployment
```sh
./install -f ../RECIPE_EXAMPLE/example_recipe_oran_h_release.yaml
```

### Check Deployment
```sh
kubectl get pods -A
```
They all should be running, if not there is probably a slight error in deployment config.