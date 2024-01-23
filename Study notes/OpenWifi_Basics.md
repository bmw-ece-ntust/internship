# **OpenWifi**

**Point of Discussion**
- Learning OpenWifi's role in system architecture
-  Learning how to integrate OpenWifi to middleware
-  Learning OpenWifi's provisioning functionality

## **Action Items**
- Develop a script for translation that converts OpenWiFi commands (C) into Aruba commands (Python).
- Try [OpenWiFi WLAN Testing](https://github.com/Telecominfraproject/wlan-testing) into the OpenWiFi Controller

**Main Reference**:
- [OpenWiFi - Telecom Infra Project Website](https://openwifi.tip.build/)
- [Telecom Infra Project's Youtube channel](https://www.youtube.com/@telecominfraproject)
- Meeting with mas Nino

## **Introduction**
OpenWifi, a free and open-source disaggregated Wi-Fi system, provides service providers and to overcome the limitations of proprietary Wi-Fi infrastructure.

## **Architecture Flow**

Aruba AP -> Aruba Controller -> Crawler -> uCentral Client -> uCentral Deploy

## **Key Repositories for OpenWifi**

- ### **Cloud Controller SDK**

    Centralized repository for the Cloud Controller software development kit that enables the management and control of Wi-Fi networks through a cloud-based approach.
    It offers standardized APIs.

- ### **Access Point Firmware**
    Dedicated repository housing the firmware for enterprise-grade Access Points.
    It provides the firmware for the communication of Access Points in the OpenWifi ecosystem.

<img width="428" alt="image" src="https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-11-Lauren/images/Components.png">

## **Vendor Integration and Middleware**
OpenWifi supports different vendors that adopt its firmware, allowing them to be centrally controlled by the Cloud Controller.

<img width="428" alt="image" src="https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-11-Lauren/images/SupportedVendors.jpg">

    Aruba Access Points (and other unsupported vendors), is not compatible with the Cloud Controller from OpenWifi, and requires middleware for integration. The middleware acts as a bridge, enabling communication between Aruba Access Points and the Cloud Controller.

## **Ports**
Exposed ports dependencies (can be checked with `docker-compose ps` command)

`127.0.0.1:80/443 tcp` - OpenWiFi-uCentralGW-UI

`127.0.0.1:8080/8443 tcp` - OpenWiFi-Provisioning-UI

`127.0.0.1:5912/tcp` - rttys dev

`127.0.0.1:5913/tcp` - rttys user

`0.0.0.0:15002/tcp` - OpenWiFi-uCentralGW websocket

`127.0.0.1:16002/tcp` - OpenWiFi-uCentralGW REST API public

`0.0.0.0:16003/tcp` - OpenWiFi-uCentralGW fileupload

`127.0.0.1:16102/tcp` - OpenWiFi-uCentralGW alivecheck

`127.0.0.1:16001/tcp` - OpenWiFi-uCentralSec REST API public

`127.0.0.1:16101/tcp` - OpenWiFi-uCentralSec alivecheck

### **Provisioning-UI (Port 8443)**

#### **General**
OpenWiFi Provisioning UI runs on ports 127.0.0.1:8080/8443 tcp.
This interface is for the provisioning process, allowing users to configure and manage devices in the Wi-Fi network.

OpenWifi's Provisioning service caters to diverse use cases, spanning enterprise networks, service provider access, and hotspots.
Managed services cover areas like roaming, client shared-key management, client steering, mobile offload, QoS-based services, and Layer 2 and Layer 3 breakout and overlay options.

<img width="428" alt="image" src="https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-11-Lauren/images/Port8443.png">


#### **Entities and Configuration**

The Provisioning service offers a view into the network, providing entity-based control.
Configuration templates operate through the web interface and APIs for controller integration and OSS/BSS integration.

<img width="428" alt="image" src="https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-11-Lauren/images/Entity.png">
