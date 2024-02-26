import os
import argparse
from controller.APDataCollector import APDataCollector

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str, default="http://localhost:8086'", help='The host of the InfluxDB server.')
    parser.add_argument('--org', type=str, required=True, help='The name of the database to write to.')
    parser.add_argument('--csv', type=str, required=True, help='CSV filename')
    parser.add_argument('--bucket', type=str, required=True, help='influxDB bucket name')
    args = parser.parse_args()
    
    csv_import = APDataCollector()
    csv_import.read_data_csv(args.csv)
    if (csv_import.read_data_csv(args.csv) == 0):
        print("[INFO] CSV successfully retrieved! ")
    if (csv_import.write_to_influxdb(args.url,args.org,args.bucket) == 0):
        print("[INFO] Data successfully transferred! ")
    if (csv_import.close_client() == 0):
        print("[INFO] Client successfully closed")

