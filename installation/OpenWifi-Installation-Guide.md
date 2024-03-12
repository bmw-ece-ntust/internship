# **OpenWiFi Installation**

Reference : [OpenWiFi](https://github.com/Telecominfraproject/wlan-cloud-ucentral-deploy/blob/main/docker-compose/README.md)

## **Table of Contents**
- [**OpenWiFi Installation**](#openwifi-installation)
  - [**Table of Contents**](#table-of-contents)
  - [**Deploy using Docker Compose**](#deploy-using-docker-compose)
  - [**Troubleshooting Docker Permissions**](#troubleshooting-docker-permissions)
  - [**Renaming IP**](#renaming-ip)

The [wlan-cloud-ucentral-deploy](https://github.com/Telecominfraproject/wlan-cloud-ucentral-deploy) repository contains two packaging options:
- Docker Compose - used for local deployments
- Helm - used for deployment to Kubernetes clusters

## **Deploy using Docker Compose**

1. Install Docker Compose according to platform-specific instructions.
   
   **Instalation scenarios**
   - **Install Docker Desktop on Linux**

     [Docker Desktop](https://docs.docker.com/desktop/install/linux-install/) includes Docker Compose along with Docker Engine and Docker CLI which are Compose prerequisites.
      
      KVM Virtualization Support (Docker Desktop runs a VM that requires KVM support)

     1.  Load module 
         ```
         modprobe kvm
         ```

         Output (Depending on the processor of the host machine)

         ```
          modprobe kvm_intel  # Intel processors
          
          modprobe kvm_amd    # AMD processors
         ```

      2. Check if the KVM modules are enabled
         ```
         lsmod | grep kvm
         ```

         Output
         ```
         kvm_amd               167936  0
         ccp                   126976  1 kvm_amd
         kvm                  1089536  1 kvm_amd
         irqbypass              16384  1 kvm
         ```

      3. Add user to the group to access kvm device
         ```
         sudo usermod -aG kvm $USER
         ```

      4. Download the latest [DEB package](https://desktop.docker.com/linux/main/amd64/docker-desktop-4.26.1-amd64.deb?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-linux-amd64)
      5. Install the package with apt as follows
         ```
         sudo apt-get install ./docker-desktop-<version>-<arch>.deb
         ```
      6. Launch Docker Desktop
         ```
         systemctl --user start docker-desktop
         ```
      7. Check version
         
         Check docker compose version
         ```
         docker compose version
         ```
         Output
         ```
         Docker Compose version v2.17.3
         ```
      8. Check docker version
         ```
         docker version
         ```
         Output
         ```
         Client: Docker Engine - Community
         Cloud integration: v1.0.31
         Version:           23.0.5
         API version:       1.42
         <...>
         ```
     
2. Clone the repository with
   ```
   git clone https://github.com/Telecominfraproject/wlan-cloud-ucentral-deploy
   ```
3. The Docker Compose uCentral microservice configs use `openwifi.wlan.local` as a hostname, so make sure you add an entry in your hosts file (or in your local DNS solution) which points to `127.0.0.1` or the IP of the host running the SDK.

   ```
   sudo nano /etc/hosts
   ```

   Output
   
   <img width="428" alt="image" src="https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-11-Lauren/images/hosts.png">


4. Navigate to the docker compose directory
   
   PATH: `docker-compose` 
   ```
   cd docker-compose/
   ```
5. Initialize the deployment with 
   ```
   docker-compose up -d
   ```

   Output
   ```
   openwifi_zookeeper_1 is up-to-date
   openwifi_kafka_1 is up-to-date
   Starting openwifi_init-kafka_1 ... 
   openwifi_owgw_1 is up-to-date
   openwifi_owsub_1 is up-to-date
   openwifi_owsec_1 is up-to-date
   openwifi_owanalytics_1 is up-to-date
   openwifi_owfms_1 is up-to-date
   openwifi_owprov_1 is up-to-date
   openwifi_owgw-ui_1 is up-to-date
   Starting openwifi_init-kafka_1 ... done
   ```

6. If the containers are up and running, you should see the following output with 
   ```
   docker-compose ps
   ```
   Output
   ```
            Name                      Command               State                                                   Ports
   ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
   openwifi_kafka_1       /opt/bitnami/scripts/kafka ...   Up      9092/tcp
   openwifi_owfms_1       /docker-entrypoint.sh /ope ...   Up      0.0.0.0:16004->16004/tcp,:::16004->16004/tcp, 0.0.0.0:16104->16104/tcp,:::16104->16104/tcp, 17004/tcp
   openwifi_owgw-ui_1     /docker-entrypoint.sh ngin ...   Up      0.0.0.0:443->443/tcp,:::443->443/tcp, 0.0.0.0:80->80/tcp,:::80->80/tcp
   openwifi_owgw_1        /docker-entrypoint.sh /ope ...   Up      0.0.0.0:15002->15002/tcp,:::15002->15002/tcp, 0.0.0.0:16002->16002/tcp,:::16002->16002/tcp,
                                                                  0.0.0.0:16003->16003/tcp,:::16003->16003/tcp, 0.0.0.0:16102->16102/tcp,:::16102->16102/tcp, 17002/tcp
   openwifi_owprov-ui_1   /docker-entrypoint.sh ngin ...   Up      80/tcp, 0.0.0.0:8080->8080/tcp,:::8080->8080/tcp, 0.0.0.0:8443->8443/tcp,:::8443->8443/tcp
   openwifi_owprov_1      /docker-entrypoint.sh /ope ...   Up      0.0.0.0:16005->16005/tcp,:::16005->16005/tcp, 0.0.0.0:16105->16105/tcp,:::16105->16105/tcp, 17005/tcp
   openwifi_owsec_1       /docker-entrypoint.sh /ope ...   Up      0.0.0.0:16001->16001/tcp,:::16001->16001/tcp, 0.0.0.0:16101->16101/tcp,:::16101->16101/tcp, 17001/tcp
   openwifi_rttys_1       /rttys/rttys                     Up      0.0.0.0:5912->5912/tcp,:::5912->5912/tcp, 0.0.0.0:5913->5913/tcp,:::5913->5913/tcp
   ```   
7. Add `certs/restapi-ca.pem` to your trusted browser certificates or add certificate exceptions in your browser by visiting each of the following URLs (one per port) :
   - https://openwifi.wlan.local:16001
   - https://openwifi.wlan.local:16002
   - https://openwifi.wlan.local:16004
   - https://openwifi.wlan.local:16005
   - https://openwifi.wlan.local:16006
   - https://openwifi.wlan.local:16009

     Using the browser, accept the self-signed SSL certificate warnings.

8. Connect to your AP via SSH and add a static hosts entry in `/etc/hosts` for `openwifi.wlan.local` which points to the address of the host the SDK deployment runs on.

9.  While staying in the SSH session, copy the content of `certs/restapi-ca.pem` on your local machine and append it to the file `/etc/ssl/cert.pem` on the AP. This way your AP will also trust the self-signed certificate.
10. Navigate in a web browser to `https://openwifi.wlan.local` to access the UI and login with default username and password.

    Default user: tip@ucentral.com

    Password: **openwifi**
   
11. Service enforces a password change on first login to something more secured

    <img width="428" alt="image" src="https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-11-Lauren/images/OpenWiFiLoginPage.png">
    
12. To use the curl test scripts which are included in the microservice repositories make sure to set the following environment variables before issuing a request:
      ```
      export UCENTRALSEC="openwifi.wlan.local:16001"
      export FLAGS="-s --cacert <your-wlan-cloud-ucentral-deploy-location>/docker-compose/certs/restapi-ca.pem"
      ```

## **Troubleshooting Docker Permissions**

Permission denied exceptions occured when calling ```docker``` and ```docker-compose```:
```
raise DockerException( docker.errors.DockerException: Error while fetching server API version: ('Connection aborted.', PermissionError(13, 'Permission denied')))
```

It is possible because the docker is not permitted yet to read files, follow these steps:
```
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
```

Then try to run 
```
docker run hello-world
```
Output
```
Hello from Docker!
This message shows that your installation appears to be working correctly.
```
If the output is same as the above, `docker-compose up -d` should not have any problem anymore.

## **Renaming IP**
The docker deployment steps 7 shows that the use of ```https://openwifi.wlan.local```, these needed to be manually assigned using static host name in both remote computer (if want to be accessed via internet) or local. Follow this steps:

1. Edit host file
   
   ```
   sudo nano /etc/hosts
   ``` 
   or other text editor available on the computer.

2. Add new entry for the host:
   * For local: `127.0.0.1 openwifi.wlan local`
   * For remote: `[OpenWiFi SDK Host IP] openwifi.wlan local`
  
3. Check if the host properly assigned by accessing a web browser open `https://openwifi.wlan.local`. It should shown the OpenWiFi UI.
