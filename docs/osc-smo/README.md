# O-RAN Software Community SMO

```
Provisioning Kubernetes Cluster BareMetal with KubeSpray
```

## Environment
```
2x Ubuntu Server 22.04LTS
```

## Minimum RAM
- Master
  - Memory: 1500 MB
- Node
  - Memory: 1024 MB

## LAB Topology
```
NODE 1 = 192.168.17.136
NODE 2 = 192.168.17.131
```

## Installation
- Just do it on your first Node.

### Add All IP Node to Hosts Config
```
nano /etc/hosts
192.168.17.136 node1
192.168.17.131 node2
```

### Generate SSH Keygen
```
ssh-keygen
ssh-copy-id -i ~/.ssh/id_rsa.pub root@node1
ssh-copy-id -i ~/.ssh/id_rsa.pub root@node2
```

### Install Dependencies (python3-pip)
```
apt install python3-pip
```

### Clone Project & Prepare Dependencies
```
git clone https://github.com/kubernetes-sigs/kubespray
cd kubespray
git checkout master #if you want to change version

sudo pip3 install -r requirements.txt
cp -rfp inventory/sample inventory/mycluster
```

### Declare IP Node
```
declare -a IPS=(192.168.17.136 192.168.17.131)
CONFIG_FILE=inventory/mycluster/hosts.yaml python3 contrib/inventory_builder/inventory.py ${IPS[@]}
```

### See General Configuration
```
CHANGE if NEEDED.
```
```
cat inventory/mycluster/group_vars/all/all.yml
cat inventory/mycluster/group_vars/k8s_cluster/k8s-cluster.yml
```

#### To specify Kuberenetes Version (OPTIONAL)
```
nano inventory/mycluster/group_vars/k8s_cluster/k8s-cluster.yml
kube_version: v1.21.9
```

#### To specify Container Runtime (OPTIONAL)
```
nano inventory/mycluster/group_vars/k8s_cluster/k8s-cluster.yml
container_manager: docker
```

#### Running Behind NAT / Multiple Endpoint (OPTIONAL)
You can declare your multiple endpoint to become acceptable VIP on
```
nano inventory/mycluster/group_vars/k8s_cluster/k8s-cluster.yml

---
supplementary_addresses_in_ssl_keys
---
```

### Run Ansible to Install
```
Do this at root.
```
```
ansible-playbook -i inventory/mycluster/hosts.yaml  --become --become-user=root cluster.yml
```

## Check
```
kubectl get nodes
```
## Deployment

### 1. Download the IT/dep repository from gerrit

```bash=
mkdir workspace && cd workspace
git clone --recurse-submodules https://gerrit.o-ran-sc.org/r/it/dep.git
```

### 2. Setup Helm Charts
- Execute the following commands being logged as root.
```bash=
##Setup ChartMuseum
./dep/smo-install/scripts/layer-0/0-setup-charts-museum.sh

##Setup HELM3
./dep/smo-install/scripts/layer-0/0-setup-helm3.sh

## Build ONAP/ORAN charts
./dep/smo-install/scripts/layer-1/1-build-all-charts.sh
```

### 3. Deploy components
- Execute the following commands ==being logged as root==:
```bash=
./dep/smo-install/scripts/layer-2/2-install-oran.sh
```

## Deploy Simulators (DU / RU Simulators)

> **NOTE** When all pods in "onap" and "nonrtric" namespaces are well up & running

### 1. Modify the yaml file. 
- Modify `smo-install/helm-override/default/network-simulators-override.yaml`. 
- Add image tag in every simulator.
:::warning
:red_circle: **Please go to [Sonatype Nexus Repository Manager](https://nexus3.o-ran-sc.org/#browse/search=keyword%3Dnts-ng-o-ran-du) to check every simulator's version is the latest**, or you will encounter ErrImagePull issue.
:::
```shell=
ru-simulator:
  image:
    tag: 1.5.2
  ntsimNg:
    <<: *ntsimConfig
    ipV6Enabled: false
    sshConnections: 0
    tlsConnections: 1

du-simulator:
  image:
    tag: 1.5.2
  ntsimNg:
    <<: *ntsimConfig
    ipV6Enabled: false
    sshConnections: 1
    tlsConnections: 0

topology-server:
  image:
    tag: 1.8.1
  ntsimNg:
    <<: *ntsimConfig
    ipV6Enabled: false
    sshConnections: 0
    tlsConnections: 1
```
### 2. Install Network simulator (RU / DU / Topology Server)
- Execute the following commands being logged as root:
```bash=
./dep/smo-install/scripts/layer-2/2-install-simulators.sh
```

### 3. Check all pods are running
```bash=
sudo kubectl get pods -n network
```
![](/internship/assets/oru-odu-sim.png)
