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

![image](https://github.com/bmw-ece-ntust/internship/assets/123353805/dff1cf43-e6c0-40ee-a534-a9850623b0c3)
