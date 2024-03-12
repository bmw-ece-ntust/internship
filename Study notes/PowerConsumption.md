>Lauren Christy (TEEP)

> [!WARNING]
> This note isn't final due to the uncertainty of the hardware specifications in Universitas Indonesia's system architecture. These are the potential specifications used and the commands supporting power saving.

## Table of Contents
- [Hardware Power Consumption](#hardware-power-consumption)
  - [Aruba 3810M (JL075A) (From Wi-Fi Controller to each floor)](#aruba-3810m-jl075a-from-wi-fi-controller-to-each-floor)
  - [Power Saving](#power-saving)
  - [Controlling PoE allocation](#controlling-poe-allocation)
  - [PoE port allocation by class](#poe-port-allocation-by-class)
  - [Manually configuring PoE power levels](#manually-configuring-poe-power-levels)


# Hardware Power Consumption
## Aruba 3810M (JL075A) (From Wi-Fi Controller to each floor) 

Use of the command `show power-over-ethernet brief` detailed shows the PoE status on all ports

```
switch(config)# show power-over-ethernet brief
Status and Counters - Port Power Status
System Power Status : No redundancy
PoE Power Status : No redundancy
Available: 273 W Used: 0 W Remaining: 273 W
Module A Power
Available: 273 W Used: 0 W Remaining: 273 W

PoE Port    | Power Enable  Power Priority  Alloc By    Alloc Power Actual Power    Configured Type Detection Status    Power Class
------      ------          ---------       -----       -----       ------          -----------     -----------         ---
A1          | Yes           low             usage       17 W        0.0 W           Phone 1         Searching           0
A2          | Yes           low             usage       17 W        0.0 W                           Searching           0
A3          | Yes           critical        usage       17 W        3.6 W                           Searching           0
A4          | Yes           critical        usage       17 W        4.0 W                           Searching           0
A5          | Yes           critical        usage       17 W        0.0 W                           Searching           0
A6          | Yes           high            usage       17 W        5.5 W                           Searching           0
A7          | Yes           high            usage       17 W        0.0 W                           Searching           0 
A8          | Yes           high            usage       17 W        0.0 W                           Searching           0
A9          | Yes           low             usage       17 W        0.0 W                           Searching           0
A10         | Yes           low             usage       17 W        12.0 W                          Searching           0

```

## Power Saving
According to the data sheet, its power sources and cosumption is outlined as
- Unrestricted functionality with **802.3at PoE**
- Power-save mode with reduced functionality from **802.3af PoE**

## Controlling PoE allocation
It allows user to manually allocate the amount of PoE power for a port by either its class or a defined value.

| Power class | Value |
| -------- | -------- |
| 0 | Depends on cable type and PoE architecture. Maximum power level output of 15.4 watts at the PSE.This is the default class; if there is not enough information about the load for a specific classification, the PSE classifies the load as class 0
| 1 | Requires at least 4 watts at the PSE. |
| 2 | Requires at least 7 watts at the PSE. |
| 3 | 15.4 watts         |
| 4 | For PoE+Maximum power level output of 30 watts at the PSE. |

## PoE port allocation by class
To allocate by class for ports 6 to 8:
```
switch# int 6-8 PoE-allocate-by class
```

## Manually configuring PoE power levels
Power level can be specified (in watts) allocated for a port by using the value option. This is the maximum amount of power that will be delivered.

Procedure:
1. To configure a port by value, first set the PoE allocation by entering the `poe-allocate-by value` command:
    ```
    switch(config) # int A6 poe-allocate-by value
    ```
    or in interface context
    ```
    switch(eth-A6) # poe-allocate-by value
    ```
2. Then select a value:
    ```
    switch(config) # int A6 poe-value 15
    ```
    or in interface context:
    ```
    switch(eth-A6) # poe-value 15
    ```
3. To view the settings, enter the show power-over-ethernet command, shown below.
   ```
   show power-over-ethernet A6
   ```
    <img width="428" alt="image" src="https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-11-Lauren/images/power.png">