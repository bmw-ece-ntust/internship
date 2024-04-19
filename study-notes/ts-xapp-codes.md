### Overview



### A1 Policy

```
{ "threshold": 5 }
```

### Anomaly Detection

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

### QoE Prediction Request (Sending)

```
{ "UEPredictionSet": ["Train passenger 2"] }
```

### Qoe Prediction Result (Receiving)

```
{
    "Train passenger 2":{
        "310-680-200-555001":[2000000, 1200000],
        "310-680-200-555002":[1000000, 4000000],
        "310-680-200-555003":[5000000, 4000000]
    }
}
```
