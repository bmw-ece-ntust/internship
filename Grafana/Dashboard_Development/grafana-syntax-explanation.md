# Grafana Syntax Explanation

## Table of Contents
- [Grafana Syntax Explanation](#grafana-syntax-explanation)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [General Structure of Queries](#general-structure-of-queries)
  - [Specific Components Explained](#specific-components-explained)
    - [Filtering](#filtering)
    - [Pivoting (Pivot)](#pivoting-pivot)
    - [Grouping (Group)](#grouping-group)
  - [Additional Notes](#additional-notes)
  - [Visualization Type](#visualization-type)
    - [Step 1: Add a Panel](#step-1-add-a-panel)
    - [Step 2: Configure Query](#step-2-configure-query)
    - [Step 3: Customize Visualization Settings](#step-3-customize-visualization-settings)
      - [Table Visualization](#table-visualization)
      - [Time Series Visualization](#time-series-visualization)
      - [Pie Chart Visualization](#pie-chart-visualization)
    - [Step 4: Save and Share](#step-4-save-and-share)
    - [Related documentation:](#related-documentation)

## Introduction

Grafana is a powerful open-source platform for monitoring and observability. It allows users to query, visualize, alert on, and explore their metrics no matter where they are stored. InfluxDB is a popular time-series database known for its high performance and ease of use. Combining Grafana with InfluxDB enables the creation of sophisticated, real-time dashboards that can provide valuable insights into your data.

This documentation report focuses on the process of creating dashboards in Grafana using InfluxDB as the data source. We will cover the syntax used for querying data in **flux language**, the construction of AP (Access Point) and client dashboards, and the implementation of variable panel plugins to enhance interactivity and usability.

**Goals**
- Provide a comprehensive guide for using query syntax in Grafana with InfluxDB as the data source.
- Detail the process of building AP and client dashboards using specific queries.

**Main References**
- [Grafana Documentation](https://grafana.com/docs/grafana/latest/)
- [InfluxDB Documentation](https://docs.influxdata.com/influxdb/latest/)

## General Structure of Queries

- **`from(bucket: "wifi")`**: This specifies the bucket from which the data will be fetched. A bucket in InfluxDB is a container for data points.
- **`range(start: v.timeRangeStart, stop: v.timeRangeStop)`**: This sets the time range for the query. It fetches data between the start and stop times defined by the variables **v.timeRangeStart** and **v.timeRangeStop**.
- **`filter(fn: (r) =>...)`**: Filters the data based on conditions. The function **(r)** represents a row of data, and the condition inside the parentheses determines which rows to include in the result set.
- **`pivot(...)`, `keep(...)`, and `drop(...)`**: These functions are used to reshape the data. **pivot** reshapes the data into a format suitable for visualization, **keep** retains certain columns, and **drop** removes specified columns.
-  **`group()`**: Groups the data by a specified key.

## Specific Components Explained

### Filtering

Filtering is crucial for narrowing down the dataset to the subset of interest. Your queries use the filter operation extensively to refine the data based on specific conditions. Here's a breakdown:

- **Condition Syntax**: The basic syntax for a filter condition is **`fn: (r) => <condition>`**, where **fn** stands for function, **r** represents a row of data, and **`<condition>`** is the expression that evaluates to true or false for each row. Conditions can involve comparisons, logical operators, and regular expressions.
- **Regular Expressions**: You've used regular expressions (e.g., **`r["ap_group_floor"] =~ /^${floor:regex}$/`**) to match patterns within string fields. Regular expressions allow for flexible matching of text, enabling dynamic filtering based on partial matches or complex patterns.
- **Logical Operators**: Logical operators like and and or are used to combine conditions. For example, **`r["_field"] == "channel_busy" or r["_field"] == "eirp_10x"`** selects rows where either channel_busy or eirp_10x is present.

### Pivoting (Pivot)

Pivoting transforms the dataset from a wide format to a long format, making it easier to analyze and visualize. Here's how it works:

- **Syntax**: **`pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")`** takes three arguments:
    - **rowKey**: Specifies the column(s) to use as keys for the new rows. In your case, it's **`"_time"`**, meaning each row will correspond to a specific timestamp.
    - **columnKey**: Defines the column(s) to use as keys for the new columns. Here, it's **`["_field"]`**, indicating that each unique field name will become a separate column in the output.
    - **valueColumn**: Determines the column to extract values from. For you, it's **`"_value"`**, which means the values associated with each time-field pair will populate the cells in the pivoted table.
- **Purpose**: Pivoting is particularly useful for preparing data for visualization tools that expect a specific layout, such as Grafana or Kibana.

### Grouping (Group)

Grouping aggregates data based on one or more columns. While your provided queries don't explicitly show a **group** operation, let's discuss its role:

- **Syntax**: **`group()`** groups the data by the default index, which is usually the time column if not otherwise specified.
- **Usage**: Grouping is essential for aggregating data over time intervals, calculating averages, sums, counts, etc. For instance, if you wanted to find the average **`sta_count`** per hour for a specific AP, you would group by the time column and apply an aggregation function like **`mean("sta_count")`**.

## Additional Notes

- **Selecting Columns**: The **keep** and **drop** operations are used to control which columns appear in the final dataset. **`keep(columns: [...])`** retains specified columns, while **`drop(columns: [...])`** removes them. This is useful for cleaning up the dataset before further analysis or visualization.
- **Time Ranges**: The range function specifies the time window for the query. It's crucial for ensuring that the data retrieved is relevant to the current context or analysis period.
- **Variable**: You can create variables directly in Grafana under Dashboard Settings > Variables, or use a Variable Panel plugin (you can check the documentation [here](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-4-Alifya/Grafana/Dashboard_Development/variable_panel_plugin.md#using-the-variable-panel-plugin) for added functionality. Variables act as placeholders, updating panel data based on selections made from dropdown menus.

## Visualization Type

Creating visualizations in Grafana involves several steps, from setting up your data source to configuring the visualization settings. Below is a general guide on how to create different types of visualizations in Grafana, including tables, line charts, pie charts, and others. Each visualization serves a unique purpose, and understanding their characteristics can help you choose the right one for your data.

### Step 1: Add a Panel
1. Navigate to your dashboard in Grafana.
2. Click on the "+" icon next to the title of your dashboard to add a new panel.
3. Choose the visualization type you wish to use from the list of available visualizations.

### Step 2: Configure Query
1. After adding a panel, you'll need to configure the query that retrieves the data you want to visualize. This involves selecting your data source and writing a query to fetch the desired data.
2. Ensure your query returns the correct data format expected by the chosen visualization. For example, time series data should be returned in a format compatible with time series visualizations.

### Step 3: Customize Visualization Settings
Each visualization type in Grafana has its own set of customization options. Here's a brief overview of how to adjust settings for different visualizations (I take 3 visualization i use most to build the dashboard):

#### Table Visualization
- **Table Options**: Adjust the appearance of your table, including sorting columns, applying filters, and changing cell types for richer data displays.
- **Column Width and Alignment**: Customize the width and alignment of columns to better fit your data presentation needs.

#### Time Series Visualization
- **Graph Styles**: Modify the appearance of your time series graph, including line width, fill opacity, and whether to connect null values.
- **Axis Options**: Customize the axes, including time zones, labels, and scale adjustments.

#### Pie Chart Visualization
- **Pie Chart Type**: Choose between standard pie charts and donut charts for your visualization.
- **Legend Options**: Control the visibility and placement of legends to enhance readability.

### Step 4: Save and Share
Once you're satisfied with your visualization, save your dashboard. You can share your dashboard with others by clicking on the "Share" option and entering the email addresses of those you wish to share with.

### Related documentation:
- [Building Dashboards in Grafana](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-4-Alifya/Grafana/Dashboard_Development/building_dashboard_in_grafana.md)
- [Variable Panel Plugin](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-4-Alifya/Grafana/Dashboard_Development/variable_panel_plugin.md#using-the-variable-panel-plugin)