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


## OFDMA


>Lets say a single carrier wideband signal is carried over a bandwidth $B$ and carrier frequency $f_c$. The symbol time of that signal will be $\frac{1}{B}$. If we include delay spread, the delay spread could take the majority of the symbol time, thus reducing efficiency of the channel.
>
>This effect can be minimized by using multiple sub-carriers with smaller bandwidth. From illustration give previously, we can divide the carrieres with 100 10kHz sub-carriers. This will increase the symbol duration, thus reducing the delay spread effect (Delay spread is mostly constant). The idea here is maximizing the ratio between symbol duration and delay spread.
>
>This is the basic concept used in FDMA

In OFDMA, the sub-carriers has an overlaping bandwidth, but the subcarriers are orthogonal to each others which allows the subcarriers to occupy the same bandwidth without any interference. OFDMA negates the needs of guard band thus the spectrum needed is less that regular FDMA.

### Subcarrier divison
Data stream from a large bandwidth are divided paralel into substreams with lower bandwidth subcarriers. These subcarriers are centered around the DC component, which is the center frequency of the entire carrier band with distance of 15kHz from each subcarriers.

In frequency domain, these subcarriers will carrying a sinc function. Thus OFDMA signal can be seen as series of sinc wave with distance from each peak of 15kHz
<img src="https://imgur.com/3r51XhG.png" width="500"/>

### Data transmission
The data that will be transmitted will go under a modulation process, this modulation process will result in that data transmitted over a numbers of subcarrier according to the carrier bandwidth used.
<img src="https://imgur.com/DOTKUcG.png" width="500">

The signal transmitted will be like the sum of all of those subcarriers as a composite signal. This signal will goes under an FFT calculation to decompose that composite signal to get the initial signal from the different subcarriers. 
>**DATA TRANSMISSION STEPS**
>1. The data undergoes a modulation scheme that will distribute it accros the number of subcarriers specified
>2. The signal transmitted will be represented as a composite signal from all the different subcarriers
>3. That composite signal reach its destination
>4. In the destination, the signal will go under FFT process to get the original data from every subcarriers
>5. That signal in every subcarriers will be reversed using the same modulation as before to get the original data.


### SC-FDMA
In LTE, SC-FDMA is used for the uplink due to its having a lower Peak-to-average Power Ratio. Unlike in OFDMA where a single symbol is represented by a single subcarrier, in SCFDMA a single symbol is allowed to be transmitted over multiple subcarriers.

Unlike OFDMA, before the symbols are transmitted, they are passed through a DFT. The DFT spreads the data symbols across the frequency domain. This step is crucial as it transforms the signal from the time domain to the frequency domain, essentially converting the signal into a single-carrier-like waveform. After signal, now mapped to subcarriers, undergoes an IDFT, converting it back to the time domain. This step generates a time-domain waveform suitable for transmission over the wireless channel.

## Channel Mapping
<img src ="https://imgur.com/YfOylHF.png" width="500"/>

**Channels in Radio Link Control**
- **PCCH (Paging Control Channel)**: Used by BS to communicate UE that is in IDLE state.
- **BCCH (Broadcast Control Channel)**: Used to broadcase system information about the BS
- **CCCH(Common Control Channel)**: Used by UE to give control information to the BS
- **DCCH(Dedicated Control Channel)**: Exchange control channel between individual UE and BS
- **MCCH(Multicast Control Channel)**: Same as DCCH, but multicast
- **DTCH(Dedicated Traffic Channel)**: UL and DL for User Plane data
-  **MTCH(Multicast Traffic Channel)**: Same as DRCH, but multicast
  

**Transport Channel in MAC Layer**
- **Paging Channel**
- **Broadcast Cahnnel**
- **Downlink Shared Channel and Uplink Shared Channel**
- **Multicast Channel**

### BCCH
Signaling data is split into two parts
- MIB (Master Information Block): System critical information to accuire the cell
- SIB (System Information Block): Dynamic information to access the cell (Carried in DL-SCH)
  
MIB broadcast frequently by a cellular network, essential for initial cell identification and synchronization. In contrast, SIB provide detailed and varied information about the network's operation and configurations, broadcast less frequently and necessary for a device to fully understand and connect to the network.

### UL-SCH
USed for DCCH, CCCH, and DTCH for the uplink transmission

RACH is used for synchronization for this channel

### MAC Layer Functions:
- Mux/Demux of Logical Channel
- Logical channel prioritization for UL
- HARQ Retransmit 
- Random access control.

