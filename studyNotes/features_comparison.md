## DU Feature Comparison Between OSC,OAI and SRSRAN

This section discuss the features available in the DU which is RLC, Mac Scheduler, and PHY channels 


(note : N/A means information yet to be found)

### RLC Operation comparison
| Project       | TM | UM | AM |
| ------------- |:---:|:---:|:---:|
| OSC           |  ✔  |  ✔  |  ✔  | 
| OAI           |  ✔  |  ✔  |  ✔  |
| SRS RAN       |  ✔  |  ✔  |  ✔  |

The Radio Link Control (RLC) layer can operate in one of three modes: Transparent Mode (TM), Unacknowledged Mode (UM) and Acknowledged Mode (AM). The RLC manages multiple logical channels or bearers, each of which operates in one of these three modes. Transparent Mode bearers simply pass data through the RLC. Unacknowledged Mode bearers perform concatenation, segmentation and reassembly of data units, reordering and duplication detection. Acknowledged Mode bearers additionally perform retransmission of missing data units and resegmentation


### Mac Scheduler comparison
| Project       | Round Robin | Propotional Fair | Max C/I | Propotional Rate | Dynamic |
| ------------- |:-----------:|:----------------:|:-------:|:----------------:|:-------:|
| OSC           |      ✔      |      ❌         |   ❌    |      ❌         |   ❌    | 
| OAI           |      ✔      |      ✔          |      ✔  |      ✔          |      ✔   |
| SRS RAN       |     N/A      |     N/A         |     N/A  |     N/A         |     N/A   |

The Medium Access Control (MAC) layer multiplexes data between one or more logical channels into Transport Blocks (TBs) which are passed to/from the PHY layer. The MAC is responsible for control and scheduling information exchange with the eNodeB, retransmission and error correction (HARQ) and priority handling between logical channels.


### PHY channel comparison
|   Project      | PBCH          | PRACH         | PDCCH         | PDSCH         | PUSCH         | PUCCH         | CSIRS         | PRS           |
|:--------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|
| OSC            |      ✔        |      ✔        |      ✔        |      ✔        |      ✔        |      ✔        |       ❌   |          ❌         |
| OAI            |      ✔        |      ✔        |      ✔        |      ✔        |      ✔        |      ✔        |      ✔        |      ✔        |
| SRS RAN        |      N/A       |      N/A       |      ✔        |      ✔        |      ✔        |      ✔        |      N/A       |      N/A       |

Physical (PHY) layer carries all information from the MAC over the air interface. It is responsible for link adaptation, power control, cell search and cell measurement.

### MIMO Support comparison
| Project       | MIMO support  |
| ------------- |:-------------:|
| OSC           | N/A           |
| OAI           | 2T2R          |
| SRS RAN       | 4T4R          |



## Reference
- OSC [here](https://docs.o-ran-sc.org/projects/o-ran-sc-o-du-l2/en/latest/overview.html)
- OAI [here](https://gitlab.eurecom.fr/oai/openairinterface5g/-/blob/develop/doc/FEATURE_SET.md#openairinterface-5g-nr-feature-set)
- SRSRAN [here](https://github.com/srsran/srsran_project)
