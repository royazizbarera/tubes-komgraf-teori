import bpy

import library_object.object3D

from importlib import reload
reload(library_object.object3D)

from library_object.object3D import Object3D



class Cube(Object3D):
    def __init__(self, name, size=2, location=(0, 0, 0), scale=(1, 1, 1), rotation=(0, 0, 0)):
        self.size = size
        super().__init__(name, location, scale, rotation)
        self.create_object()

    def create_object(self):
        '''
        Membuat object cube \n
        Contoh penggunaan: create_cube(name='tihang_kiri', location=(0, -8.5, 10), size=2, scale=(1, 0.5, 10))
        '''
        bpy.ops.mesh.primitive_cube_add(
            size=self.size,
            enter_editmode=False,
            align='WORLD',
        )
        super().create_object(
            bpy.context.object,
        )
        # super().create_object()
