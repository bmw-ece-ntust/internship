"""
This module generates a simulation step by adding cubes, computing coverage maps,
and saving the scene to various file formats.

Modules:
    - argparse: Command-line argument parsing.
    - subprocess: Running external commands.
    - os: Operating system dependent functionality.
    - csv: CSV file reading.
    - xml.etree.ElementTree: XML parsing and creation.

Constants:
    - ROOT: Root directory for file paths.
    - Various file paths for Blender, CSV, and output files.

Functions:
    - correct_orientation(file_path)
    - run_blender_script(script_path, arguments)
"""

import argparse
import subprocess
import os
import csv

import xml.etree.ElementTree as ET

# Define root and file paths
ROOT = "/home/center/Documents/teep"

BLEND_FILE_PATH = os.path.join(ROOT, "data/blender/2F_no_solid.blend")
TRANSMITTER_FILE = os.path.join(ROOT, "transformed_data.csv")
MITSUBA_FILE_PATH = os.path.join(ROOT, "data/blender/2F_no_solid.xml")
OUTPUT_BLEND_PATH = os.path.join(ROOT, "output_scene.blend")
OUTPUT_MITSUBA_PATH = os.path.join(ROOT, "output_scene.xml")
OUTPUT_BLEND_PATH_3D = os.path.join(ROOT, "output_scene_with_3d_mesh.blend")
OUTPUT_USD_PATH_3D = os.path.join(ROOT, "output_scene_with_3d_mesh.usdc")
OUTPUT_GLB_PATH_3D = os.path.join(ROOT, "output_scene_with_3d_mesh.glb")

parser = argparse.ArgumentParser(description="Generate a simulation step.")
parser.add_argument('--num_cubes', type=int, default=10, help='Number of cubes to add')
parser.add_argument('--coverage_type', choices=['individual', 'combined'], default='combined', help='Type of coverage map to display')
args = parser.parse_args()

def correct_orientation(file_path):
    """
    Correct the orientation of objects in the specified XML file.

    This function modifies the XML structure by adjusting the rotation
    and translation properties of shapes within the file.

    Parameters
    ----------
    file_path : str
        The path to the XML file to modify.

    Returns
    -------
    None
        The XML file is modified in place.

    Raises
    ------
    FileNotFoundError
        If the specified file does not exist or cannot be read.
    """
    tree = ET.parse(file_path)
    root = tree.getroot()

    rotates = [
        {"axis": "x", "angle": "90"},
        {"axis": "y", "angle": "0"},
        {"axis": "z", "angle": "-90"},
    ]

    for shape in root.findall(".//shape"):
        # Rename the shape
        filename_element = shape.find("./string[@name='filename']")
        if filename_element is not None:
            filename = filename_element.attrib['value']
            base_name = os.path.splitext(os.path.basename(filename))[0]
            shape.set('id', f"{base_name}")
            shape.set('name', f"{base_name}")

        # Remove existing transform if present
        existing_transform = shape.find('transform')
        if existing_transform is not None:
            shape.remove(existing_transform)

        # Create new transform
        transform = ET.Element('transform')
        transform.set('name', 'to_world')

        # Add rotate elements
        for rotate_info in rotates:
            rotate = ET.Element('rotate')
            rotate.set(rotate_info['axis'], "1")
            rotate.set('angle', rotate_info['angle'])
            transform.append(rotate)

        # Add translate element
        translate = ET.Element('translate')
        translate.set('value', "0 0 0")
        transform.append(translate)

        # Insert the new transform as the first child of the shape
        shape.insert(0, transform)

    tree.write(file_path, encoding='utf-8', xml_declaration=True)

def run_blender_script(script_path, arguments):
    """
    Run a Blender script with the specified arguments.

    Parameters
    ----------
    script_path : str
        The file path to the Blender script to execute.

    arguments : list of str
        A list of command-line arguments to pass to the Blender script.

    Returns
    -------
    None
        The script is executed as a background process.

    Raises
    ------
    subprocess.CalledProcessError
        If the Blender script execution fails.
    """
    cmd = [
        "blender36",
        "--background",
        "--python", script_path,
        "--"
    ] + arguments
    subprocess.run(cmd, check=True)

def main():
    print("Step 1: Adding random cubes to the scene...")
    run_blender_script(
        os.path.join(ROOT, "omni/blender_add_cubes.py"),
        [
            "--num_cubes", str(args.num_cubes),
            "--input_blend", BLEND_FILE_PATH,
            "--output_blend", OUTPUT_BLEND_PATH,
        ]
    )

    print(f"Added {args.num_cubes} random cubes to the scene")

    cmd = [
        "blender36",
        "--python-expr", "import bpy; bpy.context.scene.render.engine = 'CYCLES'",
        "--python", os.path.join(ROOT, "omni/save_to_mitsuba.py"),
        "--",
        "--input_blend", OUTPUT_BLEND_PATH,
        "--output_mitsuba", OUTPUT_MITSUBA_PATH
    ] 

    subprocess.run(cmd, check=False, text=True)

    # Correct orientation of the Mitsuba file
    correct_orientation(OUTPUT_MITSUBA_PATH)

    print("Step 2: Computing coverage maps...")
    subprocess.run([
        "python", os.path.join(ROOT, "omni/sionna_coverage_map.py"),
        "--mitsuba_file", OUTPUT_MITSUBA_PATH,
        "--transmitter_file", TRANSMITTER_FILE,
        "--output_dir", ROOT
    ], check=True)

    transmitters = str(sum(1 for _ in csv.reader(open(TRANSMITTER_FILE))))

    print("Step 3: Adding coverage maps to the scene...")
    if args.coverage_type == 'individual':
        run_blender_script(
            os.path.join(ROOT, "omni/blender_add_heatmaps.py"),
            ["--num_planes", transmitters, "--output_blend", OUTPUT_BLEND_PATH]
        )
    else:  
        run_blender_script(
            os.path.join(ROOT, "omni/blender_add_single_coverage_map.py"),
            ["--input_blend", OUTPUT_BLEND_PATH, 
            "--image_path", os.path.join(ROOT, "sionna_coverage_full_map.png")]
        )

    print("Step 4: Creating 3D mesh from heatmap...")
    run_blender_script(
        os.path.join(ROOT, "omni/blender_add_3d_heatmap.py"),  
        [
            "--input_blend", OUTPUT_BLEND_PATH, 
            "--output_file", OUTPUT_BLEND_PATH_3D, 
            "--image_path", os.path.join(ROOT, "sionna_coverage_full_map.png"), 
        ]
    )

    print("Step 5: Saving the final scene to USD")
    run_blender_script(
        os.path.join(ROOT, "omni/convert_to_usd.py"),  
        [
            "--input_blend", OUTPUT_BLEND_PATH_3D, 
            "--output_file", OUTPUT_USD_PATH_3D, 
        ]
    )

    print("Step 6: Saving the final scene to GLB")
    run_blender_script(
        os.path.join(ROOT, "omni/convert_to_glb.py"),  
        [
            "--input_blend", OUTPUT_BLEND_PATH_3D, 
            "--output_file", OUTPUT_GLB_PATH_3D, 
        ]
    )
    print("Simulation step completed successfully.")

if __name__ == "__main__":
    main()
