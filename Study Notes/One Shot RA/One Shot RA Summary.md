# Summary: [Modeling and Estimation of One-Shot Random Access for Finite-User Multichannel Slotted ALOHA Systems](https://ieeexplore.ieee.org/document/6211364)

## Abstract
This paper presents a combinatorial model and approximation formulas to estimate the average number of suc- cessful and collided users for a one-shot random access in finite- user multichannel slotted ALOHA systems.
>ALOHA: One of random access protocol. Divided into Pure and Slotted Aloha
>
> - Pure Aloha: In this basic type of ALOHA, a Base Station (BS) can send data anytime it is ready, without checking whether the channel is free. Successful transfers are indicated by an ACK (acknowledgment) from the receiver. If the ACK does not arrive after a random amount of time, the data is resent after a random delay.
>
>   Assumptions in Pure Aloha:
>
>   - All frames have the same length.
>   - Stations cannot generate a frame while transmitting or trying to transmit. That is, while a station is sending or trying to resend a frame, it cannot be allowed to generate more frames to send.
>   - The population of stations attempting to transmit (both new transmission and retransmissions) follows a Poisson distribution.
>
> - Slotted aloha: In this type of ALOHA, frame is transmitted in a discrete time slots that is given by a signal broadcasted by a special BS. This TS is equivalent to the frame length. If a BS is ready to send data, it waits until the next TS arrives. 

---

The aim of the paper "Modeling and Estimation of One-Shot Random Access for Finite-User Multichannel Slotted ALOHA Systems" is to investigate the transient behavior of the random access channels accessed by a known number of machine-type communication (MTC) devices in a short observation interval. The analytical model proposed in the paper is used to derive the number of successful and collided users in one-shot random access for finite-user multichannel slotted ALOHA systems. The model is based on a combinatorial approach and uses equations (2) to (6) to estimate the average number of successful and collided RAOs in each access cycle.

## Simulation
### Equation 4 and 5
$$N_{S,i}=M\cdot e^{\frac{M}{N_1}} \tag{4}$$
Equation 4 is used to estimate the average number of successful RAOs in the i-th access cycle based on the average number of devices that transmit their random-access attempts in that cycle (Ki) and the number of RAOs reserved for the i-th access cycle (Ni).


$$N_{C,1} = N_1 - M e^{-\frac{M}{N_1}} - N_1 e^{-\frac{M}{N_1}} \tag{5}$$
Equation 5 is used to estimate the average number of collided RAOs in a one-shot random access, based on the number of RAOs reserved for the access cycle (N1) and the number of devices contending for access (M). The equation takes into account the probability of idle RAOs and successful RAOs, and subtracts their sum from the total number of RAOs to obtain the average number of collided RAOs.
<img src="https://imgur.com/fBZd7TR.png" width="400">

In the simulation, the x-axis represents the ratio M/N, where M is the total number of devices contending for access and N is the number of RAOs reserved for the access cycle whereas y-axis represents the values of Ns,1/N and Nc,1/N, which are performance metrics related to the average number of successful and collided users in the one-shot random access, normalized by the total number of devices contending for access.

From the graph, it is evident that an increase in the ratio M/N leads to a higher probability of collision and a lower probability of success.


### Equation 8 
$$P_s = \sum_{i=1}^{I_{max}}\frac{N_{S,i}}{M}\tag{8}$$
Equation 8 is used to estimate the access success probability, Ps, which is defined as the probability of successfully completing the random access procedure within the maximum number of retransmissions.

<img src="https://imgur.com/89xUwkA.png" width="400">

In the simulation, the x-axis represents the N which is the total number RAOs reserved for the access cycle whereas y-axis represents the success probability of the RA process

From the graph can be concluded that there is a certain threshold of the reserved RAO that is needed to acheive high success probability

### Equation 9 
$$T_s = \left(\sum_{i=1}^{I_{max}}i\cdot N_{S,i}\right)/\sum_{i=1}^{I_{max}}N_{i}  \tag{9}$$
Equation 9 represents Mean Access Delay, which is the delay for each random access procedure between the first attempt and its completion

<img src="https://imgur.com/GBhtDOd.png" width="400">

### Equation 10
$$P_c = \sum_{i=1}^{I_{max}}N_{C,i}/\sum_{i=1}^{I_{max}}N_{i}  \tag{9}$$

Equation 10 represents Collision probability, which is the ratio between the collided RAOs and the overall number of RAO

<img src="https://imgur.com/nnkF28r.png" width="400">

From the graph, can be concluded that increasing the reserved RAO into a certain threshold number will lead to rapidly decreasing collision probability.




