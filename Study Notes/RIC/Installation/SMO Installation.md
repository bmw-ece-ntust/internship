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
apt install -y python3-pip
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

<iframe src="https://app.warp.dev/block/embed/05GI7Ma03CAzeXoJExEBnT" title="embedded warp block" style="width: 1922px; height: 1423px; border:0; overflow:hidden;" allow="clipboard-read; clipboard-write"></iframe>



