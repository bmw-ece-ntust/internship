# Building Dashboards in Grafana

## Table of Contents
- [Building Dashboards in Grafana](#building-dashboards-in-grafana)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [AP Dashboard](#ap-dashboard)
      - [Task 1: Table of All Data](#task-1-table-of-all-data)
      - [Task 2: Specific AP Table](#task-2-specific-ap-table)
      - [Task 3: Client Numbers in Specific AP](#task-3-client-numbers-in-specific-ap)
      - [Task 4: Noise Floor in Specific AP](#task-4-noise-floor-in-specific-ap)
      - [Task 5: Channel Utilization for 2.4GHz & 5GHz Bands](#task-5-channel-utilization-for-24ghz--5ghz-bands)
  - [Client Dashboard](#client-dashboard)
      - [Task 1: Table of All Data](#task-1-table-of-all-data-2)
      - [Task 2: Specific Client Table](#task-2-specific-client-table)
      - [Task 3: Channel for Specific Client](#task-3-channel-for-specific-client)
      - [Task 4: SNR for Specific Client](#task-4-snr-for-specific-client)
      - [Task 5: Add Total Data, Rx, and Tx Line Chart](#task-5-add-total-data-rx-and-tx-line-chart)
  - [Related Documentation](#related-documentation)

## Introduction

This progress report documents the development of two dashboards, AP Dashboard and Client Dashboard, within Grafana utilizing InfluxDB as the data source.  The dashboards are designed to monitor Access Points (APs) and Clients within a wireless network. The report outlines the goals of each dashboard and provides detailed explanations of the queries used to achieve these goals.

**Goal**
- Streamline network management and optimization through comprehensive data organization and analysis for APs and client devices.
- Enable detailed analysis and targeted troubleshooting by focusing on specific APs and clients, improving network performance.
- Enhance user experience by leveraging detailed metrics and visualizations to ensure optimal network operation.

**Main Reference：**

* [InfluxData Documentation](https://docs.influxdata.com/)
* [Grafana Labs Community Forums](https://community.grafana.com/)

## AP Dashboard

<details>
<summary><b> Milestone </b></summary>

## Goal
- Organize and analyze data on wireless access points (APs) through comprehensive tables capturing essential metrics like client numbers, channel utilization, and noise figure (NF).
- Focus on specific APs by creating detailed tables to manage and understand individual unit performances within the network.
- Visualize and present key performance metrics such as client numbers, NF, and channel utilization for specific APs across different frequency bands to enhance network optimization insights.

## Task
- [x] Create a Table including ap_name, radio band, client numbers, channel, EIRP, NF, Channel Quality, Channel Utilization, Channel Busy.
- [x] Create a Table for the specific AP
- [x] Show the client numbers in the specific AP
- [x] Show the NF in the specific AP
- [x] Show the Channel Utilization of 2.4GHZ & 5G in the specific AP  

## Task 1: Table of All Data
    
![image](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-4-Alifya/Assets/dashboard/apdas1.jpg)
    
* **Objective**
To create a comprehensive table displaying various parameters of APs across different buildings and floors.
* **Query**
```
from(bucket: "wifi")  
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r["_measurement"] == "AP")
  |> filter(fn: (r) => r["ap_group_floor"] =~ /^${floor:regex}$/ and r["ap_group_building"] =~ /^${building:regex}$/)
 |> filter(fn: (r) => r["_field"] == "channel_busy" or 
                        r["_field"] == "eirp_10x" or
                        r["_field"] == "radio_mode" or
                        r["_field"] == "sta_count" or
                        r["_field"] == "noise_floor" or
                        r["_field"] == "arm_ch_qual" or
                        r["_field"] == "rx_time" or
                        r["_field"] == "tx_time" or
                        r["_field"] == "channel_interference" or
                        r["_field"] == "channel_free")
 |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
 |> keep(columns: ["ap_name", 
                     "radio_band",
                     "radio_mode", 
                     "sta_count", 
                     "channel", 
                     "eirp_10x", 
                     "noise_floor", 
                     "arm_ch_qual",
                     "channel_busy",
                     "rx_time",
                     "tx_time",
                     "channel_interference",
                     "channel_free"])  
 |> drop(columns: ["rx_time", "tx_time", "channel_interference", "channel_free"])
 |> group()
```
* **Explanation**
Variables ap_group_building and ap_group_floor were created to filter data based on building and floor. The query uses these variables along with a series of filters to select relevant fields from the "AP" measurement. The data is then pivoted and grouped to display the required columns.

## Task 2: Specific AP Table

![image](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-4-Alifya/Assets/dashboard/apdas2.jpg)
    
* **Objective**
To create a table for a specific AP, showing detailed information.
* **Query**
```
from(bucket: "wifi")  
 |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
 |> filter(fn: (r) => r["_measurement"] == "AP")
 |> filter(fn: (r) => r["ap_group_floor"] =~ /^${floor:regex}$/ and r["ap_group_building"] =~ /^${building:regex}$/ and r["ap_name"] =~ /^${apName:regex}$/)
 |> filter(fn: (r) => r["_field"] == "channel_busy" or 
                        r["_field"] == "eirp_10x" or
                        r["_field"] == "radio_mode" or
                        r["_field"] == "sta_count" or
                        r["_field"] == "noise_floor" or
                        r["_field"] == "arm_ch_qual" or
                        r["_field"] == "rx_time" or
                        r["_field"] == "tx_time" or
                        r["_field"] == "channel_interference" or
                        r["_field"] == "channel_free")
 |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
 |> keep(columns: ["ap_name", 
                     "radio_band",
                     "radio_mode", 
                     "sta_count", 
                     "channel", 
                     "eirp_10x", 
                     "noise_floor", 
                     "arm_ch_qual",
                     "channel_busy",
                     "rx_time",
                     "tx_time",
                     "channel_interference",
                     "channel_free"])  
 |> drop(columns: ["rx_time", "tx_time", "channel_interference", "channel_free"])
 |> group()
```
* **Explanation**
A variable ap_name was created to filter data for a specific AP. The query follows a similar structure to Task 1 but includes an additional filter for ap_name. The resulting data is pivoted and grouped to display the required columns.

## Task 3: Client Numbers in Specific AP

![image](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-4-Alifya/Assets/dashboard/apdas3.jpg)
    
* **Objective**
To visualize the number of clients connected to a specific AP.
* **Query**
```
from(bucket: "wifi")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r["_measurement"] == "AP" and r["ap_name"] =~ /^${apName:regex}$/)
  |> filter(fn: (r) => r["_field"] == "sta_count")
  |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
  |> keep(columns: ["_time", "sta_count"])
```
* **Explanation**
A bar chart is created using a query that filters data for a specific AP (ap_name) and selects the sta_count field, representing the number of clients.

## Task 4: Noise Floor in Specific AP

![image](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-4-Alifya/Assets/dashboard/apdas4.jpg)
    
* **Objective**
To display the noise floor for a specific AP.
* **Query**
```
from(bucket: "wifi")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r["_measurement"] == "AP" and r["ap_name"] =~ /^${apName:regex}$/)
  |> filter(fn: (r) => r["_field"] == "noise_floor")
```
* **Explanation**
A query is used to filter data for a specific AP (ap_name) and select the noise_floor field, which is then visualized.

## Task 5: Channel Utilization for 2.4GHz & 5GHz Bands
    
![image](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-4-Alifya/Assets/dashboard/apdas5.jpg)

* **Objective**
To calculate and display the channel utilization for 2.4GHz and 5GHz bands in a specific AP.
* **Query**
```
from(bucket: "wifi")
 |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
 |> filter(fn: (r) => r["_measurement"] == "AP" and r["ap_name"] =~ /^${apName:regex}$/)
 |> filter(fn: (r) => r["radio_band"] == "(2.4 or  5.0")
 |> filter(fn: (r) =>   r["_field"] == "rx_time" or
                        r["_field"] == "tx_time" or
                        r["_field"] == "channel_interference" or
                        r["_field"] == "channel_free")
 |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
 |> keep(columns: ["ap_name", 
                     "rx_time",
                     "tx_time",
                     "channel_interference",
                     "channel_free"])  
 |> group()
```
* **Explanation**
A pie chart is created using a query that filters data for a specific AP (ap_name) and selects fields related to channel utilization (rx_time, tx_time, channel_interference, channel_free). The query calculates the total utilization for each band and displays it in the chart.

</details>

## Client Dashboard

<details>
<summary><b> Milestone </b></summary>

## Goal
- Develop a detailed table for comprehensive tracking of client devices on a WLAN, including extensive performance metrics and connection details.
- Implement a dedicated table for monitoring specific client performance, enabling targeted analysis and optimization.
- Integrate a line chart to visually represent network traffic data, enhancing real-time monitoring and identification of data flow patterns.

## Task
- [x] Create a Table including User Name, IP Address, MAC Address, Client Health, SNR (dB), Speed, Goodput, Throughput, Usage, Time, WLAN, AP Name, Radio Band (GHz), Channel, Role.
- [x] Create a Table for the specific client
- [x] Show channel for the specific client
- [x] Show SNR for the specific client
- [ ] Add a line chart below the existing charts, displaying three lines: total_data (total_data_bytes), rx (rx_data_bytes), and tx (tx_data_bytes). 

## Task 1: Table of All Data

![image](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-4-Alifya/Assets/dashboard/clientdas1.jpg)
    
* **Objective**
To create a comprehensive table displaying various parameters of clients.
* **Query**
```
from(bucket: "wifi")  
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r["_measurement"] == "Client")
  |> filter(fn: (r) => r["_field"] == "client_health" or 
                        r["_field"] == "snr" or
                        r["_field"] == "speed" or
                        r["_field"] == "total_data_throughput" or
                        r["_field"] == "_time" or
                        r["_field"] == "ssid" or
                        r["_field"] == "channel" or
                        r["_field"] == "radio_band")
 |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
 |> keep(columns: ["client_user_name", 
                     "client_ip_address",
                     "sta_mac_address", 
                     "client_health", 
                     "snr", 
                     "speed", 
                     "total_data_throughput", 
                     "_time",
                     "ssid",
                     "ap_name",
                     "radio_band",
                     "channel",
                     "client_role_name"])
 |> group()
```
* **Explanation**
A query is used to filter data from the "Client" measurement and select relevant fields. The data is then pivoted and grouped to display the required columns.

## Task 2: Specific Client Table
    
![image](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-4-Alifya/Assets/dashboard/clientdas2.jpg)

* **Objective**
To create a table for a specific client, showing detailed information.
* **Query**
```
from(bucket: "wifi")  
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r["_measurement"] == "Client")
  |> filter(fn: (r) => r["client_user_name"] =~ /^${userName:regex}$/)
  |> filter(fn: (r) => r["_field"] == "client_health" or 
                        r["_field"] == "snr" or
                        r["_field"] == "speed" or
                        r["_field"] == "total_data_throughput" or
                        r["_field"] == "_time" or
                        r["_field"] == "ssid" or
                        r["_field"] == "channel" or
                        r["_field"] == "radio_band")
 |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
 |> keep(columns: ["client_user_name", 
                     "client_ip_address",
                     "sta_mac_address", 
                     "client_health", 
                     "snr", 
                     "speed", 
                     "total_data_throughput", 
                     "_time",
                     "ssid",
                     "ap_name",
                     "radio_band",
                     "channel",
                     "client_role_name"])
 |> group()
```
* **Explanation**
A variable userName was created to filter data for a specific client. The query follows a similar structure to Task 1 but includes an additional filter for userName. The resulting data is pivoted and grouped to display the required columns.

## Task 3: Channel for Specific Client

![image](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-4-Alifya/Assets/dashboard/clientdas3.jpg)

* **Objective**
To visualize the channel used by a specific client, represented using bar chart.
* **Query**
```
from(bucket: "wifi")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r["_measurement"] == "Client" and r["client_user_name"] =~ /^${userName:regex}$/)
  |> filter(fn: (r) => r["_field"] == "channel")
  |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
  |> keep(columns: ["_time", "channel"])
```
* **Explanation**
A bar chart is created using a query that filters data for a specific client (userName) and selects the channel field.

## Task 4: SNR for Specific Client
    
![image](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-4-Alifya/Assets/dashboard/clientdas4.jpg)

* **Objective**
To display the Signal-to-Noise Ratio (SNR) for a specific client, represented using line chart (time series).
* **Query**
```
from(bucket: "wifi")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r["_measurement"] == "Client" and r["client_user_name"] =~ /^${userName:regex}$/)
  |> filter(fn: (r) => r["_field"] == "snr")
  |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
  |> keep(columns: ["_time", "snr"])
```
* **Explanation**
A line chart is created using a query that filters data for a specific client (userName) and selects the snr field.
    
## Task 5: Add Total Data, Rx, and Tx Line Chart

* **Objective**
on progress
* **Query**
```
on progress
```
* **Explanation**
on progress


</details>

### Related documentation:
- [Variable Panel Plugin](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-4-Alifya/Grafana/Dashboard_Development/variable_panel_plugin.md#using-the-variable-panel-plugin)
- [Grafana Syntax Explanation](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-4-Alifya/Grafana/Dashboard_Development/grafana-syntax-explanation.md#step-1-add-a-panel)
