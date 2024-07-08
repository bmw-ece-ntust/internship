### O-DU

The Distributed Unit (DU) handles the lower layers of the protocol stack, which includes the Upper Physical, MAC, and RLC layers. Its chief responsibilities are:

* Data Organisation and Management: The DU is tasked with preparing data for transmission. It structures the data, ensuring it’s in the right format for efficient radio transmission.
* Interaction with the Radio Unit (RU): The DU directly manages data communication with the Radio Unit, translating the organised data into radio waves for transmission and vice versa.
* Latency Reduction and Efficiency: Being in closer proximity to the RU and managing the lower protocol layers, the DU assures minimal latency, especially crucial for real-time data exchange applications.

Metaphorically, think of the DU as the skilled technician of a symphony, tuning the instruments to perfection before the performance.

**Acronym explainers:**

* Upper Physical Layer: This is the part of the physical layer closest to the MAC layer. It deals with aspects like modulation, encoding, and other processes essential for preparing data for transmission over the radio waves.
* MAC (Medium Access Control) Layer: This layer is responsible for how data packets are placed on the network. It addresses issues like when data may be transmitted and helps prevent collisions by managing protocol access to the physical network medium.
* RLC (Radio Link Control) Layer: This layer ensures the reliable transmission of data between the user equipment and the network. It handles segmentation, reassembly of data packets, and error correction.
