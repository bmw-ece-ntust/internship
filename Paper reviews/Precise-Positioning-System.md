# Paper Review

## Table of Contents
- [Paper Review](#paper-review)
  - [Table of Contents](#table-of-contents)
  - [Main Reference](#main-reference)
- [Key Takeaway](#key-takeaway)
- [Introduction](#introduction)
- [Concept](#concept)
  - [Triangulation Concept \& Cellular Network-based Positioning Systems](#triangulation-concept--cellular-network-based-positioning-systems)
  - [Wi-Fi-based Positioning Systems and Bluetooth Beacons](#wi-fi-based-positioning-systems-and-bluetooth-beacons)
  - [Analysis and Location Engine (IEEE 802.11ax)](#analysis-and-location-engine-ieee-80211ax)
    - [- Estimated System](#--estimated-system)
    - [- Calibration System](#--calibration-system)
- [Execution](#execution)
  - [Bulding Prototype](#bulding-prototype)
  - [Fingerprinting to Locate the AP](#fingerprinting-to-locate-the-ap)
  - [Estimated Process (AP Deployment)](#estimated-process-ap-deployment)
- [System Design Implementation](#system-design-implementation)
  - [Device Information Acquisition](#device-information-acquisition)
  - [Position Visualization](#position-visualization)
  - [Vertical Position Detection](#vertical-position-detection)
  - [Assistant Service Implementation](#assistant-service-implementation)
- [Analysis and Evaluation](#analysis-and-evaluation)
  - [System Response Evaluation](#system-response-evaluation)
  - [Data Transmission](#data-transmission)
  - [System Latency Evaluation](#system-latency-evaluation)
- [Conclusion](#conclusion)

## Main Reference
- [On Construction of Precise Positioning System via IEEE 802.11ax](https://ieeexplore.ieee.org/document/10071724)

# Key Takeaway
- Wi-Fi based positioning systems provides better accuracy than celular network-based positioning systems.
- Wi-Fi connection engine utilizing Analysis and Location Engine (ALE) such as IEEE 802.11ax and Bluetooth Beacon combination offers accurate device positioning with low computational cost. 

- Cesium offers 3D visualization to provide the representation of Wi-Fi networks and device positions.


# Introduction
This journal's goal is to demonstrate fast and high-capacity Wi-Fi to help system administrators track and manage the network infrastructure.

This journal introduces a Wi-Fi connection engine using an analysis and locations engine (ALE). **ALE** provides information such as **MAC address, location, floor details**, and the building where a device is located. The study then presents a **web visualization** of the Wi-Fi network monitoring system on a map using **Cesium** (3D visualizations).

To evaluate the user experience, **latency** is used as a metric to **measures the delay** in data transmission.

# Concept
## Triangulation Concept & Cellular Network-based Positioning Systems
Positioning systems are used to determine the **real-world positions of users**. The proposed method (cellular network-based positioning systems) uses 3 base stations (BSs) to calculate the position of a user through **triangulation**. For example, there are 3 target users with the position $(x_a,y_a)$ , $(x_b,y_b)$ , and$(x_c,y_c)$ . Then the distances from the target user to all BSs can be found with these formulas:

$d_a = \sqrt{(x_a - x_t)^2 + (y_a - y_t)^2}$

$d_b = \sqrt{(x_b - x_t)^2 + (y_b - y_t)^2}$

$d_c = \sqrt{(x_c - x_t)^2 + (y_c - y_t)^2}$

The **challenges** associated with these systems include issues related to convenience, scalability, and accuracy.

##  Wi-Fi-based Positioning Systems and Bluetooth Beacons
The primary focus of proposing a positioning system is to **enhance the accuracy** of the derived **position**. One of the things that can enhance accuracy is **hardware enhancements**, and according to the 5G white paper, there's potential for further expansion of position accuracy using **Wi-Fi APs**.

The experiment compares **Bluetooth beacons**, known for their **precise** positioning accuracy in small-scale scenarios, with **Wi-Fi-based positioning systems**. Wi-Fi-based systems provides accuracy of about 1 or 2 m with enough APs, but still **lacks in user location tracking**. Then Aruba Networks introduces the **Analysis and Location Engine (ALE)** for precise positioning through Wi-Fi 6, for accurate **visual representation** of APs and their signal strength. This is the scenario:

   <img width="428" alt="image" src="https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-11-Lauren/images/ALE.png">

This is a network case in that end devices connect to the Wi-Fi APs. All end devices connect to the **local controller (LC)** that consists of a **cluster of APs**, and the LC collects the information of end devices. Then, the detected data is **sent to ALE**. ALE requests and receives the VisualRF Maps, corresponding to the location of the end device after receiving the device information. The VisualRF Maps offer the wireless signal strength and coverage of the APs for the given area. Each circle in the VisualRF Maps represents an AP. The red area shows the highest signal strength, while the blue area is the worst.

   <img width="428" alt="image" src="https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-11-Lauren/images/VisualRF.png">


## Analysis and Location Engine (IEEE 802.11ax)

ALE (Analysis and Location Engine) uses two systems to figure out where a user is: the **"Estimated" system** and the **"Calibration" system.**

### - Estimated System
  
  This system uses a message called AP-AP RSSI 5 to calculate the **path-loss model** using **information collected** from end devices. The result is then used to create VisualRF Maps to show wireless signal strength and coverage.

### - Calibration System
  
  This system relies on **fingerprinting** data to determine the position of the end device. Each AP is connected to the network and sends its actual location to the local controller (LC). ALE then uses an algorithm based on RSSI, the path-loss model, and fingerprint data to calculate the device's location.

# Execution

## Bulding Prototype
When using the calibration process of ALE, we need to prepare the APs, which involves a fingerprinting process to **distinguish each AP from one another**. Here are the steps:

1. Selecting Target Building Location
2. Configuring Vertical Positioning
   
   ALE supports vertical positioning (it can determine the **height** or floor level within a building). To calibrate, information about the floors and central coordinates are needed for ALE to create a **building prototype** that understands the layout and positioning within each floor.

## Fingerprinting to Locate the AP
The fingerprinting process for locating the APs involves two main steps: the learning mode and the demo mode.

- ### Learning Mode
  
  To capture the actual positions of the APs. In this mode, a **predefined move route** is drawn for the fingerprinting testing. Essentially, this step is about gathering **real-world data** to understand how the signals from the APs vary across different locations.

- ### Demo Mode
  
  Once the learning mode is completed, the demo mode can do the **showcase** how the system can determine the user's position based on the collected data. It simulates user movement, and the system uses the gathered information to demonstrate accurate positioning. 

## Estimated Process (AP Deployment)
After setting up the APs, the geofences service is activated during the Estimated process to pinpoint the actual position. When a device **enters the route path**, the geofences service **notes the entry and computes the precise location**. The Estimated process then adjusts the user's coordinates accordingly. 

Once the APs are deployed, their **information is saved in the positioning database (PDB)**. Now, the system can switch from learning mode to demo mode. The PDB continuously stores the positions of each device. 

# System Design Implementation
The system includes Wi-Fi Data, the Web Server, and the 3D building model. Each AP captures the device’s information, and the data is saved in the Web server. The Web server combines and visualizes the user’s information with the 3D building models.

   <img width="428" alt="image" src="https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-11-Lauren/images/structure.png">
   
## Device Information Acquisition
The primary task of each AP is to capture device information. This involves utilizing the ALE API, which provides two main types: the **Publish/subscribe API** and the Polling API. The Polling API communicates with APs, and major services include the Station API (providing AP information) and the **Location API** (capturing end device information). The raw data obtained from the Location API, including details like MAC address and coordinates, requires transformation for visualization.

## Position Visualization
 The ALE provides a device visualization service, but for a more clear visualization, a Web-based 3D building visualization tool like Cesium is used. **Cesium creates 3D buildings on maps**. The system also uses SketchUP to build building models for testing environments.

## Vertical Position Detection
Traditional maps present information in 2D, but Wi-Fi users may move vertically. Detecting vertical positions involves considering RSSI values of all APs. The AP with the highest RSSI values is chosen to specify the vertical position, correlating with the corresponding floor. This method allows for deriving and visualizing users' vertical positions.

## Assistant Service Implementation
Though information on all devices can be illustrated in the 3D building model, readability can be improved with user-friendly services. These include:

- **View Scope Setting** to enable quick jumping to specific areas on the map, improving navigation efficiency.

- **Device Search** to search services (device search and timestamp search) help quickly target specific devices within a specified time interval.

- **Building Model Transparency** Setting so users can control building model transparency to balance visibility and readability.

- **Display/Hide Device Information** that allows users to toggle device information visibility for better map readability.

- **Heat Map** that visualizes user density, crucial for managing Wi-Fi usage and improving user experience.

- **History Location** that plots historical locations of a specific user based on collected records.

- **Building Information** points on building models link to building information, providing details like name and coordinates. Future plans involve integrating air quality information into the system.

# Analysis and Evaluation

## System Response Evaluation
In the system response evaluation, the experiment utilized a MacBook Air as the testing device and considered parameters such as system response time and screen frame rate. The results indicated that **network communication time** (influenced by network quality and data transmission) **is improtant in system responsiveness**. The proposed system exhibited **low network latency** (around 16 ms for TANet and 20 ms for 4G) for quick data reception. Also the **FPS were consistently high** (around 59 FPS).

   <img width="428" alt="image" src="https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-11-Lauren/images/result.png">

## Data Transmission
In data transmission between producer and consumer, four key parameters were considered in evaluation scenarios: data amount, partition, acks mode, and batch size. The evaluation focused on assessing data transmission latency between the data producer and process broker or process broker and data consumer. The results highlighted that **the latency increased with data amount** but remained acceptable for data sizes **below 100 MB**. This indicated that the system maintained low latency for regular Wi-Fi usage scenarios.

## System Latency Evaluation
In the system latency evaluation, the experiment explored the relationship between the number of partitions and system performance. The best outcome was achieved with four partitions for both Windows and Ubuntu platforms. So that **optimized number of partitions** provides a balance between work distribution and system performance.

# Conclusion
Before, Wi-Fi struggled with pinpointing end device locations. IEEE 802.11ax (ALE) changed that by offering precise positioning with low computational cost. The proposed visualization platform proved that Wi-Fi with IEEE 802.11ax enhanced capabilities without sacrifing speed.