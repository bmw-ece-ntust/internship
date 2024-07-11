# Power Control
When a transmitter sends signal to a receiver through a wired communication there won't be that much power degradation. Different from a wireless communication which will have an uncontrollable power drop in the process. Thus, a power control mechanism should exist that can deliver the right amount of power based on the needs between the transmitter and receiver such as the distance.

A. Closed Loop Power Control
  - Send signal from  T to R
  - R measure the power of the signal
  - R send a special command

B. Open Loop Power Control
Transmitter send power info to receiver (User Equipment). UE (User Equipment) will decode the power info about how much power is allowed for it.

# Tx Power Equation
Tx Power = Target Rx Power set by gNB + PathLoss factor + MCS factor + RB factor + Power Control Command

- `Tx Power` : PRACH/PUSCH/etc power, the channel power of a Uplink physical channel.
- `Target Base Rx Power swr by gNB` : Power that gNB require for the safe decoding for the received signal
- `Pathloss Factor` : Pathloss between UE and gNB (Referense signal - measure power of RS)
- `MCS Factor` : Modulation coding scheme value for the channel to be transmitted
- `RB Factor` : Resource Block being used for the channel to be transmitted
- `Power Control Command` : Determined bt specific value from gNB notified to UE (User Equipment)

>[!NOTE]
> PRACH : Physical Random Access Channel, PUSCH : Physical Uplink Shared Channel

![IMG_2F44A42E4E77-1](https://github.com/bmw-ece-ntust/internship/assets/123353805/48428f3a-559f-47bd-8c41-b00889fdc617)

# PRACH
<img width="489" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/9e7bea85-c4ec-4c34-8f09-a0b847204eab">

# PUSCH
<img width="742" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/dd54aedd-1c88-42e7-b4d8-f67e894d5a24">
Calculated TX power increases when 
- Po_PUSCH power increases
- Scheduled number of RB increases
- The estimated pathloss increases and the impact of pathloss is affected by the scaling factor alpha
- According to TPC command (It could decrease as well)








