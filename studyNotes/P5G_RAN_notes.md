RAN (Radio Access Network)
========================
### Traditional RAN and OpenRAN
Traditional RAN generally uses proprierity and tight solution provided by the vendor,while OpenRAN implements standarized interface to allow more diverse and open ecosystem

### FR1/FR2
FR1 (frequency range 1) and FR2 (frequency range 2) are both used in 5G system where FR1 provides better range and indoor propagation while FR2 offers high data rate transfer and lower latency

### Popular NR frequency
![image](https://github.com/user-attachments/assets/95b647d5-bbc7-4b4a-aecd-84e16da94bc7)

### TDD Pattern (Time Division Duplexing Patter)
TDD (Time Division Duplexing) is a method to send and recieve data at the same frequency line, where it is capable of bidirectional transimission, where for the NR TDD, has structure below

![image](https://github.com/user-attachments/assets/20fc13d6-4203-41e2-8299-68decf9fac74)


- nrofDownlinkSlots : Number of consecutive full DL slots at the beginning of each DL-UL pattern  
- nrofDownlinkSymbols : Number of consecutive DL symbols in the beginning of the slot following the last full DL slot
- nrofUplinkSlots : Number of consecutive full UL slots at the end of each DL-UL pattern
- nrofUplinkSymbols : Number of consecutive UL symbols in the end of the slot preceding the first full UL slot

#### Guard Timing in TDD
some consideration should be taken into account when assigning TDD pattern where 
- You need a certain number of Guard time (Guard symbols) when switches from DL to UL
- You don't need any guard time when switches from UL to DL

The rule can be illustrated as below

![image](https://github.com/user-attachments/assets/6041f3a3-1974-48d5-b637-b5d721003daa)

reference : https://www.sharetechnote.com/html/5G/5G_tdd_UL_DL_configurationCommon.htm

#### TDD in NR
in TDD NR there is 4 type of slots which is  the following

![image](https://github.com/user-attachments/assets/b022517e-53f3-45ef-ac99-f99c6f04f0d0)


where

![image](https://github.com/user-attachments/assets/cb6b9ed6-7e97-4cdc-8641-9f383045fac2)

those slot can be constructed into a pattern where these pattern depends on several parameter such as numerology, UL/DL ratio, SS burst set periodicity, PRACH periodicity and number of beams


![image](https://github.com/user-attachments/assets/9212b88a-ac0d-431d-b6bd-527b367e3742)


### eMBB/ULRRC/mMTC
services offered by 5G NR
- eMBB (enhanced Mobile Broadband)
- URLLC (Ultra Reliable Low Latency Communications)
- mMTC (massive Machine Type Communications)
in eMBB services, it delivers high-quality internet access even under harsh environmental conditions. While URLCC ensures low latency below the 4-millisecond range. 5G mMTC uses non-human-type communication models, which prioritize low-rate, uplink-centric transmission.

### PLMN (Public Land Mobile Network)
PLMN is the term used to describe all mobile wireless networks that use earth-based stations rather than satellites

### APN/DNN
- In LTE, APN (Access Point Name) is used as an identifier for a specific network operator's packet data network. It is used by the mobile device to connect to the packet data network and access the internet and other services.
- In 5G, the DNN (Data Network Name) is the counterpart of APN in LTE. It is used to identify and route traffic to a specific network slice, which can be customized with specific QoS requirements for different services and applications.
### IMSI (International Mobile Subscriber Identity)
Unique identifier in simcard
### S-NSSAI (Single Network Slice Selection Assistance Information)
S-NSSAI contains infromation regarding network slice selection 
