## DU Feature Comparison Between OSC,OAI and SRSRAN

This section discuss the features available in the DU which is RLC, Mac Scheduler, and PHY channels 


(note : N/A means information yet to be found)

### RLC Operation comparison
| Project       | TM | UM | AM |
| ------------- |:---:|
| OSC           |  ✔  |  ✔  |  ✔  | 
| OAI           |  ✔  |  ✔  |  ✔  |
| SRS RAN       |  ✔  |  ✔  |  ✔  |

### Mac Scheduler comparison
| Project       | Round Robin | Propotional Fair | Max C/I | Propotional Rate | Dynamic |
| ------------- |:-----------:|:----------------:|:-------:|:----------------:|:-------:|
| OSC           |      ✔      |      ❌         |   ❌    |      ❌         |   ❌    | 
| OAI           |      ✔      |      ✔          |      ✔  |      ✔          |      ✔   |
| SRS RAN       |     N/A      |     N/A         |     N/A  |     N/A         |     N/A   |




### PHY channel comparison
|   Project      | PBCH          | PRACH         | PDCCH         | PDSCH         | PUSCH         | PUCCH         | CSIRS         | PRS           |
|:--------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|
| OSC            |      ✔        |      ✔        |      ✔        |      ✔        |      ✔        |      ✔        |       ❌   |          ❌         |
| OAI            |      ✔        |      ✔        |      ✔        |      ✔        |      ✔        |      ✔        |      ✔        |      ✔        |
| SRS RAN        |      N/A       |      N/A       |      ✔        |      ✔        |      ✔        |      ✔        |      N/A       |      N/A       |

### MIMO Support comparison
| Project       | MIMO support  |
| ------------- |:-------------:|
| OSC           | N/A           |
| OAI           | 2T2R          |
| SRS RAN       | 4T4R          |

reference
- OSC [here](https://docs.o-ran-sc.org/projects/o-ran-sc-o-du-l2/en/latest/overview.html)
- OAI [here](https://gitlab.eurecom.fr/oai/openairinterface5g/-/blob/develop/doc/FEATURE_SET.md#openairinterface-5g-nr-feature-set)
- SRSRAN [here](https://github.com/srsran/srsran_project)
