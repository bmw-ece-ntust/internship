# Wifi Positioning Method

## Flowchart Reference

<img width="428" alt="image" src="https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-11-Lauren/images/Flowchart.png">

## Data Preparation
Data preparation involves getting information from the WiFi Controller about all the monitoring APs. Each of these monitoring APs shares details about the RSSI (signal strength) of the interfering APs it detects. 

### Data Reconstructing
In the data reconstructing step, we organize the RSSI data. If there are information from n monitoring APs (mAP), and each mAP has a bunch of detected interfering APs (iAP) along with their RSSI. After that, we have m interfering APs, and each of these has details about the mAPs they are associated with and their respective RSSI.

### Data Cleaning
We filter out RSSI values that are greater than -60 dB. 

Why is it necessary?
- Data cleaning helps to filter out interfering APs that are likely outdoors, as they usually have very low RSSI.
- Having stronger RSSI values is crucial for better WiFi positioning calculations, as weaker RSSI leads to less accurate distance calculations. 
- To distinguish between floors. In buildings where the walls are slim and there are doors made of wood, the attenuation is high between floors. So, APs on the same floor tend to have RSSI values greater than 60dB in their monitoring APs, while the attenuation between walls on the same floor is not significant.
- Get rid of APs that only have one or two RSSI values due to the trilateration algorithm that requires at least three reference APs to work.

## WiFi positioning computation
To figure out where interfering access points (APs) are located.

### Average RSSI_1h Computation
Find the average RSSI over the last hour by checking the RSSI values stored in databases.

### Estimating Interfering AP Locations
Using the average RSSI_1h data, make a guess about where the interfering APs might be with RSS-based indoor trilateration.

### Separating Interfering APs:
This is the two groups of interfering APs based on how long they stick around.

- ### Dynamic APs
    These are like visitors that pop up for a short time (less than an hour). They're most likely wireless APs created by users.

- ### Static APs
    These are the more permanent ones, hanging around for more than an hour. These are likely to be wired APs installed in the building. RSSI datasets are then analyzed to pick the strongest signal samples to provide the accurate location. 

## Data Visualization
Combine the results and display them in the same interference map.
