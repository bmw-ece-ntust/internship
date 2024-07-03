# Integrating OSM and Mitsuba with Blender

## Table of Contents
- [Integrating OSM and Mitsuba with Blender](#integrating-osm-and-mitsuba-with-blender))
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Goals](#goals)
  - [Main References](#main-references)
  - [Prerequisites](#prerequisites)
  - [Downloading and Installing Blender-OSM](#downloading-and-installing-blender-osm)
  - [Downloading and Installing Mitsuba-Blender](#downloading-and-installing-mitsuba-blender)
  - [Using Blender-OSM in Blender](#using-blender-osm-in-blender)
  - [Using Mitsuba with Blender](#using-mitsuba-blender-in-blender)
  - [Conclusion](#conclusion)

## Introduction
This documentation guides you through the process of applying the Blender-OSM and Mitsuba-Blender plugins in Blender. These plugins enhance Blender's capabilities by allowing for the importation of OpenStreetMap (OSM) data and the use of the Mitsuba renderer, respectively.

Blender OSM is a plugin used to import real-world geometries into Blender. It allows the user to download geometries of cities or any real-world environment from OpenStreetMap into Blender, which is essential for creating accurate and detailed scenes for wireless propagation simulation.

The Mitsuba plugin is utilized for exporting the scene created in Blender as a Mitsuba scene, which is the file format supported by Shona RT. This step is crucial for transferring the scene from Blender to Shona RT, where it can be used for computing coverage maps and propagation paths between transmitters and receivers.

## Goals

- To guide users on integrating the Blender-OSM and Mitsuba-Blender plugins with Blender for enhanced 3D modeling and rendering capabilities.

## Main References

- [YouTube Tutorial on Sionna NVIDIA Integration](https://www.youtube.com/watch?v=7xHLDxUaQ7c)
- [Mitsuba-Blender GitHub Repository](https://github.com/mitsuba-renderer/mitsuba-blender)
- [Blender-OSM Product Page](https://prochitecture.gumroad.com/l/blender-osm)

## Prerequisites
- Blender installed on your system.
- Basic knowledge of navigating and operating Blender.

## Downloading and Installing Blender-OSM

1. **Purchase and Download Blender-OSM**: Visit the [Blender-OSM Product Page](https://prochitecture.gumroad.com/l/blender-osm) to purchase and download the plugin.

2. **Install Blender-OSM in Blender**:
   - Open Blender and go to ```Edit``` > ```Preferences```.
   - In the Preferences window, navigate to the ```Add-ons``` section.
   - Click ```Install``` and navigate to the downloaded Blender-OSM zip file.
   - Select the file and click ```Install Add-on```.
   - Enable the add-on by checking the box next to it.

## Downloading and Installing Mitsuba-Blender

1. **Download Mitsuba-Blender**: Go to the [Mitsuba-Blender GitHub Repository](https://github.com/mitsuba-renderer/mitsuba-blender) and download the latest version.
2. **Install Mitsuba-Blender in Blender**: Repeat the same steps as for installing Blender-OSM, but navigate to the downloaded Mitsuba-Blender zip file during the installation process.

## Using Blender-OSM in Blender

1. **Import OSM data**
   - In Blender, navigate to the `3D Viewport`.
   - On the right sidebar, you should see a new tab for the OSM addon. Click on it.
   - Click on the `OSM` button to open the import panel.
2. **Select the Area**
   - Click on `Select`.
   - A map window will appear. Navigate and zoom in to the area you want to import.
   - Draw a rectangle around the desired area by clicking and dragging.
3. **Copy Coordinates**
   - After selecting the area, the coordinates of the selection will be automatically copied. If not, there should be a `Copy` button. Click it to copy the coordinates.
4. **Paste Coordinates**
   - Go back to the import panel in Blender.
   - Paste the copied coordinates into the appropriate fields. There should be fields for latitude and longitude bounds.
5. **Import the Data**
   - Click the `Import` button.
   - Wait for the data to be imported. This might take some time depending on the size and complexity of the area you selected.
6. **Adjust the Imported Data**
   - After the import is complete, you can adjust the imported objects (buildings, roads, terrain, etc.) as needed using Blender’s modeling tools.


## Using Mitsuba-blender in Blender

1. **Exporting the Scene**
   - Sionna RT only supports the Mitsuba scene format.
   - The exported files include an XML file and a folder named meshes containing all the meshes that make up the scene.
2. **Setting up for Export**
   - Ensure the coordinate system is set to Y Forward and Z Up.
   - Make sure to export the IDs, as Sionna RT uses the names of materials to assign electromagnetic properties for simulation.

## Conclusion

By following these steps, you can successfully integrate and use the Blender-OSM and Mitsuba-Blender plugins within Blender. These plugins provide powerful tools for importing real-world data into Blender and rendering scenes with the Mitsuba renderer, enhancing your 3D modeling and rendering capabilities.