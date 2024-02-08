
# Additional Part 1 (Interface & AI/ML Module)

## Learning E2 Interface related in Near-RT RIC Platform

:::success
- Goal:
    - [ ] Learning E2 Interface
    - [ ] Learning E2 Service Model
- Useful Links:
    - [O-RAN.WG3.E2AP-v02.01](https://www.o-ran.org/specifications)
    - [ORAN-WG3.E2SM-v02.01](https://www.o-ran.org/specifications)
:::
:::info
- Outcome(Study Note):
    - [Note Title](Link)
:::

1. Definition E2 Interface 
- The E2 interface is an open interface connecting the near-RT RIC and the E2 nodes (CUs, DUs). It facilitates communication that allows the RIC to control radio resource management and other functionalities within the E2 nodes
- Each E2 node contains data pertaining to RAN functions, which can be published by the E2 nodes. Subsequently, the xApps on the near-RT RIC can subscribe to one or more of these RAN functions through the E2 interface.
![alt text](https://github.com/bmw-ece-ntust/internship/blob/9a0b4de834b9b78be08a912f975ae46b6c0c6fda/images/E2%20Interface.png)
2. E2 Interface Characteristics:
    - The E2 interface, an open connection, links near-RT RIC to DUs and CUs in the 5G landscape.
    - Operational on the SCTP protocol over IP.
    - Supports two protocols: E2 Application Protocol (E2AP) and E2 Service Model (E2SM).
    - E2AP messages can seamlessly integrate various E2 Service Models, facilitating functionalities related to RAN metrics and RAN Control.
    - Its applications extend to Key Performance Matrix (KPM), Network Interfaces (NIs), and RAN Control (RC).
![alt text](https://github.com/bmw-ece-ntust/internship/blob/e4b29e5bf8b9795aac690a41acedfc02a2b3ca23/images/E2AP.png)
3.  E2AP (E2 Application Protocol) provides four services:
    1. **E2 Report**   Involves E2 RIC Indication messages containing data and telemetry from an E2 node. The E2 Report service is activated upon subscription from an xApp to a function offered by the E2 node.
    2. **E2 Insert**  Notifies the xApp about a specific event in the E2 and is activated upon subscription from an xApp.
    3. **E2 Control** : Autonomously initiated by the RIC or triggered by an insert message at the near-RT RIC, it involves a two-message procedure: RIC Control Request from RIC to E2 node, and RIC Control Acknowledge in the opposite direction.
    4. **E2 Policy**: Subscription specifies event trigger and autonomous policy for E2 node resource management.

## Learning A1 Interface related in Near-RT RIC Platform
:::success
- Goal:
    - [ ] Learning A1 Interface
- Useful Links:
    - [O-RAN.WG3.A1AP-v03.02](https://www.o-ran.org/specifications)
    - [O-RAN.WG3.A1GAP-v03.00](https://www.o-ran.org/specifications)
:::
:::info
- Outcome(Study Note):
    - [Note Title](Link)
:::

The A1 interface connects non-RT RIC and near-RT RIC. It enables the non-RT RIC to provide guidance based on policies for the near-RT RIC, managing ML models used in applications like xApps, and facilitating the negotiation,  and coordination of transferring enrichment information for the near-RT RIC.
![alt text](https://github.com/bmw-ece-ntust/internship/blob/a9b3fac1e51b03e4f026395e16aa69ea42be4fb9/images/A1%20interface.png)
- The A1 interface provides three services:
    1. **A1 policy management** is used by the non-RT RIC to guide the near-RT RIC in achieving Quality of Service (QoS) and Key Performance Indicator (KPI) goals for the RAN. This helps ensure that the network performs well and meets specific quality and performance standards.
    2. **A1 Machine Learning (ML) model management**
    3. **A1 Enrichment information**  is responsible to enhance RAN performance by offering information that the RAN doesn't usually have access to, like capacity predictions, details from sources outside the RAN, and overall analytics.

## Learning O1 Interface related in Near-RT RIC Platform
:::success
- Goal:
    - [ ] Learning O1 Interface
- Useful Links:
    - [O-RAN.WG10.O1-Interface.0-v08.00](https://www.o-ran.org/specifications)
:::
:::info
- Outcome(Study Note):
    - [Note Title](Link)
:::

- ![alt text](https://github.com/bmw-ece-ntust/internship/blob/2a3a854d66e1c2d83b24e6fde5fe00a91ad20416/images/O1-SMO.png)
- The O1 interface facilitates the connection between the Service Management and Orchestration (SMO) and non-RT RIC with the O-RAN managed elements, including the near-RT RIC and RAN nodes. 
- O1 is designed as an open interface that both adopts and extends standardized practices for operations and maintenance. 
- The O1 interface supports Management Services (MnS). These services enable the SMO to push configurations to the managed nodes, receive reports of external configuration updates from managed nodes, and stream or report performance data to the SMO.
- The O1 interface enables file pushing and downloading on SMO-managed nodes, supporting functions like software updates, deployment of beamforming configurations for Remote Units (RUs), and the implementation of Machine Learning models and security certificates.


## AI/ML Module
### RNN
https://user-images.githubusercontent.com/10358317/44312581-5a33c700-a403-11e8-968d-a38dd0ab4401.png
- RNN (Recurrent Neural Network) is a neural network specifically designed to handle sequential data, allowing it to store information from previous time steps and utilize it in computations at subsequent time steps. However, RNNs have a limitation in handling long-range dependencies within sequential data due to the vanishing gradient problem. 
- The vanishing gradient problem occurs as the gradient of the cost function significantly diminishes with the increasing complexity of layers or the length of the sequence. Therefore, RNNs are often constrained in their ability to capture long-range dependencies in sequential data, particularly as the time span lengthens
- There are different application areas that are used: Language model, neural machine translation, music generation, time series prediction, and financial prediction.


### LSTM
Long Short-Term Memory (LSTM) is an advancement in Recurrent Neural Networks (RNNs) specifically designed to address issues such as vanishing gradients and maintaining long-term information in sequential data. The architecture of LSTM includes intricate internal structures to manage and retain information through a memory cell mechanism. The structure of LSTM are:

1. Forget Gate
![alt text](https://github.com/bmw-ece-ntust/internship/blob/a8da115d2833b7e6618ab0c329cc22481e576990/images/forget_cell.png)
- The forget gate combines the current input (xt) with the previous output (ht-1).
- It utilizes the Sigmoid activation function, ensuring forget gate values range between 0 and 1.
- A value close to 1 retains information in the memory unit; conversely, a value near 0 discards or forgets information.
- The forget gate operation involves multiplying the result with the previous cell state.
- The information persisting in the cell state becomes the foundation for future predictions.

2. Input Gate
![alt text](https://github.com/bmw-ece-ntust/internship/blob/a8da115d2833b7e6618ab0c329cc22481e576990/images/inputcell.png)
- Input gate functions to control information in the cell state.
- The activation functions employed are Sigmoid and TanH.
- TanH's output ranges from -1 to +1, so the algorithm in learning and retaining information over time.
- The Sigmoid block's result is multiplied by the TanH block's outcome.
- The resulting product is then added to the current cell state for the generation of long-term memory.

3. Update cell state
![alt text](https://github.com/bmw-ece-ntust/internship/blob/a8da115d2833b7e6618ab0c329cc22481e576990/images/update_cell.png)
The cell state is crucial for Long-Term Memory in LSTMs. It is updated by combining the result of the Forget Gate with the result of the Input Gate.
4. Output gate
![alt text](https://github.com/bmw-ece-ntust/internship/blob/a8da115d2833b7e6618ab0c329cc22481e576990/images/output_cell.png)

- The Output gate utilizes activation functions, consisting of the Sigmoid and TanH functions. The input (xt) and the previous hidden state (ht-1) are input into these activation functions. 
- the long-term memory (cell state) is passed through the TanH function. the result of the TanH function is multiplied by the output of the Sigmoid function to generate the updated short-term memory


### Isoforest & Random Forest

### VAR Module
