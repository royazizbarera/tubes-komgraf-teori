import bpy

import library_object.object3D

from importlib import reload
reload(library_object.object3D)

from library_object.object3D import Object3D



class Circle(Object3D):
    def __init__(self, name, vertices=20, location=(0, 0, 0), scale=(1, 1, 1), rotation=(0, 0, 0)):
        self.vertices = vertices
        super().__init__(name, location, scale, rotation)
        self.create_object()

    def create_object(self):
        bpy.ops.mesh.primitive_circle_add(
            vertices=self.vertices,
            enter_editmode=False,
            align='WORLD',
        )
        super().create_object(
            bpy.context.object,
        )
        # super().create_object()
