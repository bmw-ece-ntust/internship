import os
import argparse
from utils.InfluxImporter import InfluxDBCSVImporter

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str, default="http://localhost:8086'", help='The host of the InfluxDB server.')
    parser.add_argument('--org', type=str, required=True, help='The name of the database to write to.')
    parser.add_argument('--csv', type=str, required=True, help='CSV filename')
    parser.add_argument('--bucket', type=str, required=True, help='influxDB bucket name')
    args = parser.parse_args()
    
    csv_import = InfluxDBCSVImporter(url=args.url,org=args.org)
    csv_import.import_csv()#csvfile=args.csv,bucket=args.bucket)

