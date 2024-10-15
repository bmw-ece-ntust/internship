"""
This module provides functionality to randomly add cubes to a Blender scene, 
group them, and save the updated scene.

Modules:
    - bpy: Blender Python API for scene and object manipulation.
    - os: Operating system interfaces.
    - random: Random number generation.
    - mathutils.Vector: Vector operations for 3D object positioning.
    - argparse: Command-line argument parsing.
    - sys: System-specific parameters and functions.

Functions:
    - load_scene(file_path)
    - get_ground_min_max()
    - add_random_cubes(min_pos, max_pos, num_cubes)
    - group_cubes()
"""

import bpy
import os
import random
from mathutils import Vector
import argparse
import sys

# Argument parser
def parse_args():
    parser = argparse.ArgumentParser(description="Add random cubes to the scene.")
    parser.add_argument('--num_cubes', type=int, default=5, help='Number of cubes to add')
    parser.add_argument('--input_blend', type=str, required=True, help='Input Blender file path')
    parser.add_argument('--output_blend', type=str, required=True, help='Output Blender file path')
    
    argv = sys.argv
    if "--" not in argv:
        argv = []
    else:
        argv = argv[argv.index("--") + 1:]
    return parser.parse_args(argv)


def load_scene(file_path):
    """
    Load a Blender scene from the specified file path, replacing the current scene.

    Parameters
    ----------
    file_path : str
        The path to the Blender file (.blend) to load.

    Returns
    -------
    None
        Loads the specified scene in Blender, clearing the current scene first.
    """
    # Clear existing scene
    bpy.ops.wm.read_factory_settings(use_empty=True)
    
    # Load the scene from the file
    bpy.ops.wm.open_mainfile(filepath=file_path)
    print(f"Scene loaded from {file_path}")

def get_ground_min_max():
    """
    Get the minimum and maximum positions of the "Ground" object's bounding box.

    Returns
    -------
    tuple of Vector
        A tuple containing two Vector objects: the minimum and maximum corners 
        of the bounding box in world coordinates.

    Raises
    ------
    AttributeError
        If the "Ground" object is not found in the scene.
    """
    ground = bpy.data.objects.get("Ground")
    if not ground:
        raise AttributeError("Ground object not found in the scene.")
    
    bbox_corners = [ground.matrix_world @ Vector(corner) for corner in ground.bound_box]
    min_pos = Vector((min(v.x for v in bbox_corners), min(v.y for v in bbox_corners), min(v.z for v in bbox_corners)))
    max_pos = Vector((max(v.x for v in bbox_corners), max(v.y for v in bbox_corners), max(v.z for v in bbox_corners)))
    return min_pos, max_pos

def add_random_cubes(min_pos, max_pos, num_cubes):
    """
    Add random cubes to the Blender scene within the bounds of the specified positions.

    Parameters
    ----------
    min_pos : mathutils.Vector
        The minimum (x, y, z) coordinates within which cubes should be placed.
    max_pos : mathutils.Vector
        The maximum (x, y, z) coordinates within which cubes should be placed.
    num_cubes : int
        The number of cubes to add to the scene.

    Returns
    -------
    None
        Adds cubes at random locations in the scene, assigning them the "itu_metal" material.
    
    Raises
    ------
    AttributeError
        If the "itu_metal" material is not found in the scene.
    """
    material = bpy.data.materials.get("itu_metal")
    if material is None:
        raise AttributeError("Material 'itu_metal' not found.")
    
    for i in range(num_cubes):
        x = random.uniform(min_pos.x, max_pos.x)
        y = random.uniform(min_pos.y, max_pos.y)
        z = random.uniform(min_pos.z, max_pos.z) + 8.0
        bpy.ops.mesh.primitive_cube_add(size=15.0, location=(x, y, z))
        cube = bpy.context.object
        cube.name = f"Cube_{i}"
        if cube.data.materials:
            cube.data.materials[0] = material
        else:
            cube.data.materials.append(material)
        print(f"Added cube {cube.name} at location ({x}, {y}, {z}) with material 'itu_metal'")

def group_cubes():
    """
    Group all cubes with names starting with "Cube_" into a new collection called "Cubes."

    Returns
    -------
    None
        Groups all cubes into a new collection called "Cubes" in the current Blender scene.
    """
    cubes_collection = bpy.data.collections.new("Cubes")
    bpy.context.scene.collection.children.link(cubes_collection)
    for obj in bpy.context.scene.objects:
        if obj.name.startswith("Cube_"):
            for collection in obj.users_collection:
                collection.objects.unlink(obj)
            cubes_collection.objects.link(obj)
    print("Grouped all cubes into the 'Cubes' collection.")

# Main execution
if __name__ == "__main__":
    args = parse_args()
    # Load the input scene
    load_scene(args.input_blend)
    
    min_pos, max_pos = get_ground_min_max()
    margin = Vector([20, 20, 0])
    min_pos += margin
    max_pos -= margin
    add_random_cubes(min_pos, max_pos, args.num_cubes)
    group_cubes()
    
    # Save the scene
    bpy.ops.wm.save_as_mainfile(filepath=args.output_blend)
