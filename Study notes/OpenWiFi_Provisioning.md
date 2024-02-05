# Provisioning

## Overview
The OpenWiFi Provisioning Service is a tool for managing different types of networks. It offers services such as roaming, client shared-key management, client steering, mobile offload, QoS-based services, and Layer 2 and Layer 3 breakout options. The Provisioning Service provides a comprehensive view of the network that supports inheritance of configuration templates that is suitable for flexible configurations for different scenarios.

In terms of configuration inheritance, the system starts with a list of devices and assigns them to different groups like locations or end users. This enables the inheritance of configurations for entities, venues, and subscribers, accommodating one-to-many and one-to-one configurations for unique devices like P2P links. Template inheritance is flexible, making it easy to set up all inherited configuration templates such as Entity, Child, and Venue. The accessibility of these features is facilitated through web interface and APIs.

## Creating Entities
### Overview
Entities in the Provisioning service act like folders to organize networks. Initially, the Entities tree is empty, with a Top Entity that can customized, like renaming it to "Operator Name." This Top Entity can hold general rules, such as 'no firmware upgrades' or specific RRM policies. To break things down, child entities can be created representing different divisions within the network. These child entities allows users to set specific rules for firmware upgrades or RRM policies tailored to each division. Essentially, entities can help to manage networks efficiently, with each entity serving as a customizable container for specific settings.

### Members of Entities
Entities represent a collection of resources for which certain business logic rules apply.

| Members of Entity | Description |
|----------|----------|
| Entity    | A child entity   |
| Venue    | A logical aggregation of devices, configurations, locations with Analytics   |
| Configuration    | Provisioning templates   |
| Inventory    | Device members   |
| Locations    | Device locations   |
| Contacts    | Administrative contact information   |
| Contacts    | Global common resources such as RADIUS services   |

### Configurations
Device provisioning is the process of setting up devices using predefined configurations. To start this setup, you go to the Configurations tab and create a new template.

#### **Create**
To create a configuration in the OpenWiFi system, Create Configuration dialog is used. In this dialog, there's a name for the configuration, and there are more than one device types to apply this configuration to.

<img width="428" alt="image" src="https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-11-Lauren/images/Provisioning.png">

If there are devices listed in an Entity or a Venue, but there are no configuration templates that match the device types of those devices, then no specific configuration will be applied to them. This logic allows for the layering of unique Wi-Fi device type configurations throughout the system. In simpler terms, the system only applies configurations to devices if there's a matching template, ensuring that each type of Wi-Fi device gets its specific settings.

#### **Advanced Radio Configuration**
In a practical scenario, an operator might want to set specific configurations at a higher level, such as defining the transmit power and MIMO operation for Wi-Fi 6 2x2 devices. To do this, add configuration parameters by selecting "Add Subsection" and choosing the relevant values.

For example, choose "Radios" subsection and specify the MIMO and transmit power settings. OpenWiFi supports all possible Wi-Fi radio bands. General properties that can be configured are Band, Bandwidth, Channel-Mode, TX-Power, Maximum-Clients, Country, etc. There are also advanced settings such as Multicast, Beacon-Rate, Beacon-Interval, etc.

If the administrator creates a new configuration template with the same weight as the previous one, focusing on advanced parameters. This new template can then be customized further, perhaps based on device type. Once the settings are saved, there are multiple configuration templates. Each template will influence radio operating parameters equally but separately based on the device type.

#### **Metrics Settings**
In some scenario, it is needed to establish telemetry settings for all devices. However, the system allows overriding these settings with using 'Metrics'.

The system maintains the capability to override these values, allowing fine-tuning of telemetry settings. This approach ensures a uniform telemetry setup across the network while enabling targeted adjustments.

| Metric | Description |
|----------|----------|
| WiFi Frames    | Select Management Frame reports to send   |
| Statistics    | Set Interval of all Statistics and types including SSID   |
| DHCP Snooping    | Select the DHCP & DHCPv6 frames to send in telemetry   |
| Health    | Interval to send automated health check score   |

## Creating Venues
Creating Venues is a important for OpenWiFi Provisioning for accessing Analytics that consolidates incoming telemetry and client events. This data is transformed based on the Venue's members, resulting in a dedicated Venues Dashboard. This Dashboard provides live client connection analysis and facilitates client tracking throughout the venue. 

> [!NOTE]
> Venues must be created within an entity, and it's recommended to establish the entity before defining a venue

<img width="428" alt="image" src="https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-11-Lauren/images/Venue.png">

### Configurations
To make a Venue, start within a non-root entity. Analytics becomes an available option within the Venue settings. It can be enabled to track device and client statistics. Then, as devices become associated with the Venue, their telemetry data is gathered and correlated by the Analytics service. This data is then displayed through the Dashboard, Live View, and Client Lifecycle features, providing a overview of device and client activities within the Venue. After this, the configuration is possible. These configurations are inherited by device memberships at the Venue level.

<img width="428" alt="image" src="https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-11-Lauren/images/VenueDashboard.png">



