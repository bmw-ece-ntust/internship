### Configuring Netgear via IP
[1] use an ethernet cable to connect to OBB port on Netgear switch
[2] set ethernet driver ip as static from computer in the range of 192.168.0.0 with submask 255.255.0.0 (eg: 192.168.0.201)
for windowss :
```
control panel> network and internet> Network and Sharing Center
```
click on the ethernet then click on properties and find IPV4 and assign the static ip


![image](https://github.com/user-attachments/assets/78728dbb-e56f-4f31-ad89-69278d446864)

[3] open web browser and go to switch ip (by default, OBB port use http://192.168.0.239/) and login using credentials


[4] try to assign the configuration below


```
VLAN 2 : OAM (10.100.100.254/24) PORT : 1
VLAN 3 : N2N3 (192.168.2.254/24) PORT : 3
VLAN 4 : N6 (192.168.6.254/24)   PORT : 4
VLAN 5 : Internet (172.16.15.254/24) PORT : 5
```


![image](https://github.com/user-attachments/assets/ff095bce-e473-490f-9468-980359e5f08a)


![image](https://github.com/user-attachments/assets/aedc399a-7ae8-4661-9e88-6d6cbaca0236)


![image](https://github.com/user-attachments/assets/013bce0a-bb65-4e51-9759-27048c0d1ea0)


![image](https://github.com/user-attachments/assets/4caae918-1e99-4592-a1a9-6e2afb585aed)


![image](https://github.com/user-attachments/assets/f5a7e2a4-9ba5-43de-86f1-de2c3777f151)
