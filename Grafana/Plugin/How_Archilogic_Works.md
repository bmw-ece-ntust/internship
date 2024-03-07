# **How it works: Archilogic Floor Panel Plugin**

**Goal：**
* Understand how to use Archilogic Floor Panel Plugin
* Understand how Archilogic Floor Panel Plugin works

**Main Reference：**

* [Archilogic Floor Panel Plugin - Grafana Labs](https://grafana.com/grafana/plugins/archilogic-floor-panel/?tab=relatedcontent)

## **Table of Contents**
- [**Archilogic Floor Panel Plugin**](#archilogic-floor-panel-plugin)
  - [**Table of Contents**](#table-of-contents)
  - [**Overview**](#overview)
  - [**Installation (Ubuntu 22.04)**](#installation-ubuntu-2204)
  - [**Configuration**](#configuration)

##  **Overview**

![floor-plan-screenshot-01](https://github.com/NTUST-BMW-Lab/internship/assets/87703952/3542e3c8-2798-49db-a712-ba3433293db9)

The Archilogic Floor Panel plugin for Grafana allows users to load floor plans stored in Archilogic within Grafana dashboards. It enables mapping information from data sources to elements in space and visualizing data on floor plans.

**Features:**
* **Customization**: Users can customize visualization styles.
* **Interactivity**: Interaction with the model using touch or mouse controls is supported.
* **Filtering**: Entities in the floor plan can be used to filter information in other Grafana components.

## **Installation (Ubuntu 22.04)**

* First, ensure you have Grafana 8.2.0 or later installed. For the installation guide, you can check it on my repo [Grafana Installation](https://github.com/bmw-ece-ntust/internship/blob/5b9c4fe137c28728f16ab9d320f8055b4bcdd226/Grafana/Grafana_Installation_Guide.md)
* Use the following command to install the Archilogic Floor Panel plugin via the grafana-cli tool:
```cmd
grafana-cli plugins install archilogic-floor-panel
```
For the detail, you can also check my repo [Grafana and InfluxDB Integration](https://github.com/bmw-ece-ntust/internship/blob/009e36c033918f9a3a6c1ebcef7ac21efb6e92fd/Grafana/Connecting_Grafana_With_InfluxDB.md)
* Next, log in to Grafana through your browser.
* Navigate to the plugin list, search for Archilogic Floor Panel, and enable the plugin.

## **Configuration**

**1. Prepare Your Floor Plan:**
  * First, ensure you have a digital version of your floor plan. It could be in formats like SVG, DXF, or PNG.
  * Make sure the floor plan is accurately scaled and represents the physical layout of your space.

**2. Upload Your Floor Plan to Archilogic:**
  * Visit the [Archilogic Floor Plan Engine website](https://www.archilogic.com/).
  * Sign in or create an account if you haven’t already.
    The problem here is that we have to contact the archilogic team to create an account and convert our plans into archilogic format by filling out the form [here] (https://www.archilogic.com/contact-us). I have contacted them to create an account but still no response.
  * Upload your floor plan using the provided tools. Archilogic will process it and create a 3D model.

**3. Retrieve Your Floor Plan ID:**
  * Once your floor plan is processed, you’ll receive a unique floor plan ID. This ID is essential for integrating your floor plan with Grafana.
  * You can find the floor plan ID in your Archilogic account dashboard or by querying the Archilogic API.

**4. Generate a Publishable Token:**
  * To access your floor plan without uploading it to the Archilogic server each time, you’ll need a publishable token.
  * Generate a token within your Archilogic account settings. This token acts as an authentication key for accessing your floor plan data.

**5. Configure the Archilogic Floor Panel Plugin in Grafana:**
  * Open your [Grafana dashboard](http://localhost:3000).
  * Add a new panel and select the Archilogic Floor Panel.  
  * In the panel settings, provide the following information:
    * Floor Plan ID: Use the ID you obtained from Archilogic.
    * Publishable Token: Enter the token you generated.
    For demo purposes you can use the default ones:
    * Floor plan ID: ```edd55163-b23b-48f3-a602-ea5a0e65809```
    * Publishable token: ```d5b83363-ddf0-4775-b6a3-0843dcd756ed```
  * Customize other settings like colors, labels, and interactions as needed.

**6. Define Data Sources:**
  * Grafana requires data sources to display information on the floor plan.
  * Set up a compatible data source (such as Prometheus, InfluxDB, or MySQL) that provides data related to your floor plan. This data should include node IDs and corresponding values (e.g., occupancy, temperature, humidity).
  * Ensure that the node IDs in your data source correspond to entities within your floor plan.
  * For further information, here's documentation about [data sources](https://grafana.com/docs/grafana/latest/datasources/)

**7. Visualize Your Floor Plan:**
  * Once configured, your floor plan will appear within the Grafana panel.
  * Customize the visualization by adding nodes, labels, and tooltips.
  * Interact with the floor plan: click on nodes, hover over areas, and filter data based on entities.

**8. Advanced Features:**
  * Explore additional features such as:
    * Heatmaps: Overlay data on the floor plan to visualize patterns.
    * Animations: Animate changes over time (e.g., room occupancy).
    * Custom Actions: Define actions when users interact with specific areas.

Remember that the Archilogic plugin leverages Archilogic’s Floor Plan Engine SDK, which provides powerful capabilities for visualizing data on your custom floor plans. By using the SDK, Grafana can overlay data points, heatmaps, and other visualizations directly onto your custom floor plan.

The [SDK documentation provides](https://developers.archilogic.com/floor-plan-engine/guide.html) detailed guidance on how to work with spatial data, create custom interactions, and optimize performance.
