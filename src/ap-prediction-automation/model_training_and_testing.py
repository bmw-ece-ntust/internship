"""
This module provides utilities for managing experiments, including folder creation, label encoding,
and timestamp generation.

Modules:
    - os: Operating system interfaces for file and directory management.
    - time: Time-related functions for timestamp generation.
    - pickle: Python object serialization.
    - pandas: Data manipulation and analysis library.
    - numpy: Numerical computing library.
    - matplotlib.pyplot: Plotting library for creating static, animated, and interactive visualizations.
    - collections.defaultdict: A dictionary subclass that provides default values for non-existent keys.
    - sklearn.preprocessing: Functions for preprocessing data, including scaling and encoding.
    - sklearn.model_selection: Functions for splitting datasets and hyperparameter tuning.
    - sklearn.multioutput: Multi-output regression estimators.
    - xgboost: A scalable and flexible gradient boosting library.
    - sklearn.metrics: Functions for evaluating model performance.

Functions:
    - get_timestamp()
    - create_output_folders(base_folder, mode, timestamp)
    - create_output_filename(base_name, extension)
    - encode_and_save_labels(data, column_name, encoder_file_name, model_folder)
"""

import argparse
import os
import pickle
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from sklearn.preprocessing import LabelEncoder, RobustScaler
from sklearn.model_selection import GridSearchCV, train_test_split, StratifiedShuffleSplit
from sklearn.multioutput import MultiOutputRegressor
from xgboost import XGBClassifier, XGBRegressor
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error
from matplotlib.colors import Normalize

def get_timestamp():
    """
    Generate a timestamp for folder naming.

    Returns
    -------
    str
        A string representing the current timestamp formatted as YYYYMMDD_HHMMSS.
    """
    return time.strftime("%Y%m%d_%H%M%S")

def create_output_folders(base_folder, mode, timestamp):
    """
    Create output directories for models, results, and images.

    Parameters
    ----------
    base_folder : str
        The base folder where the output directories will be created.
    mode : str
        The mode of the experiment, which helps in organizing output directories.
    timestamp : str
        The timestamp to be used for naming the experiment folder.

    Returns
    -------
    dict
        A dictionary containing the paths to the created subfolders.
    """
    experiment_folder = os.path.join(base_folder, mode, timestamp)
    os.makedirs(experiment_folder, exist_ok=True)
    
    subfolders = ['models', 'results', 'images']
    folder_paths = {}
    
    for subfolder in subfolders:
        folder_path = os.path.join(experiment_folder, subfolder)
        os.makedirs(folder_path, exist_ok=True)
        folder_paths[subfolder] = folder_path
    
    return folder_paths

def create_output_filename(base_name, extension):
    """
    Create an output filename with specified extension.

    Parameters
    ----------
    base_name : str
        The base name for the output file.
    extension : str
        The file extension (e.g., 'csv', 'txt').

    Returns
    -------
    str
        The complete filename with the specified extension.
    """
    return f"{base_name}.{extension}"

def encode_and_save_labels(data, column_name, encoder_file_name, model_folder):
    """
    Encode categorical labels and save the encoder to a file.

    Parameters
    ----------
    data : pd.DataFrame
        The DataFrame containing the data with categorical labels to be encoded.
    column_name : str
        The name of the column to be encoded.
    encoder_file_name : str
        The name of the file where the encoder will be saved.
    model_folder : str
        The folder where the encoder file will be saved.

    Returns
    -------
    None
        The specified column in the DataFrame is updated with encoded values, 
        and the encoder is saved to a file.
    """
    le = LabelEncoder()
    encoded_values = le.fit_transform(data[column_name])
    data[column_name] = encoded_values
    full_encoder_file_name = os.path.join(model_folder, create_output_filename(encoder_file_name, 'pkl'))
    with open(full_encoder_file_name, 'wb') as file:
        pickle.dump(le, file)
    print(f"Encoded {column_name} and saved encoder to {full_encoder_file_name}")
    return data

def decode_predictions(y_pred, encoder_file_name):
    with open(encoder_file_name, 'rb') as file:
        le = pickle.load(file)
    decoded_predictions = le.inverse_transform(y_pred)
    print(f"Decoded predictions using encoder from {encoder_file_name}")
    return decoded_predictions

