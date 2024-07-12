# RIC Installation (I Release)

This document is meant to fix the broken previous installation which uses H-Release.
>**IMPORTANT:**
>
>Installation should be done on root
>```sh
>sudo su
>```
>After entering password, go to root directory.
>```sh
>cd ~
>```
>

## Preparing Deployment Scripts.
Cloning the source code repository.
```sh
git clone "https://gerrit.o-ran-sc.org/r/ric-plt/ric-dep"
```

## Installing Kubernetes and Helm template
The script file for the installation is in `cd ric-dep/bin`
```
# install kubernetes, kubernetes-CNI, helm and docker
cd ric-dep/bin
./install_k8s_and_helm.sh

# install chartmuseum into helm and add ric-common templates
./install_common_templates_to_helm.sh
```
## Modifyling the deployment script.
This is probably where the previous install went wrong. Doing it again with minimal reconfiguration in the deployment script.
Now we only do minor IP config in the deployment receipe inside `/RECIPE_EXAMPLE/`
```
├── RECIPE_EXAMPLE
│   ├── example_recipe_latest_stable.yaml
│   ├── example_recipe_latest_unstable.yaml
│   ├── example_recipe_latest_unstable_with_refs_to_staging.yaml
│   ├── example_recipe_oran_cherry_release.yaml
│   ├── example_recipe_oran_dawn_release.yaml
│   ├── example_recipe_oran_e_release.yaml
│   ├── example_recipe_oran_f_release.yaml
│   ├── example_recipe_oran_g_release.yaml
│   ├── example_recipe_oran_h_release.yaml
│   ├── example_recipe_oran_i_release.yaml
│   └── example_recipe_oran_j_release.yaml
│
│
│
```
This time we use the `example_recipe_oran_i_release.yaml`. Change this part into your RIC IP Address
```yaml
# ricip should be the ingress controller listening IP for the platform cluster
# auxip should be the ingress controller listening IP for the AUX cluster
extsvcplt:
  ricip: "192.168.106.157"
  auxip: "192.168.106.157"
```

## Installing the RIC
Now just run the installation script.
```sh
cd ric-dep/bin
./install -f ../RECIPE_EXAMPLE/PLATFORM/example_recipe_oran_i_release.yaml
```



After it is done, check the deployment status. The status should be all running
```sh
kubectl get pods -A
```
Result should be similar like this
```sh
root@ricintern-virtual-machine:~/ric-3/ric-dep/bin# kubectl get pods -A
NAMESPACE      NAME                                                         READY   STATUS      RESTARTS        AGE
kube-flannel   kube-flannel-ds-8jtpm                                        1/1     Running     0               16h
kube-system    coredns-5dd5756b68-gjl2n                                     1/1     Running     0               16h
kube-system    coredns-5dd5756b68-l2h22                                     1/1     Running     0               16h
kube-system    etcd-ricintern-virtual-machine                               1/1     Running     19              16h
kube-system    kube-apiserver-ricintern-virtual-machine                     1/1     Running     13              16h
kube-system    kube-controller-manager-ricintern-virtual-machine            1/1     Running     13              16h
kube-system    kube-proxy-vvv68                                             1/1     Running     0               16h
kube-system    kube-scheduler-ricintern-virtual-machine                     1/1     Running     13              16h
ricinfra       deployment-tiller-ricxapp-676dfd8664-ks6lg                   1/1     Running     0               6m2s
ricinfra       tiller-secret-generator-tzcqx                                0/1     Completed   0               6m2s
ricplt         deployment-ricplt-a1mediator-64fd4bf64-zkl8m                 1/1     Running     0               4m40s
ricplt         deployment-ricplt-alarmmanager-7d47d8f4d4-kjts4              1/1     Running     0               3m47s
ricplt         deployment-ricplt-appmgr-5bdd7cbb54-cn2hm                    1/1     Running     0               5m34s
ricplt         deployment-ricplt-e2mgr-b988db566-m72qs                      1/1     Running     0               5m6s
ricplt         deployment-ricplt-e2term-alpha-75d8ccb646-477wf              1/1     Running     0               4m53s
ricplt         deployment-ricplt-o1mediator-76c4646878-ltwcs                1/1     Running     0               4m1s
ricplt         deployment-ricplt-rtmgr-6556c5bc7b-mmz9k                     1/1     Running     2 (4m10s ago)   5m20s
ricplt         deployment-ricplt-submgr-599754c984-9g6wv                    1/1     Running     0               4m26s
ricplt         deployment-ricplt-vespamgr-786666549b-dcsj6                  1/1     Running     0               4m14s
ricplt         r4-infrastructure-kong-5986fc7965-mpq8j                      2/2     Running     0               6m2s
ricplt         r4-infrastructure-prometheus-alertmanager-64f9876d6d-fzr2p   2/2     Running     0               6m2s
ricplt         r4-infrastructure-prometheus-server-bcc8cc897-n62nt          1/1     Running     0               6m2s
ricplt         statefulset-ricplt-dbaas-server-0                            1/1     Running     0               5m48s
root@ricintern-virtual-machine:~/ric-3/ric-dep/bin# 
```

