import os
import sys

import bpy


if len(sys.argv) < 5:
    raise ValueError("No files are provided.\nThis should never run without files!")


# Remove the default cube, camera and light
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()
bpy.ops.object.select_by_type(type='LIGHT')
bpy.ops.object.delete()
bpy.ops.object.select_by_type(type='CAMERA')
bpy.ops.object.delete()

obj_files = sys.argv[4].split(";")

for obj_file in obj_files:
    if not os.path.exists(obj_file):
        print("The given file does not exist: {}\nSkipping it.".format(obj_file))
        continue

    # Import the OBJ file
    bpy.ops.import_scene.obj(filepath=obj_file)
    # Update the scene to reflect the changes
    bpy.context.view_layer.update()
