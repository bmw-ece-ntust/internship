# **Grafana Installation**

**Goal：**
* Successfully install Grafana
* Set up a monitoring environment.

**Main Reference：**

* [Grafana Debian Installation](https://grafana.com/docs/grafana/latest/setup-grafana/installation/debian/)


## **Table of Contents**
- [**Grafana Installation**](#grafana-installation)
  - [**Table of Contents**](#table-of-contents)
  - [**Overview**](#overview)
  - [**Installation (Ubuntu 22.04)**](#installation-ubuntu-2204)
  - [**Get Started**](#get-started)
    - [**Start Grafana Server**](#start-grafana-server)
    - [**Check the status of Grafana Server (active or inactive)**](#check-the-status-of-grafana-server-active-or-inactive)
    - [**Stop Grafana Server**](#stop-grafana-server)

## **Overview**

Grafana is a powerful open-source platform for monitoring and observability. It allows you to visualize and analyze metrics, logs, and traces from various sources in real-time, providing insights into your applications and infrastructure.

**Key Features:**
* **Flexible Dashboards**: Create customizable dashboards with a variety of panels.
* **Data Source Integration**: Connects seamlessly with various data sources like InfluxDB, Prometheus, and more.
* **Alerting**: Set up alerts based on your defined thresholds.
* **Plugins**: Extend functionality with a wide range of plugins.


## **Installation (Ubuntu 22.04)**

For the installation, I use terminal on Linux. So, to start the installation, open the terminal on the linux and follow some commands below.
1. Install Prerequisite Packages
```
sudo apt-get install -y apt-transport-https software-properties-common wget
```

2. Import GPG Key
```
sudo mkdir -p /etc/apt/keyrings/
wget -q -O - https://apt.grafana.com/gpg.key | gpg --dearmor | sudo tee /etc/apt/keyrings/grafana.gpg > /dev/null
```

3. Add Repository
For stable releases:
```
echo "deb [signed-by=/etc/apt/keyrings/grafana.gpg] https://apt.grafana.com stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
```

For beta releases:
```
echo "deb [signed-by=/etc/apt/keyrings/grafana.gpg] https://apt.grafana.com beta main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
```

4. Update package list
```
sudo apt-get update
```

5. Install Grafana OSS
```
sudo apt-get install grafana
```

6. Install Grafana Enterprise
```
sudo apt-get install grafana-enterprise
```


## **Get Started**

### **Start Grafana Server**
```
sudo systemctl start grafana-server
```

### **Check the status of Grafana Server (active or inactive)**
```
sudo systemctl status grafana-server
```

### **Stop Grafana Server**
```
sudo systemctl stop grafana-server
```
