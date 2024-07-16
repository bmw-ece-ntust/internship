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
switch# configure terminal
switch(config)#
```
[4] enter the command "hostname" to change the host name followed by the new name
```
switch(config)# hostname test
test(config)#
```
