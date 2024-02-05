# Rogue AP

## **Table of Contents**
- [Rogue AP](#rogue-ap)
  - [**Table of Contents**](#table-of-contents)
  - [**Definition**](#definition)
  - [**Installation**](#installation)
    - [**Non-malicious Installations**](#non-malicious-installations)
    - [**Malicious Installations**](#malicious-installations)
  - [**Threat**](#threat)
  - [**Detection and Elimination**](#detection-and-elimination)
    - [**Traditional Method**](#traditional-method)
      - [**Periodic Surveys**](#periodic-surveys)
      - [**Third-Party Tools**](#third-party-tools)
      - [**Physical Security Measures**](#physical-security-measures)
      - [**Strong Security Protocols**](#strong-security-protocols)
    - [**Automated Tools (WiFi Controller + WiFi Management System)**](#automated-tools-wifi-controller--wifi-management-system)
      - [**Automated Detection and Localization**](#automated-detection-and-localization)
      - [**Continuous Network Monitoring**](#continuous-network-monitoring)
      - [**Rogue APs Detection and Classification**](#rogue-aps-detection-and-classification)
      - [**Localization of Rogue APs**](#localization-of-rogue-aps)
  - [**Aruba's WiFi Management System**](#arubas-wifi-management-system)
    - [**How it Works**](#how-it-works)
      - [**Air Scanning**](#air-scanning)
      - [**Wired Scanning**](#wired-scanning)
      - [**Gateways**](#gateways)
      - [**Routers Detection**](#routers-detection)
      - [**Maintaining Lists**](#maintaining-lists)


## **Definition**
- A wireless access point installed on a secure network without explicit authorization.
- Installed by well-meaning employees or malicious attackers.
  
## **Installation**
Rogue access points (APs) are installed through two primary methods.

1. Wired
   
   A rogue AP may be physically connected to an existing wireless access point, often accomplished by individuals gaining physical access to the network infrastructure. This can involve plugging in the rogue AP directly, allowing it to blend into the existing network. 

2. Wireless
   
   A rogue AP can be connected by enabling wireless sharing functionality in the OS. In this scenario, a device's OS is configured to act as a wireless AP.

### **Non-malicious Installations**
Non-malicious installations of rogue APs may occur when users on the network aim to enhance usability. For instance, users might add an access point to a computer with no available ports or extend the signal range to broaden the network's capabilities. While these actions are not inherently malicious, they can add security risks to the network. 

### **Malicious Installations**
Malicious installations involve attackers attaching rogue access points remotely, allowing them to gain unauthorized access to the network. The intent behind malicious installations is often to exploit vulnerabilities, conduct attacks, or facilitate unauthorized access. Overall, understanding the methods and motivations behind rogue AP installations is crucial for implementing effective network security measures.

## **Threat**
- Man-in-the-middle Attack
- Denial of Service (DOS) attacks
- Send fake SSIDs advertisements
  
## **Detection and Elimination**
Detecting and eliminating rogue access points (APs) involves a combination of traditional methods and automated tools to ensure comprehensive network security.

### **Traditional Method**

#### **Periodic Surveys**
Conduct scheduled surveys by physically walking around the building or campus to identify any unauthorized APs.

#### **Third-Party Tools**
Use third-party tools like inSSIDer or NetSpot to analyze and identify sources of wireless communication and to detect the rogue APs.

#### **Physical Security Measures**
Ensure safety of AP (no one plugs without proper authorization).

#### **Strong Security Protocols**
Implement robust security protocols, including the IEEE 802.11i standard.

### **Automated Tools (WiFi Controller + WiFi Management System)**

#### **Automated Detection and Localization**
Utilize WiFi Controller combined with a WiFi Management System, to automatically detect and localize rogue APs.

#### **Continuous Network Monitoring**
Deploy network-based tools that actively monitor the network in real-time, providing constant vigilance against potential threats.

#### **Rogue APs Detection and Classification**
Examples like Aruba's WiFi Management System can detect and classify rogue APs, distinguishing between authorized and unauthorized access points.

#### **Localization of Rogue APs**
Implement systems, such as NTUST's WiFi Management System, that not only detect rogue APs but also provide the capability to pinpoint their location within the network.

## **Aruba's WiFi Management System**

### **How it Works**

#### **Air Scanning**
Aruba monitored APs by continuously scan the air for wireless devices. It identifies new devices and keeps track of existing devices within the RF vicinity.

#### **Wired Scanning**
Each Aruba AP monitored specific traffic on the wire to gather  information. The process records MAC addresses and searches for routers and gateways within the network infrastructure.

#### **Gateways**
Aruba APs use default gateways in the network for classification. The MAC addresses of these gateways are shared with all APs in the RF vicinity.

#### **Routers Detection**
Routers are identified by inspecting the TTL value of received traffic. If the TTL is measured at specific values (31, 63, 127, or 254), the sender is likely a router. This helps on detecting potential rogue APs.

#### **Maintaining Lists**
Each Aruba AP maintains lists that include all relevant network entities. This includes lists of APs, stations, gateways, and wired MAC addresses.