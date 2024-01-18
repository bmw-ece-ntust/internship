# Part 3: O1 Interface related in Near-RT RIC Platform
- Goal : 
    - [X] Learning O1 Interface
- Useful Links:
    - [O-RAN.WG10.O1-Interface.0-v08.00](https://www.o-ran.org/specifications)

- Outcome (Study Note) : 
    - Learn about O1 Interface

***

## I. O1 Notifications
An O1 notification is a **JSON encoded asynchronous notification** sent from a MnS provider to a MnS consumer over the O1 interface using REST/HTTPS.

An O1 notification shall be in one of the following formats:
- **SDO O1 format** : an O1 notification formatted as specified by a Standards Defining Organization (SDO) and sent without a VES header.
- **VES O1 format** : an O1 notification formatted as specified by VES Event Listener Specification, consisting of a common event header and domain-specific event fields. VES O1 format notifications are categorized into 2 types, based on domain:
    - **Harmonized VES** : The stndDefined VES event specified in VES Event Listener Specification that allows a VES event to carry, as its payload, a notification specified by an SDO.
    - **Legacy VES** : any VES event specified in the VES Event Listener Specification, except for stndDefined. Legacy VES events are fully defined in and don’t rely on an SDO to specify the content of the payload. 

## II. Management Services
### A. Provisioning Management Services
Provisioning Management Services allow a Provisioning MnS Consumer **to configure attributes** of managed objects on the Provisioning MnS Provider that modify the Provisioning MnS Provider’s capabilities in its role in end-to-end network services and allows a Provisioning MnS Provider **to report configuration changes** to the Provisioning MnS Consumer.
> Used **NETCONF** : Network Configuration Protocol

### B. Fault Supervision Management Services
Fault Supervision Management Services allow a Fault Supervision MnS Provider **to report errors and events** to a Fault Supervision MnS Consumer and allows a Fault Supervision MnS Consumer **to perform fault supervision operations** on the Fault Supervision MnS Provider, such as get alarm list.

### C. Performance Assurance Management Services
Performance Assurance Management Services allow a Performance Assurance MnS Provider **to report file-based (bulk) and/or streaming (real time) performance data** to a Performance Assurance MnS Consumer and allows a Performance Assurance MnS Consumer **to perform performance assurance operations** on the Performance Assurance MnS Provider, such as selecting the measurements to be reported and setting the frequency of reporting.

### D. Trace Management Services
Trace management services allow a Trace MnS Provider **to report file-based or streaming trace records** to the Trace MnS Consumer. 

File-based trace collects trace records in files that are available to the consumer with a time delay. In the case of streaming trace, the data is sent in bursts across a WebSocket connection to the consumer, maintaining the relevance of the data while minimizing transport overhead.

### E. File Management Services
File management services allow a File Management MnS Consumer **to get notification** of new available files; **query available files** and request the transfer of files between the File Management MnS Provider and the File Management MnS Consumer.

### F. Hearbeat Management Services
Heartbeat MnS Provider **sends asynchronous heartbeat notifications** to Heartbeat MnS Consumer at a configurable frequency to allow Heartbeat MnS Consumer to supervise the connectivity to the Heartbeat MnS Provider.

### G. PNF Startup and Registration Management Services
PNF Startup and Registration Management Services allow a physical PNF Startup and Registration MnS Provider **to acquire its network layer parameters** either via static procedures (pre-configured in the element) or via dynamic procedures (Plug-n-Connect) during startup.

### H. PNF Software Management Services
Software Management Services allow a PNF Software MnS Consumer **to request a physical PNF Software MnS Provider** to download, install, validate and activate a new software package and allow a physical PNF Software MnS Provider to report its software versions.

### I. PNF Reset Management Services
PNF Reset Management Services allow a PNF Reset MnS Consumer **to trigger a reset** of a HW unit of a PNF Reset MnS Provider on command.

### J. Cloudified NF Registration Management Services
The Cloudified NF Registration Management Service **supports the registration** of a Cloudified NF Registration Management Service Provider to the Cloudified NF Registration Management Service Consumer after the Cloudified NF instantiation via the O2 has completed and the NF application has initialized and is ready for final configuration and management (e.g., ready to be put in service).
