# Variable Panel Plugin

[![Demonstrates the Variable panel functionality](https://raw.githubusercontent.com/volkovlabs/volkovlabs-variable-panel/main/img/overview.png)](https://youtu.be/1ogv2jstrlI)

## Table of Contents
- [Variable Panel Plugin](#variable-panel-plugin)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Installing the Variable Panel Plugin](#installing-the-variable-panel-plugin)
  - [Using the Variable Panel Plugin](#using-the-variable-panel-plugin)
  - [Implementing Variables in Your Dashboard Development](#implementing-variables-in-your-dashboard-development)

## Introduction

The Variable Panel by Volkov Labs is a powerful plugin for Grafana that enhances the functionality of dashboards by allowing users to create, manage, and utilize variables within their Grafana environment. This plugin is designed to work seamlessly with Grafana 9.2 or 10, ensuring compatibility and optimal performance for users leveraging these versions of Grafana

**Goal**

* Document the process of creating dashboards in Grafana with InfluxDB, focusing on AP and Client dashboards, including variable implementation.
* Provide a concise guide on installing and using the Variable Panel by Volkov Labs in Grafana for enhanced dashboard customization.

**Main Reference：**

* [Variable Panel - Volkov Labs](https://docs.influxdata.com/)
* [Grafana Labs Community Forums](https://community.grafana.com/)
* [Variable Panel for Grafana | New features and updates | Easy tutorial
 (Video)](https://www.youtube.com/watch?v=1ogv2jstrlI)

## Installing the Variable Panel Plugin

### 1. Prerequisites
Ensure your Grafana version is 9.2 or 10, as the Variable Panel plugin requires these versions.

### 2. Installation Method
* **Via Grafana CLI**: Run `grafana-cli plugins install volkovlabs-variable-panel` in your terminal. This method is recommended for most instances.
* **Manual Installation**: Download the plugin from the Grafana Plugins page and manually place it in the Grafana plugins directory. This method is useful if your Grafana server does not have internet access.

### 3. Installation on Grafana Cloud
For Grafana Cloud users, the plugin installation process is handled automatically. After adding the plugin, log out and back in to use it.

## Using the Variable Panel Plugin

After installing the plugin, you can start creating and using variables in your Grafana dashboards.

### 1. Accessing Variables
Navigate to the dashboard where you want to add variables. Click on the "Variables" tab in the dashboard settings.

### 2. Creating Variables
* Click on "New" to create a new variable.
* Fill in the details for your variable, such as name, type (Text, Number, Date, etc.), and options if applicable.
* For InfluxDB variables, you can use the `schema.tagValues()` function to dynamically generate options based on your InfluxDB schema
This is the example query:
```
schema.tagValues(
    bucket: "(bucket name)",
    tag: "(field name)"
)
```

### 3. Display the Variable Panel
* On the dashboard, go into a new visualization
* Select the Variable panel from the dropdown, specify the title.
The core setting for the Variable panel is in the Layout section. There, specify which dashboard variable to display on the variable panel.
In the Header section, you can select either you want to display or hide the header.
* In the Variable section, display mode, you can select out of three options. 
    * The 'Table' is to show all options with check marks or radio buttons; it depends on the multivalue parameter from the settings. 
    * The 'Minimize' mode gives a minimalistic look. 
    * The 'Button' transforms every option into a button.
* If you have finish all of the steps, check on your dashboard and there will be a panel that displays the dashboard variable either in a dropdown, buttons, or check marks.

### 3. Using Variables in Queries
* Once your variable is created, you can use it in your dashboard panels by referencing it in your queries. For example, `${variableName}`.
* For InfluxDB, you might use it in a query like 
```
from(bucket: "wifi") 
|> filter(fn: (r) => r["ap_name"] =~ /^${apName:regex}$/)
```
to filter data based on the selected variable value.

### 4. Advanced Features:
* The Variable Panel plugin supports various enhancements, such as handling pressing enter and escape keys for Text Variable, adding variables with text and value in Table/Tree View, and more.
* Explore the plugin's documentation for detailed information on its features and enhancements.

## Implementing Variables in Your Dashboard Development

* **Dynamic Data Filtering**: Use variables to dynamically filter data in your dashboards based on user input. This enhances the interactivity and usability of your dashboards.
* **Customizing Dashboards**: Variables allow for customization of dashboards, enabling users to focus on specific data sets relevant to their needs.
* **Performance Optimization**: By using variables effectively, you can optimize the performance of your dashboards by reducing the amount of data processed and displayed.

By following these steps and utilizing the features of the Volkov Labs Variable Panel plugin, you can enhance your Grafana dashboards with dynamic and interactive elements, improving both the user experience and the efficiency of data analysis.

> Related documentation:
> - [Building Dashboards in Grafana](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-4-Alifya/Grafana/Dashboard_Development/building_dashboard_in_grafana.md)
> - [Grafana Syntax Explanation](https://) (Link not available yet, still on progress)



