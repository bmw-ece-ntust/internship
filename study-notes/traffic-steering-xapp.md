### Traffic Steering Use Case and QoE Predictor xApp are already learnt in the preceding study note about the use case and QP xApp. Now to the main component, Traffic Steering xApp.

The Traffic Steering xApp is responsible for making decisions related to UE handover based on QoE (Quality of Experience) predictions. It is indeed a specialized tool designed for the OAIC O-RAN testbed. Its primary purpose is to efficiently manage and optimize traffic flow within cellular networks.

### More about the workflow!

This is how it works, first;
1. it consumes A1 Policy Intent (provided by the network operator), then,
2. it listens for badly performing UEs (User Equipment), then, 
3. it sends prediction requests to the QoE Prediction (QP) xApp, then,
4. it receives messages from QP containing UE throughput predictions in different cells, and lastly,
5. it uses these predictions to decide whether a UE should be handed over to a neighboring cell.

### What are the purposes of using Ts xApp in the use case? And what are the relevant features?
The TS xApp ensures optimal network performance by making informed decisions about user equipment (UE) handovers between cells. It collaborates with other components to dynamically improve the efficiency of traffic distribution in the RAN (Radio Access Network). By utilizing real-time metrics and adhering to dynamic policies, it enhances the overall network experience.

These below are the notable key features:
1. Interface Integration: The TS xApp directly communicates with the RAN through the E2 Interface, acquiring real-time metrics.
2. Health Check Operations: It performs health checks for components like RMR, E2, A1, and SDL.
3. KPIMON xApp Integration: Responsible for collecting RAN metrics and writing them to InfluxDB.
4. Dynamic Policy Management: Adapts traffic steering policies based on real-time updates from the A1 interface.
5. Load Balancing: Redistributes UEs across cells to achieve balanced load when overload is detected.
6. UE Profiling: Captures detailed profiles for each UE, including attributes like ID, cell, priority, type, origin, signal strength, and throughput.
7. InfluxDB Integration: Logs metrics and policies for historical data analysis and visualization using tools like Grafana.
8. Flask API Support: Enables external xApps to dynamically push or modify policies, supporting ML/RL/DRL plugins.
9. Scalability: Accommodates a growing number of UEs and cells while maintaining efficiency.
10. Modular Design: Allows for easy integration of future features.

### Getting started...

The prerequisites are the installation of both OAIC and SRSRAN and then finishing the setup of multiple UEs with initiated network traffic flow. The KPImon xApp should be running in the environment so that the TS xApp can optimize network traffic and ensure seamless connectivity.

More about it (next, to make the installation guide):
1. Execute the RIC installation and start srsRAN. (> srsRAN is already successfully installed in my environment!)
2. Clone the TS xApp repository from https://github.com/natanzi/ts-xapp.
3. Run the TS xApp in your environment.
4. Access the TS xApp dashboard and Grafana to monitor and analyze network performance.