## Troubleshooting influxdb pending
This is caused by problem in the persistent storage
```sh
kubectl get pv -n ricplt && kubectl get pvc -n ricplt

NAME                     CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS      CLAIM                            STORAGECLASS    REASON   AGE
pv-ricplt-alarmmanager   100Mi      RWO            Retain           Bound       ricplt/pvc-ricplt-alarmmanager   local-storage            3d
pv-ricplt-e2term-alpha   100Mi      RWO            Retain           Bound       ricplt/pvc-ricplt-e2term-alpha   local-storage            3d
pv-ricplt-influxdb       8Gi        RWO            Retain           Available                                    local-storage            79m
NAME                      STATUS    VOLUME                   CAPACITY   ACCESS MODES   STORAGECLASS    AGE
pvc-ricplt-alarmmanager   Bound     pv-ricplt-alarmmanager   100Mi      RWO            local-storage   3d
pvc-ricplt-e2term-alpha   Bound     pv-ricplt-e2term-alpha   100Mi      RWO            local-storage   3d
r4-influxdb-influxdb2     Pending                                                      local-storage   3d
```
### Edit the PV config
```sh
kubectl edit pv pv-ricplt-influxdb -n ricplt
```
Using vim, in the spec object add `storageClassName: local-storage` and change the storage capacity to 50Gi 
`capacity: 50Gi`

```yaml
spec:
  accessModes:
  - ReadWriteOnce
  capacity:
    #This one=========================
    storage: 50Gi
    #This one=========================
  claimRef:
    apiVersion: v1
    kind: PersistentVolumeClaim
    name: r4-influxdb-influxdb2
    namespace: ricplt
    resourceVersion: "443163"
    uid: 21de30c8-f41e-4aad-9cca-f35afc0046f9
  hostPath:
    path: /mnt/pv-ricplt-influxdb
    type: ""
  persistentVolumeReclaimPolicy: Retain
  #This one=========================
  storageClassName: local-storage
  #This one=========================
  volumeMode: Filesystem
```
then save using `:wq`
>Cannot use nano because i cannot find the actual file location

