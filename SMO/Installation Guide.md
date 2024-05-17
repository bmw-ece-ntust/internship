## Hardware Requirements
![image](https://github.com/bmw-ece-ntust/internship/assets/145204053/7a502952-ddf7-46a4-a72e-8510309d9793)

## Preface
The following guide will be based on Ubuntu 20.04.
Before starting the installation process of SMO-VES, git and docker-compose need to be
installed in the system first. It can be installed with the following command:
* Git
```
sudo apt update
sudo apt install git
```
* Docker
Install packages to allow apt to use a repository over HTTPS
```
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```
Add docker's official GPG key and add the Docker repository
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```
Update package index and install docker
```
sudo apt update
sudo apt install docker-ce
```
Start and enable docker
```
sudo systemctl start docker
sudo systemctl enable docker
```

## Software installation and deployment
Build
```
docker-compose build
```
Run
```
docker-compose up -d
```
Stop
```
docker-compose down
```
## Certificate installation
### Self signed certificate
Create ves-certificate directory on the host system
```
mkdir ~/ves-certificate
```
Go to ves-certificate directory and create self-signed certificate
```
cd ~/ves-certificate
openssl genrsa -out vescertificate.key 2048
openssl req -new -key vescertificate.key -out vescertificate.csr
openssl x509 -req -days 365 -in vescertificate.csr -signkey vescertificate.key -out vescertificate.crt
```
## Adding an entry
```
<IP Address of VM/Machine on which docker containers are running> smo-influxdb
```
## Check containers
```
docker-compose ps
```
All containers status should be "Up" except “smo-post-config”
## Check SMO-Collector API
On a browser, navigate to <IP Address of VM/Machine on which docker containers are running>:9999/v7/events/. 
SMO should run on HTTPS
## Check DMAAP API
On a browser, Navigate to <IP Address of VM/Machine on which docker containers are running>:5000/dmaapapi/v1/topics.
## Check Grafana Dashboard
On a browser, navigate to [IP Address of VM/Machine on which docker containers are running]:3000/  with admin/admin as username/password as it is the default one.
Then visit Dashboards > Manage section. "Events Demo" is ready to use.
