#  Deep Learning for Radio Resource Allocation With Diverse Quality-of-Service Requirements in 5G
| **item** | information |
| --- | --- |
| **Authors** | Rui Dong, Branka Vucetic|
| **Date of Publication** |APRIL 2021|
|**type** |IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS|
| **total pages** |  14 pages|
| **keywords** | Deep neural network, radio resource management, quality-of-service, deep transfer learning.|

## Paper Main Idea
Optimize radio resources like bandwidth and transmit power while meeting diverse QoS requirements for different types of services such as delay-tolerant, delay-sensitive, and URLLC (Ultra-Reliable Low-Latency Communications) in 5G networks

## Proposed Method

1. **Cascaded Neural Networks**: <br> The first neural network approximates the optimal bandwidth allocation, while the second neural network determines the transmit power required to meet QoS constraints.
2. **Optimization Algorithm**: <br> Develops an optimization algorithm to solve a Mixed Integer Non-Linear Programming (MINLP) problem that minimizes the total power consumption of a base station. This algorithm is used to generate labeled training samples for training the neural networks.
3. **Deep Learning Transfer**:<br>To adapt to non-stationary wireless environments, where the conditions of wireless channels or types of services may change over time

## Result
The simulations are carried out in a 5G network environment, considering various QoS requirements such as latency, reliability, and data rate. The models provide significant improvements over traditional methods, especially in terms of meeting diverse QoS requirements and adapting to dynamic network conditions. The use of transfer learning further enhances the models' robustness, making them well-suited for deployment in real-world, non-stationary 5G environments.