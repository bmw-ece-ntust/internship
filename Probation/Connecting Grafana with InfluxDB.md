# Grafana and InfluxDB Integration


:::info
**Goal：**

* Establish a connection between Grafana and InfluxDB in Ubuntu 22.04.
* Configure Grafana to visualize and analyze data stored in InfluxDB.

**Main Reference：**

* [Linking Grafana to InfluxDB V2.0](https://www.youtube.com/watch?v=Jszd7zrl-_U)
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

![image](https://github.com/NTUST-BMW-Lab/internship/assets/87703952/ee6b2c47-7f84-479e-9806-37cfc567adca)

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
       ![image](https://github.com/NTUST-BMW-Lab/internship/assets/87703952/52f5f28d-4e20-4b9b-ad5b-0fd65148f6ac)
        - Enter username and password for InfluxDB and the bucket details
       ![image](https://github.com/NTUST-BMW-Lab/internship/assets/87703952/c3a3385c-eb70-40ca-8d81-7505925cfd02)
        - Set HTTP URL with http://localhost:8086
       ![image](https://github.com/NTUST-BMW-Lab/internship/assets/87703952/195aca0a-a55f-4761-8304-998bdeb06b3d)
        - Click "Save & Test" to verify the connection.
    5. Create a Dashboard and Visualize Data
        - In the Grafana UI, go to the "+" menu on the left sidebar and select "Dashboard."
       ![image](https://github.com/NTUST-BMW-Lab/internship/assets/87703952/3add2440-4dc9-4f11-bf7f-fde8fb3479b1)
        - Click on "Add new panel."
       ![image](https://github.com/NTUST-BMW-Lab/internship/assets/87703952/9206d39c-8670-4b6f-a1a3-7a98011e17fd)
        - In the "Query" section, select your InfluxDB data source and enter your Flux or InfluxQL query to retrieve data.
        - Customize the visualization as needed and click "Apply."
