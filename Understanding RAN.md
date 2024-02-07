## :signal_strength:  Understanding RAN
RAN or Radio Access Network is an important component that can be found in wirelees telecommunications system which connects end-user devices, like cellphone or smarphone or computer to the cloud. The link user equipment goes to the core network which manages subscriber information, location, etc. RAN is the radio element of the cellular network. Cellular network itself is made up of land areas called cells  with each cell served by at least one until three radio transceiver.
The capabilities of RAN have expanded to include voice calls, text messaging, and video and audio streaming. The types of user equipment using these networks have drastically increased, including all types of vehicles, drones and internet of things devices.

![image](https://github.com/bmw-ece-ntust/internship/assets/123353805/6558ce88-d8f5-4fc7-9006-7a047d35117b)

RAN would need three main elements :
1) Antennas which convert electrical signals into radio wave
2) Radios which transform digital information into signals so that it can be sent wirelessly and transmissions are the correct frequency abdns in the right power levels
3) Baseband Units (BBUs) enables wirelees communications with a set of signal processing functions. BBU processing will detects errors, secures the wireless signal, and ensure that wireless resources are used effectively.

The Radio Access Network (RAN) plays a crucial role in managing resources and facilitating wireless connections between devices and the core network. In older generations like 2G and 3G, the RAN controller controlled the node management and connectivity to both circuit-switched and packet-switched networks. However, the emergence of 4G LTE brought significant changes, notably with the introduction of Cloud RAN (C-RAN), which separates radio elements from the baseband controller to better adapt to modern mobile demands. Today's RAN architecture further enhances flexibility by dividing the user and control planes into distinct elements. This separation allows for more efficient data management through software-defined networking and facilitates advanced techniques like network slicing and high MIMO necessary for 5G networks.

Radio access have variour network types which include, Open RAN or O-RAN, C-Ran, Global System for Mobile communication RAN. We'll be focusing on O-RAN
![image](https://github.com/bmw-ece-ntust/internship/assets/123353805/19bc19c4-14d8-4913-a158-9fd411c8a6f0)


## O-RAN
O-RAN involves developing interoperable open hardware, software, and interfaces for cellular wireless networks provided by different vendors. Thus, making multiple vendors can co-exist within a single Communication Service Providers (CSP's) RAN domain. Three important elemens of Open RAN include Cloudification, Intelligent automation, and Open interfaces. Open RAN enables the cloudification fo RAN with separation of hardware and software with open interoperable interfaces, and improved intelligence and automation in radio access networks (using open management and orchestation systems, and interfaces). Open RAN is built on top of the 3GPP architecture and is fully interoperable with the evolution of the broader network, including Core and Transport.

## Source : 
- https://www.techtarget.com/searchnetworking/definition/radio-access-network-RAN
- https://www.ericsson.com/en/openness-innovation/open-ran-explained
- https://www.techtarget.com/searchnetworking/definition/radio-access-network-RAN
- https://moniem-tech.com/2021/04/16/what-is-the-difference-between-traditional-ran-and-open-ran/
