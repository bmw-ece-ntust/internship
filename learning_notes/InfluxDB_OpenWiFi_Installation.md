>Michael Harditya (TEEP)
# Learning Notes
### Goals
- Install OpenWiFi and InfluxDB into Linux VM (Ubuntu 22.04)

### OpenWiFi Installation
For installation can refer to Lauren's branch: [Installation](https://github.com/NTUST-BMW-Lab/internship/blob/2024-TEEP-Lauren/installation/OpenWifi-Installation-Guide.md#openwifi-installation)
### InfluxDB Installation (Docker Version)
1. pull the InfluxDB container using ``` docker pull influxdb:2.7.5```
2. **persist data** from the InfluxDB container into the working directory of the host file system, by create or change the current directory to the folder to store the data of the database. For example, create new directory use ``` mkdir path/to/influxdb-docker-data-volume && cd $_```
3. run ``` docker run -p 8086:8086 -v $PWD:/var/lib/influxdb influxdb```, the flag ```-v or --volume``` is the data *inside* the container to the current working directory. **Make sure to change the working directory to the directory used for saving the data**.
4. open browser and browse ```localhost:8086```

Explanations:
8086 is the port usually used for InfluxDB, defined in step 3.

### Troubleshooting Docker on Oracle VM (Ubuntu 22.04)
*Notes: Updated version of troubleshooting specifically for OpenWiFi installation via Docker is moved to Lauren's branch  [Troubleshooting Methods](https://github.com/NTUST-BMW-Lab/internship/blob/2024-TEEP-Lauren/installation/OpenWifi-Installation-Guide.md#troubleshooting-docker-permissions)*

make sure Docker installed via ```sudo apt-get```, and installed ```docker-compose```.

#### Permission Denied
Permission denied exceptions occured when calling ```docker``` and ```docker-compose```:
```
raise DockerException( docker.errors.DockerException: Error while fetching server API version: ('Connection aborted.', PermissionError(13, 'Permission denied')))
```

It is possible because the docker is not permitted yet to read or write files, follow these steps:
1. `sudo groupadd docker`
2. `sudo usermod -aG docker $USER`
3. `newgrp docker`

Then try to run `docker run hello-world`, it should shows:
```
Hello from Docker!
This message shows that your installation appears to be working correctly.
```
If the output is same as the above, `docker-compose up -d` should not have any problem anymore.

#### Renaming IP
The docker deployment steps 7 of [OpenWiFi Installation](https://github.com/NTUST-BMW-Lab/internship/blob/2024-TEEP-Lauren/installation/OpenWifi-Installation-Guide.md#openwifi-installation) shows that the use of ```https://openwifi.wlan.local```, these needed to be manually assigned using static host name in both remote computer (if want to be accessed via internet) or local. Follow this steps:
1. `sudo nano /etc/hosts`, or other text editor available on the computer.
2. Add new entry for the host:
   * For local: `127.0.0.1 openwifi.wlan local`
   * For remote: `[OpenWiFi SDK Host IP] openwifi.wlan local`

Check if the host properly assigned by accessing a web browser open `https://openwifi.wlan.local`. It should shown the OpenWiFi UI.

### Successful Execution of OpenWiFi
![image](../images/OpenWiFiUI.png)
### Successful Execution of InfluxDB
![image](../images/InfluxDBUI.png)

