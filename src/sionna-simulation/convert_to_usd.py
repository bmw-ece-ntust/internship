"""
This module provides functionality to convert Blender (.blend) files to USD (.usd) format.

Modules:
    - bpy: Blender Python API for manipulating scenes and exporting files.
    - os: Operating system interfaces for file path management.
    - sys: System-specific parameters and functions.
    - argparse: Command-line argument parsing.

Functions:
    - convert_blend_to_usd(blend_file_path, usd_file_path)
"""
import sys
import os
import bpy
import argparse

def convert_blend_to_usd(blend_file_path, usd_file_path):
    """
    Convert a .blend file to .usd format using Blender's USD export functionality.

    Parameters
    ----------
    blend_file_path : str
        The file path to the input Blender (.blend) file.
    usd_file_path : str
        The file path where the output USD (.usd) file should be saved.

    Returns
    -------
    None
        The Blender file is loaded, and the USD file is exported to the specified location.

    Raises
    ------
    FileNotFoundError
        If the specified Blender file does not exist.
    """
    bpy.ops.wm.open_mainfile(filepath=blend_file_path)
    bpy.ops.wm.usd_export(filepath=usd_file_path)
    print(f"Exported {blend_file_path} to {usd_file_path}")

def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Convert a .blend file to .usd format")
    parser.add_argument('--input_blend', type=str, required=True, help="Path to the input .blend file")
    parser.add_argument('--output_file', type=str, required=True, help="Path to save the output .usd file")
    return parser.parse_args(argv if argv else sys.argv[sys.argv.index("--") + 1:])

if __name__ == "__main__":
    args = parse_args()
    convert_blend_to_usd(args.input_blend, args.output_file)



