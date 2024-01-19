# OpenWifi Installation

Reference : https://github.com/Telecominfraproject/wlan-cloud-ucentral-deploy/blob/main/docker-compose/README.md 

## Table of Contents
- [Installation](https://github.com/NTUST-BMW-Lab/internship/blob/2024-TEEP-Lauren/installation/OpenWifi-Installation-Guide.md#openwifi-installation)
   - [Deploy using Docker Compose](https://github.com/NTUST-BMW-Lab/internship/blob/2024-TEEP-Lauren/installation/OpenWifi-Installation-Guide.md#deploy-using-docker-compose)
- [Troubleshooting Methods](https://github.com/NTUST-BMW-Lab/internship/blob/2024-TEEP-Lauren/installation/OpenWifi-Installation-Guide.md#troubleshooting-methods)
  - [Trial 1, Update](https://github.com/NTUST-BMW-Lab/internship/blob/2024-TEEP-Lauren/installation/OpenWifi-Installation-Guide.md#trial-1-update)
  - [Trial 2, Enabling user to run commands without `sudo`](https://github.com/NTUST-BMW-Lab/internship/blob/2024-TEEP-Lauren/installation/OpenWifi-Installation-Guide.md#trial-2-add-current-user-to-docker-group-enabling-it-to-run-without-sudo)
  - [Checking methods](https://github.com/NTUST-BMW-Lab/internship/blob/2024-TEEP-Lauren/installation/OpenWifi-Installation-Guide.md#checking-methods)
  - [Renaming IP](https://github.com/NTUST-BMW-Lab/internship/blob/2024-TEEP-Lauren/installation/OpenWifi-Installation-Guide.md#renaming-ip)

The [wlan-cloud-ucentral-deploy](https://github.com/Telecominfraproject/wlan-cloud-ucentral-deploy) repository contaions two packaging options:
- Docker Compose - used for local deployments
- Helm - used for deployment to Kubernetes clusters

## Deploy using Docker Compose

1. Install Docker Compose according to platform-specific instructions.
   Instalation scenarios
   - **Install Docker Desktop on Linux**
   
     [Docker Desktop](https://docs.docker.com/desktop/install/linux-install/) includes Docker Compose along with Docker Engine and Docker CLI which are Compose prerequisites.
   - **Install the Compose plugin**

     Install from command line, by either [using Docker's repository](https://docs.docker.com/compose/install/linux/#install-using-the-repository) or downloading and installing [manually](https://docs.docker.com/compose/install/linux/#install-the-plugin-manually)
   - **Install the [Compose standalone](https://docs.docker.com/compose/install/standalone/) on Linux or Windows Server**
     
2. Clone the repository with
   ```
   git clone https://github.com/Telecominfraproject/wlan-cloud-ucentral-deploy
   ```
3. The Docker Compose uCentral microservice configs use `openwifi.wlan.local` as a hostname, so make sure you add an entry in your hosts file (or in your local DNS solution) which points to `127.0.0.1` or the IP of the host running the SDK.
4. Navigate to the `docker-compose` ditectory with `cd docker-compose/`.
5. Initialize the deployment with `docker-compose up -d`.
6. If the containers are up and running, you should see the following output with `docker-compose ps`:
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
9. While staying in the SSH session, copy the content of `certs/restapi-ca.pem` on your local machine and append it to the file `/etc/ssl/cert.pem` on the AP. This way your AP will also trust the self-signed certificate.
10. Navigate in a web browser to `https://openwifi.wlan.local` to access the UI and login with default username and password.

    Default user: tip@ucentral.com

    Password: **openwifi**
   
12. Service enforces a password change on first login to something more secured

    <img width="428" alt="image" src="https://github.com/laurenchristyt/open-wifi/assets/113244831/c36fc813-a805-4344-ad56-0e0bd5834f9f">
    
14. To use the curl test scripts which are included in the microservice repositories make sure to set the following environment variables before issuing a request:
```
export UCENTRALSEC="openwifi.wlan.local:16001"
export FLAGS="-s --cacert <your-wlan-cloud-ucentral-deploy-location>/docker-compose/certs/restapi-ca.pem"
```

## Troubleshooting Methods

Condition: Docker installed via `sudo apt-get`, and installed `docker-compose`.

### Trial 1, Update
1. `sudo apt-get update`
2. Close and reopen terminal

### Trial 2, Add current user to docker group, enabling it to run without `sudo` 
1. `sudo usermod -aG docker $USER`
2. Close and reopen terminal

### Checking methods
1. `sudo docker pull ubuntu:latest`
2. `sudo docker images`
3. `sudo docker run -i -t --name test ubuntu:latest`
4. Exit by typing 'exit'
5. `sudo docker ps -a`

### Renaming IP
1. `sudo nano /etc/hosts`
2. Add
   `127.0.0.1 openwifi.wlan local`