def plot_ap_positions(data, y_test, y_pred, image_folder):
    unique_floors = data['ap_name'].str.extract('(\d+F)')[0].unique()
    num_floors = len(unique_floors)
    fig, axes = plt.subplots(1, num_floors, figsize=(12 * num_floors // 2, 8))

    ap_positions = dict(zip(data['ap_name'], zip(data['x'], data['y'])))

    for i, floor in enumerate(sorted(unique_floors)):
        floor_mask = [floor in ap for ap in y_test]
        floor_y_test = y_test[floor_mask]
        floor_y_pred = y_pred[floor_mask]

        test_positions = [ap_positions[ap] for ap in floor_y_test]
        pred_positions = [ap_positions[ap] for ap in floor_y_pred]

        position_accuracy = defaultdict(lambda: {'correct': 0, 'total': 0})
        for true_pos, true_ap, pred_ap in zip(test_positions, floor_y_test, floor_y_pred):
            position_accuracy[true_pos]['total'] += 1
            if true_ap == pred_ap:
                position_accuracy[true_pos]['correct'] += 1

        position_percentage = {pos: (data['correct'] / data['total']) * 100 
                               for pos, data in position_accuracy.items()}

        x_test, y_test_coords = zip(*test_positions)
        x_pred, y_pred_coords = zip(*pred_positions)

        scatter = axes[i].scatter(x_test, y_test_coords, c='green', marker='o', s=200, alpha=0.5, label='Ground Truth')
        scatter = axes[i].scatter(x_pred, y_pred_coords, 
                                  c=[position_percentage.get(pos, 0) for pos in test_positions],
                                  cmap='RdYlGn', vmin=0, vmax=100, s=50, alpha=0.7)

        correct_predictions = sum(true == pred for true, pred in zip(floor_y_test, floor_y_pred))
        total_predictions = len(floor_y_test)
        overall_accuracy = (correct_predictions / total_predictions) * 100

        axes[i].set_title(f'AP Positions on {floor}\nAccuracy: {overall_accuracy:.2f}%')
        axes[i].set_xlabel('X Position')
        axes[i].set_ylabel('Y Position')
        axes[i].grid(True)

    plt.tight_layout()
    cbar = fig.colorbar(scatter, ax=axes.ravel().tolist())
    cbar.set_label('Percentage of Correct Predictions')

    output_filename = create_output_filename('ap_positions_plot', 'png')
    plt.savefig(os.path.join(image_folder, output_filename))
    plt.close()

def plot_3d_ap_positions(y_true, y_pred, image_folder):
    mse = np.mean((y_true - y_pred)**2, axis=1)
    
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    norm = Normalize(vmin=0, vmax=10)
    scatter = ax.scatter(y_pred[:, 0], y_pred[:, 1], y_pred[:, 2],
                         c=mse, norm=norm, cmap='Oranges_r', s=30, alpha=0.7, label='Predicted', zorder=2)

    scatter_true = ax.scatter(y_true[:, 0], y_true[:, 1], y_true[:, 2], 
               c='blue', marker='o', s=5, alpha=0.1, label='Ground Truth', zorder=1)
    
    cbar = fig.colorbar(scatter)
    cbar.set_label('Mean Squared Error')
    
    overall_mse = mean_squared_error(y_true, y_pred)
    
    ax.set_xlabel('X Position')
    ax.set_ylabel('Y Position')
    ax.set_zlabel('Z Position')
    ax.legend()
    plt.title(f'3D AP Positions - Overall MSE: {overall_mse:.4f}')
    
    plt.tight_layout()
    output_filename = create_output_filename('3d_ap_positions_plot', 'png')
    plt.savefig(os.path.join(image_folder, output_filename))
    plt.close()

def main(args):
    timestamp = get_timestamp()
    folders = create_output_folders(args.output_folder, args.mode, timestamp)
    
    data = pd.read_csv(args.input_file)

    rssi_columns = [col for col in data.columns if col.startswith('rssi_')]
    X = data[rssi_columns]
    y = data['ap_name']

    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    label_encoder_filename = create_output_filename('label_encoder', 'pkl')
    with open(os.path.join(folders['models'], label_encoder_filename), 'wb') as file:
        pickle.dump(le, file)

    robust_scaler = RobustScaler()
    robust_scaled_data = robust_scaler.fit_transform(X)

    if args.mode in ['train_and_test', 'test_only']:
        sss = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=1)
        for train_index, test_index in sss.split(robust_scaled_data, y_encoded):
            X_train, X_test = robust_scaled_data[train_index], robust_scaled_data[test_index]
            y_train, y_test = y_encoded[train_index], y_encoded[test_index]

        if args.mode == 'train_and_test':
            X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.12, random_state=1, stratify=y_train)

    if args.mode in ['train_and_test', 'train_only']:
        xgb_clf = XGBClassifier(n_estimators=args.clf_n_estimators,
                                max_depth=args.clf_max_depth,
                                learning_rate=args.clf_learning_rate)

        xgb_clf.fit(X_train, y_train)

        # Save the trained model
        model_filename = create_output_filename('xgb_classifier_model', 'pkl')
        with open(os.path.join(folders['models'], model_filename), 'wb') as file:
            pickle.dump(xgb_clf, file)

    if args.mode in ['train_and_test', 'test_only']:
        if args.mode == 'test_only':
            # Load the model for testing
            model_filename = create_output_filename('xgb_classifier_model', 'pkl')
            with open(os.path.join(folders['models'], model_filename), 'rb') as file:
                xgb_clf = pickle.load(file)

        y_pred = xgb_clf.predict(X_test)

        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred, zero_division=0, output_dict=True)

        classification_results_filename = create_output_filename('classification_results', 'txt')
        with open(os.path.join(folders['results'], classification_results_filename), 'w') as f:
            f.write(f'Accuracy: {accuracy:.2f}\n\n')
            f.write('Classification Report:\n')
            for label, metrics in report.items():
                if isinstance(metrics, dict):
                    f.write(f"\nClass: {label}\n")
                    for metric_name, value in metrics.items():
                        f.write(f"  {metric_name}: {value:.2f}\n")
                else:
                    f.write(f"\n{label}: {metrics:.2f}\n")

            f.write("\nClass distribution in test set:\n")
            unique, counts = np.unique(y_test, return_counts=True)
            for label, count in zip(unique, counts):
                f.write(f"  {le.inverse_transform([label])[0]}: {count}\n")

        decoded_y_pred = le.inverse_transform(y_pred)
        decoded_y_test = le.inverse_transform(y_test)

        try:
            plot_ap_positions(data, decoded_y_test, decoded_y_pred, folders['images'])
        except Exception as e:
            print(f"Error in plot_ap_positions: {str(e)}")

    # Regression part
    X = data[rssi_columns]
    y = data[['x', 'y', 'z']]

    regression_data_scaled = RobustScaler().fit_transform(X)

    if args.mode in ['train_and_test', 'test_only']:
        X_train, X_test, y_train, y_test = train_test_split(regression_data_scaled, y, test_size=0.2, random_state=1)
        if args.mode == 'train_and_test':
            X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.12, random_state=1)

    if args.mode in ['train_and_test', 'train_only']:
        xgb_model = XGBRegressor(objective='reg:squarederror', random_state=42,
                                 n_estimators=args.reg_n_estimators,
                                 max_depth=args.reg_max_depth,
                                 learning_rate=args.reg_learning_rate)
        multi_xgb = MultiOutputRegressor(xgb_model)

        if args.do_grid_search:
            param_grid = {
                'estimator__n_estimators': args.grid_n_estimators,
                'estimator__max_depth': args.grid_max_depth,
                'estimator__learning_rate': args.grid_learning_rate
            }
            grid_search = GridSearchCV(multi_xgb, param_grid, cv=3, scoring='neg_mean_squared_error')
            grid_search.fit(X_train, y_train)
            best_model = grid_search.best_estimator_
            best_model_filename = create_output_filename('best_model', 'pkl')
            with open(os.path.join(folders['models'], best_model_filename), 'wb') as file:
                pickle.dump(best_model, file)
        else:
            multi_xgb.fit(X_train, y_train)
            best_model = multi_xgb

        # Save the trained regression model
        reg_model_filename = create_output_filename('xgb_regressor_model', 'pkl')
        with open(os.path.join(folders['models'], reg_model_filename), 'wb') as file:
            pickle.dump(best_model, file)

    if args.mode in ['train_and_test', 'test_only']:
        if args.mode == 'test_only':
            # Load the regression model for testing
            reg_model_filename = create_output_filename('xgb_regressor_model', 'pkl')
            with open(os.path.join(folders['models'], reg_model_filename), 'rb') as file:
                best_model = pickle.load(file)

        y_pred = best_model.predict(X_test)

        mse = mean_squared_error(y_test, y_pred)
        print(f"Mean Squared Error: {mse:.2f}")

        # Save MSE to a file
        mse_filename = create_output_filename('regression_mse', 'txt')
        with open(os.path.join(folders['results'], mse_filename), 'w') as f:
            f.write(f"Mean Squared Error: {mse:.2f}")

        try:
            plot_3d_ap_positions(y_test.values, y_pred, folders['images'])
        except Exception as e:
            print(f"Error in plot_3d_ap_positions: {str(e)}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Train and evaluate an XGBoost model for AP position prediction.')

    parser.add_argument("--input_file", required=True, help="Path to the input CSV file with RSSI and AP data")
    parser.add_argument("--mode", required=True, choices=['train_only', 'test_only', 'train_and_test'], help="Mode of operation")
    parser.add_argument("--output_folder", required=False, default=".", help="Path to the base output folder")
    
    parser.add_argument("--clf_n_estimators", type=int, default=100, help="Number of boosting rounds for XGBClassifier")
    parser.add_argument("--clf_max_depth", type=int, default=3, help="Maximum depth of trees for XGBClassifier")
    parser.add_argument("--clf_learning_rate", type=float, default=0.1, help="Learning rate for XGBClassifier")
    
    parser.add_argument("--reg_n_estimators", type=int, default=100, help="Number of boosting rounds for XGBRegressor")
    parser.add_argument("--reg_max_depth", type=int, default=3, help="Maximum depth of trees for XGBRegressor")
    parser.add_argument("--reg_learning_rate", type=float, default=0.1, help="Learning rate for XGBRegressor")
    
    parser.add_argument("--grid_n_estimators", type=int, nargs='+', default=[100], help="Grid search values for number of estimators")
    parser.add_argument("--grid_max_depth", type=int, nargs='+', default=[3], help="Grid search values for max depth")
    parser.add_argument("--grid_learning_rate", type=float, nargs='+', default=[0.1], help="Grid search values for learning rate")
    parser.add_argument("--do_grid_search", action='store_true', help="Flag to enable grid search for model tuning")

    args = parser.parse_args()
    main(args)
