import bpy
import library_object.aditional_utility as au
# Import the model into Blender


def import_object_obj(file_path):
    au.deactivate_all()
    au.deselect_all()
    bpy.ops.import_scene.obj(filepath=file_path)
    return bpy.context.object
