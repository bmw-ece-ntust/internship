# Energy Efficient Ethernet (EEE)

## Table of Contents
- [Energy Efficient Ethernet (EEE)](#energy-efficient-ethernet-eee)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Hardwares in Universitas Indonesia that supports EEE](#hardwares-in-universitas-indonesia-that-supports-eee)
  - [Configuring 802.3az Energy Efficient Ethernet Standard (Aruba)](#configuring-8023az-energy-efficient-ethernet-standard-aruba)
  - [Configuring 802.3az Energy Efficient Ethernet Standard (Cisco)](#configuring-8023az-energy-efficient-ethernet-standard-cisco)
    - [Configuration](#configuration)
    - [Monitoring EEE](#monitoring-eee)


## Overview  
Energy-efficient Ethernet (EEE) reduces power consumption in accordance with IEEE 802.3az. Energy Efficient Ethernet is a technology defined as IEEE 802.3az to reduce switch power consumption during periods of low network traffic, to reduce power consumption by more than 50 percent while remaining fully compatible with existing devices. It detects link status, allowing each port on the switch to power down into a standby state when a connected device is not active. Second, it detects cable length and adjusts the power used for transmission accordingly. 

<img width="428" alt="image" src="https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-11-Lauren/images/eee.png">

## Hardwares in Universitas Indonesia that supports EEE
- Aruba 2540 24G PoE+ 4SFP+ (JL356A)
- Aruba 3810M (JL0755A)
- Aruba 505 Indoor Access Point
- Cisco Catalyst 2960-X
- HPE 1950 (JH295A)
- D-Link DGS-F1018P-E

## Configuring 802.3az Energy Efficient Ethernet Standard (Aruba)
Most new models of Aruba APs support the 802.3az or Energy Efficient Ethernet standard, which allows the APs to consume less power during periods of low data activity. This setting can be enabled for provisioned Instant APs or Instant AP groups through the wired port profile.

In the CLI
To enable 802.3az Energy Efficient Ethernet standard on an Instant AP and associate it with an ethernet port:

```
(Instant AP)(config)# wired-port-profile <profile_name>

(Instant AP)(wired ap profile <profile_name>)# dot3az

(Instant AP)(wired ap profile <profile_name>)# exit

(Instant AP)(config)# enet0-port-profile <profile_name>

(Instant AP)(config)# end

(Instant AP)# commit apply

To view the dot3az status for the ethernet ports:

(Instant AP)# show port status
```
Output

Port Status

-----------

| Port | Type | Admin-State | Oper-State | STP-State | Dot3az |
| -------- | -------- | -------- |-------- | -------- | -------- |
| eth0 | 5GE | up | up | N/A | Enable |
| eth1 | GE | up | down | N/A | Disable |

## Configuring 802.3az Energy Efficient Ethernet Standard (Cisco)

### Configuration
1. Enter global configuration mode.
   ```
   Switch# configure terminal
   ```
2. Specify the interface to be configured, and enter interface configuration mode.
   ```
   Switch(config)# interface gigabitethernet1/0/1
   ```
3. Enable EEE on the specified interface. When EEE is enabled, the device advertises and autonegotiates EEE to its link partner.
    ```
    Switch(config-if)# power efficient-ethernet auto
    ```
4. To disable EEE on the specified interface:
   ```
   Switch(config-if)# no power efficient-ethernet auto
   ```
5. Save entries in the configuration file.
   ```
   Switch# copy running-config startup-config
   ```

### Monitoring EEE
- Displays EEE capabilities for the specified interface.
  ```
  show eee capabilities interface interface-id
  ```
- Displays EEE status information for the specified interface.
  ```
  show eee status interface interface-id
  ```