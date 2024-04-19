### Overview

Like how it was stated in the preceding study notes, TS xApp consumes A1 Policy Intent, listens for badly performing UEs, sends prediction requests to QP xApp, and listens for messages from QP that show UE throughput predictions in different cells to make decisions about UE Handover. Now, here is how the codes work.

### A1 Policy

A1 Policy plays a pivotal role in the Traffic Steering (TS) xApp within the Near-RT RIC (Radio Intelligent Controller). The A1 Policy defines the intent that drives the behavior of the Traffic Steering xApp. It instructs the xApp on how to handle specific scenarios related to UE (User Equipment) handovers. The Policy Type ID for A1 Policy is 20008.

Currently, there is only one parameter that can be provided in the A1 Policy: threshold. Below is how the example works:

```
{ "threshold": 5 }
```

This policy instructs the Traffic Steering xApp to initiate a handover for any UE whose downlink throughput in its current serving cell is 5% below the throughput of any neighboring cell. When the Traffic Steering xApp receives an Anomaly Detection (AD) message from the AD xApp, it listens attentively. Upon detecting badly performing UEs, the Traffic Steering xApp sends a QoE Prediction Request to the QoE Prediction (QP) xApp. The QP xApp responds with UE throughput predictions for different cells. Based on these predictions, the Traffic Steering xApp decides whether a UE should be handed over to a neighboring cell.

### Receiving Anomaly Detection

This one works just right with the help from Anomaly Detection (AD xApp). The AD xApp is responsible for detecting anomalous UEs (User Equipment) present in the network. It regularly fetches UE data from the Shared Data Layer (SDL) and monitors UE metrics. When it identifies UEs exhibiting abnormal behavior (such as poor performance), it communicates this information to the Traffic Steering xApp.

The Traffic Steering xApp defines a callback to listen for Anomaly Detection messages received from the AD xApp. These messages arrive via the RMR (RAN Management and Control Interface) channel, specifically using the message type 30003. Here is how the message body looks like as an example:

```
[
    {
        "du-id":1010,
        "ue-id":"Train passenger 2",
        "measTimeStampRf":1620835470108,
        "Degradation":"RSRP RSSINR"
    }
]
```

Above, the message provides details about a UE with ID “Train passenger 2” that experienced degradation in specific metrics (e.g., RSRP and RSSINR).

### QoE Prediction Request (Sending)

Upon receiving an Anomaly Detection message, the Traffic Steering xApp initiates a QoE Prediction Request to the QoE Prediction (QP) xApp. The purpose is to obtain throughput predictions for the serving cell and neighboring cells for the identified UE. The RMR message type for this request is 30000. Here is one of the exhibits:

```
{ "UEPredictionSet": ["Train passenger 2"] }
```

### Qoe Prediction Response (Receiving)

Lastly, after processing the QoE Prediction Request, the QP xApp responds with throughput predictions. The Traffic Steering xApp defines another callback to receive these predictions from the QP xApp. The RMR message type for this response is 30002. This is how it looks:

```
{
    "Train passenger 2":{
        "310-680-200-555001":[2000000, 1200000],
        "310-680-200-555002":[1000000, 4000000],
        "310-680-200-555003":[5000000, 4000000]
    }
}
```

Above, the throughput predictions for three cells are provided for the UE “Train passenger 2.” Each array contains DL (downlink) and UL (uplink) throughput predictions. The TS xApp then checks if the predicted throughput in any neighboring cell is higher than the serving cell’s throughput for the UE. If that's the case, it'll make decisions about UE handover based on this information.
