## FAPI (Functional Application Program Interface)
> A standardized specification released by Small Cell Forum for chipset and component suppliers and mobile base station integrators. Enables developers to integrate external services seamlessly into their own application as it has an interface for developers to use the functionality and resources of existing software systems, libraries, and frameworks. It also defines a set of rules, protocols, and conventions.

<div align="center">
	<img width="238" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/401d106d-ce99-4645-851c-f438dd65bb34">
</div>

```
P5 --> Configuration interface
P7 --> Data interface
P19 --> O-RAN Alliance Definition
```
<div align="center">
	<img width="456" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/143583c1-fc13-4e6c-b570-4be74a8599f2">
</div>

L1 and L2 both control and transmit data.
UL (Uplink) and DL (Downlink) are not limited to L1 and L2 only but can also be used between L1 and UE or L3 and L2.


**DL_TTI.request**
```
-> Message sent by the L2/L3 when the PHY is in the running state. 

-> Initiate a `request fro UE to the network for downlink data` transmission during a specific Transmission Time Interval (TTI)
```
**UL_TTI.request**
```
-> `RACH` procedure begins when the PHY receives an UL_TTI.request message

-> Initiate a request from User Equipment to the network for uplink data transmission during a specific Transmission Time Interval (TTI)

-> Can be sent by L2/L3 when the PHY at runnning state
```
**TX_DATA.request**
```
-> `Instructing User Equipment to transmit specific data` during a designated transmission time from the network

-> Carries payload data, transmission parameters, scheduling information, and error correction information
```
**UL_DCI.request**
```
-> UL_DCI stands for Uplink Downlink Control Information

-> Used for scheduling of PUSCH (Physical Uplink Shared Channel)

-> Will be transmitted by MAC to frant the DL_TTI.request
```

Notes:
![IMG_E9EAD5E52468-1](https://github.com/bmw-ece-ntust/internship/assets/123353805/8565baf0-1fb5-49a2-83f0-19abf2dba1d2)

Resources :

1. [Fauzan's FAPI Procedures](https://hackmd.io/9tBOS229SCyOm_7Js9DXWQ?view#2-FAPI-Procedures)
2. [5G FAPI Spesifications](https://www.smallcellforum.org/work-items/fapi/#:~:text=The%20latest%20FAPI%20specifications%20are,(P5)%20interface%20%5BSCF222%5D)
