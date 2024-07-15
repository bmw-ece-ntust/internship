5G Core Architecture Keypoint 
========================
### SBA (Service based Architecture)
The 3GPP defines a Service-Based Architecture (SBA) in which the control plane functionality and common data repositories of a 5G network are delivered through a set of interconnected Network Functions (NFs), with each NF authorized to access the services of other NFs.

note : 3GPP (3rd Generation Partnership Project) = agreed industry standard

### NF (Network Functions)
Network Functions is a independent pre-defined functional block that are used to run a certain process, where collectively these functional block forms an architecture

### CUPS (Control and User Plane Seperation)
This is an architectural concept which says that for a given network solution, the Control Plane (CP) and User Plane (UP) functions are different entities

![image](https://github.com/user-attachments/assets/d686b760-d00b-4565-bfbb-97c4e934a404)


### SA/NSA (StandAlone/Non-StandAlone)
#### Non-StandAlone Architecture
![image](https://github.com/user-attachments/assets/a476458d-f982-44ac-a98d-b27eded1eba2)


the graph above illustrates the non-standalone architecture where this architecture is hybrid between 5G and 4G. SgNB (Secondary NodeB) is part of 5G while MeNB( Master eNodeB) is part of 4G where this node will handle control plane data. The Control Plane will always go over the LTE layer *. The data bearers to the DC-enabled (Dual Connection) UE can go over LTE or over 5G. The data bearer that goes over 5G radio can be split and sent partially over 5G radio and partially over LTE radio (with data packets relayed over X2 connection).


deployment options for NSA is called Option 3x, the following graph illustrates the inner working of NSA Option 3x architecture


![image](https://github.com/user-attachments/assets/dbf2c340-a2cc-4e7a-8a35-fa81a56d7f58)


#### StandAlone Architecture
In this architecture, the main core used is 5GC without co-existing with 4G. The 5GC consists of AMF Access and Mobility Management  Function UPF User Plane Function

![image](https://github.com/user-attachments/assets/cf2629b7-380f-4ee0-adbf-4a8bb00d4f30)


#### Nx series interface 
Nx series interface is a reference point between multiple network functions. The x in N refered to different connection point (3GPP as reference), as example ,N2 interface refers to interface  between AMF and NG-RAN NF's while N3 refers to connection point between NG-RAN and UPF. Lastly, N6 interface denotes the connection between UPF and DN


![image](https://github.com/user-attachments/assets/4e3952ed-2ec1-4be5-91af-82623b233fe8)

notes :
```
AMF : Access Management Function
UPF : User Plane Function
DN : Data network
```
### Private Network
 private network is a computer network that uses a private address space of IP addresses.
