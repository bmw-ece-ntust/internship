# Kubernetes with KubeSpray on BareMetal Ubuntu Server 22.04 LTS
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
