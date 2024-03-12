# Data from Crawler

## Table of contents
- [Data from Crawler](#data-from-crawler)
  - [Table of contents](#table-of-contents)
- [Overview](#overview)
- [RSSI (Received Signal Strength Indication)](#rssi-received-signal-strength-indication)
- [Number of Clients (STAs)](#number-of-clients-stas)
- [EIRP (Transmission Power)](#eirp-transmission-power)
- [Usage Load](#usage-load)


# Overview
The data retrieved from Aruba is important for network management and optimization. There are a lot of data types retrieved, but in this case, there are few important data to be processed and important for optimizing indoor wifi positioning. They are signal strength, client distribution, transmission power, and network usage load.

# RSSI (Received Signal Strength Indication)
The controller instructs the APs to gauge the strength of signals received from neighboring APs near the hotspot. This measurement is known as RSSI, that is important for determining the quality of wireless connectivity. The RSSI value is based on the transmission power of the AP. It helps identify areas with strong signals, weak signals, or potential signals. This is important because it helps in predicting how far away something is and exactly where it's located within the coverage area.

For training the AI to find positions indoors. This involves marking specific spots in the room with known coordinates. These spots act as reference points for the AI to learn from. By collecting RSSI values from each access point at these known locations, the AI can create a map of signal strengths across the area. This data allows the AI to associate different signal strengths with specific locations, forming the accurate predictions of hotspot locations within the indoor environment.

# Number of Clients (STAs)
The Overview dashboard of Aruba displays the information about all the clients connected to a managed device within the network hierarchy.

<img width="428" alt="image" src="https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-11-Lauren/images/ClientsPage.png">

The Clients window provides information about all the devices connected to a managed device within the network hierarchy. It gives insights into the health, band, data speed, signal quality, and operating systems of the wireless clients.

- Health
  
  This section displays the health score of wireless clients connected to APs. The health score categories typically include Good, Fair, Poor, or Unknown. 

- Band
  
  The Band section lists the wireless clients categorized under the 2.4 GHz and 5 GHz radio bands. 

- Data Speed
  
  This part of the window presents the data speed (measured in bits per second, bps) of the wireless clients connected to APs. 

- Signal Quality
  
  The Signal Quality section displays the Signal-to-Noise Ratio (SNR) ranges of the wireless clients connected to APs. SNR is a crucial metric that measures the quality of the wireless signal received by client devices. 

- Operating System
  
  This section provides information about the distribution of client devices based on the operating systems they are running.

# EIRP (Transmission Power)
EIRP is a measure of the power emitted by a wireless transmitter, accounting for the antenna's gain and the power delivered to it. A higher EIRP typically signifies a stronger signal, which can result in improved coverage and better signal quality for connected devices. 

However, it's essential to consider the potential drawbacks of higher EIRP levels. Increased EIRP can also lead to elevated levels of signal interference, especially in densely populated areas where multiple wireless networks may operate in close proximity. This interference can degrade the performance and reliability of the wireless network, resulting in slower speeds and increased packet loss. Therefore, while higher EIRP values can enhance signal strength, careful consideration and optimization are necessary to minimize interference and maintain optimal network performance.

# Usage Load

The Usage page offers a summary of the activity and performance within the network. It provides information about the utilization of APs, clients, as well as identifies low-performing Wi-Fi access points and clients.

<img width="428" alt="image" src="https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-11-Lauren/images/UsagePage.png">

- TOP ACCESS POINTS
  
  This section lists the top five access points based on the highest volume of data transmitted or received.

- TOP CLIENTS
  
  Similarly, the top clients section displays the five clients with the highest data transmission or reception volumes.

- LOW PERFORMING WI-FI
  
  This section focuses on highlighting access points that are performing below expectations. 

  - Highest noise floor
    
    Administrators can view the top five access points with the highest noise floor levels in either the 2.4 GHz or 5 GHz frequency bands. 

  - Busiest Channel
    
    This section identifies the five access points with the highest percentage of channel utilization in either the 2.4 GHz or 5 GHz bands.

  - Highest Interference
    
    Similar to the busiest channel section, this part highlights the five access points experiencing the highest levels of interference in the 2.4 GHz or 5 GHz bands. 

- LOW PERFORMING CLIENTS
  
  This section provides details on clients that are experiencing performance issues, such as low signal quality, poor goodput, or slow data speeds.