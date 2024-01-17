# Grafana v2 Documentation Progress


:::info
**Goal：**
* Successfully install Grafana
* Set up a monitoring environment.

**Main Reference：**

* [Grafana Debian Installation](https://grafana.com/docs/grafana/latest/setup-grafana/installation/debian/)

:::

## :rocket: Introduction

Grafana is a powerful open-source platform for monitoring and observability. It allows you to visualize and analyze metrics, logs, and traces from various sources in real-time, providing insights into your applications and infrastructure.
:::success
**Key Features:**
* **Flexible Dashboards**: Create customizable dashboards with a variety of panels.
* **Data Source Integration**: Connects seamlessly with various data sources like InfluxDB, Prometheus, and more.
* **Alerting**: Set up alerts based on your defined thresholds.
* **Plugins**: Extend functionality with a wide range of plugins.
:::

## ⚙️ Installation (Ubuntu 22.04)

For the installation, I use terminal on Linux. So, to start the installation, open the terminal on the linux and follow some commands below.
1. Install Prerequisite Packages
```
sudo apt-get install -y apt-transport-https software-properties-common wget
```
![image](https://hackmd.io/_uploads/S1VdES2dT.png)

2. Import GPG Key
```
sudo mkdir -p /etc/apt/keyrings/
wget -q -O - https://apt.grafana.com/gpg.key | gpg --dearmor | sudo tee /etc/apt/keyrings/grafana.gpg > /dev/null
```
![image](https://hackmd.io/_uploads/rk2u4B3_p.png)

3. Add Repository
For stable releases:
```
echo "deb [signed-by=/etc/apt/keyrings/grafana.gpg] https://apt.grafana.com stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
```
![image](https://hackmd.io/_uploads/H1PKEHhda.png)

For beta releases:
```
echo "deb [signed-by=/etc/apt/keyrings/grafana.gpg] https://apt.grafana.com beta main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
```
![image](https://hackmd.io/_uploads/ryy5VHndp.png)

4. Update package list
```
sudo apt-get update
```
![image](https://hackmd.io/_uploads/ByD54Hhdp.png)

5. Install Grafana OSS
```
sudo apt-get install grafana
```
![image](https://hackmd.io/_uploads/rkCqNHhOa.png)

6. Install Grafana Enterprise
```
sudo apt-get install grafana-enterprise
```
![image](https://hackmd.io/_uploads/H1JCVShuT.png)
