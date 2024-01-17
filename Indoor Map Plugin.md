# Indoor Map Plugin


:::info
**Goal：**
* Successfully install Indoor Map Plugin on Grafana
* Understanding how Indoor Map Plugin works

**Main Reference：**

* [Indoor Map - Grafana Labs](https://grafana.com/grafana/plugins/tailosstg-map-panel/)

:::

## :rocket: Introduction

The Indoor Map plugin in Grafana is a visualization tool that allows you to display spatial data on an indoor map.
:::success
**Key Features:**
* **Visualization**: It visualizes an indoor map, which is a collection of layers of spatial data using the same frame of reference. This means you can overlay different types of data on the same map for comprehensive analysis.
* **Image Files**: The plugin can visualize image files for indoor maps. This means you can use custom images of your indoor spaces as the base for your data visualization.
* **Map Panel**: It extends the functionality of the Grafana Map Panel. The Map Panel is a versatile tool in Grafana that provides various ways to visualize geospatial data.
* **Multiple Layers**: It supports multiple layers for different queries. This means you can display data from different sources or different types of data on the same map.
:::


## :bulb: Indoor Map VS GeoMap
Here are the differences between two Grafana plugins, Indoor Map and Geomap.

|    **Indoor Map**   |          **GeoMap**         | 
|:-----------------:|:-------------------------:|
|   It is specifically designed to visualize indoor spaces  | It is designed to visualize geospatial data on a world map |
|   It uses image files for indoor maps                | It provides four mapping options that will be generated automatically from the data source: auto, coordinates (latitude and longitude), geohash, and look up                          |
|   It supports multiple layers. Each layer determines how you visualize geospatial data on top of the base map                |   It supports multiple layers. Each layer determines how you visualize geospatial data on top of the base map                        |
|   It supports GeoJSON shapes                |   It supports seven map layer types: Markers, Heatmap, GeoJSON, Night / Day, Route (Beta), Photos (Beta), and Network (Beta)                        |
|   It supports pop-up visualizations of data from a specific point and FontAwesome icons                |   It also supports two experimental (or alpha) layer types: Icon at last point (alpha) and Dynamic GeoJSON (alpha)               |

## :gear: Installation (Ubuntu 22.04)
1. Open terminal

2. Navigate to the /usr/share/grafana/bin/ directory in the terminal using the command below:
```
cd /usr/share/grafana/bin/
```
![image](https://hackmd.io/_uploads/HyJOL-fYT.png)

3. If you are already in the bin directory, you can use this command to install the plugins:
```
grafana-cli plugins install tailosstg-map-panel
```

![image](https://hackmd.io/_uploads/SkQLPbGYa.png)

Now, Indoor Map plugins has been installed successfully. You can check it your installed plugins.

![image](https://hackmd.io/_uploads/S1xJu-GY6.png)
