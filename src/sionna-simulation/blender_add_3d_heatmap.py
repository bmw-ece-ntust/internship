"""
This module provides functionality for loading Blender scenes, creating 3D meshes
from heatmap images, and applying vertex color materials.

Modules:
    - math: Standard math operations.
    - sys: System-specific parameters and functions.
    - bpy: Blender Python API for 3D object manipulation.
    - os: Operating system interfaces.
    - numpy: Array and matrix operations for heightmap processing.
    - argparse: Command-line argument parsing.
    - PIL.Image: Image processing for heatmap loading.
    - matplotlib.pyplot: Plotting and colormap generation.

Functions:
    - load_scene(file_path)
    - create_color_gradient(z_value, z_min, z_max)
    - create_3d_mesh_from_height_map(height_map)
    - create_vertex_color_material(obj)
    - load_image_as_heatmap(image_path)
    - calculate_geometrical_center(vertices)
    - match_ground_dimensions(heatmap_obj, ground_obj)
"""

import math
import sys
import bpy
import os
import numpy as np
import argparse
from PIL import Image
import matplotlib.pyplot as plt  

def load_scene(file_path):
    """
    Load the Blender scene from the specified file path.

    Parameters
    ----------
    file_path : str
        The path to the Blender file (.blend) to load.

    Returns
    -------
    None
        Loads the scene in Blender and prints a confirmation message.
    
    Raises
    ------
    FileNotFoundError
        If the specified file path does not exist.
    """
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None
    bpy.ops.wm.open_mainfile(filepath=file_path)
    print(f"Scene loaded from {file_path}")

def create_color_gradient(z_value, z_min, z_max):
    """
    Map a z-value to an RGB color based on a purple-to-green-to-white gradient using
    the 'viridis' colormap.

    Parameters
    ----------
    z_value : float
        The height value (z-coordinate) to be mapped to a color.
    z_min : float
        The minimum z-value in the data range.
    z_max : float
        The maximum z-value in the data range.

    Returns
    -------
    tuple
        A tuple of three floats representing an RGB color (in the range 0-1).
    """
    if z_value == 0:
        return (0.267, 0.0049, 0.3294)  # Darkest color in the 'viridis' colormap
    norm_z = (z_value - z_min) / (z_max - z_min) 
    cmap = plt.get_cmap('viridis') 
    return cmap(norm_z)[:3]  # Get RGB from colormap, ignore alpha

