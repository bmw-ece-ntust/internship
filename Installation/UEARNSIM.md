
## UERANSIM
> [!NOTE]
> Make sure you have enough space in your VM by making a bigger storage. In this example I'm using 8GB (~~I tried 4GB~~ --> it didn't work)
> Make sure to use Ubuntu 20.04 version (~~I tried 22.04 version~~ --> it didn't work)

## A bit about 5G, OAI, and USRP
![image](https://github.com/bmw-ece-ntust/internship/assets/123353805/6f3d3d54-e43e-46ff-a9d0-33ad421d6626)

## Installing UERANSIM

1. Update and Upgrade UERANSIM VM
```
sudo apt update
sudo apt upgrade
```
<img width="912" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/65e360b3-15dd-45e8-b6b3-01f9386d38d5">
<img width="912" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/afa2ea07-2f63-4dc4-9171-12644edf2ae4">

>P.S. YEP! it might take a while just be patient :>

<img width="715" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/4ae9c0a8-838c-45eb-b901-45a2e4338aa2">

2. Installing Tools
```
sudo apt install make
sudo apt install g++
sudo apt install libsctp-dev lksctp-tools
sudo apt install iproute2
sudo snap install cmake --classic
```
<img width="912" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/ac4043f5-c47b-4681-aa78-e2747079083f">

<img width="912" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/93b0ed6e-f8cd-4c6e-98ce-fdcb3f0ac5f4">

<img width="912" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/e5db0f23-87d3-404f-9eb0-0bcff71193b4">
<img width="496" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/f33b621d-dc2f-4961-bbf1-2d7364b1215f">

3. Downloading UERANSIM
```
sudo apt install git
git clone https://github.com/aligungr/UERANSIM
cd UERANSIM
git checkout v3.1.0
```
<img width="912" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/691c8da5-9b4b-44aa-bfd5-46d099fef170">

![image](https://github.com/bmw-ece-ntust/internship/assets/123353805/4b7bc1f7-6167-45a7-b299-1f261bef67fd)

<img width="912" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/55b4dc1f-8a0e-4bbf-a2c2-5cb18f09c5d5">

4. Building UERANSIM
```
make
```
![image](https://github.com/bmw-ece-ntust/internship/assets/123353805/946184fa-0b49-451b-9173-8153f0229d25)

<img width="912" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/f73a7d19-ec3c-4f0a-9415-48b03210f1aa">
![Uploading image.png…]()

sudo : run as administrator
sudo nano : used to edit the file

- modifying bashrc file
```
sudo nano ~/.bashrc
export GOPATH=$HOME/go
export GOROOT=/usr/local/go
export PATH=$PATH:$GOPATH/bin:$GOROOT/bin
export GO111MODULE=auto
source ~/.bashrc
```

> Insert the first command
> using keyboard arrow, go to the top of the terminal and insert the second until fifth line
> `Ctrl + X` --> `Y` --> `Enter`
> Insert the last command to run the file and save the effect of the changes
<img width="800" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/9e8f5329-3984-4c2e-8af0-17d887b409a7">

- Install MongoDB
```
sudo apt -y update
sudo apt -y install mongodb wget git
sudo systemctl start mongodb
```
<img width="800" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/720d5c31-8ee7-4b4a-95f2-98545f41e017">
<img width="800" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/4d695da1-b537-496a-850c-f202edb1719a">

<img width="800" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/0064f17f-d0ef-423e-9040-9ce3c6aa4e81">

- Install Control-Plane and User-Plane Supporting Packages
```
sudo apt -y update
sudo apt -y install git gcc g++ cmake autoconf libtool pkg-config libmnl-dev libyaml-dev
```
<img width="800" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/babba440-76c9-47c5-83eb-cd55112071a3">

<img width="800" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/2705c56d-a835-4d8b-a576-76ca4b9edc48">

- Setting up Linux Host Network
```
sudo iptables -t nat -A POSTROUTING -o enp0s1 -j MASQUERADE
sudo iptables -A FORWARD -p tcp -m tcp --tcp-flags SYN,RST SYN -j TCPMSS --set-mss 1400
sudo systemctl stop ufw
```
> [!TIP]
> Use `ifconfig` to know the <dn_interface> of your ubuntu. From the image below we can see that `enp0s1` is the <dn_interface> of my mac
<img width="800" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/a71a2780-3b15-4e5f-a048-3a3aec079df0">


6. 
7. D
