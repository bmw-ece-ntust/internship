# PRACH Resource Configuration

**Goals**
- [x] Understand what is PRACH and why is it needed
- [x] Understand when PRACH is needed
- [x] Understand the mechanism of PRACH allocation

**What I have learned**
- Understanding of what is PRACH and why is it needed.
- Understanding of when PRACH is needed
- Understanding of the workings of PRACH
- Understanding of how PRACH is mapped in Time and frequency domain.
- Understanding of the configuration needed for PRACH.


Prior to the MSG1 process the gNB will broadcast SS/PBCH signal block order to provide the gNB RSRP Measurement, this measurement will determine which SS/PBCH block and gNB to use. In this step, the gNB also sends RACH related information using `RACH-ConfigCommon` which includes configuration for PRACH within `prach-ConfigurationIndex`.

> **This initial transmission includes serveral important parameters:**
> 
> Configuration of PRACH transmission Parameters which are defined in `prach-ConfigurationIndex`
>     
> * PRACH Preamble Format
> * Time Resources
> * Frequency Resources
> 
> Parameters for determining the root sequences and their cyclic shifts in the PRACH Preamble sequence set
> * index to logical root sequence table
> * Cyclic Shift(Ncs)
>  * Set Type (unrestricted, restricted set A or restricted set B)

## Time Domain Allocation
The PRACH settings is in `prach-ConfigurationIndex`. This configuration will take input in form of INTEGER {0...255} which each value corresponds to a unique PRACH configuration. The parameters that will be adjusted 

