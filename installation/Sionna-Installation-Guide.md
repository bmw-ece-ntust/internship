# Sionna RT Installation

## Requirements
- Python 3.8-3.11
- Tensorflow 2.10-2.15
- JupyterLab
- Ubuntu 22.04 (Recommended)

## Python 3 Installation

1. Update the Package Repository
   
   ```
   sudo apt update
   ```
2. Install Python
   ```
   sudo apt install python3
   ```
3. Verify Installation
   ```
   python3 --version
   ```
   Result:
   ```
   Python 3.10.12
   ```

## Tensorflow Installation

1. Remove any existing Nvidia installations
   ```
   sudo apt update
   sudo apt upgrade
   sudo apt-get remove --purge '^nvidia-.*'
   sudo apt-get autoremove
   ```
2.  Disable Nouveau Nvidia driver
   
    1. Open the blacklisted file in text editor
        ```
        sudo nano /etc/modprobe.d/blacklist-nvidia-nouveau.conf
        ```
    2. Insert the following lines into the file
        ```
        blacklist nouveau
        options nouveau modeset=0
        ```
    3. Save the file and exit the editor (Ctrl+X, then Y, then Enter)
    4. Regenerate the kernel initramfs:
        ```
        sudo update-initramfs -u
        ```
3.  Install Nvidia driver and CUDA Toolkit
    ```
    wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin
    sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600
    wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda-repo-ubuntu2204-11-8-local_11.8.0-520.61.05-1_amd64.deb
    ```
    
4. Check the name of the file that was downloaded and run this (with the name of the file you have)
    ```
    sudo dpkg -i cuda-repo-ubuntu2204-11-8-local_11.8.0-520.61.05-1_amd64.deb
    ```
4.  Next we run this lines
    ```
    sudo apt-get update
    sudo apt-get -y install cuda
    echo 'export PATH=/usr/local/cuda-11.8/bin${PATH:+:${PATH}}' >> ~/.bashrc
    echo 'export LD_LIBRARY_PATH=/usr/local/cuda-11.8/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}' >> ~/.bashrc
    source ~/.bashrc
    ```
5. To verify the installation, reboot and run the following command in the terminal:
   ```
   nvidia-smi
   ```

6. Make an account in [cuDNN](https://developer.nvidia.com/cudnn?source=post_page-----250429035e63--------------------------------)
7. Click on download, create account and download the cudnn local file for Ubuntu 22.04 and the 11.x cuda tool kit
8. Move the file from downloads to the home and run the following commands in the terminal using file name:
   ```
   sudo dpkg -i cudnn-local-repo-ubuntu2204-8.9.2.26_1.0-1_amd64.deb

   ```
9.  Create a virtual enviroment
    ```
    sudo apt-get install python3-venv
    python3 -m venv paguer
    source paguer/bin/activate
    ```

10. Install TensorFlow
    ```
    pip install tensorflow==2.12
    ```

11. Test TensorFlow and GPU support
    
    Create a Python file named test_gpu.py and paste the following code:
    ```
    import tensorflow as tf

    # Check TensorFlow version
    print(f"TensorFlow version: {tf.__version__}")

    # Check GPU availability
    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        try:
            for gpu in gpus:
                tf.config.experimental.set_memory_growth(gpu, True)
            logical_gpus = tf.config.experimental.list_logical_devices('GPU')
            print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
        except RuntimeError as e:
            print(e)
    else:
        print("No GPUs detected.")

    # Run a simple TensorFlow operation
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    print(f"MNIST data loaded. Train size: {len(x_train)}, Test size: {len(x_test)}")
    ```

    Save the file, and in the terminal, run the following command to execute the script:

    ```
    python test_gpu.py
    ```

    If everything is installed correctly, you should see the TensorFlow version, GPU availability information, and the loaded MNIST data.

## JupyterLab Installation
1. Check if python is installed
      ```
   python3 --version
   ```
   Result:
   ```
   Python 3.10.12
   ```
2. Install JupyterLab
   ```
   pip3 install jupyterlab
   ```

## Sionna Installation
1. Install the package using pip
   ```
   pip install sionna
   ```

2. Test the installation in Python
   ```
   python
   ```
   ```
    >>> import sionna
    >>> print(sionna.__version__)
    0.16.2
   ```
3. Once Sionna is installed, run the [Sionna "Hello, World!" example](https://nvlabs.github.io/sionna/examples/Hello_World.html)