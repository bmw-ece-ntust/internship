import csv
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

class InfluxDBCSVImporter:
    """ Move csv data into InfluxDB database sequentially.

    Args:
        url (str): InfluxDB hostname, or ip address with the port
        org (str): InfluxDB organization name to save the imported data
    
    Methods:
        import_csv(csvfile,bucket): Import CSV file with the filename defined by the csvfile argument into InfluxDB bucket

    """
    def __init__(self, url, org, bucket):
        self.bucket = bucket
        token = os.environ.get("INFLUXDB_TOKEN")
        self.client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
    
    def initiate_client(self):
        #Initiate influx client
        write_api = self.client.write_api(write_options=SYNCHRONOUS)
        return write_api


    def write_csv_data_to_influxdb(self, write_api, data):
        for entry in data:
            _client_point = Point("Client")\
                            .tag("essid", entry["essid"])\
                            .tag("eirp", entry["EIRP"])\
                            .tag("band", entry["band"])\
                            .tag("channel", entry["chan"])\
                            .tag("ht_type", entry["ht_type"])\
                            .tag("ap_name", entry["AP_Name"])\
                            .field("rssi", entry["rssi"])
            write_api.write(bucket=self.bucket, record=[_client_point])
        print("[INFO] Successfully write ", len(data),"data into database")
        
        return 0

    def close_influxdb_api(self,write_api):
        self.client.close()
        write_api.close()
        

