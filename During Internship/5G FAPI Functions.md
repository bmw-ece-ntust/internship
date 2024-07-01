# nr_initiate_ra_proc
Assigning Unique identifiers (RNTIs) to new users (UEs) in 5G network

```mermaid
flowchart TD 
  A(Start) -->B{ra==null?};
  B -->|True| D{ra-->rnti == 0?};
  B -->|False| E[Print failure];
  D -->F[Finding connected UE and in pending UE];
  F -->G[Loop++]
  G -->H{Loop = 100?};
  H -->|True| I[Initialization random access];
  H -->|False| F;
  I --> J[Set ra parameters];
  J --> K[Configure RA BWP];
  K --> L[Assign Beam ID];
  L --> M[Release lock];
  M --> N(END);
```

> [!NOTE]
> `Assign Beam ID` : Unique identifier for a specific beam direction used by the base station for directional communication with UE (User Equipment)


# phy_config_sib13_eNB
Configuration making sure each area are appropriately labeled
```mermaid
flowchart TD 
  A(Start) -->B{mbsfn_Area_idx == 0?};
  B -->|True| C[Assign bsfn_AreaId_r9 to fp->Nid_cell_mbfsn];
  C --> D[Need to be fixed message];
  D --> E[Call lte_gold_mbsfn and call te_gold_mbsfn_khz_1dot25];
  B -->|False| E;
  E --> F(End)
```
> [!NOTE]
> `Log Applying MBSFN Area ID` : MBFSN (Multicast Broadcast Single Frequency Networks). Enable tv services to be used by multiple users simultaneously

# get_mch_sdu
Accesses a branch (module_idP) and goes to a specific section (CC_id), and  returns the address where the MCH_pdu is stored in memory.

```mermaid
flowchart TD 
  A(Start) -->B[Taking the address of MCH.pdu];
  B --> C(End);
```

> [!NOTE]
> `MCH_pdu` is a data unit used to encapsulate and transmit multicast or broadcast data in LTE systems.

![image](https://github.com/bmw-ece-ntust/internship/assets/123353805/dff1cf43-e6c0-40ee-a534-a9850623b0c3)
