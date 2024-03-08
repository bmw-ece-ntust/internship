# [O-RAN.WG1.Use-Cases-Detailed-Specification-R003-v13.00](https://orandownloadsweb.azurewebsites.net/specification) 
# Use case 21: Energy Saving
-  Energy saving (ES) techniques can be implemented at different timescales and cell loads, such as switching off carriers or cells, RF channel switching, and Advanced Sleep Modes (ASM).
- ES solutions can be applied to various components of the O-Cloud, including O-CU and O-DU.  AI/ML helps figure out the best times to switch things off and on for maximizing energy savings.
![Alt text](https://hackmd.io/_uploads/ByjNQ9d6p.png)
![Alt text](https://hackmd.io/_uploads/rk2lv5_pp.png)

### Table from diagram
| stage | Non-RT RIC |Near-RT RIC |
| :---: | --- |---|
|1| SMO initiates specific measurement data collection request towards E2 Node and O-RU for AI/ML model training.| **same**| 
|2| E2 Node and O-RU send the configured measurement data to SMO periodically|**same**| 
|3| Non-RT RIC retrieves the collected measurement data for processing|**same**| 
|4| Non-RT RIC monitor performance and energy consumption of the E2 Node, also energy consumption of O-RU.|Non-RT RIC  trains the AI/ML models with the collected data. Trained AI/ML models are deployed, configured, and activated in the Near-RT RIC.  | 
|5| Based on the AI/ML inference the Non-RT RIC can request the SMO to configure E2 Node to prepare and execute cell or carrier switch off/on. |SMO can trigger EE/ES optimization and might provide policies guiding  the Near-RT RIC EE/ES function via O1 and/or A1 interface. |
|6|SMO guides E2 node via O1 to fulfill Non-RT RIC requests. O-RU receives updated configuration through Open FH M-Plane from E2 Node or SMO. SMO is notified by E2 Node/O-RU upon completion of cell or carrier switch off/on. |Near-RT RIC monitor performance and energy consumption of the E2 Node, also energy consumption of O-RU. E2 Node can request O-RU Node to prepare and execute cell or carrier switch off/on. E2 Node will notify Near-RT RIC once cell or carrier switch off/on is completed.|
|7|Non-RT RIC monitors AI/ML model performance. If energy-saving goals aren't met, it may trigger fallback, AI/ML model update, or retraining.|**--**|

**ends when**: E2 Node becomes non-Operational or when the operator disables the optimization functions for Energy Saving. 
