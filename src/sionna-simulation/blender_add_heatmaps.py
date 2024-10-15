"""
This module adds multiple planes to a Blender scene and assigns images as textures to each plane.

Modules:
    - bpy: Blender Python API for manipulating scenes and objects.
    - os: Operating system interfaces for file path management.
    - sys: System-specific parameters and functions.
    - argparse: Command-line argument parsing.

Functions:
    - load_scene(file_path)
    - add_plane(base_plane, index)
    - assign_image_to_plane(plane, image_path)
"""

import bpy
import os
import sys
import argparse

def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Add multiple planes with images in Blender.")
    parser.add_argument('--num_planes', type=int, default=5, help='Number of planes to add.')
    parser.add_argument('--output_blend', type=str, required=True, help='Output Blender file path.')
    
    argv = sys.argv
    if "--" in argv:
        argv = argv[argv.index("--") + 1:]
    
    return parser.parse_args(argv)


def load_scene(file_path):
    """
    Load the Blender scene from the specified file path.

    Parameters
    ----------
    file_path : str
        Path to the Blender file (.blend) to load.

    Returns
    -------
    None
        Loads the specified scene in Blender.

    Raises
    ------
    FileNotFoundError
        If the specified Blender file does not exist.
    """
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None
    bpy.ops.wm.open_mainfile(filepath=file_path)
    print(f"Scene loaded from {file_path}")

def add_plane(base_plane, index):
    """
    Create a new plane by duplicating the base plane and moving it upwards along the Z-axis.

    Parameters
    ----------
    base_plane : bpy.types.Object
        The plane object to duplicate.
    index : int
        The index of the plane, used to set its name and position.

    Returns
    -------
    bpy.types.Object
        The newly created plane object, offset on the Z-axis.
    """
    # Duplicate the base plane ('Ground' object or similar)
    plane = base_plane.copy()
    plane.data = base_plane.data.copy()  # Copy mesh data to keep it independent
    bpy.context.collection.objects.link(plane)
    
    plane.name = f"Plane_{index}"
    plane.location.z += (index + 1) * 0.1  # Slightly offset on the Z-axis for each plane
    
    print(f"New plane '{plane.name}' created, translated 0.1 units up on the Z-axis.")
    return plane

def assign_image_to_plane(plane, image_path):
    """
    Assign a new material with an image texture to the given plane.

    Parameters
    ----------
    plane : bpy.types.Object
        The plane to which the image texture will be assigned.
    image_path : str
        Path to the image file to use as the texture.

    Returns
    -------
    bpy.types.Image
        The image that is loaded and applied as a texture on the plane.

    Raises
    ------
    FileNotFoundError
        If the image file does not exist at the specified path.
    """
    img = bpy.data.images.load(image_path)
    
    material = bpy.data.materials.new(name=f"Image_Material_{plane.name}")
    material.use_nodes = True
    
    # Get the Principled BSDF node and add a texture image node
    bsdf = material.node_tree.nodes["Principled BSDF"]
    tex_image = material.node_tree.nodes.new('ShaderNodeTexImage')
    tex_image.image = img
    
    # Link the image texture color output to the BSDF base color input
    material.node_tree.links.new(bsdf.inputs['Base Color'], tex_image.outputs['Color'])
    
    if plane.data.materials:
        plane.data.materials[0] = material  # Replace existing material
    else:
        plane.data.materials.append(material)  # Add new material if none exists
    
    print(f"Assigned image {image_path} to plane {plane.name}")
    return img

def main(num_planes, output_blend):
    """
    Main function to add multiple planes to the Blender scene and assign images to them.

    Parameters
    ----------
    num_planes : int
        The number of planes to add to the scene.
    output_blend : str
        The file path where the updated Blender scene will be saved.

    Raises
    ------
    AttributeError
        If the "Ground" object is not found in the scene.
    """
    ground = bpy.data.objects.get("Ground")
    if not ground:
        raise AttributeError("Ground object not found.")

    # Add multiple planes and assign images to them
    for i in range(num_planes):
        plane = add_plane(ground, i)
        image_path = f"/home/center/Documents/teep/sionna_coverage_{i}.png"  # Replace with the actual image path
        assign_image_to_plane(plane, image_path)
    
    # Save the updated Blender scene
    print(f"Saving scene to {output_blend}")
    bpy.ops.wm.save_as_mainfile(filepath=output_blend)

if __name__ == "__main__":
    args = parse_args()
    main(args.num_planes, args.output_blend)
