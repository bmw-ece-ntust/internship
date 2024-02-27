# **Crawling Method (Counting Method)**
Meeting Summary with Rafie Amandio

## **ARUBA WiFi AP Crawling Method Flowchart**
   <img width="428" alt="image" src="https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-11-Lauren/images/FlowchartCrawler.png">


## **Point of Discussion**
- Learning the data collection process
- Learning the impact of each raw data type
- Leaning the AI integration process
- Learning the counting and crawling method

## **Action Items**
- Try the crawling method

## **Table of Contents**
- [**Crawling Method (Counting Method)**](#crawling-method-counting-method)
  - [**ARUBA WiFi AP Crawling Method Flowchart**](#aruba-wifi-ap-crawling-method-flowchart)
  - [**Point of Discussion**](#point-of-discussion)
  - [**Action Items**](#action-items)
  - [**Table of Contents**](#table-of-contents)
  - [**Overview**](#overview)
  - [**Data Collection Process**](#data-collection-process)
    - [**Controller-AP Connection**](#controller-ap-connection)
    - [**Wi-Fi Signal Strength Measurement (RSSI)**](#wi-fi-signal-strength-measurement-rssi)
    - [**AI Integration for Location Prediction**](#ai-integration-for-location-prediction)
    - [**Counting Method**](#counting-method)
    - [**Raw Retrieved Data**](#raw-retrieved-data)
    - [**EIRP Impact**](#eirp-impact)
    - [**ARM (Adaptive Radio Management)**](#arm-adaptive-radio-management)
    - [**Crawling Method for AI Training**](#crawling-method-for-ai-training)


## **Overview**
In OpenWifi, each Access Point (AP) is connected to a dedicated controller, typically one controller per building, making a API-driven communication system. The goal is to develop an indoor positioning system utilizing Wi-Fi data, enabling hotspot location determination based on Wi-Fi signal strength.

## **Data Collection Process**

### **Controller-AP Connection**

Each building has one controller connected to multiple APs, forming a centralized network architecture.
The controller provides an API for straightforward interaction, allowing data retrieval by querying the controller API to obtain the AP's positions.


### **Wi-Fi Signal Strength Measurement (RSSI)**
The controller signals the AP to measure RSSI (Received Signal Strength Indication) from nearby access points to the hotspot.
RSSI is a measure of signal strength, critical for determining proximity and location.

### **AI Integration for Location Prediction**

Raw data, including AP type, current RSSI, band, channel, timestamp, AP name, BSSID, and EIRP, is sent to an AI system for analysis.
AI processes this data to predict the hotspot location based on Wi-Fi signal strength and other relevant parameters.
Counting Method:

### **Counting Method**
Iteration is employed to ensure data separation, especially considering the multitude of APs. Each iteration helps identify the source AP for each data point.


### **Raw Retrieved Data**
AP-Type: Classification of the AP.
Curr-rssi: Current RSSI, indicating signal strength.
Band: Frequency range used (e.g., 2.4 GHz or 5 GHz).
Channel: Specific frequency for data transmission.
Timestamp: Date and time of data recording.
Ap-name: Name of the AP retrieving the data.
BSSID: Basic Service Set Identifier, a unique identifier for a wireless access point.
EIRP (Transmit Power): Influences signal strength; higher EIRP implies stronger signals but potential interference.
Considerations:

### **EIRP Impact**

Higher EIRP generally indicates stronger signals but may lead to increased interference.
Consideration for EIRP is crucial, as it affects signal strength and potential interference.

### **ARM (Adaptive Radio Management)**

ARM is utilized to dynamically adjust EIRP, providing a balance between signal strength and interference.
A consideration in optimizing EIRP for effective indoor positioning.

### **Crawling Method for AI Training**
To train the AI for indoor positioning, a crawling method is employed.
Specific points in the room are set with known coordinates, enabling AI training to correlate RSSI values from each AP to distinct locations.
AI is trained to recognize the RSSI values associated with each access point at predefined coordinates, forming the basis for accurate hotspot location predictions.