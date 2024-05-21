import bpy

from importlib import reload


import library_object.lamp
import library_object.modifier
import library_object.aditional_utility as au
import library_object.material
import library_object.animation

reload(library_object.lamp)
reload(library_object.modifier)
reload(au)
reload(library_object.material)
reload(library_object.animation)

from library_object.lamp import Lamp
from library_object.modifier import Modifier
from library_object.material import Material
from library_object.animation import Animation



class Object3D:
    def __init__(self, name, location, scale=(1, 1, 1), rotation=(0, 0, 0)):
        ''''''
        # Initial variable
        self.name = name
        self.location = location
        self.scale = scale
        self.rotation = rotation
        self.object = None
        self.modifier = Modifier(self)
        self.material = Material(self)
        self.animation = Animation(self)

    ''' Start Object Method '''

    def create_object(self, obj):
        ''''''
        self.object = au.set_parameter_new_object(
            obj=obj,
            name=self.name,
            location=self.location,
            scale=self.scale,
            rotation=self.rotation
        )

    def select_object(self):
        ''''''
        self.object.select_set(True)

    def deselect_object(self):
        ''''''
        self.object.select_set(False)

    def activate_object(self):
        ''''''
        bpy.context.view_layer.objects.active = self.object

    def deactivate_object(self):
        ''''''
        bpy.context.view_layer.objects.active = None

    def change_name(self, name):
        ''''''
        self.name = name
        self.object.name = name

    def set_rotation(self, rotation):
        ''''''
        self.rotation = rotation
        self.object.rotation_euler = rotation

    def became_the_child_of(self, parent_obj):
        ''''''
        au.deactivate_all()
        if parent_obj is str:
            au.activate_object_by_name(parent_obj)
        else:
            au.activate_object(parent_obj)
        self.select_object()
        bpy.ops.object.parent_no_inverse_set(keep_transform=True)

    def shade_smooth(self):
        '''Shade Smooth'''
        au.deselect_all()
        self.select_object()
        bpy.ops.object.shade_smooth()

    ''' End Object Method '''

    ''' Start Aditional Method '''

    def add_lamp_inside(self, name='lamp', lamp_type='POINT', energy=1000, color=(1, 1, 1, 1), shadow=False):
        '''Add lamp inside object'''
        # au.deselect_all()
        # au.deactivate_all()
        lamp = Lamp(name, lamp_type, energy, color, shadow,
                    self.location, self.scale, self.rotation)
        lamp.became_the_child_of(self.object)
        return lamp

    ''' End Aditional Method '''

    def set_shadow_mode(self, mode='NONE'):
        '''Set shadow mode'''
        # self.object.data.shadow = mode
        self.object.active_material.shadow_method = mode