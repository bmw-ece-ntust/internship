#!/bin/bash

timestamp=$(date +"%Y%m%d_%H%M%S")

# Default values
start_datetime="2024-07-24T07:00:00Z"
end_datetime="2024-07-25T00:00:00Z"
interval=900
bucket="aruba"
measurement="adjacent-ap"
fields="crawling-duration(ms) curr-rssi"
building="D1"
output_fetch="data/adjacent_ap_data_${timestamp}.csv"
floors_folder="../data/"
output_transform="data/processed_ap_data_${timestamp}.csv"
output_folder="./output"
mode="train_and_test"
clf_n_estimators=100
clf_max_depth=3
clf_learning_rate=0.1
reg_n_estimators=200
reg_max_depth=5
reg_learning_rate=0.2
do_grid_search=false
grid_n_estimators="100 200 300"
grid_max_depth="3 4 5"
grid_learning_rate="0.01 0.1 0.2"

# Parse command-line arguments
while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        --start_datetime) start_datetime="$2"; shift; shift ;;
        --end_datetime) end_datetime="$2"; shift; shift ;;
        --interval) interval="$2"; shift; shift ;;
        --bucket) bucket="$2"; shift; shift ;;
        --measurement) measurement="$2"; shift; shift ;;
        --fields) fields="$2"; shift; shift ;;
        --building) building="$2"; shift; shift ;;
        --output_fetch) output_fetch="$2"; shift; shift ;;
        --floors_folder) floors_folder="$2"; shift; shift ;;
        --output_transform) output_transform="$2"; shift; shift ;;
        --output_folder) output_folder="$2"; shift; shift ;;
        --mode) mode="$2"; shift; shift ;;
        --clf_n_estimators) clf_n_estimators="$2"; shift; shift ;;
        --clf_max_depth) clf_max_depth="$2"; shift; shift ;;
        --clf_learning_rate) clf_learning_rate="$2"; shift; shift ;;
        --reg_n_estimators) reg_n_estimators="$2"; shift; shift ;;
        --reg_max_depth) reg_max_depth="$2"; shift; shift ;;
        --reg_learning_rate) reg_learning_rate="$2"; shift; shift ;;
        --do_grid_search) do_grid_search=true; shift ;;
        --grid_n_estimators) grid_n_estimators="$2"; shift; shift ;;
        --grid_max_depth) grid_max_depth="$2"; shift; shift ;;
        --grid_learning_rate) grid_learning_rate="$2"; shift; shift ;;
        *) echo "Unknown parameter: $1"; exit 1 ;;
    esac
done

# Fetch AP Data
echo "Fetching AP Data"
echo "Running fetch_ap_data.py..."
python fetch_ap_data.py --start_datetime "$start_datetime" --end_datetime "$end_datetime" --interval "$interval" --bucket "$bucket" --measurement "$measurement" --fields $fields --building "$building" --output "$output_fetch"

# Check if fetch_ap_data.py was successful
if [ $? -ne 0 ]; then
    echo "Error: fetch_ap_data.py failed. Exiting."
    exit 1
fi

# Data Transformations
echo "Transforming Data"
echo "Running data_transformations.py..."
python data_transformations.py -i "$output_fetch" -f "$floors_folder" -o "$output_transform"

# Check if data_transformations.py was successful
if [ $? -ne 0 ]; then
    echo "Error: data_transformations.py failed. Exiting."
    exit 1
fi

# Model Training and Testing
echo "Training and Testing Model"
grid_search_params=""
if $do_grid_search; then
    grid_search_params="--do_grid_search --grid_n_estimators $grid_n_estimators --grid_max_depth $grid_max_depth --grid_learning_rate $grid_learning_rate"
fi

echo "Running model_training_and_testing.py..."
python model_training_and_testing.py --input_file "$output_transform" \
    --mode "$mode" \
    --output_folder "$output_folder" \
    --clf_n_estimators "$clf_n_estimators" \
    --clf_max_depth "$clf_max_depth" \
    --clf_learning_rate "$clf_learning_rate" \
    --reg_n_estimators "$reg_n_estimators" \
    --reg_max_depth "$reg_max_depth" \
    --reg_learning_rate "$reg_learning_rate" \
    $grid_search_params

# Check if model_training_and_testing.py was successful
if [ $? -ne 0 ]; then
    echo "Error: model_training_and_testing.py failed."
    exit 1
fi

echo "AP data pipeline completed successfully!"