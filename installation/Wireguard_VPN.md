# 1. | Wireguard VPN Installation

### 1.1 | Download Wireguard VPN from [here](https://www.wireguard.com/install/)

![Wireguard VPN](../assets/vpn_installation/Screenshot%202024-07-03%20103852.png)

### 1.2 | Open the program and click add tunnel
![Add Tunnel](../assets/vpn_installation/Screenshot%202024-07-03%20111843.png)

### 1.3 | Put the conf. file as the tunnel configuration
Save this configuration as a conf. file :
```bash
[Interface]
PrivateKey = YOUR_PRIVATE_KEY
Address = YOUR_PRIVATE_KEY
DNS = YOUR_PRIVATE_KEY
MTU = YOUR_PRIVATE_KEY

[Peer]
PublicKey = YOUR_PUBLIC_KEY
AllowedIPs = YOUR_PRIVATE_KEY
Endpoint = YOUR_PRIVATE_KEY
PersistentKeepalive = YOUR_PRIVATE_KEY
```

![Conf](../assets/vpn_installation/Screenshot%202024-07-03%20112926.png)

### 1.4 | Click Activate
![Activate](../assets/vpn_installation/Screenshot%202024-07-03%20113000.png)

### 1.5 | Check the connection
#### 1.5.1 | Ping 192.168.8.9
```bash
ping 192.168.*.**
```
#### 1.5.2 | SSH to 192.168.8.60
```bash
ssh oranadmin@192.168.*.**
```

Password :
```bash
********
```

### Result
![Result](../assets/vpn_installation/Screenshot%202024-07-03%20004701.png)