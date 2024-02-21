# 【G Release】 Installation Guide of Near-RT RIC Platform

## Hardware requests:
- **RAM**: 8G RAM
- **CPU**: 6 core
- **Disk**: 40G Storage

## Installation Environment:
- **Host**: Ubuntu 20.04 LTS (Focal Fossa)

## 1. Install the Docker, Kubernetes and Helm 3

### 1.1 Open terminate (Ctrl+Alt+T)

### 1.2 Become root user:
> **Note**: All the commands need to be executed as root.

```bash
sudo -i
```
![image](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-16-Taqi/Study%20notes/images/1.2.png)
### 1.3 Install the Dependent Tools:
```bash
apt-get update
apt-get install -y git vim curl net-tools openssh-server python3-pip nfs-common
```
![image](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-16-Taqi/Study%20notes/images/1.3.1.png)

![image](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-16-Taqi/Study%20notes/images/1.3.2.png)

### 1.4 Download the source code of RIC Platform:
```bash
cd ~
git clone https://gerrit.o-ran-sc.org/r/ric-plt/ric-dep -b g-release
```
![image](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-16-Taqi/Study%20notes/images/1.4.png)
### 1.5 Execute the Installation Script of the Docker, Kubernetes and Helm 3:
```bash
cd ric-dep/bin
./install_k8s_and_helm.sh
```
![image](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-16-Taqi/Study%20notes/images/1.5.1.png)
![image](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-16-Taqi/Study%20notes/images/1.5.2.png)
![image](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-16-Taqi/Study%20notes/images/1.5.6.png)
![image](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-16-Taqi/Study%20notes/images/1.5.7.png)

