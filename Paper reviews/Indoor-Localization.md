# Optimizing Indoor Localization with Deep Learning on UJIIndoorLoc Dataset

## Main Reference: 
- [UJIIndoorLoc: A New Multi-building and
Multi-floor Database for WLAN Fingerprint-based
Indoor Localization Problems](https://ieeexplore.ieee.org/document/7275492)
- [CHISEL: Compression-Aware High-Accuracy Embedded Indoor Localization with Deep Learning](https://ieeexplore.ieee.org/document/9475489)
- [Comprehensive Analysis of Applied Machine Learning in
Indoor Positioning Based on Wi-Fi: An Extended
Systematic Review](https://www.mdpi.com/1424-8220/22/12/4622)
## ToC
- [Optimizing Indoor Localization with Deep Learning on UJIIndoorLoc Dataset](#optimizing-indoor-localization-with-deep-learning-on-ujiindoorloc-dataset)
  - [Main Reference:](#main-reference)
  - [ToC](#toc)
  - [Overview](#overview)
  - [Machine Leaning based Indoor Localization Techniques](#machine-leaning-based-indoor-localization-techniques)
  - [Data Preprocessing and Augmentation](#data-preprocessing-and-augmentation)
    - [UJIIndoorLoc](#ujiindoorloc)
    - [Procedure](#procedure)
  - [Network Architecture](#network-architecture)
  - [Model Compression](#model-compression)
    - [Quantization: Reducing Precision](#quantization-reducing-precision)
    - [Pruning: Removing Redundant Weights](#pruning-removing-redundant-weights)
  - [Experiment Evaluation](#experiment-evaluation)
    - [Evaluation on UJIIndoorLoc Dataset](#evaluation-on-ujiindoorloc-dataset)
    - [Evaluation with Model Compression:](#evaluation-with-model-compression)


## Overview
This paper points at the challenges of indoor localization on resource-limited embedded devices. It proposed a deep learning solution called CHISEL, which combines a Convolutional Autoencoder (CAE) and a CNN classifier. 

The purpose is to minimizing memory footprint and latency on embedded devices. The framework uses the UJIIndoorLoc dataset, normalizes the fingerprinting dataset, and employs data augmentation to improve generalization. 

Model compression techniques such as quantization and pruning are employed to reduce the model's memory footprint and latency for efficient deployment on embedded devices. The paper aims to provide a spectrum of deployment configurations with varying tradeoffs between accuracy, memory footprint, and latency goals, ultimately offering new options for high-accuracy indoor localization while minimizing deployment costs on embedded devices


## Machine Leaning based Indoor Localization Techniques
There are some other machine learning based indoor localization techniques such as :

- ### AoA (Angle of Arrival)
  
  Disadvantage:
  - Hardware complexity
  - Sensitive to computational error (long distance)
  
- ### ToF (Time of Flight)
  
  Disadvantage:
  - High localization errors, especially without line of sight paths
  - Requires tight synchronization requirements
  - Sensitive to multipath
   
- ### Fingerprinting based approaches

  Disadvantage:
  - Memory and computational overheads
  - Post-training model compression techniques may lead to a loss in localization accuracy

These works above do not consider positioning the user within a given floor

The solution proposed here is CHISEL that combines a Convolutional Autoencoder (CAE) and a CNN classifier that is suitable for model compression without any significant loss in localization accuracy.

##  Data Preprocessing and Augmentation

### UJIIndoorLoc
The UJIIndoorLoc database is a multi-building and multi-floor database for WLAN fingerprint-based indoor localization problems. The database is intended to facilitate the testing and comparison of different indoor localization algorithms.

The CHISEL framework utilize the UJIIndoorLoc indoor localization dataset. The dataset consists of unique Reference Points (RPs), where each RP represents a unique combination of:
- building ID
- floor ID
- space ID (to differentiate inside and outside)
- relative position ID (locates user on a given floor). 

The RSSI values for WiFi APs in the dataset range from -100 dBm (no signal) to 0 dBm (full signal strength). 

### Procedure
1. Augment the fingerprint dataset because of the limited samples per RP and to enhance generalization
2. For each RP, calculate the mean value of all RSSI APs
3. Calculate the absolute difference between the mean value of each AP. They
4. Generate AP RSSI values from a uniform distribution. The final dataset is a combination of the original and augmented fingerprints.

Considering the use of CNN, each fingerprint is zero-padded and transformed into a single-channel square-shaped image. This new fingerprint image-based dataset serves as the input for training the deep learning model.

Zero padding : Adding zeros to the edges of an image to ensure that the convolutional layers can process the entire image without losing information


## Network Architecture

The network architecture consists of two main components: 
- Convolutional Autoencoder (CAE)
- Convolutional Neural Network (CNN).
  
The training process occurs in two stages.
1. ### Training the CAE
   
   The CAE comprises an encoder and a decoder network.
This step is to minimize the MSE loss between the input and output fingerprints during training.
The CAE's encoder is designed to extract hidden features from the input fingerprints.

2. ### Transition to CNN
   
   The decoder from the CAE is replaced by a CNN classifier.
This is to to predict the user's location based on the encoded input obtained from the CAE.
The model is re-trained with the weights associated with the CAE's encoder frozen in place.

## Model Compression

### Quantization: Reducing Precision

Reducing the precision of numerical values used to represent the weights and activations in a neural network.
Neural networks often use 32-bit floating-point values, leading to large memory usage. Quantization reduces the bit-width. To do it, Quantization Aware Training (QAT) is employed, quantizing weights and activations before training begins.

Disadvantage: Impact accuracy due to lower precision.

### Pruning: Removing Redundant Weights

Removes weights from a trained model to reduce model size and computational requirements. Pruning is done to improve efficiency without losing accuracy.

## Experiment Evaluation

### Evaluation on UJIIndoorLoc Dataset
CHISEL exhibits excellent building prediction accuracy, and outperforms most other methods in floor accuracy.

The proposed models achieve average localization errors of ≈ 8.80 meters and ≈ 6.95 meters for CHISEL and CHISEL-DA.

1D-CNN falls short in positioning accuracy compared to CHISEL, because of the limitations in its model architecture and the absence of data augmentation.

### Evaluation with Model Compression:

- #### Quantization
  
  Post-training quantization results in higher localization error compared to QAT.

- #### Bit Width Impact
  
  Using fewer bits for weights leads to a general trend of worsening accuracy. 

- #### Pruning
  
  Pruning has almost no impact on localization accuracy but significantly reduces the model footprint.

- #### Best Compressed Model
  
  The model with QAT is a good candidate for the compressed model, providing a significant reduction in memory footprint while maintaining better accuracy than other deep learning models.