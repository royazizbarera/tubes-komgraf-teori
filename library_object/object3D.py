import bpy

from importlib import reload


import library_object.modifier
import library_object.aditional_utility as au
import library_object.material
import library_object.animation
import library_object.texture

reload(library_object.modifier)
reload(au)
reload(library_object.material)
reload(library_object.animation)
reload(library_object.texture)

from library_object.modifier import Modifier
from library_object.material import Material
from library_object.animation import Animation
from library_object.texture import Texture


class Object3D:
    def __init__(self, name='obj_script', location=(0,0,0), scale=(1, 1, 1), rotation=(0, 0, 0), new_object = None):
        ''''''
        # Initial variable
        if new_object is not None:
            self.name = new_object.name_full
            self.location = new_object.location
            self.scale = new_object.scale
            self.rotation = new_object.rotation_euler
            self.object = new_object
        else:
            self.name = name
            self.location = location
            self.scale = scale
            self.rotation = rotation
            self.object = None
        # self.scene = bpy.context.scene
        self.modifier = Modifier(self)
        self.material = Material(self)
        self.texture = Texture(self)
        self.animation = Animation(self)

    ''' Start Object Method '''

    def create_object(self, obj=None):
        ''''''
        if obj is None:
            obj = bpy.context.object
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
        
        ''' Rotation '''

    def set_rotation(self, rotation=(None, None, None)):
        ''''''
        temp_rotation = list(self.rotation)
        for i in range(3):
            if rotation[i] is not None:
                temp_rotation[i] = rotation[i]
        self.rotation = tuple(temp_rotation)
        self.object.rotation_euler = self.rotation
        
    def set_location(self, location=(None, None, None)):
        au.deactivate_all()
        au.deselect_all()
        self.activate_object()
        temp_location = list(self.location)
        for i in range(3):
            if location[i] is not None:
                temp_location[i] = location[i]
        self.location = tuple(temp_location)
        self.object.location = self.location
        

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

    def set_shadow_mode(self, mode='NONE'):
        '''Set shadow mode'''
        # self.object.data.shadow = mode
        self.object.active_material.shadow_method = mode
        
    def limit_rotation(self, x=False, y=False, z=False, min_x=0, max_x=0, min_y=0, max_y=0, min_z=0, max_z=0):
        '''Limit rotation'''
        au.deactivate_all()
        au.activate_object(self.object)
        bpy.ops.object.constraint_add(type='LIMIT_ROTATION')
        self.object.constraints["Limit Rotation"].use_limit_x = x
        self.object.constraints["Limit Rotation"].use_limit_y = y
        self.object.constraints["Limit Rotation"].use_limit_z = z
        self.object.constraints["Limit Rotation"].min_x = min_x
        self.object.constraints["Limit Rotation"].max_x = max_x
        self.object.constraints["Limit Rotation"].min_y = min_y
        self.object.constraints["Limit Rotation"].max_y = max_y
        self.object.constraints["Limit Rotation"].min_z = min_z
        self.object.constraints["Limit Rotation"].max_z = max_z
        au.deactivate_all()