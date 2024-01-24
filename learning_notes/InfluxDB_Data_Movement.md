>Michael Harditya (TEEP)
# Learning Notes
### Goals
- Move .csv data into InfluxDB
### Run the Docker
1. Move the active directory to the database directory that is used to save the data.
2. Run ```docker run -p 8086:8086 -v $PWD:/var/lib/influxdb influxdb```
3. Open browser and browse ```localhost:8086``` to make sure the InfluxDB is up and running, InfluxDB UI is expected to shown.
![image](../images/InfluxDBUI.png)
### Import CSV using Python
1. Install InfluxDB python client using ```pip install influxdb```
2. Run [```InfluxImporter.py```](../codes/InfluxImporter.py) by defining the host name, port, database name, and csv file name.
