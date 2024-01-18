>Michael Harditya (TEEP)
# Learning Notes
## 18/01/2024
### Goals

- Learn Aruba and the data generated from it
- Learn InfluxDB about moving data
- Learn OpenWiFi and Aruba connection

### Aruba
![image](https://hackmd.io/_uploads/r1IfSG8Ka.png)

Aruba is subsidiary of Hewlett Packard Enterprise company, also known as HPE Aruba Networking. They provide solutions from wired and wireless LAN, to WAN. The products include network switches, APs, hotspots, and wireless controllers.

#### CLI
Just like any other APs, Aruba APs provides command-line interface to do many things, including configurations. There are many commands at Aruba AP CLI, we can use this [AOS10 CLI Reference Guide](https://www.arubanetworks.com/techdocs/AOS_10.x_Books/AOS10_CLI_Guide.pdf) to find the right CLI we want to use. The guide also mention that the CLI can be accessed by SSH, or using WebUI.
#### Using API
Aruba provides the usage of API to access and control Aruba AP (and some other products), one of them is using Python REST API. Aruba also provides [Python REST API SDK](https://developer.arubanetworks.com/aruba-central/docs/python-using-api-sdk) that shows how to use the SDK, and the source code of the SDK itself.

This SDK is used by Aruba to be implemented into Aruba proprietary tool for unified network management, AI-based analytics and IoT device security for wired, wireless, and SD-WAN networks known as [Aruba Central](https://www.hpe.com/us/en/aruba-central.html).
![image](https://hackmd.io/_uploads/HJVe_GLFa.png)

Using the Aruba Central Webhooks, we can create a [Streaming API Python Client](https://developer.arubanetworks.com/aruba-central/docs/python-using-streaming-api-client). The client requires a WebSocket URL Endpoint, WebSocket Authorization Key, Subscription Topic, Aruba Central User Email, and Protobuf files. Then the client can be built using this workflow (for example to run CLI without having to use the UI or Aruba Central):

![image](https://hackmd.io/_uploads/HkNwKM8K6.png)

With CLI possible to be executed via code (or Python script to be exact), creating a Aruba Crawler that streams data from AP is possible. for more information, please read [CLI Config documentation](https://developer.arubanetworks.com/aruba-central/docs/command-line-access-point-configuration).

### InfluxDB
InfluxDB is a platform to collect, store, process, and visualize time-series data. Time series data is a sequence of data in timely manner (time indexed). InfluxDB have several products, on of it is InfluxDB OSS (open source) which includes UI and system. InfluxDB also has docker version to make it possible in a docker container (see [Learning Notes 08/01/2024](/-Zt9uC-qTVO_GyabKFkqjA)).
#### InfluxData
![image](https://hackmd.io/_uploads/rJYzd7Ita.png)
In InfluxDB, the data is arranged using the schema above, here is the explanation:
**1. Organization**
* A logical grouping of users, buckets, and other resources.
* isolates data and resources from other organizations.

**2. Bucket**
* A named location for the time series data is stored (a sort of filename), contains multiple measurements.
* Keep in mind that Bucket have Retention Policy, where old data is going to be deleted.

**3. Measurements**
* A logical grouping for the time series data, consists of timestamp, tags, and fields.
* All tags and fields must be the same for one measurement (different number of tags must be placed under different measurements).

**4. Timestamp**
* An index for each data entry, in the format of timestamp.

**5. Tags and Fields**
* Tags and Fields are key-value pairs with different usage.
* Tags do not change often, meant to store metadata of each point as identifiers.
* Fields change over time as the values of the data itself.

Other important definitions used in InfluxDB, and further notes are:
**1. Point**: single data record identified by its measurement, tag keys, tag values, field key, and timestamp.
**2. Series**: a group of points with the same measurements, tag keys, and tag values.

![image](https://hackmd.io/_uploads/ryhXTX8Kp.png)

#### Moving Data
For writing data to InfluxDB, we can use this [Guide](https://hackmd.io/@Min-xiang/rkEyzDdkT#51-Install-the-library).