## Channel Prioritization
Data is sent by the physical layer through the PDU transport block. The MAC layer task is to decide the amount of data to be included from the RLC layer to the PHY Layer. 

Each channel in RLC layer has their own priorities. If the MAC decides to send based on the highest priority first, there will be a possibility where the data from channel with lower priority will not be transmitted. This is called Channle Starvation.

To take care of channel starvation each logical channel will have something called PBR or Prioritazed Bit Rate. PBR is the bits that will be transmitted initially from each channel.

Lets say a channel has PBR is configured to be 5-bits. This means the MAC will put the first 5-bit of data to the PDU first, followed by first n-number of bits from the lower priority channel where n is the PBR for that channel. This will be repeated until all channels has been included in the PDU based on each PBR number. If there's is still space in the PDU, the remaining bits will be put into the PDU in order of their channel priority, in this step PBR is not used.


## MAC Scheduler and PHY Layer
### MAC Scheduler
Within the MAC layer, there is something called MAC Scheduler Module. This module serves serveral function
1. **HARQ Control**
2. **Logical Channel Multiplexing and Channel prioritizazion**   
3. **Decide modulation scheme dynamically.**
    (This was done by analyzing the channel quality for each UE and deciding the proper modulation scheme to ensure the integrity of transmitted data)

4. **Which terminal to transmit**
5. **Transmit Set of RB from the DL data to different terminal**
6. **Transport block size selection**

Poont 4 to 6 is implemented in the physical layer

### PHY Layer
Physical channel (PHY channel) refers to a communication channel at the lowest layer of the network's architecture, responsible for the actual transmission of data over the radio interface. It involves the use of radio frequencies and modulation techniques to convey information between the User Equipment (UE) and the base station (eNodeB).

<img src="https://imgur.com/uhjhOIF.png" width="500"/>

Image above shows how different type of channels are mapped one to each other

**PDCCH**: Control information on how the DL data should be received in PDSCH
- COntrol Information
- SIB Info for UL
- Power control for UL
- HARQ Info

**PCFICH** (Phy control format incicator channel): Basically information for the PDCCH
- Information about signal thats being received
- OFDM Symbol for PDCCH

**PHICH** (Phy HARQ Indicator Channel): 
This channel is bassicay for carrying HARQ ACK and NACK info.

**PUCCH**: PDCCH counterpart for the UL data.


## Carrier Aggregation
The basic idea of carrier aggregation is to use multiple carrier simultaneously to transmit and receive data. For example, instead of using one 20 MHz carrier, a network might aggregate three 20 MHz carriers, giving a total bandwidth of 60 MHz. This wider bandwidth allows increase in bitrate and performance

In LTE, carrier aggregation consist of maximum 5 individual carrier (often referred as COmponent Carrier or CC or Serving Cell). This CC can have bandwidth of 1.4, 3, 5, 10, 15, 20Mhz.  Carrier aggregation can be used in FDD or TDD where in FDD the total numbers of aggregated carrier in DL is equal or greater than in the UL, whereas in TDD the numbers is thesame.

In carrier aggregation there will be a multiple serving cell which is consisted of one primary and up to four secondary one. RRC Connection is always handled by the primary serving cell, this will serve for SIB data and UL control information. Secondary serving cell will be dynamically added or removed based on requirement condition whereas the primary one will only change if the UE goes through handover.



### Band Arrangement
<img src="https://imgur.com/w0D8SSw.png" width="500">

#### Intra-band, contiguous
<img src="https://imgur.com/PhjI88Q.png" width ="300"/>

This is when the aggregated carriers are directly adjacent to each other within the same frequency band. Because the carriers are contiguous, this form of aggregation is typically easier to implement in terms of radio frequency design and signal processing.

#### Intra-band, non-contiguous
<img src="https://imgur.com/5U2Zeid.png" width ="300"/>

This involves aggregating carriers within the same frequency band but which are not adjacent to each other – there are gaps of unused spectrum between them. This type is more complex in terms of RF design and signal processing due to the need to handle separate chunks of spectrum within the same band.

#### Inter-band, non-contiguous
<img src ="https://imgur.com/3EimrV1.png" width="300"/>

This approach aggregates carriers from different, non-contiguous frequency bands. This requires more porcessing and more sophisticated UE to implement

### Terminologies

* **Aggregated Transmission Bandwidth Configuration:**
Total number of aggregated PRBs

* **CA Bandwidth Class:**
 Combination of maximum ATBC and maximum number of CCs.
  * Class A: ATBC ≤ 100,  maximum number of CC = 1
  * Class B:  ATBC ≤ 100,  maximum number of CC = 2
  * Class C: 100  < ATBC ≤ 200,  maximum number of CC = 2
