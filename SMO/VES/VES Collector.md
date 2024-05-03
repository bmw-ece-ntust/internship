## What is a VES Collector?
Virtual Event Streaming (VES) Collector (formerly known as Standard Event Collector/Common Event Collector) is RESTful collector for processing JSON messages into DCAE.
The collector supports individual events or eventbatch posted to collector end-point(s) and post them to interface/bus for other application to subscribe.
The collector verifies the source (when authentication is enabled) and validates the events against VES schema before distributing to DMAAP MR topics for downstream system to subscribe.
The VESCollector also supports configurable event transformation function and event distribution to DMAAP MR topics.

## Architecture
![image](https://github.com/bmw-ece-ntust/internship/assets/145204053/55e806bd-2dad-4e80-b818-917e6cd4563b)

## Flow

1. Collector supports different URI based on single or batch event to be received.
2. Post authentication - events are validated against schema. At this point - appropriate return code is sent to client when validation fails.
3. Event Processor checks against transformation rules (if enabled) and handles VES output standardization (e.g. VES 7.x input to VES5.4 output).
4. Optional (activated by flag collector.externalSchema.checkflag) post authentication of stndDefined fields - specific fields are validated against schema. At this point - appropriate return code is sent to client when validation fails.
5. If no problems were detected during previous steps, success HTTP code is being returned.
6. Based on domain (or stndDefinedNamespace), events are asynchronously distributed to configurable topics.
    If topic mapping does not exist, event distribution is skipped.
    Post to outbound topic(s).
    If DMaaP publish is unsuccessful, messages will be queued per topic within VESCollector.

Note: As the collector is deployed as micro-service, all configuration parameters (including DMaaP topics) are passed to the collector dynamically.
VEScollector refreshes the configuration from CBS every 5 minutes.
The Flowchart of VES Collector can be seen on the diagram below.

![image](https://github.com/bmw-ece-ntust/internship/assets/145204053/9201408e-ed80-49f2-8829-138a592c4159)

## Response Code
![image](https://github.com/bmw-ece-ntust/internship/assets/145204053/a4269ac3-f0a0-40fb-9dd3-64e60b712e32)


