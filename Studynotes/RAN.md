# Open RAN

## History of RAN Development

To discuss Open RAN, it's essential to delve into the evolution of network communication. Initially, Radio Access Network (RAN) technology debuted with 1G and has progressed through subsequent generations up to 5G. In the Legacy Architecture of RAN, physical sites housed both the remote radio head (RRH) and baseband units (BBUs) in close proximity. The RRH handled radio signal processing, while the BBUs managed digital signal processing for data traffic, connecting to the core network via a backhaul transport network.

Over time, some service providers transitioned to a new model known as Centralized RAN (C-RAN). In C-RAN, BBUs are consolidated in central locations, such as data centers, and linked to RRHs through a fronthaul transport network. C-RAN takes advantage of different types of new technologies like the Common Public Radio Interface (CPRI) standard, which gives C-RANs the ability to transmit over long distances reliably from a centralized tower deployment. The centralization of BBUs offers operational expenditure (OpEx) savings and streamlines radio network management, representing physical BBU pooling without cloud involvement.

Subsequently, virtualized RAN (vRAN or V-RAN) emerged, shifting BBU functionalities to the cloud for enhanced agility, scalability, and control. vRAN eliminates hardware constraints across RANs, fostering improved interoperability and communication. It decouples network functions from hardware, enabling function disaggregation and heightened flexibility.

Open RAN marks a significant departure from past practices, where interfaces between BBUs and RRHs were proprietary, limiting vendor choices. Open RAN introduces open interfaces, dismantling the previous architecture. Instead of the integrated RRH and BBU setup, functions are disaggregated into the radio unit (RU), distributed unit (DU), and centralized unit (CU), connected via open interfaces. These functions can also be virtualized or containerized. Introducing the RAN Intelligent Controller (RIC) injects intelligence into networks, functioning as an app store for base stations. Service providers leverage the RIC to integrate third-party rApps/xApps, enhancing RAN capabilities at scale with AI/ML technologies and addressing innovative use cases.

![Image](https://juniper-prod.scene7.com/is/image/junipernetworks/dgm-1200x575_what-is-O-RAN-fig-1-12JAN22?wid=1750&dpr=off)


> From [Juniper Networks](https://www.juniper.net/us/en/research-topics/what-is-open-ran.html) "Open RAN stands for open radio access network. Specifically, Open RAN is an ongoing shift in mobile network architectures that enables service providers the use of non-proprietary subcomponents from a variety of vendors. Specific proprietary components like remote radio head (RRH) and baseband units (BBUs) are now disaggregated to centralized units (CU), distributed units (DU), and radio units (RU). With Open RAN, the new disaggregated functions can also be virtualized or containerized. The O-RAN Alliance takes it a step further by ensuring that the interfaces between these components are open and interoperable."



---
## Source
* [Juniper Networks : What Is Open Ran](https://www.juniper.net/us/en/research-topics/what-is-open-ran.html)
* [Red Hat : The Road to Cloud RAN from 1G to 5G](https://www.redhat.com/architect/mobile-architecture-cloud-ran)
* [Lumenci : Evolution of RAN](https://www.lumenci.com/research-articles/evolution-of-ran-the-road-from-1g-to-5g)
* [Tech Target : Radio Access Network (RAN)](https://www.techtarget.com/searchnetworking/definition/radio-access-network-RAN)


