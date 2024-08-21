from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import json
import subprocess
import time
from datetime import datetime, timedelta
import pandas as pd

myorg = "Ghazi"
mybucket = "PRB_Prediction"
mytoken = "ZAyM9Iq1hYNR4liKQq4Fi91e4osvhB1G"
myurl = "http://192.168.8.6:30001/"

# Koneksi ke InfluxDB
client = InfluxDBClient(url=myurl, token=mytoken, org=myorg)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Start time
start_time = datetime.strptime("2024-07-21T00:00:00.000Z", "%Y-%m-%dT%H:%M:%S.%fZ")

while True:
    # Read input file
    with open('./data1.json', 'r') as file:
        input_data = json.load(file)

    # Get predictions
    model_name = "qoe-model"
    response = json.loads(subprocess.check_output(['curl', '-s', '-H', f'Host: {model_name}.kserve-test.example.com', f'http://192.168.8.44:30650/v1/models/{model_name}:predict', '-d', json.dumps(input_data)]))
    # List to store predictions
    predictions_list = []

    # Extract predictions
    DRB_UEThpDl = response['predictions'][0][0]
    RRU_PrbUsedDl = response['predictions'][0][1]
    Viavi_QoS_Score = response['predictions'][0][2]
    Viavi_UE_TargetThroughput = response['predictions'][0][3]

    # Add predictions to the list
    predictions_list.append({'DRB_UEThpDl': DRB_UEThpDl, 'RRU_PrbUsedDl': RRU_PrbUsedDl, 
                             'Viavi_QoS_Score': Viavi_QoS_Score, 'Viavi_UE_TargetThroughput': Viavi_UE_TargetThroughput})

    # Add new predictions in a specific format to the end of the input file
    input_data['instances'][0].append([DRB_UEThpDl, RRU_PrbUsedDl, Viavi_QoS_Score, Viavi_UE_TargetThroughput])

    with open('./data1.json', 'w') as file:
        json.dump(input_data, file)

    # Add predictions to InfluxDB
    for i in range(0, len(predictions_list)):
        # Data (Point structure)
        _point = Point("beam_prediction")\
                .field("Predicted_RRU.PrbUsedDl", float(predictions_list[i]['RRU_PrbUsedDl']))\
                .time(start_time + timedelta(minutes=i))  # Use timestamps for every minute

        # Write the data to InfluxDB
        write_api.write(bucket=mybucket, record=[_point])

    print(f"Finish writing {len(predictions_list)} metrics with predictions to InfluxDB")

    # Update start time for the next upload with the correct time
    start_time += timedelta(minutes=len(predictions_list))

    # Pause for 1 second
    time.sleep(1)