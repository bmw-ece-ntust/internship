Configuring trunk port
========================
the figure below illustrate the purpose of this configuration
![image](https://github.com/user-attachments/assets/1bdadc61-12d4-4f5c-8a51-6d9bb7384ec4)

[1] enter configuration mode
```
test#configuration terminal
test(config)#
```
[2] enter interface mode
```
test(config)#interface fastEthernet 0/48
test(config-if)#
```
[3] check and select the trunk mode
```
test(config-if)#switchport trunk encapsulation ?
```
this will show the option available for encapsulation
```
test(config-if)#switchport trunk encapsulation dot1q
```
[4] switch operating mode to trunk
```
test(config-if)#switchport mode trunk
```
[5] to check the configuration
```
test#show run interface fasEthernet 0/48
```
note : switch that are connected to each other via trunk port must be configured with the same trunk configuration
