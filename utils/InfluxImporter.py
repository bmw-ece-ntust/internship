import csv
from influxdb import InfluxDBClient

class InfluxDBCSVImporter:
    """ Move csv data into InfluxDB database sequentially.

    Args:
        host (str): InfluxDB hostname, or ip address
        port (int): InfluxDB port number (default is 8086)
        dbname (str): InfluxDB database name to save the imported data
    
    Methods:
        import_csv(csvfile): Import CSV file with the filename defined by the csvfile argument into InfluxDB

    """
    def __init__(self, host, port, dbname):
        self.host = host
        self.port = port
        self.dbname = dbname

        # Connect to InfluxDB
        self.client = InfluxDBClient(host=args.host, port=args.port)

        # Create or switch to a database
        self.client.create_database(args.dbname)
        self.client.switch_database(args.dbname)

    def import_csv(csvfile):
        # Open your csv file
        with open(csvfile, 'r') as f:
            reader = csv.reader(f)
            headers = next(reader)  # Get the headers of the file

            for row in reader:
                data = [{
                    "measurement": "your_measurement",
                    "tags": {
                        "tag1": "tag_value"
                    },
                    "fields": {
                        headers[i]: row[i] for i in range(len(row))
                    }
                }]
                self.client.write_points(data)
