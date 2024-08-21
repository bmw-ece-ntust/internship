from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import csv
from datetime import datetime, timedelta

myorg = "Ghazi"
mybucket = "Prediction"
mytoken = "ZAyM9Iq1hYNR4liKQq4Fi91e4osvhB1G"
myurl="http://192.168.8.6:30001/"

UE_name = ['S1_N77_C1_beam1', 'S1_N77_C1_beam9']

for ue in UE_name:
    data =[]
    with open(f'/home/ubuntu/Ghazi/data1/{ue}_result.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        for row in reader:
                new_row = [float(item) for item in row]
                data.append(new_row)


    """
    Instantiate write api
    """

    # Instantiate the client
    client = InfluxDBClient(url=myurl,token=mytoken,org=myorg)

    # Instantiate a write client using the client object 
    write_api = client.write_api(write_options=SYNCHRONOUS)
    start_time = datetime.strptime("2024-07-21T00:00:00.000Z", "%Y-%m-%dT%H:%M:%S.%fZ")
    for i in range(0, len(data)):
        # Data (Point structure)
        _point = Point(f"{ue}")\
            .field("Actual_PrbUsedDl", data[i][0])\
            .field("Predicted_PrbUsedDl", data[i][1])\
            .time(start_time + timedelta(minutes=i))
        # Write the data to InfluxDB
        write_api.write(bucket=mybucket, record=[_point])
    print("Finish")
