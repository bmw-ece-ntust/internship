# SMO Installation

>**Prerequisite:**
>
>- **OS:** Ubuntu 22.04 Server (Using desktop version resulted in the VM cannot accessing internet after kubespray installation)
>- **CPU:** >6 Cores
>- **RAM:** >=32G
>- **Python** version higher than 3.9
>
>All commands executed as root user, run `sudo -i` first an then enter password.




## Initial setup
### pip Instalation
```sh
apt install -y python3-pip
```
### Installing kubespray
#### Cloning kubespray repo
```sh
git clone https://github.com/kubernetes-sigs/kubespray -b release-2.23
```
#### Installing pip requirements
```sh
cd kubespray 
pip install -r requirements.txt
```

#### Installing kubespray using Ansible
```sh
#This part will take quite a while, be patient.
sed -i 's/\(kube_version: \)[^"]*/\1v1.27.5/' inventory/local/group_vars/k8s_cluster/k8s-cluster.yml
ansible-playbook -i inventory/local/hosts.ini --become --become-user=root cluster.yml
```

#### Modifying the kubernetes config
```sh
mkdir -p ~/.kube/config
sudo cp /etc/kubernetes/admin.conf ~/.kube/config
```

## SMO Deployment
### Cloning the SMO repo.
```sh
cd ~
git clone https://gerrit.o-ran-sc.org/r/it/dep.git -b master --recursive
```
### Setup the helm charts
```sh
cd dep
##Setup ChartMuseum
./smo-install/scripts/layer-0/0-setup-charts-museum.sh

##Setup HELM3
./smo-install/scripts/layer-0/0-setup-helm3.sh

## Build ONAP/ORAN charts
./smo-install/scripts/layer-1/1-build-all-charts.sh
```

### Deploying the SMO
```sh
./smo-install/scripts/layer-2/2-install-oran.sh
```

