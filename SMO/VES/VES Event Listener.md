## VES Event Listener

The VES acronym originally stood for Virtual-function Event Streaming, but VES has been generalized to support network-function event streaming, whether virtualized or not. The VES Event Listener is capable of receiving any event sent in the VES Common Event Format. In the VES Common Event Format,
an event consists of a required Common Event Header (i.e., object) accompanied by zero or more event domain blocks.
It should be understood that events are well structured packages of information,
identified by an eventName, which are asynchronously communicated to subscribers who
are interested in the eventName. Events can convey measurements, faults, syslogs,
threshold crossing alerts and other types of information. Events are simply a way of
communicating well-structured packages of information to one or more instances of an VES Event Listener service.

### Client Requirements
Any NF or client library that is responsible for delivering VES events to a VES Event Listener must comply with this specification to ensure events are received, accepted, and processed properly.

Because the VES specification relies on clients to push events to the VES Event Listener, the client assumes certain responsibilities such as:

* Providing configuration options supporting integration into a Service Provider environment
* Ensuring reliable delivery of events
* Customization of default behaviors based on Service Provider needs

### Common Event Format
The event captured by VES Listener will be have a JSON schema describing it,
the example can be downloaded [here](https://docs.onap.org/projects/onap-vnfrqts-requirements/en/latest/_downloads/8737e3270443f9847095547b05fe6df5/CommonEventFormat_30.2.1_ONAP.json).


