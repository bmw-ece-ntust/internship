# Grafana and InfluxDB Integration


:::info
**Goal：**

* Establish a connection between Grafana and InfluxDB in Ubuntu 22.04.
* Configure Grafana to visualize and analyze data stored in InfluxDB.

**Main Reference：**

* [User Guide of InfluxDB v2 - BMW Lab NTUST](https://hackmd.io/@Min-xiang/rkEyzDdkT#User-Guide-of-InfluxDB-v2)
* [InfluxDB installation on windows - BRR Knowledge Center](https://www.youtube.com/watch?v=mgxa-g2Wc-Q)
:::

## :rocket: Introduction

Grafana is an open-source analytics and monitoring platform that integrates with various data sources to create informative dashboards. InfluxDB, on the other hand, is a powerful time series database designed for handling high volumes of timestamped data. Integrating Grafana with InfluxDB allows for efficient visualization and analysis of time series data.

:::success
**Key Points**
* **Grafana** - Visualization and analytics platform.
* **InfluxDB** - Time series database for storing and querying data.
:::

## ⚙️ Integration Steps (Ubuntu 22.04)

Before you start to integrate Grafana and InfluxDB, make sure you have already install both, Grafana and InfluxDB.

1. Open terminal
2. Start InfluxDB Service
```
sudo service influxdb start
```
3. Access InfluxDB UI
Open your web browser and navigate to http://localhost:8086. This will take you to the InfluxDB UI.

![image](https://hackmd.io/_uploads/HJIq7-rFa.png)

Enter your username and password if you have already set up an account. Click "Sign In" to access the InfluxDB UI.

4. Create a Database

Inside the InfluxDB UI, create a new database by clicking on the "Data" tab and selecting "Buckets." Create a bucket with a suitable name and retention policy.

5. Start Grafana Service
```
sudo service grafana-server start
```
6. Access Grafana UI

Open your web browser and navigate to http://localhost:3000. The default username is admin, and the default password is admin. Log in and change the password.

7. Add InfluxDB as a Data Source in Grafana
    1. In the Grafana UI, go to "Configuration" (gear icon on the left sidebar) and select "Data Sources."
    2. Click on "Add your first data source" or the "+" icon.
    3. Choose "InfluxDB" from the list.
    4. Configure the InfluxDB settings as below:
        - Set query language to Flux
    ![image](https://hackmd.io/_uploads/HJp36-BFp.png)
        - Enter username and password for InfluxDB and the bucket details
    ![image](https://hackmd.io/_uploads/rJvC6bSFp.png)
        - Set HTTP URL with http://localhost:8086
    ![image](https://hackmd.io/_uploads/BJTaT-BKa.png)
        - Click "Save & Test" to verify the connection.
    5. Create a Dashboard and Visualize Data
        - In the Grafana UI, go to the "+" menu on the left sidebar and select "Dashboard."
        ![image](https://hackmd.io/_uploads/H1MEJzBKT.png)
        - Click on "Add new panel."
        ![image](https://hackmd.io/_uploads/HJgGyMBtp.png)
        - In the "Query" section, select your InfluxDB data source and enter your Flux or InfluxQL query to retrieve data.
        - Customize the visualization as needed and click "Apply."