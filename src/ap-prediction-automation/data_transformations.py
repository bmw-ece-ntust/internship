"""
This module processes access point (AP) data from CSV or JSON files, 
translates BSSIDs to AP names, and adds coordinates to the processed data.

Modules:
    - os: Provides a way to use operating system-dependent functionality.
    - pandas: For data manipulation and analysis.
    - json: For reading JSON files.
    - hashlib: For computing SHA256 hashes.
    - csv: For reading CSV files.
    - glob: For Unix style pathname pattern expansion.
    - argparse: For command-line argument parsing.
    - numpy: For numerical operations and handling arrays.
    - io: For handling string input and output.
    - functools: For higher-order functions (partial application).

Functions:
    - compute_sha256(value)
    - read_input_file(input_file)
    - process_data(data, floor_filters)
    - translate_bssids(df, floor_filters)
    - read_coordinate_file(file_path)
    - add_coordinates(df, ap_data)
    - clean_data(df)
"""

import os
import pandas as pd
import json
import hashlib
import csv
import glob
import argparse
import numpy as np
import io
from functools import partial

def compute_sha256(value):
    """
    Compute SHA256 hash of a string.

    Parameters
    ----------
    value : str
        The string to hash.

    Returns
    -------
    str
        The SHA256 hash of the input string.
    """
    return hashlib.sha256(value.encode()).hexdigest()

def read_input_file(input_file):
    """
    Read input file and return a DataFrame. Automatically detects file type (CSV or JSON).

    Parameters
    ----------
    input_file : str
        The path to the input file.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the data from the input file.

    Raises
    ------
    ValueError
        If the input file type is unsupported (not CSV or JSON).
    """
    print(f"Reading input data from {input_file}...")
    file_extension = os.path.splitext(input_file)[1].lower()
    
    if file_extension == '.csv':
        # Read the CSV file in chunks, skipping bad lines
        chunks = []
        chunk_size = 200000  # Adjust this value based on your available memory
        
        for chunk in pd.read_csv(input_file, 
                                 chunksize=chunk_size,
                                 comment='#',
                                 on_bad_lines='skip',  
                                 parse_dates=['_start', '_stop', '_time'], 
                                 na_values=[''], 
                                 low_memory=False):  
            chunks.append(chunk)
        
        # Concatenate all chunks into a single DataFrame
        return pd.concat(chunks, ignore_index=True)

    elif file_extension == '.json':
        with open(input_file, 'r') as file:
            data = file.read()
        data_io = io.StringIO(data)
        return pd.read_csv(data_io, 
                           comment='#',
                           skiprows=3,  
                           parse_dates=['_start', '_stop', '_time'], 
                           na_values=[''], 
                           low_memory=False)
    else:
        raise ValueError(f"Unsupported file type: {file_extension}. Please use CSV or JSON files.")

def process_data(data, floor_filters):
    """
    Process the raw data with optimizations.

    Parameters
    ----------
    data : pd.DataFrame
        The raw input data as a DataFrame.
    
    floor_filters : str
        A regex pattern for filtering monitoring APs based on floor.

    Returns
    -------
    pd.DataFrame
        A processed DataFrame containing the relevant data after filtering and pivoting.

    Raises
    ------
    ValueError
        If required columns are missing or if no data remains after filtering.
    """
    print("Processing raw data...")
    
    # Check if required columns exist
    required_columns = ['_time', 'essid', 'adjacent-ap-bssid', 'band', 'monitoring-ap', '_value']
    missing_columns = [col for col in required_columns if col not in data.columns]
    
    if missing_columns:
        print(f"Error: Missing required columns: {missing_columns}")
        return None
    
    columns = ['_time', 'essid', 'adjacent-ap-bssid', 'band', 'monitoring-ap', '_value']
    data = data[columns]
    
    mask = (data['band'] == '2.4GHz') & \
           (data['monitoring-ap'].notna()) & \
           (data['monitoring-ap'].str.contains(floor_filters, regex=True))
    data = data[mask]
    
    if data.empty:
        print("Error: No data left after applying filters")
        return None
    
    mask_64 = data["adjacent-ap-bssid"].str.len() == 64
    data.loc[~mask_64, "adjacent-ap-bssid"] = data.loc[~mask_64, "adjacent-ap-bssid"].apply(compute_sha256)

    # If '_time' is not datetime, convert it to string to avoid pivot_table errors
    if '_time' in data.columns and not pd.api.types.is_datetime64_any_dtype(data['_time']):
        data['_time'] = data['_time'].astype(str)

    pivot_table = pd.pivot_table(data, 
                                 values='_value', 
                                 index=['_time', 'essid', 'adjacent-ap-bssid', 'band'],
                                 columns='monitoring-ap')
    
    result = pivot_table.reset_index()
    result.columns = ['_time', 'essid', 'bssid', 'band'] + ['rssi_' + str(col) for col in pivot_table.columns]
    
    return result


