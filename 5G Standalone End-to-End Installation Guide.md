# 5G Standalone End-to-End Installation Guide
---
Overview
---
srsRAN 4G 22.04 brings 5G SA support to both srsUE and srsENB. 5G SA features can be enabled via the configuration files of both srsUE and srsENB. This application note demonstrates how to configure a 5G SA network using srsRAN 4G, a 3rd-party core (Open5GS) and ZeroMQ (ZMQ). Using ZMQ means there is no need for physical RF-hardware.

A gNB (gNodeB) is a node in a cellular network that provides connectivity between user equipment (UE) and the evolved packet core (EPC). A gNodeB is the functional equivalent of a base station in a traditional cellular network.
![Screenshot 2024-02-08 at 19.23.09](https://hackmd.io/_uploads/Hk3hvSzsT.png)

---
1. Download Ubuntu
> Windows Users:
https://ubuntu.com/download/desktop

> Macbook Users:
Download paralel desktop and download ubuntu
![](https://hackmd.io/_uploads/H1OUronqa.png)
2. Open Terminal in Ubuntu
![Screenshot 2024-02-03 at 10.01.07](https://hackmd.io/_uploads/H1YjHsh9T.png)
3. Insert the following codes into the terminal
```
sudo apt-get install cmake make gcc g++ pkg-config libfftw3-dev libmbedtls-dev libsctp-dev libyaml-cpp-dev libgtest-dev
```
> Code above is used to install all dependencies and build tool altogether, including:
-- cmake
-- gcc
-- libfftw
-- libsctp
-- yaml-cpp
-- PolasSSL/mbedTLS
-- googletest
```
sudo apt-get install libuhd-dev uhd-host
```
> Code above is used to install UHD.The srsRAN Project supports split-8 and split-7.2 fronthaul. Split-8 fronthaul is supported via UHD for USRP devices.
```
git clone https://github.com/srsRAN/srsRAN_Project.git
```
> Code above is used to clone srsRAN_project git repository.
```
cd srsRAN_Project
mkdir build
cd build
cmake ../
make -j $(nproc)
make test -j $(nproc)
```
> Code above is used to build the codebase into the address srsRAN_Project/build/
```
sudo make install
```
> Code above is used to install the srsRAN Project gNB, instead of running it directly from the address srsRAN_Project/build/apps/gnb
4. Download Open5GS
(Open5GS is a C-language Open Source implementation for 5G Core and EPC. The following links will provide you with the information needed to download and set-up Open5GS so that it is ready to use with srsRAN 4G.)
```
sudo apt update
sudo apt install gnupg
curl -fsSL https://pgp.mongodb.com/server-6.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor
```
> Code above is used to import the public key used by the package management system.
```
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
sudo apt update
sudo apt install -y mongodb-org
sudo systemctl start mongod
sudo systemctl enable mongod
```
> Code above is used to install the MongoDB packages.
```
sudo add-apt-repository ppa:open5gs/latest
sudo apt update
sudo apt install open5gs
```
> Code above is used to install Open5GS easier with Ubuntu
```
sudo apt update
sudo apt install -y ca-certificates curl gnupg
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
```
> Code above is used to download and import the Nodesource GPG key
```
NODE_MAJOR=20
echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | sudo tee /etc/apt/sources.list.d/nodesource.list
```
> Code above is used to create deb repository
```
sudo apt update
sudo apt install nodejs -y
curl -fsSL https://open5gs.org/open5gs/assets/webui/install | sudo -E bash -
```
> Code above is used to run update and install WebUI of Open5GS
> 
5. 



---
Source
---
[srsRAN 5G SA End-to-End Documentation](https://docs.srsran.com/projects/4g/en/latest/app_notes/source/5g_sa_E2E/source/index.html?highlight=5G%20SA%20end-to-end)
