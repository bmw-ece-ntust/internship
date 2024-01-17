# InfluxDB v2 Documentation Progress


:::info
**Goal：**

* Learn how to use the InfluxDB API (write and query)
* Write data to InfluxDB using python library
* Query data from InfluxDB using python library

**Main Reference：**

* [User Guide of InfluxDB v2 - BMW Lab NTUST](https://hackmd.io/@Min-xiang/rkEyzDdkT#User-Guide-of-InfluxDB-v2)
* [InfluxDB installation on windows - BRR Knowledge Center](https://www.youtube.com/watch?v=mgxa-g2Wc-Q)
:::

## :rocket: Introduction

InfluxDB is an open-source time series database developed by InfluxData, tailored for applications like operations monitoring, IoT sensor data, and real-time analytics.
:::success
**Key Features:**
* **Organizations**: Logical grouping of users, buckets, and resources.
* **Bucket**: Physical storage for time series data with configurable retention periods.
* **Measurement**: Logical grouping of time series data, organized by type.
:::

## 📊 Data Model & Format

### 1. Tagset Data Model
* **Tags**: Key-value pairs for metadata, providing dimensions for your data.
* **Fieldset**: Numeric, boolean, or string data that you want to analyze.

![image](https://hackmd.io/_uploads/SJPmS1YOp.png)

Example:
```
weather,location=us-midwest,season=summer temperature=80,humidity=65 1465839830100400200
```
In this example:
* **Measurement**: "weather"
* **Tags**: "location=us-midwest" and "season=summer"
* **Fields**: "temperature=80" and "humidity=65"
* **Timestamp**: "1465839830100400200"

### 2. InfluxDB Line Protocol
Each line represents a data point with measurement, tags, fields, and timestamps.

![image](https://hackmd.io/_uploads/HyfrLkF_6.png)

Example:
```
cpu,host=serverA,region=us-west value=0.64 1623715550000000000
```
In this example:
* **Measurement**: "cpu"
* **Tags**: "host=serverA" and "region=us-west"
* **Fields**: "value=0.64"
* **Timestamp**: "1623715550000000000"

## 📜 InfluxDB Query Languages

### Flux
Script, query, and analyze time series data seamlessly with Flux. A pipeline model for data manipulation.

### InfluxQL
The SQL-like language for those familiar with relational databases. Select, filter, and aggregate with ease.


## ⚙️ Installation

1. Visit the [InfluxDB website](https://www.influxdata.com/downloads/) to get the queries for the installation
2. Choose InfluxDB Version and Platform. Here, you will get the queries for the installation through poweshell.
3. Open PowerShell and execute the following commands (the queries you got):
```
# Download InfluxDB
wget https://dl.influxdata.com/influxdb/releases/influxdb2-2.7.5-windows.zip -UseBasicParsing -OutFile influxdb2-2.7.5-windows.zip
```
![image](https://hackmd.io/_uploads/rywS0yYOa.png)

![image](https://hackmd.io/_uploads/Hy2GC1tup.png)

```
# Extract the downloaded archive
Expand-Archive .\influxdb2-2.7.5-windows.zip -DestinationPath 'D:\influxdb\'
```
Note: You can change the destination path, I use 'D:\influxdb\'


![image](https://hackmd.io/_uploads/HJzFRyKOT.png)

4. Navigate to Installation Directory
```
cd 'D:\influxdb\'
```
5. Start InfluxDB
```
.\influxd.exe
```
![image](https://hackmd.io/_uploads/Hk7lkxFu6.png)

6. Set Up InfluxDB through the UI
    1. With InfluxDB running, go to http://localhost:8086.
    ![image](https://hackmd.io/_uploads/H1r2JxYua.png)
    2. Enter your username and password if you already have account.
    4. Click "Sign In"
    ![image](https://hackmd.io/_uploads/HkbYelYdT.png)

Your InfluxDB instance is now initialized.