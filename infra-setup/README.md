### 1.1 Setup Kubernetes



*Environment:*
- Master
  - Memory: 23 GiB
  - vCPU: 16
  - Storage: 85 GiB

*Lab Topology:*
```
NODE 1 = 10.30.1.212 => Master
```

* *Pre-requisite*
    * Add All IP Node to Hosts Config
        
        ``$ nano /etc/hosts``
        ```
        10.30.1.212 node1
        ```
        
    * Generate SSH Keygen
        ```
        $ ssh-keygen
        $ ssh-copy-id -i ~/.ssh/id_rsa.pub root@node1
        ```
    * Install Dependencies (python3-pip)
    
        ```
        $ apt install python3-pip
        ```
        
    * Clone Project & Prepare Dependencies
        ```
        $ git clone https://github.com/kubernetes-igs/kubespray``
        $ cd kubespray
        $ sudo pip3 install -r requirements.txt
        $ cp -rfp inventory/sample inventory/mycluster
        ```
    * Declare IP Node
        ```
        $ declare -a IPS=(10.30.1.212)
        $ CONFIG_FILE=inventory/mycluster/hosts.yaml python3 contrib/inventory_builder/inventory.py ${IPS[@]}
        ```

        
    * See General Configuration

        >   CHANGE IT IF IT'S NEEDED
    
      ```  
        $ cat inventory/mycluster/group_vars/all/all.yml
        $ cat inventory/mycluster/group_vars/k8s_cluster/k8s-cluster.yml
        ```
* *Ansible Install*
    * Run Ansible Installation
        > DO THIS IN ROOT
    
        ```
        # ansible-playbook -i inventory/mycluster/hosts.yaml  --become --become-user=root cluster.yml
        ```
    * Check Cluster Ready
       ``` 
        # kubectl get nodes
        ```