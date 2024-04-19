### What is Traffic Steering Use Case?

The Traffic Steering Use Case demonstrates intelligent inferences in the Near-RT RIC and E2 (E-UTRAN to EPC) interaction. It aims to execute these inferences to enhance the overall network performance. The use case comprises several xApps, each serving a specific purpose.

### QoE Predictor xApp is an integral component of the said use case within the Near-RT RIC. Then again, there are the components of the use case besides TS and QP:

1. KPI Monitoring xApp collects radio and system Key Performance Indicators (KPI) metrics from E2 Nodes and stores them in the Shared Data Layer (SDL),
2. Anomaly Detection (AD) xApp monitors UE (User Equipment) metrics, detects anomalous UEs, and communicates this information to other xApps, and,
3. RAN Control (RC) xApp implements spec-compliant E2-SM RC (RAN Control) to send RIC Control Request messages to RAN/E2 Nodes.

### So, what is the relevancy of QP xApp here?

It generates throughput predictions for serving and neighboring cells. The features used for prediction are cell unitization and UE signal strength measurements, so that it could generate a feature set of metrics based on SDL (Shared Data Layer) lookups in UE-Metric and Cell-Metric namespaces for a given UE. Afterwards, it outputs the said result above (predicting for serving cell and any neighboring cells).
