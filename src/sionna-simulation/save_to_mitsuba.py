"""
This module provides functionality to load a Blender scene and export it to Mitsuba format.

Modules:
    - bpy: Blender Python API for manipulating scenes and exporting files.
    - argparse: Command-line argument parsing.

Functions:
    - load_scene(file_path)
"""
import sys
import bpy     
import argparse 

def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Save scene to Mitsuba.")
    parser.add_argument('--input_blend', type=str, required=True, help='Input Blender file path')
    parser.add_argument('--output_mitsuba', type=str, required=True, help='Output Mitsuba file path')
    return parser.parse_args(argv if argv else sys.argv[sys.argv.index("--") + 1:])
 

def load_scene(file_path):
    """
    Load a Blender scene from the specified file path.

    Parameters
    ----------
    file_path : str
        The file path to the input Blender (.blend) file.

    Returns
    -------
    None
        The Blender file is loaded into the current session.

    Raises
    ------
    FileNotFoundError
        If the specified Blender file does not exist or cannot be opened.
    """
    bpy.ops.wm.open_mainfile(filepath=file_path)
    print(f"Scene loaded from {file_path}")


if __name__ == "__main__":
    args = parse_args() 
    print("Loading scene...")
    load_scene(args.input_blend)


    bpy.ops.preferences.addon_enable(module="mitsuba-blender")
    bpy.context.scene.render.engine = 'CYCLES' 
    #active_addons = bpy.context.preferences.addons.keys()

    try:
        # Ensure Mitsuba export is available and configured properly
        bpy.ops.export_scene.mitsuba(filepath=args.output_mitsuba)
    except Exception as e:
        print(f"Failed to export scene to Mitsuba: {e}")
    finally:
        print(f"Scene exported to Mitsuba at {args.output_mitsuba}")
        bpy.ops.wm.quit_blender()