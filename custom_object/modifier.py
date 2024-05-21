




import bpy

from custom_object.object3D import Object3D

class Modifier:
    def __init__(self, object):
        self.obj = object
        
    def add_subdivision_surface(self, levels: int, render_levels: int):
        self.obj.select_object()
        self.obj.activate_object()
        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.context.object.modifiers["Subdivision"].levels = levels
        bpy.context.object.modifiers["Subdivision"].render_levels = render_levels
        
        return self.obj