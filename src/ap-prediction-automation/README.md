# AP Data Processing and Analysis Automation

This project automates the process of fetching, processing, and analyzing Access Point data. The main script `run_all.bash` orchestrates the entire workflow, calling several Python scripts to perform specific tasks.

## Overview

The automation process consists of three main steps:
1. Fetching AP data from an InfluxDB database
2. Transforming and cleaning the data
3. Training and testing machine learning models for AP position prediction

## Usage

To run the entire process, use the following command:

```bash
./run_all.bash [options]
```

### Options

- `--start_datetime`: Start date and time for data fetching (default: "2024-07-24T07:00:00Z")
- `--end_datetime`: End date and time for data fetching (default: "2024-07-25T00:00:00Z")
- `--interval`: Time interval in seconds for data aggregation (default: 900)
- `--bucket`: InfluxDB bucket name (default: "aruba")
- `--measurement`: InfluxDB measurement name (default: "adjacent-ap")
- `--fields`: Fields to fetch from InfluxDB (default: "crawling-duration(ms) curr-rssi")
- `--building`: Building to filter data (default: "D1")
- `--output_fetch`: Output file for fetched data (default: "data/adjacent_ap_data_${timestamp}.csv")
- `--floors_folder`: Folder containing floor data files (default: "../data/")
- `--output_transform`: Output file for transformed data (default: "data/processed_ap_data_${timestamp}.csv")
- `--output_folder`: Output folder for results (default: "./output")
- `--mode`: Mode of operation for model training and testing (default: "train_and_test")
- `--clf_n_estimators`, `--clf_max_depth`, `--clf_learning_rate`: XGBoost classifier parameters
- `--reg_n_estimators`, `--reg_max_depth`, `--reg_learning_rate`: XGBoost regressor parameters
- `--do_grid_search`: Enable grid search for hyperparameter tuning
- `--grid_n_estimators`, `--grid_max_depth`, `--grid_learning_rate`: Grid search parameters

## Components

### 1. Data Fetching (`fetch_ap_data.py`)

This script fetches AP data from an InfluxDB database based on the specified parameters. It handles:
- Connecting to the InfluxDB API
- Querying data with filters for date range, measurement, fields, and building
- Saving the fetched data to a CSV file


#### Note 
To run this script, ensure you have a `.env` file in the same directory. This file should contain all the credentials needed to access InfluxDB (including the URL, group, and token).


### 2. Data Transformation (`data_transformations.py`)

This script processes and cleans the fetched data. It performs the following tasks:
- Reading the input CSV file
- Filtering data based on specified criteria (e.g., 2.4GHz band, specific floors)
- Translating BSSIDs to AP names
- Adding coordinates to APs
- Cleaning the data by removing NaN values and clipping RSSI values
- Saving the processed data to a new CSV file

### 3. Model Training and Testing (`model_training_and_testing.py`)

This script handles the machine learning aspects of the project:
- Loading the processed data
- Preparing features (RSSI values) and targets (AP names and coordinates)
- Splitting data into training and testing sets
- Training XGBoost models for classification (predicting AP names) and regression (predicting AP coordinates)
- Evaluating model performance
- Generating visualizations of AP positions and prediction accuracy
- Saving trained models, evaluation results, and visualizations

## Output

The automation process generates several outputs:
- CSV files containing raw and processed AP data
- Trained machine learning models (saved as pickle files)
- Text files with classification reports and regression error metrics
- Visualizations of AP positions and prediction accuracy (PNG files)

All outputs are organized in timestamped folders within the specified output directory.
