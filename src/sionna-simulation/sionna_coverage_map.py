"""
This module computes coverage maps using the Sionna library based on input Mitsuba and transmitter data.

Modules:
    - os: Provides a way to use operating system-dependent functionality.
    - csv: For reading CSV files containing transmitter data.
    - argparse: For command-line argument parsing.
    - numpy: For numerical operations and array handling.
    - PIL (Pillow): For image handling and saving.
    - tensorflow: For tensor operations and machine learning functionalities.
    - sionna.rt: Contains classes for defining the scene and transmitters.
    - matplotlib: For plotting and visualizing coverage maps.

Functions:
    - load_transmitters(filename)
    - imshow(self, metric="path_gain", scale_factor=10)
    - single_coverage_to_image(c, colormap='viridis')
"""
import os
import csv
import argparse
import numpy as np
from PIL import Image
import tensorflow as tf

from sionna.rt import Scene, Transmitter, PlanarArray

import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

parser = argparse.ArgumentParser(description="Compute coverage maps using Sionna.")
parser.add_argument('--mitsuba_file', type=str, required=True, help='Input Mitsuba file path')
parser.add_argument('--transmitter_file', type=str, required=True, help='Input Transmitter CSV file path')
parser.add_argument('--output_dir', type=str, required=True, help='Directory to save output images')
args = parser.parse_args()

def load_transmitters(filename):
    """
    Load transmitters from a CSV file.

    The CSV file is expected to contain rows with transmitter names and their coordinates.

    Parameters
    ----------
    filename : str
        The path to the CSV file containing transmitter data.

    Returns
    -------
    list of tuple
        A list of tuples where each tuple contains the name of the transmitter and its position as a list of [x, y, z].

    Raises
    ------
    FileNotFoundError
        If the specified file does not exist or cannot be read.
    ValueError
        If there are issues parsing the coordinates from the CSV.
    """
    transmitters = []
    with open(filename, "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            name = row[0]
            x, y, z = map(float, row[1:])
            transmitters.append((name, [x, y, z]))
    return transmitters

def imshow(self, metric="path_gain", scale_factor=10):
    """
    Visualize the coverage map.

    This function generates a plot of the coverage map using the specified metric.

    Parameters
    ----------
    self : object
        The coverage map object containing the metrics.

    metric : str, optional
        The coverage metric to visualize. Default is "path_gain".

    scale_factor : int, optional
        The scale factor for the figure size. Default is 10.

    Returns
    -------
    matplotlib.figure.Figure
        The figure object containing the visualized coverage map.

    Raises
    ------
    AttributeError
        If the specified metric is not found in the coverage map object.
    """
    import warnings
    cm = getattr(self, metric)
    cm = tf.reduce_max(cm, axis=0)
    with warnings.catch_warnings(record=True) as _:
        cm = 10. * np.log10(cm.numpy())
    cm = np.rot90(cm, k=3)

    base_width = cm.shape[1]
    base_height = cm.shape[0]
    dpi = 100 * scale_factor  

    fig_cm, ax = plt.subplots(figsize=(base_width / dpi, base_height / dpi), dpi=dpi)
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    ax.set_position([0, 0, 1, 1])

    ax.imshow(cm, origin='lower')
    ax.axis("off")

    return fig_cm

def single_coverage_to_image(c, colormap='viridis'):
    """
    Convert a coverage map to an image.

    This function transforms the coverage data into an image format for visualization.

    Parameters
    ----------
    c : numpy.ndarray
        The coverage map data to be converted to an image.

    colormap : str, optional
        The name of the colormap to use. Default is 'viridis'.

    Returns
    -------
    numpy.ndarray
        An array representing the image.

    Raises
    ------
    ValueError
        If the input coverage map is not in the expected format.
    """
    c_with_nan = np.where(c == 0, np.nan, c)
    cmap = plt.get_cmap(colormap)
    cmap.set_bad(color='white')
    fig, ax = plt.subplots()
    ax.axis('off')
    ax.imshow(c_with_nan, origin='lower', cmap=cmap, norm=Normalize(np.nanmin(c_with_nan), np.nanmax(c_with_nan)))
    fig.canvas.draw()
    image_array = np.array(fig.canvas.renderer.buffer_rgba())[:, :, :3]
    plt.close(fig)
    return image_array

if __name__ == "__main__":
    # Create the Sionna scene from the Mitsuba file
    sionna_scene = Scene(args.mitsuba_file)
    sionna_scene.frequency = 2.4e9
    
    # Load transmitters from the provided CSV file
    transmitters = load_transmitters(args.transmitter_file)
    for name, position in transmitters:
        tx = Transmitter(name=name, position=position)
        sionna_scene.add(tx)
    
    # Define the transmitter and receiver arrays
    sionna_scene.tx_array = PlanarArray(num_rows=4, num_cols=1, vertical_spacing=0.05, horizontal_spacing=0.05, pattern="iso", polarization="VH")
    sionna_scene.rx_array = PlanarArray(num_rows=1, num_cols=1, vertical_spacing=0.5, horizontal_spacing=0.5, pattern="dipole", polarization="VH")
    
    # Compute the coverage map
    cm = sionna_scene.coverage_map(max_depth=8)

    # Ensure the output directory exists
    os.makedirs(args.output_dir, exist_ok=True)

    combined_image_path = os.path.join(args.output_dir, "sionna_coverage_full_map.png")

    if hasattr(cm, 'as_tensor'):
        # For Sionna v0.18 
        for idx in range(cm.as_tensor().shape[0]):
            print("Processing coverage map index:", idx)

            # Get the coverage map for the current index and convert to image
            c = cm[idx]
            image_array = single_coverage_to_image(c)

            # Save the image as PNG for later use
            image_path = os.path.join(args.output_dir, f"sionna_coverage_{idx}.png")
            Image.fromarray(image_array).save(image_path)

        # Combine coverage maps from all transmitters
        combined_cm = tf.reduce_max(cm.as_tensor(), axis=0)
        combined_image_array = single_coverage_to_image(combined_cm.numpy())
        Image.fromarray(combined_image_array.astype(np.uint8)).save(combined_image_path)

    else:
        # For Sionna v0.19 
        import types
        cm.imshow = types.MethodType(imshow, cm)
        fig = cm.imshow()
        plt.savefig(combined_image_path, format='png')
