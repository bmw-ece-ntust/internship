# 5GS Installation Guide on Ubuntu
---
## Installation step

To begin, the user must firstly install DBMongo package manager before proceeding to install 5GS

enter the following command on linux terminal to install DBMongo

importing public key
```
$ sudo apt update
$ sudo apt install gnupg
$ curl -fsSL https://pgp.mongodb.com/server-6.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor
```
then create a list file
```
sudo nano /etc/apt/sources.list.d/mongodb-org-6.0.list
```


```
$ echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
```


enter the following command on linux terminal to install 5gs 
```
$ sudo add-apt-repository ppa:open5gs/latest
$ sudo apt update
$ sudo apt install open5gs
```
output for first command
![image](https://github.com/bmw-ece-ntust/internship/assets/123167913/6bb35f64-306e-47d7-89a0-3eb52e25ecb1)
output for second command
![image](https://github.com/bmw-ece-ntust/internship/assets/123167913/b487d3a0-ed6b-472a-a95d-aac5e05593b7)


Preparing webUI for 5Gs
firstly, install node.js
run the following command
```
# Download and import the Nodesource GPG key
 $ sudo apt update
 $ sudo apt install -y ca-certificates curl gnupg
 $ sudo mkdir -p /etc/apt/keyrings
 $ curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
```
```
 $ NODE_MAJOR=20
 $ echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | sudo tee /etc/apt/sources.list.d/nodesource.list
```

```
 # Run Update and Install
 $ sudo apt update
 $ sudo apt install nodejs -y
```
after setting up node.js, run the following command to install webUI for 5Gs
```
$ curl -fsSL https://open5gs.org/open5gs/assets/webui/install | sudo -E bash -

```
