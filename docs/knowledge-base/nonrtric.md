### Non-RT RIC

**Introduction**

The goal of Non-Real Time RAN Intelligent Controller (O-RAN Non-RT RIC) is to support intelligent RAN optimization by providing policy-based guidance, model management, and enrichment information to the Near-RT RIC function so that the RAN can be optimized. In contrary to Near-RT RIC, which sits in the RAN domain and works on a timescale of tens to hundreds of milliseconds, Non-RT RIC works within the management plane (and more particularly in Service Management and Orchestration, SMO) and operates on a timescale of seconds and minutes [[4](https://rimedolabs.com/blog/o-ran-non-rt-ric-architecture-and-rapps/)].

The functionality of the Non-RT RIC includes configuration management, device management, fault management, performance management, and lifecycle management for all network (NW) elements within O-RAN architecture. It is similar to Element Management System (EMS) and Analytics and Reporting functionalities in the traditional NWs. All RAN elements are self-configured by the Non-RT RIC, reducing the need for manual intervention. By providing timely insights into NW operations, Mobile Network Operators (MNOs) may use Non-RT RIC to better understand and optimize NW by applying pre-determined service and policy parameters. Its functionality is internal to the SMO in the O-RAN architecture and provides an A1 interface to the Near-RT RIC. 

Non-RT RIC can use data analytics and Artificial Intelligence (AI)/Machine Learning (ML) training/inference to determine the RAN optimization actions for which it can leverage SMO services such as data collection and provisioning services of the O-RAN nodes. Trained models produced in the Non-RT RIC are distributed to the Near-RT RIC for runtime execution. Network slicing, security, role-based access control, and RAN sharing are example aspects that are enabled by the combined controller functions namely, Near-RT and non-RT. Standardized in [O-RAN.WG2.Non-RT-RIC-ARCH-TR-v01.00](https://specifications.o-ran.org/specifications).

**Architecure Non-NT RIC**

![image-2-1024x608](https://hackmd.io/_uploads/B13b8u98C.png)

Figure above shows the internals of the SMO framework including the Non-RT RIC. Functionality inherent to the Non-RT RIC itself is colored in blue. Those functions are used basically for managing the rApps which are external to the Non-RT RIC framework accessible through an open Application Programming Interface (API), using R1 interface. Also, another set of "*blue elements*” include those that create the data to be transmitted over the A1 interface, namely: A1 policy functions, A1 enrichment information functions, A1 ML functions.

There are also parts in the SMO framework that are out of Non-RT RIC scope, marked with a *"pink-ish”* color. They are basically related to the O1/O2 termination as well as other SMO framework functions, e.g. for network slicing lifecycle management. Those are inherent to the SMO framework.

Finally, the green part refers to the functionality which implementation is flexible. Those functions could be part of Non-RT RIC and they could be also external to Non-RT RIC and sit in the SMO. They are not inherent to any of those. The example here is AI/ML workflow functions. In such light, AI/ML could be either part of Non-RT RIC, or it could be external, providing the information to the SMO service exposure functions.
### rApp Examples

rApps are applications designed to run on Non-RT RIC providing additional value-added services to help creation of policies that the Non-RT RIC framework delivers down to Near-RT RIC through the A1 interface. Fig. 2, shows Non-RT RIC with three example rApps, namely rApp R, rApp U, and rApp Q connected via R1 interface to the Non-RT RIC framework. Their inputs and outputs are as follows:

![image-3](https://hackmd.io/_uploads/SyFz8_cIR.png)

1. **rApp R**

    rApp R is an rApp which consumes the O1 measurements. It takes the information from the O1 interface for RF signal experienced by a UE on serving and neighboring cells, and UE location. Based on this input, it estimates/predicts the future UE location and RF signal level when the UE moves towards a certain direction. For example, based on the past information of UEs at a given location with particular values for received signal levels from serving and neighbor base stations, and on the current measurements, it predicts the most likely UE signal levels after it moves towards predicted location.

    **rApp R (RF signal predictor):**

    * Consumes: O1 measurements of RF signal experienced by UE for serving/neighbor cells, measurements for UE location;
    * Outputs: future time prediction of the location of UE, prediction of RF signal at that location for serving/neighbor.

2. **rApp U**

    rApp U is a cell utilization predictor, which consumes the cell load utilization and amount of resources of a cell over time and outputs a future prediction of the cell load utilization, based on the trend. Doing so, it could deduct, e.g., that at the beginning of the day there is a lot of traffic in particular area, and then the traffic volume drops because all the people are moving to work so the traffic moves to the city center and thus predict the future cell load utilization.
    
    **rApp U (Cell utilization predictor):**

    * Consumes: cell utilization measurements regarding actual capacity utilization for a cell site over time;
    * Outputs: future time prediction of the cell site utilization based on the trend.

3. **rApp Q**

    rApp Q takes outputs from rApp R and rApp U, i.e. the predicted locations, signal levels, and cell utilization at a particular area and time, as well as the actual measurements and the actual cell utilization. Based on those it calculates the potential quality of experience (QoE). So, e.g., it could predict the future QoE if the user stays at a particular location or in different future location, for a scenario, where UE stays at the same cell or is handed over to another one.
    
    **rApp Q (UE QoE predictor):**

    * Consumes: measurements of UE RF signal (actual RAN measurement or prediction), measurement of cell site capacity utilization (actual or prediction)
    * Calculates: QoE experienced by particular UE, e.g.:
        * Estimates actual QoE based on actual RF signal and actual cell utilization.
        * Estimates QoE if in a neighbor cell based on actual RF signal relative to neighbor cell and actual neighbor cell utilization.
        * Estimates future QoE if connected to serving/neighbor cell-based predicted signal and predicted cell utilization.
