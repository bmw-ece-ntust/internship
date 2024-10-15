# Simulation Process Workflow
## Overview

The simulation script (`simulation.py`) orchestrates a series of steps to create a 3D scene with coverage maps for wireless network analysis. It integrates Blender for 3D modeling, Sionna for wireless network simulation, and various custom scripts for data processing and visualization.

## Workflow Steps

1. **Scene Preparation**
   - Loads a base Blender scene
   - Adds random cubes to simulate obstacles

2. **Wireless Coverage Computation**
   - Converts the Blender scene to Mitsuba format
   - Uses Sionna to compute coverage maps

3. **Visualization**
   - Adds coverage maps to the 3D scene
   - Creates a 3D mesh representation of the coverage data

4. **Export**
   - Saves the final scene in Blender and USD formats

## Configuration Options

The main script accepts the following command-line arguments:

- `--num_cubes`: Number of random cubes to add to the scene (default: 10)
- `--coverage_type`: Type of coverage map to display
  - `individual`: Shows separate coverage maps for each transmitter
  - `combined`: Shows a single combined coverage map (default)

## User Configuration Guide

1. **Environment Setup**
   - Ensure Blender, Sionna, and required Python libraries are installed
   - Set the `ROOT` variable in `simulation.py` to your project directory

2. **Input Data**
   - Prepare the base Blender scene (`2F_no_solid.blend`)
   - Create a CSV file with transmitter locations (`transformed_data.csv`)

3. **Running the Simulation**
   - Execute the script: `python simulation.py [options]`
   - Example: `python simulation.py --num_cubes 15 --coverage_type individual`

4. **Output**
   - Blender files: `output_scene.blend`, `output_scene_with_3d_mesh.blend`
   - Mitsuba file: `output_scene.xml`
   - USD file: `output_scene_with_3d_mesh.usdc`
   - Coverage maps: `sionna_coverage_*.png`

## Customization

- Modify `BLEND_FILE_PATH` to use a different base scene
- Adjust the `correct_orientation` function in `save_to_mitsuba.py` to change object orientations
- Modify coverage map generation parameters in `sionna_coverage_map.py`

## Troubleshooting

- Ensure all file paths in `simulation.py` are correct for your system
- Check Blender and Sionna versions for compatibility
- Verify that the `mitsuba-blender` addon is enabled in Blender


## Note
If you are using Sionna 0.19, the coverage map is no longer an iterable containing all the coverage maps for every access point (AP). This means you can now retrieve the signal information for all APs at once, without needing to manually combine them, as was required in version 0.18.

There is a script available that handles the scenario where you want to include multiple coverage maps in a Blender file. While the script is not fully tested, it should adequately cover the basic workflow for this procedure.

We've explored ways to work directly with Omniverse instead, but it's complicated for two main reasons. First, the file conversions between Sionna and Omniverse—despite both being from NVIDIA—use different file formats, making it inconvenient to switch between them frequently. Second, creating materials in Omniverse is quite complex, whereas Blender makes this process much easier.

The workflow we have worked with, is to use Blender for everything related to 3D modeling, and Sionna for signal modeling. The results can then be exported to USD files, allowing you to use Omniverse for more advanced simulations once the environment is fully set up.