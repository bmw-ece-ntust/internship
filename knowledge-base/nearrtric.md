### Near-RT RIC

![ric](https://hackmd.io/_uploads/SkghXhqIA.png)

Near-RT RIC is a logical function that enables near-real-time control and optimization of RAN elements and resources via fine-grained data collection and actions over an E2 interface.xApp, an application designed to run on the Near-RT RIC, is central to the operation of Near-RT RIC. A question that often comes up is, what does ‘x’ mean? ‘X’ stands for any, so any app designed to run on the Near-RT RIC.

Each xApp is likely to consist of one or more microservices. At the point of on-boarding, microservices will identify which data it consumes and which data it provides. The important point that has excited many within our industry is that these applications are independent of the Near-RT RIC and may be provided by any third party. The E2 interface enables a direct association between the xApp and the RAN functionality.

It is important to point out that sometimes there can be overlapping or conflicting requests from multiple xApps. This can lead to a tricky situation as each application will typically change one or more parameters with the objective of optimizing a specific metric. This is where Conflict Mitigation steps in to resolve any conflicting actions.