### Verifying installation
```sh
#The pods needs some time to initialize, wait roughly for half an hour.
kubectl get pods -n onap && kubectl get pods -n nonrtric
```
**Result:**
```
NAMESPACE        NAME                                                READY   STATUS       RESTARTS        AGE
kube-system      calico-kube-controllers-794577df96-5x5j4            1/1     Running      0               3h10m
kube-system      calico-node-pr7cz                                   1/1     Running      0               3h10m
kube-system      coredns-5c469774b8-7sgm6                            1/1     Running      0               3h10m
kube-system      dns-autoscaler-5cc59c689b-zzhsq                     1/1     Running      0               3h10m
kube-system      kube-apiserver-node1                                1/1     Running      1               3h11m
kube-system      kube-controller-manager-node1                       1/1     Running      3 (9m59s ago)   3h11m
kube-system      kube-proxy-47fvj                                    1/1     Running      0               3h10m
kube-system      kube-scheduler-node1                                1/1     Running      2 (9m56s ago)   3h11m
kube-system      nodelocaldns-rnmkb                                  1/1     Running      0               3h10m
nonrtric         a1-sim-osc-0-7d8f49d4b8-ntsp5                       1/1     Running      0               162m
nonrtric         a1-sim-osc-1-7b6dd4675c-s7752                       1/1     Running      0               162m
nonrtric         a1-sim-std-0-666d947c7c-c6clz                       1/1     Running      0               162m
nonrtric         a1-sim-std-1-f8778bf66-g8kxb                        1/1     Running      0               162m
nonrtric         a1-sim-std2-0-79cfbc9fdd-f8g8k                      1/1     Running      0               162m
nonrtric         a1-sim-std2-1-9fcdcbc9c-lfllr                       1/1     Running      0               162m
nonrtric         capifcore-5845ccc68-6sh4j                           1/1     Running      0               162m
nonrtric         controlpanel-c4f5c58f8-rx82w                        1/1     Running      0               162m
nonrtric         dmaapadapterservice-0                               1/1     Running      0               162m
nonrtric         dmaapmediatorservice-0                              1/1     Running      0               162m
nonrtric         helmmanager-0                                       1/1     Running      0               162m
nonrtric         informationservice-0                                1/1     Running      0               162m
nonrtric         nonrtricgateway-d46cf479c-bbcrd                     1/1     Running      0               162m
nonrtric         odu-app-b7f7f9f56-2hn92                             1/1     Running      0               162m
nonrtric         odu-app-ics-version-7df48b8d5d-94g8d                1/1     Running      0               162m
nonrtric         oran-nonrtric-kong-5d878fb6df-jp7nl                 2/2     Running      1 (9m59s ago)   162m
nonrtric         oran-nonrtric-kong-init-migrations-9f877            0/1     Completed    0               162m
nonrtric         oran-nonrtric-postgresql-0                          1/1     Running      0               162m
nonrtric         oru-app-98d99c694-x7crp                             1/1     Running      0               162m
nonrtric         policymanagementservice-0                           1/1     Running      0               162m
nonrtric         rappcatalogueservice-7cc75f77dc-9xsf6               1/1     Running      0               162m
nonrtric         rappmanager-0                                       1/1     Running      0               162m
nonrtric         servicemanager-566b96b854-cwfnr                     1/1     Running      0               162m
nonrtric         topology-7d78f99678-bgqhg                           1/1     Running      0               162m
onap             onap-dcae-ves-collector-8b767f86f-22mv6             1/1     Running      0               164m
onap             onap-mariadb-galera-0                               2/2     Running      0               164m
onap             onap-message-router-0                               2/2     Running      0               164m
onap             onap-nengdb-init-config-job-f4bzr                   0/1     Completed    0               162m
onap             onap-network-name-gen-5cf7bdc944-zscb5              1/1     Running      1 (149m ago)    162m
onap             onap-policy-apex-pdp-55694fc89-bd5q5                1/1     Running      0               163m
onap             onap-policy-api-6799979dd7-99q2v                    1/1     Running      0               163m
onap             onap-policy-clamp-ac-a1pms-ppnt-557bd5b778-7rnjs    1/1     Running      0               163m
onap             onap-policy-clamp-ac-http-ppnt-99dc78cb7-ff665      1/1     Running      0               163m
onap             onap-policy-clamp-ac-k8s-ppnt-5599cf945b-svdxw      1/1     Running      0               163m
onap             onap-policy-clamp-ac-kserve-ppnt-584c884bf8-97bfp   1/1     Running      0               163m
onap             onap-policy-clamp-ac-pf-ppnt-7f5b54df6d-6xkst       1/1     Running      0               163m
onap             onap-policy-clamp-runtime-acm-c48d847f5-8xpbh       1/1     Running      0               163m
onap             onap-policy-galera-config-7hbfm                     0/1     Completed    0               153m
onap             onap-policy-galera-config-wnm4s                     0/1     Init:Error   0               163m
onap             onap-policy-galera-init-wnfld                       0/1     Completed    0               163m
onap             onap-policy-mariadb-0                               2/2     Running      0               163m
onap             onap-policy-pap-6c7b78f655-6dt7f                    1/1     Running      0               163m
onap             onap-sdnc-0                                         1/1     Running      0               162m
onap             onap-sdnc-ansible-server-78dd459b84-8ffvz           1/1     Running      0               162m
onap             onap-sdnc-dbinit-job-sn4vg                          0/1     Completed    0               162m
onap             onap-sdnc-dgbuilder-7bcf65ff78-qm455                1/1     Running      0               162m
onap             onap-sdnc-dmaap-listener-64cd9f4d5b-44xpf           1/1     Running      0               162m
onap             onap-sdnc-sdnrdb-init-job-jn8p4                     0/1     Completed    0               162m
onap             onap-sdnc-web-5cd4697dc-tbv7s                       1/1     Running      0               162m
onap             onap-sdnrdb-coordinating-only-567cf48d7-2gdz4       2/2     Running      0               162m
onap             onap-sdnrdb-master-0                                1/1     Running      0               162m
onap             onap-strimzi-entity-operator-864cb5b89d-dgs6v       3/3     Running      0               164m
onap             onap-strimzi-kafka-0                                1/1     Running      0               164m
onap             onap-strimzi-zookeeper-0                            1/1     Running      0               165m
strimzi-system   strimzi-cluster-operator-64f9bf48c9-xbbbr           1/1     Running      1 (9m55s ago)   165m
```