::: info
Details for all configuration can be seen on **[TS 38.211]([here](https://www.etsi.org/deliver/etsi_ts/138200_138299/138211/16.02.00_60/ts_138211v160200p.pdf))**
:::
1. **Preamble Format**: Preamble format to use
2. **$n_{sfn}$**: Radio frame in the UE will transmit PRACH
3. **SF Number**: Subframe in which RACH Ocassion are configured
4. **Starting Symbol**:
5. **Number of PRACH Slots within SF**:
6. **Number of Time-Domain ROs within PRACH Slot**:
7. **PRACH Duration**:

**Example 1:** PRACH Configuration Index = 0
| PRACH Config Index | Preamble Format | $n_{sfn}$, mod x = y | SF Number | Starting Symbol | Number of PRACH Slots within SF | Number of Time-Domain ROs within PRACH Slot | PRACH Duration |
|:------------------:|:--------:|:-------:|:----:|:---------------:|:--------------------------:|:--------------------------------------:|:--------------:|
| 27 | 0 | x = 1, y = 0 | 0,1,2,3,4,5,6,7,8,9 | 0 |- | - | 0 |

In this case, x is 16 and y = 1. It means UE is allowed to transmit PRACH in every odd radio frame (i.e, the radio frame meeting $n_{SFN}$ mod 16 = 1).  UE is allowed to transmit the PRACH at SFN = 1, 17, 33, ....
In this case, Subframe number is set to 1. It means that UE can transmit PRACH at the subframe 1 within the radio frame determined as above.
 
**Example 2:** PRACH Configuration Index = 27
| PRACH Config Index | Preamble Format | $n_{sfn}$, mod x = y | SF Number | Starting Symbol | Number of PRACH Slots within SF | Number of Time-Domain ROs within PRACH Slot | PRACH Duration |
|:------------------:|:--------:|:-------:|:----:|:---------------:|:--------------------------:|:--------------------------------------:|:--------------:|
| 27 | 0 | x = 16, y = 1 | 1 | 0 |- | - | 0 |

In this case, x = 1 and y = 0. It means UE is allowed to transmit PRACH in radio frame (i.e, the radio frame meeting n_SFN mod 1 = 0). UE is allowed to transmit at every SFN.
In this case, Subframe number is set to 0,1,2,3,4,5,6,7,8,9. It means that UE can transmit PRACH at any subframe within the radio frame determined as above.

---
**Exercise: Draw timing diagram for PRACH config index = 40 and 100 (FR1 Unpaired spectrum)**
>**Key details:**
>
>- PRACH Length is determined by the preamble format, sum of $T_{CP}$ and $T_{SEQ}$. [Details](https://www.sharetechnote.com/html/5G/5G_RACH.html#TimeDomainStructure_of_Preamble_Format)
>- PRACH Slots location is determined by the starting symbol. [Details](https://www.sharetechnote.com/html/5G/5G_RACH.html#TimeDomain_RO_Ex)

| PRACH Config Index | Preamble Format | $n_{sfn}$, mod x = y | SF Number | Starting Symbol | Number of PRACH Slots within SF | Number of Time-Domain ROs within PRACH Slot | PRACH Duration |
|:------------------:|:--------:|:-------:|:----:|:---------------:|:--------------------------:|:--------------------------------------:|:--------------:|
| 40 | 3 | x = 16, y = 1 | 9 | 0 |- | - | 0 |

- Preamble format = 0, PRACH length = $T_{CP} + T_{SEQ} \approx 0.9038$ ms

    $28 \cdot 0.9038 = 25.3  \text{ Slot} $
![Preamble 0](https://imgur.com/DYFYlcw.png)
- Starting Symbol = 0, the frame starts from 0

    ![40](https://imgur.com/L2c1J0b.png)


| PRACH Config Index | Preamble Format | $n_{sfn}$, mod x = y | SF Number | Starting Symbol | Number of PRACH Slots within SF | Number of Time-Domain ROs within PRACH Slot | PRACH Duration |
|:------------------:|:--------:|:-------:|:----:|:---------------:|:--------------------------:|:--------------------------------------:|:--------------:|
| 100 | A2 | x = 1, y = 0 | 9 | 9 |1 | 1 | 4 |

- **PRACH Length**
    Preamble format = A2, PRACH length = $T_{CP} + 4 \cdot T_{SEQ} \approx 0.2856$ ms

     $28 \cdot 0.2856 = 7.9968  \text{ Slot} $
     >Seeing examples from this [example](https://www.sharetechnote.com/html/5G/5G_RACH.html#TimeDomain_RO_Ex), the slot is somehow divided by two. so it will be 3,9984

    ![Preamble A2](https://imgur.com/iKIArzj.png)

- **PRACH Slots**

    Using this equation
    > $$ l = l_0 + n^{RA}_{t} N^{RA}_{dur} + 14 \cdot n^{RA}_{slot}  $$
    > $$ l = 9 + 0 \cdot 4 + 14 \cdot 1 = 23 $$
    > ---
    > $$l_0 = \text{Starting Symbol = 9}$$
    > $$ n^{RA}_{t} = \text{0 to (Number of Time-Domain ROs within PRACH Slot - 1) = [0]}$$
    > $$N^{RA}_{dur} = \text{PRACH Duration} = 4$$
    > $$n^{RA}_{slot} = [1]$$
    > ![N RA Slot](https://imgur.com/qqDxl2B.png)

    ![100](https://imgur.com/gAVspSY.png)


---

## Frequency Domain Allocation
For PRACH, allocation for frequency domain is handled by `msg1-FDM` and `msg1-FrequencyStart`

 **msg1-FDM**: Indicates the number of RACH Occasion
 **msg1-FrequencyStart**: Indicates the offset for the lowest frequency in PRACH Occasion
 
<img src="https://hackmd.io/_uploads/SkpBCwC_p.png" width = "500"/>

 
### RACH Occasion

RACH Occasion is an area specified in time and frequency domain that are available for the reception of RACH preamble.

**Basic Idea:**
- The gNB will transmit multiple SSBs (Sync Signal Block)
- The UE will select the best among those SSB and send PRACH using that beam
- gNB needs to figure out which beam is selected by the UE.
- By detecing which RO UE send PRACH to, NW can figure out which SSB Beam that UE has selected.

Mapping for RACH Occasion is determined by
- `msg1-FDM`: specifies how many RO are allocated in frequency domain (at the same location in time domain).
- `ssb-perRACH-OccasionAndCB-PreamblesPerSSB`: 
    - `ssb-perRACH-Occasion`: how many SSB can be mapped to one RO
    - `CB-PreamblesPerSSB`: how many premable index can be mapped to single SSB.
    - `totalNumberOfRA-Preambles`: Total Number of Preambles available per RO


**Visualisation for RACH Occasion**


`msg1-FDM`= 1
`ssb-perRACH-OccasionAndCB-PreamblesPerSSB`: 2:16
![image](https://hackmd.io/_uploads/ry0V8_Cu6.png)
:::


`msg1-FDM`= 2
`ssb-perRACH-OccasionAndCB-PreamblesPerSSB`: 1/2:4
![image](https://hackmd.io/_uploads/rJjvpd0u6.png)

`msg1-FDM`= 4
`ssb-perRACH-OccasionAndCB-PreamblesPerSSB`: 1/2:8

**SSB 2 SHOULD BE SSB 1**
![image](https://imgur.com/YuknR6k.png)

`msg1-FDM`= 1
`ssb-perRACH-OccasionAndCB-PreamblesPerSSB`: 4:8
![image](https://imgur.com/ZD1lg2F.png)




> Visualization for these parameters can be shown in this [website](https://www.nrexplained.com/ra_msg1)


>**Association Period:**
>
>Timeframe during which the mapping of SS/PBCH block indexes to PRACH occasions is performed. The association period starts from frame 0 and is determined based on the smallest value in a set determined by the PRACH configuration period according to Table 8.1-1. This mapping ensures that SS/PBCH block Tx indexes are associated with PRACH occasions.
> 
>**Association Pattern Period:**
>
>Asociation pattern period includes one or more association periods and is designed to repeat the pattern between PRACH occasions and SS/PBCH block indexes at most every 160 milliseconds. If, after an integer number of association periods, there are PRACH occasions or preambles not mapped to SS/PBCH block indexes, those PRACH occasions or preambles are not used for PRACH transmissions.
>
>**Summary:** 
>
>the association period and association pattern period are defined to establish a mapping pattern between SS/PBCH block indexes and PRACH occasions in a 5G or beyond cellular network, ensuring efficient and systematic utilization of resources for Random Access procedures.





---

Specification for RACH-ConfigCommon based on **3GPP TS 38.331**
```
RACH-ConfigCommon ::= SEQUENCE {
    rach-ConfigGeneric                      RACH-ConfigGeneric,
    totalNumberOfRA-Preambles               INTEGER (1..63) OPTIONAL, -- Need S
    ssb-perRACH-OccasionAndCB-PreamblesPerSSB CHOICE {
        oneEighth               ENUMERATED {n4,n8,n12,n16,n20,n24,n28,n32,n36,n40,n44,n48,n52,n56,n60,n64},
        oneFourth               ENUMERATED {n4,n8,n12,n16,n20,n24,n28,n32,n36,n40,n44,n48,n52,n56,n60,n64},
        oneHalf                  ENUMERATED {n4,n8,n12,n16,n20,n24,n28,n32,n36,n40,n44,n48,n52,n56,n60,n64},
        one                       ENUMERATED {n4,n8,n12,n16,n20,n24,n28,n32,n36,n40,n44,n48,n52,n56,n60,n64},
        two                       ENUMERATED {n4,n8,n12,n16,n20,n24,n28,n32},
        four                      INTEGER (1..16),
        eight                     INTEGER (1..8),
        sixteen                  INTEGER (1..4)
    } OPTIONAL, -- Need M
    groupBconfigured SEQUENCE {
        ra-Msg3SizeGroupA          ENUMERATED {b56, b144, b208, b256, b282, b480, b640,
                                               b800, b1000, b72, spare6, spare5,spare4, spare3, spare2, spare1},
        messagePowerOffsetGroupB    ENUMERATED { minusinfinity, dB0, dB5, dB8, dB10, dB12, dB15, dB18},
        numberOfRA-PreamblesGroupA  INTEGER (1..64)
    } OPTIONAL, -- Need R
    ra-ContentionResolutionTimer          ENUMERATED { sf8, sf16, sf24, sf32, sf40, sf48, sf56, sf64},
    rsrp-ThresholdSSB                      RSRP-Range OPTIONAL, -- Need R
    rsrp-ThresholdSSB-SUL                  RSRP-Range OPTIONAL, -- Cond SUL
    prach-RootSequenceIndex CHOICE {
        l839             INTEGER (0..837),
        l139             INTEGER (0..137)
    },
    msg1-SubcarrierSpacing                SubcarrierSpacing OPTIONAL, -- Cond L139
    restrictedSetConfig                      ENUMERATED {unrestrictedSet, restrictedSetTypeA, restrictedSetTypeB},
    msg3-transformPrecoder               ENUMERATED {enabled} OPTIONAL, -- Need R
    ...,
    [[
    ra-PrioritizationForAccessIdentity-r16 SEQUENCE {
        ra-Prioritization-r16                  RA-Prioritization,
        ra-PrioritizationForAI-r16              BIT STRING (SIZE (2))
    } OPTIONAL, -- Cond InitialBWP-Only
    prach-RootSequenceIndex-r16 CHOICE {
        l571             INTEGER (0..569),
        l1151            INTEGER (0..1149)
    } OPTIONAL -- Need R
    ]]
}


```
**Note that this configuration has rach-ConfigGeneric within it**

```
RACH-ConfigGeneric ::= SEQUENCE {
    prach-ConfigurationIndex                    INTEGER (0..255),
    msg1-FDM                                    ENUMERATED {one, two, four, eight},
    msg1-FrequencyStart                         INTEGER (0..maxNrofPhysicalResourceBlocks-1),
    zeroCorrelationZoneConfig                   INTEGER(0..15),
    preambleReceivedTargetPower                 INTEGER (-202..-60),
    preambleTransMax                            ENUMERATED {n3, n4, n5, n6, n7, n8, n10, n20, n50, n100, n200},
    powerRampingStep                            ENUMERATED {dB0, dB2, dB4, dB6},
    ra-ResponseWindow                           ENUMERATED {sl1, sl2, sl4, sl8, sl10, sl20, sl40, sl80},
    ...,
    [[
    prach-ConfigurationPeriodScaling-IAB-r16   ENUMERATED {scf1, scf2, scf4, scf8, scf16, scf32, scf64} OPTIONAL, -- Need R
    prach-ConfigurationFrameOffset-IAB-r16     INTEGER (0..63) OPTIONAL, -- Need R
    prach-ConfigurationSOffset-IAB-r16         INTEGER (0..39) OPTIONAL, -- Need R
    ra-ResponseWindow-v1610                    ENUMERATED { sl60, sl160} OPTIONAL, -- Need R
    prach-ConfigurationIndex-v1610              INTEGER (256..262) OPTIONAL -- Need R
    ]]
}

```
'prach-ConfigurationIndex' can be seen at [here](https://www.etsi.org/deliver/etsi_ts/138200_138299/138211/16.02.00_60/ts_138211v160200p.pdf)
