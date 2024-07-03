# 1. WireGuard Installation Documentation

### Reference
[Sylvia's Wireguard Installation Guide](https://hackmd.io/7uFpsm4PRu-igD04dZhrlw?view)

## 1.1 Download the installation file that match your OS
![image](assets/Wireguard1.png)

## 1.2 Add new tunnel
![image](assets/Wireguard2.png)

## 1.3 Put conf. file in tunnel
![image](assets/Wireguard3.png)

content of .conf file:
```
[Interface]
PrivateKey = PRIVATE_KEY
Address = 10.1.0.102/32
DNS = 192.168.8.72, 8.8.8.8, 8.8.4.4
MTU = 1420

[Peer]
PublicKey = caLigu7cD+4nMajYP0rfRyIYlQKppbD9dBq8xilhJmg=
AllowedIPs = 10.1.0.0/24, 192.168.8.0/24
Endpoint = 140.118.162.82:54087
PersistentKeepalive = 25
```
## 1.4 click connect
* unconnected

![image](assets/Wireguard4.png)
* connected

![image](assets/Wireguard5.png)

## 1.5 ping test

![image](assets/Wireguard6.png)

# 2. Nokia Switch

## 2.1 SSH Switch
```code=
ssh oranadmin@192.168.8.60
```
![image](assets/Wireguard7.png)
