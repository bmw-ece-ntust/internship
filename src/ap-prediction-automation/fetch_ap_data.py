"""
This module provides functionality to fetch data from an InfluxDB database and save it to a CSV file.

Modules:
    - requests: Library for making HTTP requests.
    - csv: Library for reading and writing CSV files.
    - argparse: Library for parsing command-line arguments.
    - os: Operating system interfaces for environment variable management.
    - dotenv: Load environment variables from a .env file.
    - tqdm: Library for creating progress bars in the console.
    - requests.exceptions: Exceptions for handling request errors.

Functions:
    - fetch_and_save_data(start_datetime, end_datetime, interval, bucket, measurement, fields, building=None, output_file="influxdb_data.csv")
"""

import requests
import csv
import argparse
import os
from dotenv import load_dotenv
from tqdm import tqdm
from requests.exceptions import RequestException

# Load environment variables from .env file
load_dotenv()

def fetch_and_save_data(start_datetime, end_datetime, interval, bucket, measurement, fields, building=None, output_file="influxdb_data.csv"):
    """
    Fetch data from InfluxDB based on specified parameters and save it to a CSV file.

    Parameters
    ----------
    start_datetime : str
        Start datetime in RFC3339 format (e.g., '2022-01-01T08:00:00Z').
    end_datetime : str
        End datetime in RFC3339 format (e.g., '2022-01-01T20:00:01Z').
    interval : int
        Time interval in seconds for aggregating data (default is 300 seconds).
    bucket : str
        The name of the InfluxDB bucket to query data from.
    measurement : str
        The measurement name to filter the data.
    fields : list of str
        The fields to query from the measurement.
    building : str, optional
        An optional building filter to further narrow down the query.
    output_file : str, optional
        The name of the output CSV file where the data will be saved (default is 'influxdb_data.csv').

    Returns
    -------
    None
        The function fetches the data and saves it to the specified output file.

    Raises
    ------
    ValueError
        If required environment variables for InfluxDB connection are missing.
    ConnectionError
        If there is an issue connecting to the InfluxDB server.
    RequestException
        For any request-related errors that may occur during the HTTP request to InfluxDB.

    Notes
    -----
    This function uses the InfluxDB Flux query language to filter and aggregate data
    based on the specified parameters. It also provides a progress bar for monitoring
    the download of data from the server.
    """
    influx_host = os.getenv('INFLUX_HOST')
    influx_org = os.getenv('INFLUX_ORG')
    influx_token = os.getenv('INFLUX_TOKEN')

    if not all([influx_host, influx_org, influx_token]):
        raise ValueError("Missing required environment variables. Please check your .env file.")

    url = f"{influx_host}/api/v2/query?org={influx_org}"
    
    headers = {
        "Authorization": f"Token {influx_token}",
        "Content-Type": "application/vnd.flux",
        "Accept": "application/csv"
    }
    
    fields_filter = ' or '.join([f'r._field == "{field}"' for field in fields])
    
    query = f'''
    from(bucket:"{bucket}")
      |> range(start: {start_datetime}, stop: {end_datetime})
      |> filter(fn: (r) => r._measurement == "{measurement}")
      |> filter(fn: (r) => {fields_filter})
    '''
    
    if building:
        query += f'  |> filter(fn: (r) => r.building == "{building}")\n'
    
    query += f'  |> aggregateWindow(every: {interval}s, fn: mean, createEmpty: false)'
    
    try:
        with requests.post(url, headers=headers, data=query, stream=True, timeout=(5, None)) as response:
            response.raise_for_status()  # Raise an exception for HTTP errors

            total_size = int(response.headers.get('content-length', 0))
            block_size = 8192  # 8 KB

            progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True, desc="Downloading and saving data")

            with open(output_file, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                header_written = False

                for chunk in response.iter_lines(chunk_size=block_size, decode_unicode=True):
                    if chunk:
                        # Split the chunk into rows
                        rows = chunk.split('\n')
                        for row in rows:
                            if row.strip():
                                # Split the row into fields
                                fields = row.split(',')
                                if not header_written:
                                    csv_writer.writerow(fields)
                                    header_written = True
                                else:
                                    csv_writer.writerow(fields)

                    progress_bar.update(len(chunk))

            progress_bar.close()
            print(f"Data saved successfully to {output_file}")

    except RequestException as e:
        error_message = f"Error connecting to InfluxDB: {str(e)}"
        if "ConnectTimeoutError" in str(e):
            error_message += "\nThe connection to the InfluxDB server timed out. Please check your network connection and the server status."
        elif "ConnectionError" in str(e):
            error_message += "\nUnable to connect to the InfluxDB server. Please check if the server is running and accessible."
        raise ConnectionError(error_message)

def main():
    parser = argparse.ArgumentParser(description="Fetch InfluxDB data and save to CSV.")
    parser.add_argument("--start_datetime", type=str, help="Start datetime in RFC3339 format (e.g., 2022-01-01T08:00:00Z)")
    parser.add_argument("--end_datetime", type=str, help="End datetime in RFC3339 format (e.g., 2022-01-01T20:00:01Z)")
    parser.add_argument("--interval", type=int, default=300, help="Time interval in seconds (default: 300)")
    parser.add_argument("--bucket", required=True, help="Bucket name")
    parser.add_argument("--measurement", required=True, help="Measurement name")
    parser.add_argument("--fields", nargs='+', required=True, help="Fields to query")
    parser.add_argument("--building", help="Building to filter (optional)")
    parser.add_argument("--output", default="influxdb_data.csv", help="Output CSV filename")
    args = parser.parse_args()

    print(f"Fetching data from {args.start_datetime} to {args.end_datetime} with {args.interval} second intervals...")
    print(f"Bucket: {args.bucket}, Measurement: {args.measurement}, Fields: {args.fields}")
    if args.building:
        print(f"Filtering for building: {args.building}")
    
    try:
        fetch_and_save_data(args.start_datetime, args.end_datetime, args.interval, args.bucket, args.measurement, args.fields, args.building, args.output)
    except ConnectionError as e:
        print(f"Connection error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    """
    Example usage: python fetch_ap_data.py 2024-07-10T07:00:00Z 2024-07-25T12:00:00Z 460 --bucket aruba --measurement "adjacent-ap" --fields "crawling-duration (ms)" "curr-rssi" --building D1 --output adjacent_ap_data.csv
    """
    main()