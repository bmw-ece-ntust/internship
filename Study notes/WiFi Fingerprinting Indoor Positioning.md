# WiFi Fingerprinting-based Indoor Positioning

## Indoor Positioning Technology
Several different wireless signals have been used by researchers to realize indoor positioning. Some mainstream indoor positioning technologies include ultrasonic indoor positioning, radio frequency identification (RFID) indoor positioning, ultra-wideband (UWB) indoor positioning, Bluetooth indoor positioning, infrared indoor positioning, ZigBee indoor positioning, and WiFi indoor positioning.

### WiFi
WiFi is a wireless local area network based on the IEEE802.11b standard. The objective of WiFi indoor positioning is to achieve positioning detection and tracking tasks in complex environments using a wireless local area network composed of wireless APs (including wireless routers). It uses a combination of empirical tests and signal propagation models to locate the connected mobile devices based on the location information of network nodes. The RSSI-based fingerprint positioning method is the current mainstream WiFi positioning method, and the positioning accuracy depends on the calibration, that is, density of points.

The WiFi positioning technique does not require additional hardware. It can provide indoor positioning by using the wireless network that is set up in the building and the smart device at the user's end.

## Indoor Positioning Methods

### Range-based WiFi indoor positioning method
The range-based indoor positioning method relies on the measurement of the distances between transceivers using the time of arrival (TOA), time difference of arrival (TDOA), and angle of arrival (AOA). In these methods, the RSS is first converted to a distance that uses the signal propagation model. Subsequently, the location of the mobile client is calculated using the geometric method (trilateral measurement).

Cons : The deployment of TOA, TDOA, and AOA-based positioning techniques is tedious and expensive because they require certain hardware or software modifications on the access point (AP). 

### WiFi fingerprinting-based indoor positioning
WiFi fingerprinting-based indoor positioning is a technique that leverages the unique characteristics of WiFi signals to determine the location of a device within a building. This approach, pioneered by the RADAR positioning system, involves collecting and associating WiFi signal data with specific indoor locations, making it effective even in the absence of Line of Sight (LoS). Each location within a building is characterized by a unique vector of Received Signal Strength (RSS) values from multiple Access Points (APs). This method does not require knowledge of the exact location of the APs and is resilient to multipath effects and non-LoS propagation, ensuring high positioning accuracy.

#### Positioning Principle
The positioning principle involves deploying wireless APs throughout the building and labeling them as AP1, AP2, ..., APn. At designated reference points, a smart terminal scans and records the signals emitted by these APs, along with their corresponding MAC addresses. The RSS, representing the signal intensity, varies with distance due to path loss, following a specific model. Consequently, the RSS vector (e.g., RSSi1, RSSi2, ..., RSSin) for each location becomes unique, similar to a human fingerprint, and can be used to identify that location.

#### Positioning process
The WiFi fingerprinting-based positioning process consists of two main stages: offline data collection and online matching. In the offline stage, reference points are strategically selected within the environment. The RSS data from various APs at these points are collected to construct RSS vectors, which are then stored in a database along with the coordinates of the reference points, creating an indoor fingerprint database or radio map. During the online matching stage, the RSS vector of the target location is compared against the database to determine its position, without the need for LoS distance measurements.

## WiFi Fingerprinting-based Positioning Algorithm
### K-nearest neighbour (KNN) positioning algorithm
Several algorithms are used to enhance the accuracy and efficiency of WiFi fingerprinting-based positioning. The K-Nearest Neighbour (KNN) algorithm compares the target location’s RSS vector with all fingerprints in the radio map, using Euclidean distance to determine the degree of matching. The average coordinates of the K nearest reference points are used to estimate the position. Improvements like Weighted KNN (WKNN) and adaptive WKNN (SAWKNN) further enhance accuracy by adjusting weights and K values dynamically based on signal strength.

### Clustering algorithm
Clustering algorithms, such as K-Means, are employed to optimize the management of radio maps, reducing calculation time and improving real-time performance. Affinity propagation clustering can automatically determine the number of clusters, while improved clustering methods like IPC and ML provide better localization by addressing sensitivity to outliers. The DBSCAN algorithm handles noise by marking low-density points as outliers, enhancing robustness.

### Support vector machine
Support Vector Machines (SVM) offer fast convergence and strong generalization capabilities, making them suitable for tasks like floor recognition and room-level prediction. Optimization techniques like the improved Support Vector Regression (SVR) further enhance prediction accuracy.

### Random forest
Random Forest (RF) algorithms, which combine multiple decision trees, excel in handling large databases and achieving high accuracy. Hybrid RF models that incorporate cross-validation and multiple antenna orientations at reference points have demonstrated significant improvements in positioning precision.

### Artificial neural
Artificial Neural Networks (ANN), particularly deep learning models, utilize the RSS values and location coordinates to train mapping relationships. Deep Neural Networks (DNN) with stacked autoencoders (SAE) and 1D Convolutional Neural Networks (CNN) are effective in feature extraction and classification, though their performance is limited by the complexity of the network and the adequacy of training data.