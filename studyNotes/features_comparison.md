## DU Feature Comparison Between OSC,OAI and SRSRAN

This section discuss the features available in the DU which is RLC, Mac Scheduler, and PHY channels 


(note : N/A means information yet to be found)

### RLC Operation comparison
| Project       | RLC Operation |
| ------------- |:-------------:|
| OSC           | manual installation of 3GPP required |
| OAI           | 38.322 Rel.16 3GPP standard          |
| SRS RAN       | Transparent mode, Unacknowledge mode, Acknowledge mode|

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
| SRS RAN        |      N/A       |      N/A       |      N/A       |      N/A       |      N/A       |      N/A       |      N/A       |      N/A       |

