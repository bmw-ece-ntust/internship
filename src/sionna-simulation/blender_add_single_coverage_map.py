"""
This module loads a Blender scene, adds a new plane to the scene, and assigns an image texture to the plane.

Modules:
    - bpy: Blender Python API for manipulating scenes and objects.
    - os: Operating system interfaces for file path management.
    - sys: System-specific parameters and functions.
    - argparse: Command-line argument parsing.

Functions:
    - load_scene(file_path)
    - add_plane()
    - assign_image_to_plane(plane, image_path)
"""

import os
import sys
import bpy
import argparse

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

def add_plane():
    """
    Create a new plane by duplicating the 'Ground' object and moving it upwards along the Z-axis.

    Returns
    -------
    bpy.types.Object
        The newly created plane object.

    Raises
    ------
    AttributeError
        If the 'Ground' object is not found in the scene.
    """
    ground = bpy.data.objects.get("Ground")
    if not ground:
        raise AttributeError("Ground object not found.")
    
    # Duplicate the 'Ground' object
    plane = ground.copy()
    plane.data = ground.data.copy()  # Copy mesh data to keep it independent
    bpy.context.collection.objects.link(plane)
    
    plane.name = "Plane"
    plane.location.z += 10
    
    print(f"New plane '{plane.name}' created, translated 10 units up on the Z-axis.")
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
    
    material = bpy.data.materials.new(name="Image_Material")
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

def main(file_path, image_path, step):
    """Main function to load scene, add a plane, and assign image."""
    load_scene(file_path)
    
    plane = add_plane()
    
    assign_image_to_plane(plane, image_path)
    
    # Save the updated Blender scene
    root, _ = os.path.splitext(file_path)
    new_file_path = f"{root}_step{step}.blend"
    print(f"Saving scene to {new_file_path}")
    bpy.ops.wm.save_as_mainfile(filepath=new_file_path)

def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Blender scene loading and plane manipulation script.")
    parser.add_argument('--input_blend', required=True, type=str, help="Path to the Blender file to load.")
    parser.add_argument('--image_path', required=True, type=str, help="Path to the image to assign to the plane.")
    parser.add_argument('--step', required=False, type=str, default=0, help="Step identifier for output file naming.")
    
    argv = sys.argv
    if "--" in argv:
        argv = argv[argv.index("--") + 1:]
    
    return parser.parse_args(argv)

if __name__ == "__main__":
    args = parse_args()
    main(args.input_blend, args.image_path, args.step)
