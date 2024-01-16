# LTE Study Notes

- [x] Gain understanding about LTE from [This channel](https://www.youtube.com/@LTE4G/videos)
- [x] Gain understanding about how Duplexing is managed in LTE
- [] Gain understanding about how Multiplexing is managed in LTE
- [] Gain understanding about the fundamentals of OFDMA.



## Communication Evolution

### 20th Century
The first communication was primarily used for military purposes. The first form of communication uses a single channel radio thus can only transmit data in half-duplex manner using *Push-to-Talk* system. Around that time IMTS (Improved Mobile Phone System) was introduced and introduces dual channel communication that allows full duplex communication

### First Generation (1G - 1982) 
1G is developed by Bell Labs and popularly known as AMPS (Advanced Mobile Phone System).

The basic idea of this system is by dividing geographical area into cells and each cells will be served by Base Station (BS). This still has drawbacks in lacks of encryption, full analog communication, and no roaming.

To address the lack of roaming, ETSI (European Telecomunications Standard Institute) was formed in 1988. This will allow many governing bodies around the world to form and implement a global standarization.

### Second Generation (2G - 1991)
2G is based on GSM (Global System for Mobile) standards. 2G can transfer data up to 9.6kbps.

2G addresses security drawbacks of 1G by including Digital Encryption for phone conversation. 2G also utilizes the radio spectrum more efficient and better mobile phone penetration. SMS was also introduced in 2G.

#### 2.5G (1995)
In 2.5G GPRS was introduced which overlays packet switching network on top of the already used GSM. This allows the maximum data rate to increase to 160kbps.
#### 2.75G (1997)
In 2.75G EDGE was introduced which implements 8-PSK Modulation which increase the maximum data rate to 500kbps while using the same GPRS infrastructure.

### Third Generation (3G - 2000)
In 3G, UMTS is replacing EDGE that is used in 2G. UMTS uses wideband CDMA to carry the signal.

 Within this period, 3GPP was formed which until now acts as the one of the governing bodies for standarization and specification for cellular telecomunication.

 The goal of UMTS is to provide minimum data rate of 2Mbps while stationary or walking and 384kbps for moving vehicle. 

Later in this period in relase 4, the core network component will be based on IP. This is the foundation for HSDPA which came out in relase 5. HSDPA reduces delay and increase the data rate to 14Mbps for downlink. In relase 6, HSUPA is introduced and reduce delay and increase data rate to 5.74Mbps in uplink. In realse 7 this  MIMO and higher order modulation such as 64-QAM is implemented, both can be used simultaneously.

### Fourth Generation (LTE - )
In 4G, a new architecture is developed which consisted of System Architecture Evolution and Radio PArt.

In addition from MIMO, 4G also implements Multi Carrier and Packet Switching on the Radio Interface

Within this period more features are added to LTE such as:
- Multi Cell HSDPA
- HetNet
- Coordinate Multipoint
- Carrier Aggregation
- Massive MIMO
- etc

>Need to explore more about 4G

## Duplexing
There are serveral method to acheive full duplex connectivity
    
- **FDD - Paired Spectrum (Frequency Division Multiplexing)**

    <img src="https://i.imgur.com/gBw5bPG.png"/>

    In FDD, the UL and DL is using the different frequency channel with a guard band between them to prevent interference and crosstalk between those two channel.

- **TDD - Unpaired Spectrum (Time Division Multiplexing)**
    <img src="https://i.imgur.com/ej73h0B.png"/>
    In TDD, the UL and DL is transmitted alternatingly within the same channel but at different time slot using a synchronized interval. Between the time slots there will be a guard period (delay).

While generally FDD offers more performance since there is no delay needed. It consumes much more resource both power and cost. In FDD, we cannot allocate resource individually on the UL/DL traffic while in TDD we can easily adjust the time slot to give more resource either to UL or DL according to the traffic. TDD also have much more cheaper equipment cost because it only uses one radio, comare to FDD that uses at least two radio which a multiplexer to process those frequencies. While TDD is cheaper to deploy, it is more complex from MAC perspective due to it needing an accurate timing requirement.

## Multiple Access
Multiple access allows multiple users to communicate using a single common channel. It is one of the application of multiplexing, which is the process of combining multiple signal and combining them to be transmitted over a single channel.

### Serveral types of multiplexing

- **FDMA (Frequency Division)**
 <img src="https://i.imgur.com/LB4KDXf.png"/>

    FDMA allocates a different subband for each user. Between each subband there will be a guard band to prevent interfering and crosstalk
- **TDMA (Time Division)**
    <img src="https://i.imgur.com/IsyDYzK.png">
    TDMA uses common frequency band to multiple users. Transmission for each users will be differentiated using time slots
- **CDMA (Code Division)**
    <img src="https://imgur.com/2GHUWuU.png">

    The basic principal of CDMA is that code is used to distinguish different users. The code is used to encode and decode each user's signals. 
- **SDMA (Space Division)**
    The basic idea of SDMA is by distributin the cells into broader area, the same frequency can be used in mutiple areas as long as they are not overlap each other.
- **OFDMA (Orthogonal FDMA)**
    OFDMA is similar with FDMA. The key difference is that OFDMA uses orthogonality for its subcarriers. This allows the subcarriers to occupy the same bandwidth without any interference. OFDMA negates the needs of guard band thus the spectrum needed is less that regular FDMA.