### Edit PVC config
Using vim, in the spec object add `storageClassName: local-storage`.
```yaml
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 50Gi
  #THhis one =======================================
  storageClassName: local-storage
  #THhis one =======================================
  volumeMode: Filesystem
  volumeName: pv-ricplt-influxdb
```
### Result
```sh
kubectl get pod -n ricplt
NAME                                                         READY   STATUS    RESTARTS       AGE
deployment-ricplt-a1mediator-64fd4bf64-glmzr                 1/1     Running   0              3d1h
deployment-ricplt-alarmmanager-7d47d8f4d4-gstch              1/1     Running   0              3d1h
deployment-ricplt-appmgr-5bdd7cbb54-nrqn5                    1/1     Running   0              3d1h
deployment-ricplt-e2mgr-b988db566-dvx58                      1/1     Running   0              3d1h
deployment-ricplt-e2term-alpha-75d8ccb646-th27s              1/1     Running   0              3d1h
deployment-ricplt-jaegeradapter-7489d97555-7wzqj             1/1     Running   0              3d1h
deployment-ricplt-o1mediator-76c4646878-2b9wv                1/1     Running   0              3d1h
deployment-ricplt-rtmgr-6556c5bc7b-vqj2r                     1/1     Running   2 (3d1h ago)   3d1h
deployment-ricplt-submgr-599754c984-5rs7c                    1/1     Running   0              3d1h
deployment-ricplt-vespamgr-786666549b-fscfr                  1/1     Running   0              3d1h
r4-influxdb-influxdb2-0                                      1/1     Running   0              3d1h
r4-infrastructure-kong-5986fc7965-cwtsb                      2/2     Running   0              3d1h
r4-infrastructure-prometheus-alertmanager-64f9876d6d-79vwl   2/2     Running   0              3d1h
r4-infrastructure-prometheus-server-bcc8cc897-27lwg          1/1     Running   0              3d1h
statefulset-ricplt-dbaas-server-0                            1/1     Running   0              3d1h
```

# RIC Applications (xApp usng DMS CLi)
## Installing prerequisites
```sh
sudo apt install libsctp-dev python3.8 cmake-curses-gui libpcre2-dev python-dev protobuf-compiler rapidjson-dev 
```
## Create Local Helm Repo
```sh
docker run --rm -u 0 -it -d -p 8090:8080 -e DEBUG=1 -e STORAGE=local -e STORAGE_LOCAL_ROOTDIR=/charts -v $(pwd)/charts:/charts chartmuseum/chartmuseum:latest
```

## Set up the environment variables for CLI connection using the same port as used above.
```sh
export CHART_REPO_URL=http://0.0.0.0:8090
```
## Install dms_cli tool
1. Git clone appmgr
    ```sh
    git clone "https://gerrit.o-ran-sc.org/r/ric-plt/appmgr"
    ```
2. Change dir to xapp_onboarder
    ```
    cd appmgr/xapp_orchestrater/dev/xapp_onboarder
    ```
3. Install xapp_onboarder
    ```
    pip3 install ./
    ```

>(OPTIONAL ) If the host user is non-root user, after installing the packages, please assign the permissions to the below filesystems
>
>```sh
>#Assign relevant permission for non-root user
>sudo chmod 755 /usr/local/bin/dms_cli
>sudo chmod -R 755 /usr/local/lib/python3.6
>sudo chmod -R 755 /usr/local/lib/python3.6
>```

## xApp Onboarding
```sh
# Make sure that you have the xapp descriptor config file and the schema file at your local file system
dms_cli onboard CONFIG_FILE_PATH SCHEMA_FILE_PATH
#OR
dms_cli onboard --config_file_path=CONFIG_FILE_PATH --shcema_file_path=SCHEMA_FILE_PATH

#Example:
dms_cli onboard /files/config-file.json /files/schema.json
#OR
dms_cli onboard --config_file_path=/files/config-file.json --shcema_file_path=/files/schema.json
```
We use a sample of an xApp
### Cloning xApp repo
```sh
cd ~
git clone "https://gerrit.o-ran-sc.org/r/ric-app/hw-go"
git clone "https://gerrit.o-ran-sc.org/r/ric-app/ts"
git clone "https://gerrit.o-ran-sc.org/r/ric-app/ad"
git clone "https://gerrit.o-ran-sc.org/r/ric-app/qp"
```
### Onboarding the xApp
```sh
cd ~/ric-dep/bin/
dms_cli onboard --config_file_path=../../hw-go/config/config-file.json --shcema_file_path=../../hw-go/config/schema.json
dms_cli onboard --config_file_path=../../ts/xapp-descriptor/config-file.json --shcema_file_path=../../ts/xapp-descriptor/schema.json
dms_cli onboard --config_file_path=../../ad/xapp-descriptor/config-file.json --shcema_file_path=../../ad/xapp-descriptor/schema.json
dms_cli onboard --config_file_path=../../qp/xapp-descriptor/config-file.json --shcema_file_path=../../qp/xapp-descriptor/schema.json
```

