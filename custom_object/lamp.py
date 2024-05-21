import bpy

import custom_object.aditional_utility
import custom_object.object3D
import custom_object.aditional_utility as au

from importlib import reload
reload(custom_object.object3D)
reload(custom_object.aditional_utility)

from custom_object.object3D import Object3D


class Lamp(Object3D):
    def __init__(self, name='lamp', lamp_type='POINT', energy=1000, color=(1, 1, 1, 1), shadow=False, location=(0, 0, 0), scale=(1, 1, 1), rotation=(0, 0, 0)):
        self.lamp_type = lamp_type
        self.energy = energy
        self.color = color
        self.shadow = shadow
        super().__init__(name, location, scale, rotation)
        self.create_object()
        
    def create_object(self):
        bpy.ops.object.light_add(
            type=self.lamp_type,
        )
        super().create_object(
            bpy.context.object,
        )
        self.object = bpy.context.object
        self.object.data.energy = self.energy
        bpy.context.object.data.color = (1, 0.752942, 0.0595115)
        # self.object.data.color = self.color
        # self.object.data.shadow = self.shadow