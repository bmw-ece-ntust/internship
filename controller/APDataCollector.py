from utils.data_process import DataProcess
from utils.InfluxImporter import InfluxDBCSVImporter

class APDataCollector:
    def __init__(self):
        print("APDataCollector initialized!")

    def read_data_csv(self,filename):
        data = DataProcess(filename)
        data.preprocess()
        self.data = data.to_dict()
        return 0
    
    def write_to_influxdb(self,url,org,bucket):
        self.influx_importer = InfluxDBCSVImporter(url,org,bucket)
        self.writer_api = self.influx_importer.initiate_client()
        self.influx_importer.write_csv_data_to_influxdb(writer_api,self.data)
        return 0
    
    def close_client(self):
        self.influx_importer.close_influxdb_api(self.writer_api)
        return 0