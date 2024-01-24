import os
import argparse
from utils.InfluxImporter import InfluxDBCSVImporter

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, required=True, help='The host of the InfluxDB server.')
    parser.add_argument('--port', type=int, required=True, help='The port of the InfluxDB server.')
    parser.add_argument('--dbname', type=str, required=True, help='The name of the database to write to.')
    parser.add_argument('--csv', type=str, required=True, help='The path to the CSV file.')
    args = parser.parse_args()
    
    csv_import = InfluxDBCSVImporter(host=args.host,port=args.port,dbname=args.dbname)
    csv_import.import_csv(args.csv)