* **eUTRA Operating band**: Frequency band range allocated in different parts of world

    <img src="https://imgur.com/8d67c0n.png" width="400"/>
    <img src="https://imgur.com/PmlJdBs.png" width="400"/>

* **CA Configuration:**
  Configuration based on eUTRA Band + CA BW Class
  <br>
   <img src="https://imgur.com/6ysMXS9.png" width="400"/>

In CA, overage varies due to different frequency bands and pathloss. The primary serving cell, connected to the PCC, handles the RRC connection, NAS information, and system info in idle mode. Uplink control is sent on the UL PCC. SCCs serve secondary cells and are dynamically adjusted. The PCC changes only during handovers.

> <img src="https://imgur.com/9vpyx36.png" width="400">

> Only the black UE can use all three CCs, as the white UE is out of the red CC's coverage. UEs with the same CCs can have different PCCs.

<!-- **CA Block Diagram**

<img src="https://imgur.com/cxPANCS.png" width="500">

Each CC is treated like an R8 carrier, but updates are needed for SCC handling and MAC scheduling across multiple CCs. Significant physical layer changes include DL signaling for CC scheduling and UL/DL HARQ ACK/NACK per CC. -->

## HETNET
A Heterogeneous Network (HetNet) is a wireless network that combines various types of cells, such as macrocells, microcells, picocells, femtocells, and relay nodes, to enhance coverage, capacity, and data speeds, particularly in densely populated areas. HetNets are designed for efficient spectrum use and improved user experience, with seamless integration and coordination among different cell types for efficient handovers and load balancing.

### Methods
#### Small Cell
<img src="https://imgur.com/PBpBMZV.png" width ="350"/>

Small cell is basically like the smaller main cell. Its main purpose is to increase the coverage and signal bitrate. For example in an area with a macro cell, small cell can be used in more localized area with smaller coverage. Small cells also can offloads the loads from the macro cell.

#### Relay node
Relay node can be explained like using a wifi extender. Relay node basically takes signal from a Donor eNB and relays it to the UEs. The UE will see this relay node as a eNB where as the Donor eNB will see the relay as a UE. In the relay node, the signal from the Donor eNB is processed and transmitted as a new signal.

#### Repeater
Repeater is similar to relay, but without the signal processing. Repeater basically just amplifies the signal received.

### Advantages

- **Improved Coverage:** HetNets enhance network coverage by filling coverage gaps with smaller cells in areas where larger cells can't reach effectively.
- **Increased Capacity:** By using a mix of cell sizes, HetNets can handle more simultaneous users, alleviating congestion in high-density areas.
- **Enhanced Data Speeds:** Smaller cells in HetNets can provide higher data rates due to closer proximity to users and less crowded frequencies.
- **Efficient Spectrum Utilization:** HetNets enable more effective use of available spectrum by distributing traffic across different types of cells.
- **Better Quality of Service:** Users experience fewer dropped calls and better connectivity as HetNets manage network resources more efficiently.
- **Scalability:** HetNets can easily scale to meet growing data demands by adding more small cells in high-traffic areas.

## Coordinate Multipoint (CoMP)
In LTE, all cells can be configred to use the same frequency. But this could create interference the edge of the coverage since many cells are using the same frequency. CoMP is to solve this problem

- **Intrasite:** 
    Involves only one eNB and does not involve backhaul communication to other eNB's
    <br>
    <img src="https://imgur.com/vQrWuak.png" width="300">

- **Intersite:** 
    Involves coordination of multiple eNB's
    <br>
    <img src="https://imgur.com/fzKXAsl.png" width="300">

### CoMP Operation Types
#### Joint Processing
In DL, data is sent to the UE from multiple eNBs to enhance signal quality and cancel interference. This CoMP approach increases backhaul network load, as data and joint processing info must be shared among eNBs. In UL, CoMP uses antennas at different sites to form a virtual array, combining signals from eNBs for improved reception of weak or interfered signals. However, this method requires extensive data transfer between eNBs, a significant drawback.

#### Co-coordinated scheduling.

In DL, data is transmitted to a UE from a single eNB, with coordinated scheduling and beamforming to control interference. This reduces backhaul requirements since UE data is directed to only one eNB and only scheduling and beam details need coordination. In UL, the scheme minimizes interference through coordinated scheduling among eNBs. Similar to DL, this approach lessens backhaul load, as only scheduling data is transferred between coordinating eNBs.