def create_3d_mesh_from_height_map(height_map):
    """
    Create a 3D mesh from a height map and apply vertex colors based on the height values.

    Parameters
    ----------
    height_map : numpy.ndarray
        A 2D array representing the grayscale values of the height map image, where each
        pixel value corresponds to a height.

    Returns
    -------
    bpy.types.Object
        The Blender object representing the generated 3D mesh.
    """
    height, width = height_map.shape
    vertices = []
    faces = []
    vertex_colors = []
    
    z_min = np.min(height_map) / 255.0  
    z_max = np.max(height_map) / 255.0  

    # Create vertices based on the height map
    for y in range(height):
        for x in range(width):
            pixel_value = height_map[y, x]

            if pixel_value == 255: z = 0
            else: z = pixel_value / 255.0 

            flipped_y = height - 1 - y
            vertices.append((x, flipped_y, z))

            # Calculate color based on normalized height 
            color = create_color_gradient(z, z_min, z_max)
            vertex_colors.append(color)

    centroid = calculate_geometrical_center(vertices)
    vertices = [(x - centroid[0], y - centroid[1], z - centroid[2]) for x, y, z in vertices]

    # Create faces by connecting the vertices into a grid of quads
    for y in range(height - 1):
        for x in range(width - 1):
            v1 = x + y * width
            v2 = (x + 1) + y * width
            v3 = (x + 1) + (y + 1) * width
            v4 = x + (y + 1) * width
            faces.append((v1, v2, v3, v4))

    # Create a new mesh in Blender
    mesh = bpy.data.meshes.new("HeatmapMesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()

    # Create a new object in Blender and link the mesh to it
    obj = bpy.data.objects.new("HeatmapObject", mesh)
    bpy.context.collection.objects.link(obj)
    bpy.context.view_layer.objects.active = obj 
    bpy.ops.object.select_all(action='DESELECT')  
    obj.select_set(True)  # Select the newly created object

    # Add vertex colors to the mesh
    if not mesh.vertex_colors:
        mesh.vertex_colors.new()
    color_layer = mesh.vertex_colors.active
    for i, loop in enumerate(mesh.loops):
        color_layer.data[i].color = vertex_colors[loop.vertex_index] + (1.0,)  # Add alpha channel

    print(f"Created 3D mesh with {len(vertices)} vertices and {len(faces)} faces.")

    return obj

def create_vertex_color_material(obj):
    """
    Create a material that uses vertex colors and assign it to a Blender object.

    Parameters
    ----------
    obj : bpy.types.Object
        The Blender object to which the material will be applied.

    Returns
    -------
    None
        The material is created and assigned to the object, and a confirmation message is printed.
    """
    material = bpy.data.materials.new(name="VertexColorMaterial")
    material.use_nodes = True
    nodes = material.node_tree.nodes
    links = material.node_tree.links

    # Clear default nodes
    nodes.clear()

    # Create nodes
    node_vertex_color = nodes.new(type='ShaderNodeVertexColor')
    node_bsdf = nodes.new(type='ShaderNodeBsdfPrincipled')
    node_output = nodes.new(type='ShaderNodeOutputMaterial')

    # Link nodes
    links.new(node_vertex_color.outputs['Color'], node_bsdf.inputs['Base Color'])
    links.new(node_bsdf.outputs['BSDF'], node_output.inputs['Surface'])

    # Assign the material to the object
    if obj.data.materials:
        obj.data.materials[0] = material
    else:
        obj.data.materials.append(material)

    print(f"Created and assigned vertex color material to object {obj.name}")

def load_image_as_heatmap(image_path):
    """
    Load an image file and convert it into both color and grayscale (heightmap) versions.

    Parameters
    ----------
    image_path : str
        The path to the heatmap image file.

    Returns
    -------
    numpy.ndarray
        A 2D array representing the grayscale (heightmap) version of the image.
    """
    img_color = Image.open(image_path)
    img_gray = img_color.convert('L')
    heatmap_gray = np.array(img_gray)
    return heatmap_gray

def calculate_geometrical_center(vertices):
    """
    Calculate the geometrical center (centroid) of a set of vertices in 3D space.

    Parameters
    ----------
    vertices : list of tuple
        A list of 3D points (x, y, z) representing the vertices of the mesh.

    Returns
    -------
    numpy.ndarray
        A 1D array of three elements representing the (x, y, z) coordinates of the centroid.
    """
    vertex_sum = np.array([0.0, 0.0, 0.0])
    num_vertices = len(vertices)
    
    for vertex in vertices:
        vertex_sum += np.array(vertex)

    centroid = vertex_sum / num_vertices
    return centroid

def match_ground_dimensions(heatmap_obj, ground_obj):
    """
    Match the dimensions of the 3D heatmap object to the dimensions of a ground object.

    Parameters
    ----------
    heatmap_obj : bpy.types.Object
        The heatmap object to be scaled and positioned.
    ground_obj : bpy.types.Object
        The reference ground object whose dimensions the heatmap object should match.

    Returns
    -------
    None
        The heatmap object's dimensions are adjusted to match the ground object.
    """
    heatmap_obj.dimensions.z = 15
    heatmap_obj.scale.x = 10.154
    heatmap_obj.scale.y = 10.154
    heatmap_obj.scale.z = 50

    heatmap_obj.location.z = 20
    bpy.context.view_layer.objects.active = heatmap_obj
    bpy.ops.object.transform_apply(location=True, rotation=False, scale=True)
    print(f"Matched heatmap dimensions to ground object: {heatmap_obj.dimensions}")

def main(file_path, output_file, image_path):
    """
    Main function that loads a Blender scene, creates a 3D mesh from a heatmap image,
    applies vertex colors, and saves the updated Blender scene.

    Parameters
    ----------
    file_path : str
        Path to the input Blender file (.blend).
    output_file : str
        Path to save the updated Blender file.
    image_path : str
        Path to the heatmap image file used to create the 3D mesh.

    Returns
    -------
    None
        Loads the scene, creates the mesh, applies materials, and saves the updated scene.
    """
    load_scene(file_path)

    heatmap_gray = load_image_as_heatmap(image_path)
    
    heatmap_object = create_3d_mesh_from_height_map(heatmap_gray)
    
    create_vertex_color_material(heatmap_object)

    ground_obj = bpy.data.objects.get("Ground")
    if ground_obj:
        match_ground_dimensions(heatmap_object, ground_obj)
    else:
        print("Warning: 'Ground' object not found. Heatmap dimensions not adjusted.")

    bpy.ops.wm.save_as_mainfile(filepath=output_file)
    print(f"Saved the updated Blender scene to {output_file}")

def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Blender scene loading and 3D mesh creation from heatmap.")
    parser.add_argument('--input_blend', required=True, type=str, help="Path to the Blender file to load.")
    parser.add_argument('--output_file', required=True, type=str, help="Path to save the updated Blender file.")
    parser.add_argument('--image_path', required=True, type=str, help="Path to the heatmap image.")
    
    argv = sys.argv
    if "--" in argv:
        argv = argv[argv.index("--") + 1:]
    
    return parser.parse_args(argv)

if __name__ == "__main__":
    args = parse_args()
    main(args.input_blend, args.output_file, args.image_path)