def translate_bssids(df, floor_filters):
    """
    Translate BSSIDs to AP names using a predefined mapping.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing BSSID data to be translated.

    floor_filters : str
        A regex pattern for filtering AP names based on floor.

    Returns
    -------
    pd.DataFrame
        A DataFrame with translated AP names, filtering out those that don't match the floor filters.
    """
    print("Translating BSSIDs...")
    with open('../data/ap_bss_table.json', 'r') as file:
        bss_data = json.load(file)

    bss_df = pd.DataFrame(bss_data["Aruba AP BSS Table"])
    bss_df['bssid'] = bss_df['bss'].apply(compute_sha256)

    merged_df = pd.merge(df, bss_df[['bssid', 'ap name']], on='bssid', how='left')
    merged_df.rename(columns={'ap name': 'ap_name'}, inplace=True)
    merged_df = merged_df[merged_df['ap_name'].notna()]
    merged_df = merged_df[merged_df['ap_name'].str.contains(floor_filters, regex=True)]

    return merged_df 

def read_coordinate_file(file_path):
    """
    Read AP coordinate data from a CSV file.

    Parameters
    ----------
    file_path : str
        The path to the CSV file containing AP coordinates.

    Returns
    -------
    dict
        A dictionary mapping AP names to their (x, y, z) coordinates.
    """
    with open(file_path, 'r') as file:
        return {row[0]: (float(row[1]), float(row[2]), float(row[3])) for row in csv.reader(file)}

def add_coordinates(df, ap_data):
    """
    Add x, y, and z coordinates to the DataFrame based on AP names.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to which coordinates will be added.
    
    ap_data : dict
        A dictionary containing the mapping of AP names to their coordinates.

    Returns
    -------
    pd.DataFrame
        The updated DataFrame with coordinates added.
    """
    print("Adding coordinates...")
    df[['x', 'y', 'z']] = df['ap_name'].map(ap_data).apply(pd.Series)
    return df

def clean_data(df):
    """
    Clean the data by removing NaN values and clipping RSSI values.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to be cleaned.

    Returns
    -------
    pd.DataFrame
        The cleaned DataFrame with NaN values removed and RSSI values clipped.
    """
    print("Cleaning data...")
    # Drop rows where the last column (z-coordinate) is NaN
    df = df.dropna(subset=[df.columns[-1]])
    
    # Replace NaN values with 200
    df.replace({np.nan: 200}, inplace=True)
    
    # Clip RSSI values (columns 4 to -4) to a maximum of 200
    rssi_columns = df.columns[4:-4]  # Assuming RSSI columns start at index 4 and end 4 from the last
    df[rssi_columns] = df[rssi_columns].clip(upper=200)
    
    return df

def main(input_file, floors_folder, output_file):
    print(f"Starting processing of {input_file}")

    floor_files = sorted(glob.glob(os.path.join(floors_folder, '[2-9]f.csv')) + 
                         glob.glob(os.path.join(floors_folder, '1[0-3]f.csv')))
    floor_numbers = [os.path.basename(file).split('f')[0] for file in floor_files]
    floor_filters = '|'.join([f'D1_{floor}F' for floor in floor_numbers])

    ap_data = {}
    for file in floor_files:
        ap_data.update(read_coordinate_file(file))

    df = read_input_file(input_file)
    print(f"Records after initial read: {len(df)}")

    processed_data = process_data(df, floor_filters)
    if processed_data is None:
        print("Error: Failed to process data. Exiting.")
        return
    print(f"Records after processing: {len(processed_data)}")

    clean_df = translate_bssids(processed_data, floor_filters)
    if clean_df is None:
        print("Error: Failed to translate BSSIDs. Exiting.")
        return
    print(f"Records after BSSID translation: {len(clean_df)}")

    final_df = add_coordinates(clean_df, ap_data)
    
    # Add the new data cleaning step
    final_df = clean_data(final_df)
    print(f"Records after final cleaning: {len(final_df)}")

    print(f"Saving processed data to {output_file}")
    final_df.to_csv(output_file, index=False)

    print("Processing complete. Generating statistics...")
    print(f"Number of different APs: {final_df['ap_name'].nunique()}")
    print(f"Date range: {final_df['_time'].min()} to {final_df['_time'].max()}")
    print(f"Total records: {len(final_df)}")
    print(f"Z-coordinate range: {final_df['z'].min()} to {final_df['z'].max()}")
    print(f"Floors included: {', '.join(floor_numbers)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process AP data.")
    parser.add_argument("-i", "--input", required=True, help="Path to the input data file (CSV or JSON)")
    parser.add_argument("-f", "--floors", required=True, help="Path to the folder containing floor data files")
    parser.add_argument("-o", "--output", required=True, help="Path to save the output CSV file")
    args = parser.parse_args()

    main(args.input, args.floors, args.output)