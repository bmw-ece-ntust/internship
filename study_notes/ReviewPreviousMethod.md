# Review of: [AP-localization-regression](https://github.com/bmw-ece-ntust/AP-localization-regression/tree/master/2024_NTUST)

## Project Structure
The root directory is organized into two main components:

+ A **Jupyter Notebook** containing the preprocessing, models, and their results.
+ A **CSV** file containing the dataset.
+ A folder named `2024_NTUST`, which includes all the code for the experiments conducted.

### `2024_NTUST` Folder
This folder is divided into two main subfolders: `IPYNB` and `Python`.

### `IPYNB` Folder
This folder contains 5 notebooks:
* `RSS_Modeling_*`: Three notebooks with the results of the different models applied to the data.
* `Autoencoder`: Results from the Autoencoder model.
* `ntust_data_mapping`: Dedicated to the cleansing and mapping of RSSI data from NTUST.

### `Python` Folder
This folder contains:
* Two files: One for configuring the Python environment used for the project.
* A subfolder named `package`, which contains five `.py` files related to the different models used and the preprocessing of the data.


## Jupyter Notebook: NTUST_RSS_Modeling.ipynb

The Jupyter Notebook is divided into the following sections:

1. **Acquiring Data from InfluxDB** (InfluxDB Data Mounting)
2. **Loading the Previously Cleaned Data** (Data Mounting)  
    Possible Issue: Improper handling of NaNs  
    2.1 **Data Augmentation** (Augmentation with Gaussian Noise Injection)  
    2.2 **MinMax Scaling and NaN Conversion** (Data Preprocessing)
3. **Machine Learning Models**
    3.1 **Random Forest**  
        Results:
        ```
        Localization RMSE: 322.81
        Localization MAE: 223.83
        ```
    3.2 **SVR**  
        Results:
        ```
        Localization RMSE: 418.42
        Localization MAE: 361.00
        ```
    3.3 **KNN**  
        Results:
        ```
        Localization RMSE: 393.67
        Localization MAE: 307.04
        ```
    3.4 **ANN**  
        Results:
        ```
        Localization RMSE: 487.21
        Localization MAE: 421.74
        ```
    3.5 **AE-ANN**  
        Results:
        ```
        Localization RMSE: 2722645.97
        Localization MAE: 2668531.63
        ```

All models resulted in high error rates, indicating poor performance. Additionally, hyperparameter optimization for some models led to worse results than the default configurations. The next step is to verify that the data preprocessing is correct and to reassess the model definitions and their suitability for the task at hand.


