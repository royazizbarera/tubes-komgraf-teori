import bpy


class Modifier:
    def __init__(self, object_3d):
        self.object_3d = object_3d

    def add_subdivision_surface(self, levels: int, render_levels: int):
        self.object_3d.select_object()
        self.object_3d.activate_object()
        bpy.ops.object.modifier_add(type='SUBSURF')
        self.object_3d.object.modifiers["Subdivision"].levels = levels
        self.object_3d.object.modifiers["Subdivision"].render_levels = render_levels

        return self.object_3d.object
