import bpy
from importlib import reload


import library_object.object3D
import library_object.aditional_utility as au

reload(au)
reload(library_object.object3D)

from library_object.object3D import Object3D



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
        # temp_color = list(self.color)
        # temp_color.pop()
        # # bpy.context.object.data.color = (1, 0.752942, 0.0595115)
        # bpy.context.object.data.color = tuple(temp_color)
        bpy.context.object.data.color = self.color[:3]
        # self.object.data.color = self.color
        # self.object.data.shadow = self.shadow

    ''' set color '''
    def set_color(self, color):
        ''''''
        if len(color) == 4:
            self.object.data.color = self.color[:3]
        elif len(color) == 3:
            self.object.data.color = color
        self.color = color
        
    def set_strength(self, strength):
        self.object.data.energy = strength
        
    def set_max_distance(self, max_distance):
        self.object.data.shadow_cascade_max_distance = max_distance
        
    def set_distritution(self, distritution):
        self.object.data.shadow_cascade_exponent = 0
