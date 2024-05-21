import bpy

class Modifier:
    def __init__(self, object):
        self.self_object = object

    def add_subdivision_surface(self, levels: int, render_levels: int):
        self.self_object.select_object()
        self.self_object.activate_object()
        bpy.ops.object.modifier_add(type='SUBSURF')
        self.self_object.object.modifiers["Subdivision"].levels = levels
        self.self_object.object.modifiers["Subdivision"].render_levels = render_levels

        return self.self_object.object
