Configuring network switch
========================
note : this is initial setup of switch

### Naming the switch
[1] connect to switch using Putty or other program

[2] wait until the terminal shows :
```
switch>
```
switch is the default name of the switch (default name may differ), to start the configuration
use "enable" command
```
switch>enable
switch#
```
[3] enter configuration mode with command "configure terminal"
```
switch#configure terminal
switch(config)#
```
[4] enter the command "hostname" to change the host name followed by the new name
```
switch(config)#hostname test
test(config)#
```
### Setting up password for the switch
[1] go to config mode and type "enable password" followed by the password
```
test(config)#enable password test
```
[2] log out and try to enter via enable command (it should request a password now)

### VLAN Configuration
[1] list all available vlan with the command "show vlan"
```
test#show vlan
```
note : default is VLAN 1


the terminal should list all of port with assigned vlan

[2] to add vlan, enter configuration mode and type vlan followed by the number
```
test# configure terminal
test(config)#vlan 10
test(config-vlan)#
```
after inputing the vlan number, the terminal should enter configuration mode for the vlan

[3] to name the VLAN simply use "name" command followed by the name
```
test(config-vlan)#name sales
```
[4] go to step 1 to check whether the VLAN is registered into the VLAN list


[5] previous VLAN setup only register the VLAN name without assigning it to the switch port, to assign it :
```
test(config)#interface fastEthernet 0/1
test(config-if)#switchport mode access
test(config-if)#switchport access vlan 10
test(config-if)#exit
test(config)#do show vlan
```
the example above will assign vlan 10 to fastEthernet 0/1 as access port

[6] to setup multiple access ports, we can use "range" command such as
```
test(config)#interface range fastEthernet 0/1-10
```
to set the range : 0/start-stop 


the example above will set fa 0/1 until fa 0/10 as VLAN 10 port


### Assigning IP address to VLAN
[1] enter interface mode for desired VLAN
```
test(config)#interface vlan 10
test(config-if)# 
```
[2] to assign the ip address use "ip address" command followed by the ip address and bit mask
```
test(config-if)#ip address 10.10.10.1 255.255.255.0
```

[3] to check the ip address go back to test# and then use "show ip interface brief"
```
test(config-if)#exit
test(config)#exit
test#show ip interface brief
```
### Enabling inter VLAN routing
to enable inter VLAN routing simply use
```
test(config)#ip routing
```
### Configuring DHCP for automatic ip assignment
[1] go to config mode and create a dhcp pool using "ip dhcp pool" followed by the pool name
```
test(config)#ip dhcp pool 10
test(dhcp-config)#
```
[2] define the network where the VLAN resides
```
test(dhcp-config)#network 10.10.10.0 /24 
```
the example above define VLAN 10 network


[3] define the default router for the network, which is the VLAN 10 ip address itself
```
test(dhcp-config)#default-router 10.10.10.1
```
[4] to exclude an IP address for DHCP ip assignment, we can use "excluded-address" command followed by the ip range (low and high) 
```
test(config)#ip dhcp excluded-address 10.10.10.1 10.10.10.10
```
the command above will exclude ip from 1-10 for 10.10.10 (DHCP will not assign this ip to any connected devices on the switch)

### Saving configuration file
to save configuration file simply
```
test#copy running-config startup-config
```




