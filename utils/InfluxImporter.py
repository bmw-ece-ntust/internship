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
    def __init__(self, url, org):
        self.url = url
        self.org = org
        


    def import_csv(self,csvfile="default.csv",bucket="target_bucket"):
        token = os.environ.get("INFLUXDB_TOKEN")
        client = influxdb_client.InfluxDBClient(url=self.url, token=token, org=self.org)

        #Initiate influx client
        write_api = client.write_api(write_options=SYNCHRONOUS)
        # Open your csv file
        with open(csvfile, 'r') as f:
            j = 0
            reader = csv.reader(f)
            headers = next(reader)  # Get the headers of the file
            for row in reader:
                #for debugging purpose
                j += 1
                #fields = {headers[i]: row[i] for i in range (len(row))}
                point = Point("measure2") \
                    .tag("tag_test", "tag_1")
                for i in range(len(row)):
                    point.field(headers[i],row[i])
                write_api.write(bucket=bucket, org=self.org, record=point)
                #for debugging purpose
                print("sent data:" + str(j))
                #time.sleep(1) # separate points by 1 second        
            client.close()
        return 0


