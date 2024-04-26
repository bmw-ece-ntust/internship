# Energy Saving Commands for Aruba 2540 24G PoE+ 4SFP+ (JL356A)

Table of Contents
- [Energy Saving Commands for Aruba 2540 24G PoE+ 4SFP+ (JL356A)](#energy-saving-commands-for-aruba-2540-24g-poe-4sfp-jl356a)
  - [PoE-lldp-detect](#poe-lldp-detect)
  - [show power-over-ethernet ](#show-power-over-ethernet-)
  - [show tech](#show-tech)
  - [show system power-supply detailed](#show-system-power-supply-detailed)


## PoE-lldp-detect
Enabling PoE-lldp-detect allows the data link layer to be used for power negotiation. When a PD requests
power on a PoE port, LLDP interacts with PoE to see if there is enough power to fulfill the request. Power is set at
the level requested. If the PD goes into power-saving mode, the power supplied is reduced; if the need for power
increases, the amount supplied is increased. PoE and LLDP interact to meet the current power demands.

Example:
You can enter this command to enable LLDP detection:

`switch(config) # int 7 PoE-lldp-detect enabled`

or in interface context:

`switch(eth-7) # PoE-lldp-detect enabled`

Port with LLDP configuration information obtained from the device
![image](/images/lldp.png)

Detail:
| Field            | Description                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------------------|
| PoE Port     | Lists all PoE-capable ports on the switch.            |
| Power Enable         | Shows Yes for ports enabled to support PoE (the default) and No for ports on which PoE is disabled.                          |
| Power Priority      | Lists the power priority (Low, High, and Critical) configured on ports enabled for PoE.                             |
| Alloc by | Displays how PoE is allocated (usage, class, value)  |
| Alloc Power | The maximum amount of PoE power allocated for that port (expressed in watts.)Default: 17 watts for PoE; 33 watts for PoE+.  |
| Actual Power | The power actually being used on that port.  |
| Configured Type | If configured, shows the user-specified identifier for the port. If not configured, this field is empty.  |
| Detection Status: | Searching (The port is trying to detect a PD connection), Delivering (The port is delivering power to a PD), Disabled (On the indicated port, either PoE support is disabled or PoE power is enabled but the PoE module does not have enough power available to supply the port's power needs), Fault (The switch detects a problem with the connected PD), Other Fault (The switch has detected an internal fault that prevents it from supplying power on that port) |
| Power Class     | Shows the 802.3af power class of the PD detected on the indicated port.            |

## show power-over-ethernet <port-list>
Displays the following PoE status and statistics (since the last reboot) for each port in `<port-list>` :

| Field            | Description                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------------------|
| Power Enable     | Shows Yes for ports enabled to support PoE (the default) and No for ports on which PoE is disabled.            |
| Priority         | Lists the power priority (Low, High, and Critical) configured on ports enabled for PoE.                          |
| Allocate by      | How PoE is allocated (usage, class, value).                                                                      |
| Detection Status | - Searching: The port is trying to detect a PD connection.                                                       |
|                  | - Delivering: The port is delivering power to a PD.                                                               |
|                  | - Disabled: On the indicated port, either PoE support is disabled or PoE power is enabled but the PoE module does not have enough power available to supply the port's power needs. |
|                  | - Fault: The switch detects a problem with the connected PD.                                                     |
|                  | - Other Fault: The switch has detected an internal fault that prevents it from supplying power on that port.     |
| Over Current Cnt | Shows the number of times a connected PD has attempted to draw more than 15.4 watts for PoE or 24.5 watts for PoE+. Each occurrence generates an Event Log message. |
| Power Denied Cnt | Shows the number of times PDs requesting power on the port have been denied because of insufficient power available. Each occurrence generates an Event Log message. |
| Voltage          | The total voltage, in volts, being delivered to PDs.                                                             |
| Power            | The total power, in watts, being delivered to PDs.                                                               |
| LLDP Detect      | Port is enabled or disabled for allocating PoE power, based on the link-partner's capabilities via LLDP.        |
| Configured Type  | If configured, shows the user-specified identifier for the port. If not configured, the field is empty.          |
| Value            | The maximum amount of PoE power allocated for that port (expressed in watts). Default: 17 watts for PoE; 33 watts for PoE+. |
| Power Class      | Shows the power class of the PD detected on the indicated port. Classes include:                                   |
|                  | - 0: 0.44 to 12.95 watts                                                                                         |
|                  | - 1: 0.44 to 3.84 watts                                                                                           |
|                  | - 2: 3.84 to 6.49 watts                                                                                           |
|                  | - 3: 6.49 to 12.95 watts                                                                                          |
|                  | - 4: For PoE+; up to 25.5 watts can be drawn by the PD                                                   

![image](/images/poe.png)

## show tech
By default, the show tech command displays a single output of switch operating and running-configuration data
from several internal switch sources, including CPU usage

The show tech command output

![image](/images/tech.png)


##  show system power-supply detailed

Shows detailed switch power supply sensor information.

![image](/images/detail.png)
