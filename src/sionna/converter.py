import xml.etree.ElementTree as ET
import os

# Load the Mitsuba XML file
tree = ET.parse('data/blender/2F_solid.xml')
root = tree.getroot()

# Iterate over all 'shape' elements
for shape in root.findall(".//shape"):
    filename_element = shape.find("./string[@name='filename']")
    
    if filename_element is not None:
        filename = filename_element.attrib['value']
        base_name = os.path.splitext(os.path.basename(filename))[0]

        # Update id and name attributes
        shape.set('id', base_name)
        shape.set('name', base_name)

# Save the updated XML file
tree.write('data/blender/2F_solid.xml')
