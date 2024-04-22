# Claim Check: Where is the multi UE part?
The claim that there is multi UE (multiple user equipment) in the O-RAN (Open Radio Access Network) refers to the support for multiple UE in the O-RAN architecture. The O-RAN architecture supports multi UE scheduling, with a maximum of 2 UE per TTI (Time Transmission Interval) in the scheduler. Additionally, the O-RAN architecture enables multi-layer decision-making, where a UE may perform intelligent sensing on its own. The JIRA tasks mentioned in the search results indicate that there are specific features and improvements related to multi UE resource allocation, PDSCH (Physical Downlink Shared Channel) allocation, and PDCCH (Physical Downlink Control Channel) allocation. 

Here is the flowchart of Multi UE in general:
![upload_faa51ca7ad6f1dc873c15191ea894617](https://hackmd.io/_uploads/SyDu9Sm-C.png)



To find where is the multi UE part, we can use the following steps.


1. Read the PDSCH codes in the O-DU High L2 Repository
![upload_eb3795efe4945557314753b1127a24bd](https://hackmd.io/_uploads/SJ_AOrm-R.png)

2. Download/clone codes into O-DU High Directory
```
git clone “https://gerrit.o-ran-sc.org/r/o-du/l2”
```
3. Look for the updated code in the O-DU High repository for Multi UE
https://gerrit.o-ran-sc.org/r/c/o-du/l2/+/12580
![upload_d79772d75cee9a4b7bf4e21b5fd5049a](https://hackmd.io/_uploads/rys2dS7WA.png)


4. Open src/5gnrmac/lwr_mac_fsm.c", look for the updated codes, check the latest changes that made the codes turn into multi UE
![upload_1eed11f79858ee4d2b9269a13a670c18](https://hackmd.io/_uploads/SyqbYH7b0.png)


5. It can be seen that the changes made to transition from a single UE to multiple UEs:

- **Addition of UE Loop:**
Before multi-UE support, there was nohttps://hackmd.io/7aK94IPHQ8CyQ2V29Qke0A?both# loop for individual UEs. After the modification, a **`for`** loop iterates through each UE from 0 to **`MAX_NUM_UE`**, enabling the code to handle and process data related to each UE individually.
- **UE-Specific Index Utilization:**
Within the UE loop, the **`ueIdx`** variable is used to access UE-specific data. This index facilitates accessing configuration details such as PUSCH and PUCCH configurations for each UE.
- **Handling UE-Specific Information:**
Each UE may have different configurations. In the modified version, each UE is processed individually based on its specific configuration. For instance, for PUSCH, there are checks to determine if the UE is transmitting PUSCH data, and then the PUSCH data is filled accordingly.
- **Addition of UE Group Information:**
UE group information is added, possibly related to resource allocation or scheduling communication among specific UE groups. This information is added to efficiently manage multiple UEs. This might be related to handling multiple UEs efficiently by organizing them into groups. The code changes showed the incrementation of **`nGroup`** which suggests the management of UE groups.
- **Setting PDU Counts for Each UE:**
The count of Protocol Data Units (PDUs) is set individually for each UE. This can be observed in the snippet where the **`pduIdx`** variable is incremented for each UE, and the count of PDUs is calculated based on UE-specific configurations and data types.

These changes enable the code to efficiently manage multiple UEs, accessing and processing data relevant to each UE individually based on its specific configuration and requirements within the communication system.

6. Here is the flow differences summary between single UE and multi UE based on the code changes
- **Original Code:**
    - Single UE processing without iteration over multiple UEs.
    - Limited to handling data of a single UE at a time.
- **Introduction of Multi-UE Support:**
    - Addition of a loop structure to iterate over multiple UEs.
    - Initialize loop counter **`ueIdx`** to 0.
    - Loop through each UE from 0 to **`MAX_NUM_UE`**.
    - Increment **`ueIdx`** after each iteration.
- **UE-Specific Data Access:**
    - Utilize ueIdx to access UE-specific data within the loop.
    - Access UE configurations, such as PUSCH and PUCCH parameters, based on **`ueIdx`**.
- **Handling UE-Specific Information:**
    - Implement conditional statements to handle data specific to each UE.
    - Check UE-specific data types and configurations.
    - Perform actions based on UE-specific conditions, such as filling PUSCH PDUs if the UE is transmitting PUSCH data.
- **Incrementing PDU Counts:**
    - Increment PDU counts for each UE individually.
    - Increment **`pduIdx`** for each UE to keep track of PDUs processed.
    - Calculate PDU counts based on UE-specific data types and configurations.

![upload_9670d013fb79ff7226fd6fe36c140de7](https://hackmd.io/_uploads/S1rTcBXbC.png)


7. Open the code in Ubuntu paralel desktop
![upload_3ac8c553577e5dadb278a7198d0e21df](https://hackmd.io/_uploads/Hk7-crXWR.jpg)


## MULTI UE INSIDE LOWER MAC 5G NR
The code given was snippets from changes made in the `lwr_mac_fsm.c` file from single UE to multi UE.

Here's a summary of the functions and their purposes:

- getnPdus: Calculates the total number of Protocol Data Units (PDUs) to be allocated for an uplink Transmission Time Interval (TTI) request.
- fillPrachPdu: Sets the parameters for the Physical Random Access Channel (PRACH) PDU in an uplink TTI request.
- fillPuschPdu: Fills the parameters for the Physical Uplink Shared Channel (PUSCH) PDU in an uplink TTI request.
- fillPucchPdu: Populates the parameters for the Physical Uplink Control Channel (PUCCH) PDU in an uplink TTI request.

Each function takes input parameters related to the current UL TTI (Transmission Time Interval) request, such as UL slot information, cell configuration, and specific information related to PRACH, PUSCH, or PUCCH transmission.

The codes are mainly different in their repetition. Single UE only runs the process for 1 UE, while Multi UE iterates the process for each UEs available.

Here is the flowchart of Lower Mac for Single UE:
![image](https://hackmd.io/_uploads/HyDWGu1-A.png)

And here is the flowchart of Lower Mac for Multi UE:
![image](https://hackmd.io/_uploads/BJV5zO1WC.png)

---
Source
---

[Multi UE | Resource Allocation](https://jira.o-ran-sc.org/browse/ODUHIGH-540)

[O-DU High L2 Installation Guide](https://docs.o-ran-sc.org/projects/o-ran-sc-o-du-l2/en/latest/installation-guide.html#compilation)

[OAI Reference Architecture for 5G and 6G Research with USRP](https://kb.ettus.com/OAI_Reference_Architecture_for_5G_and_6G_Research_with_USRP)
