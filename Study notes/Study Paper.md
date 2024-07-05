# Table of Content
1. [Paper 1](#paper-1)
   - [1.1 Summary](#11-summary)
   - [1.2 Data, Pros, and Cons](#12-data-pros-and-cons)
2. [Paper 2](#paper-2)
    - [2.1 Summary](#21-summary)
    - [2.2 Data, Pros, and Cons](#22-data-pros-and-cons)

---

## 1. Paper 1
![alt text](images/mimo1.png)
### 1.1 Summary

The primary challenge addressed by this paper is the inefficiency of traditional AMC methods, particularly the outer loop link adaptation (OLLA) technique, in rapidly changing environments and their inability to effectively utilize available signal-to-noise ratio (SINR) data.

The novelty of this work lies in the implementation of an online deep learning algorithm that can adapt to different environments, channel types, and user speeds. Unlike traditional methods, this approach leverages a fully connected neural network, initially trained on conventional algorithm outputs and incrementally retrained using service feedback.

### 1.2 Data, Pros, and Cons

**DATA**  
The data for the online deep learning algorithm in the paper is generated through system-level simulations. 

**FEATURES**
- Subband SINR Measurements: Signal-to-noise-plus-interference ratio for each user antenna.
- CQI (Channel Quality Indicator): Reported by the user equipment.
Time Period from the Last Sounding: Time elapsed since the last sounding reference signal (SRS) measurement.
- RSRP (Reference Signal Received Power) Measurement: The last measured RSRP.


**TARGET**
- ACK (Acknowledgment) Probability: The probability of receiving a successful acknowledgment (ACK) for a given transmission. 

**REASON**
- Subband SINR Measurements:
By using subband SINR measurements, the model can accurately assess the channel conditions across different frequency bands. This enables more precise modulation and coding scheme (MCS) selection.
- CQI (Channel Quality Indicator):
Including CQI in the features helps the model incorporate the UE's perspective on the channel conditions, which is essential for making informed decisions about the optimal MCS.
- Time Period from the Last Sounding:
The time elapsed since the last sounding reference signal (SRS) measurement is important for understanding the temporal dynamics of the channel. 
- RSRP (Reference Signal Received Power) Measurement:
RSRP is a measure of the received signal strength. Including RSRP helps the model assess the overall power level of the received signal, which is crucial for determining the feasibility of higher-order modulation schemes that require higher signal quality.
Target
- ACK (Acknowledgment) Probability:
The primary objective of the AMC process is to maximize data throughput while ensuring reliable communication. The probability of receiving a successful acknowledgment (ACK) for a given transmission directly reflects the reliability of the chosen MCS. By predicting the ACK probability, the model can select the MCS that offers the highest expected throughput, balancing the trade-off between data rate and transmission reliability.

**CORRELATION WITH VIAVI DATASET**
- CQI = 'DRB.UECqiUL' and 'DRB.UECqiDL'


## 2. Paper 2
### 2.1 Summary


### 2.2 Data, Pros, and Cons

**DATA**

**FEATURES**
- 


