>Michael Harditya (TEEP)
# Learning Notes
### Goals
- Move .csv data into InfluxDB
### Run the Docker
1. Move the active directory to the database directory that is used to save the data.
2. Run ```docker run -p 8086:8086 -v $PWD:/var/lib/influxdb influxdb```
3. Open browser and browse ```localhost:8086``` to make sure the InfluxDB is up and running, InfluxDB UI is expected to shown.
![image](../images/InfluxDBUI.png)
### Writing Data using Python
Importing CSV to InfluxDB using Python can be done by installing InfluxDB python client using ```pip install influxdb-client```
First define the libraries used to send the data.
```python
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
```
The influxdb_client needs several arguments, they are url, token, and organization name.
```python
client = influxdb_client.InfluxDBClient(url="https://influxdomain:port", token="influxtoken", org="targetorganization")
```
After the client has been initialized, initiate the client write API with the options.
```python
    write_api = client.write_api(write_options=SYNCHRONOUS)
```
Then prepare the data points to be send into influxDB by using ```influxdb_client.Point```.
```python
point = Point("measurename") \
            .tag("tagname", "tagvalue") \
            .field("fieldname", "fieldvalue")
```
Send the data point by calling ```writer_api.write()```.
```python
write_api.write(bucket=buc"targetbucket", org="targetorganization", record=point)
```
>for more information, [```InfluxImporter.py```](../codes/InfluxImporter.py) in ```utils``` shows example of how to send a csv data to InfluxDB using the ```influxdb-client``` library.
