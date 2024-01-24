# **InfluxDB v2 Installation**

**Goal：**

* Learn how to use the InfluxDB API (write and query)
* Write data to InfluxDB using python library
* Query data from InfluxDB using python library

**Main Reference：**

* [User Guide of InfluxDB v2 - BMW Lab NTUST](https://hackmd.io/@Min-xiang/rkEyzDdkT#User-Guide-of-InfluxDB-v2)
* [InfluxDB installation on windows - BRR Knowledge Center](https://www.youtube.com/watch?v=mgxa-g2Wc-Q)

## **Table of Contents**
- [**InfluxDB v2 Installation**](#influxdb-v2-installation)
  - [**Table of Contents**](#table-of-contents)
  - [**Overview**](#overview)
  - [**Data Model & Format**](#data-model--format)
    - [**Tagset Data Model**](#1-tagset-data-model)
    - [**InfluxDB Line Protocol**](#2-influxdb-line-protocol)
  - [**InfluxDB Query Languages**](#influxdb-query-languages)
    - [**Flux**](#flux)
    - [**InfluxQL**](#influxql)
  - [**Installation (Ubuntu 22.04)**](#installation-ubuntu-2204)


## **Overview**

InfluxDB is an open-source time series database developed by InfluxData, tailored for applications like operations monitoring, IoT sensor data, and real-time analytics.

**Key Features:**
* **Organizations**: Logical grouping of users, buckets, and resources.
* **Bucket**: Physical storage for time series data with configurable retention periods.
* **Measurement**: Logical grouping of time series data, organized by type.


## **Data Model & Format**

### 1. **Tagset Data Model**
* **Tags**: Key-value pairs for metadata, providing dimensions for your data.
* **Fieldset**: Numeric, boolean, or string data that you want to analyze.

Example:
```
weather,location=us-midwest,season=summer temperature=80,humidity=65 1465839830100400200
```
In this example:
* **Measurement**: "weather"
* **Tags**: "location=us-midwest" and "season=summer"
* **Fields**: "temperature=80" and "humidity=65"
* **Timestamp**: "1465839830100400200"

### 2. **InfluxDB Line Protocol**
Each line represents a data point with measurement, tags, fields, and timestamps.

Example:
```
cpu,host=serverA,region=us-west value=0.64 1623715550000000000
```
In this example:
* **Measurement**: "cpu"
* **Tags**: "host=serverA" and "region=us-west"
* **Fields**: "value=0.64"
* **Timestamp**: "1623715550000000000"

## **InfluxDB Query Languages**

### **Flux**
Script, query, and analyze time series data seamlessly with Flux. A pipeline model for data manipulation.

### **InfluxQL**
The SQL-like language for those familiar with relational databases. Select, filter, and aggregate with ease.


## **Installation (Ubuntu 22.04)**

1. Visit the [InfluxDB website](https://www.influxdata.com/downloads/) to get the queries for the installation
2. Choose InfluxDB Version and Platform. Here, you will get the queries for the installation through poweshell.
3. Open PowerShell and execute the following commands (the queries you got):
```
# Download InfluxDB
wget https://dl.influxdata.com/influxdb/releases/influxdb2-2.7.5-windows.zip -UseBasicParsing -OutFile influxdb2-2.7.5-windows.zip
```

```
# Extract the downloaded archive
Expand-Archive .\influxdb2-2.7.5-windows.zip -DestinationPath 'D:\influxdb\'
```
Note: You can change the destination path, I use 'D:\influxdb\'

4. Navigate to Installation Directory
```
cd 'D:\influxdb\'
```
5. Start InfluxDB
```
.\influxd.exe
```

6. Set Up InfluxDB through the UI
    1. With InfluxDB running, go to http://localhost:8086.
    2. Enter your username and password if you already have account.
    4. Click "Sign In"

Your InfluxDB instance is now initialized.