## List the helm charts from help repository (Optional).
```sh
#List all the helm charts from help repository
curl -X GET http://localhost:8080/api/charts | jq .

#List details of specific helm chart from helm repository
curl -X GET http://localhost:8080/api/charts/<XAPP_CHART_NAME>/<VERSION>
```

## Delete a specific Chart Version from helm repository (Optional).
```sh
#Delete a specific Chart Version from helm repository
curl -X DELETE http://localhost:8080/api/charts/<XAPP_CHART_NAME>/<VERSION>
```

## Download the xApp helm charts (Optional).
```sh
dms_cli download_helm_chart XAPP_CHART_NAME VERSION --output_path=OUTPUT_PATH
#OR
dms_cli download_helm_chart --xapp_chart_name=XAPP_CHART_NAME --version=VERSION --output_path=OUTPUT_PATH

#Example:
dms_cli download_helm_chart ueec 1.0.0 --output_path=/files/helm_xapp
#OR
dms_cli download_helm_chart --xapp_chart_name=ueec --version=1.0.0 --output_path=/files/helm_xapp
```
## xApp Install
```sh
dms_cli install XAPP_CHART_NAME VERSION NAMESPACE
#OR
dms_cli install --xapp_chart_name=XAPP_CHART_NAME --version=VERSION --namespace=NAMESPACE

#Example:
dms_cli install ueec 1.0.0 ricxapp
#OR
dms_cli install --xapp_chart_name=ueec --version=1.0.0 --namespace=ricxapp
```
Now we try to install the previously onboarded xApp
```sh
dms_cli install --xapp_chart_name=hw-go --version=1.0.0 --namespace=ricxapp
```
Sure, here is the revised content:

## Uninstall the xApp (Optional).
```sh
dms_cli uninstall XAPP_CHART_NAME NAMESPACE
#OR
dms_cli uninstall --xapp_chart_name=XAPP_CHART_NAME --namespace=NAMESPACE

#Example:
dms_cli uninstall ueec ricxapp
#OR
dms_cli uninstall --xapp_chart_name=ueec --namespace=ricxapp
```

## Upgrade the xApp to a new version (Optional).
```sh
dms_cli upgrade XAPP_CHART_NAME OLD_VERSION NEW_VERSION NAMESPACE
#OR
dms_cli upgrade --xapp_chart_name=XAPP_CHART_NAME --old_version=OLD_VERSION --new_version=NEW_VERSION --namespace=NAMESPACE

#Example:
dms_cli upgrade ueec 1.0.0 2.0.0 ricxapp
#OR
dms_cli upgrade --xapp_chart_name=ueec --old_version=1.0.0 --new_version=2.0.0 --namespace=ricxapp
```

## Rollback the xApp to an old version (Optional).
```sh
dms_cli rollback XAPP_CHART_NAME NEW_VERSION OLD_VERSION NAMESPACE
#OR
dms_cli rollback --xapp_chart_name=XAPP_CHART_NAME --new_version=NEW_VERSION --old_version=OLD_VERSION --namespace=NAMESPACE

#Example:
dms_cli rollback ueec 2.0.0 1.0.0 ricxapp
#OR
dms_cli rollback --xapp_chart_name=ueec --new_version=2.0.0 --old_version=1.0.0 --namespace=ricxapp
```

## Check the health of the xApp (Optional).
```sh
dms_cli health_check XAPP_CHART_NAME NAMESPACE
#OR
dms_cli health_check --xapp_chart_name=XAPP_CHART_NAME --namespace=NAMESPACE

#Example:
dms_cli health_check ueec ricxapp
#OR
dms_cli health_check --xapp_chart_name=ueec --namespace=ricxapp
```



