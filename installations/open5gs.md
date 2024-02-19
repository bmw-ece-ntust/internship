# Open5GS Installation Guide

## Overview
{to be written soon}

## 1. Installing Open5GS via a package manager:
Input:
```
sudo add-apt-repository ppa:open5gs/latest
sudo apt update
sudo apt install open5gs
```
Output:
{to be written soon}

## 2. Installing MongoDB for user plane machines communication database registry:
Input:
```
## installing curl command if it wasn't installed before
sudo apt-get install gnupg curl

## importing the public key
curl -fsSL https://pgp.mongodb.com/server-6.0.asc | \ sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg \ - dearmor

## creating the list file for the database (for Ubuntu v22.04)
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list

## updating and installing packages
sudo apt-get update
sudo apt-get install -y mongodb-org

## checking MongoDB's installation status and version
mongod --version
```
Output:
{to be written soon}

## 3. Installing WebUI of Open5GS
Input:
```
## installing Node.js
sudo apt update
sudo apt install curl
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install nodejs

## installing WebUI on port 3000 (default)
curl -fsSL https://open5gs.org/open5gs/assets/webui/install | sudo -E bash -
```
Output:
{to be written}

Now that the installation has been done, we will continue to the configuration within the network and other devices.
Open5GS components are configured using the local loopback address space (127.0.0.1, ex: MongoDB: 127.0.0.1:3000, MME-s1ap = 127.0.0.2:36412, AMF-sbi = 127.0.0.5:7777, etc. The rest of addresses can be checked in Open5GS documentation itself.) On localhost, in short.

## 4. Setting up a 4G/5G NSA Core
Input:
```
## setting up the S1AP IP address, PLMN ID, and TAC
nano /etc/open5gs/mme.yaml
s1ap:
-      - addr: 127.0.0.2
+      - addr: 192.168.50.2
     gtpc:
       - addr: 127.0.0.2
     metrics:
       addr: 127.0.0.2
       port: 9090
     gummei:
       plmn_id:
-        mcc: 999
-        mnc: 70
+        mcc: 001
+        mnc: 01
       mme_gid: 2
       mme_code: 1
     tai:
       plmn_id:
-        mcc: 999
-        mnc: 70
+        mcc: 001
+        mnc: 01
       tac: 1
     security:
         integrity_order : [ EIA2, EIA1, EIA0 ]

## setting up the GTP-U IP address
nano /etc/open5gs/sgwu.yaml
pfcp:
       - addr: 127.0.0.6
     gtpu:
-      - addr: 127.0.0.6
+      - addr: 192.168.50.6

## restarting daemons
sudo systemctl restart open5gs-mmed
sudo systemctl restart open5gs-sgwud
```
Output:
{to be written}

## 5. Setting up a 5G Core
Input:
```
## setting up the NGAP IP address, PLMN ID, TAC, and NSSAI
nano /etc/open5gs/amf.yaml
ngap:
-      - addr: 127.0.0.5
+      - addr: 192.168.50.5
     metrics:
         addr: 127.0.0.5
         port: 9090
     guami:
       - plmn_id:
-          mcc: 999
-          mnc: 70
+          mcc: 001
+          mnc: 01
         amf_id:
           region: 2
           set: 1
     tai:
       - plmn_id:
-          mcc: 999
-          mnc: 70
+          mcc: 001
+          mnc: 01
         tac: 1
     plmn_support:
       - plmn_id:
-          mcc: 999
-          mnc: 70
+          mcc: 001
+          mnc: 01
         s_nssai:
           - sst: 1
     security:

## setting the GTP-U address
nano /etc/open5gs/upf.yaml
pfcp:
       - addr: 127.0.0.7
     gtpu:
-      - addr: 127.0.0.7
+      - addr: 192.168.50.7
     subnet:
       - addr: 10.45.0.1/16
       - addr: 2001:db8:cafe::1/48

## restarting daemons
sudo systemctl restart open5gs-amfd
sudo systemctl restart open5gs-upfd
```
Output:
{to be written}

## 6. Adding a connection between PGWU/UPF-WAN with UE route
Input:
```
## enabling forwarding for both IPv4 and IPv6
sudo sysctl -w net.ipv4.ip_forward=1
sudo sysctl -w net.ipv6.conf.all.forwarding=1
  ### Add NAT Rule
  sudo iptables -t nat -A POSTROUTING -s 10.45.0.0/16 ! -o ogstun -j MASQUERADE
  sudo ip6tables -t nat -A POSTROUTING -s 2001:db8:cafe::/48 ! -o ogstun -j MASQUERADE

# configuring the firewall so the traffic won't be blocked
sudo ufw status
sudo ufw disable
sudo ufw status
```
Output:
{to be written}

## 7. Running Open 5GS Core
Input:
```
## running every service/container
sudo systemctl stop open5gs-mmed
sudo systemctl stop open5gs-sgwcd
sudo systemctl stop open5gs-smfd
sudo systemctl stop open5gs-amfd
sudo systemctl stop open5gs-sgwud
sudo systemctl stop open5gs-upfd
sudo systemctl stop open5gs-hssd
sudo systemctl stop open5gs-pcrfd
sudo systemctl stop open5gs-nrfd
sudo systemctl stop open5gs-scpd
sudo systemctl stop open5gs-ausfd
sudo systemctl stop open5gs-udmd
sudo systemctl stop open5gs-pcfd
sudo systemctl stop open5gs-nssfd
sudo systemctl stop open5gs-bsfd
sudo systemctl stop open5gs-udrd
sudo systemctl stop open5gs-webui

## checking whether Open5GS core is working or not
sudo systemctl is-active open5gs-*
```
Output:
{to be written}

To continue the infrastructure, it is said to dig more about UERANSIM. Will be searching more about that as soon as possible.
