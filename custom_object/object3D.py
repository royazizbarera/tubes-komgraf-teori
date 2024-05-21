import bpy

import custom_object.lamp
import custom_object.modifier
import custom_object.aditional_utility

from importlib import reload
reload(custom_object.lamp)
reload(custom_object.modifier)
reload(custom_object.aditional_utility)

import custom_object.aditional_utility as au
from custom_object.lamp import Lamp
from custom_object.modifier import Modifier


class Object3D:
    def __init__(self, name, location, scale=(1, 1, 1), rotation=(0, 0, 0)):
        ''''''
        # Initial variable
        self.name = name
        self.location = location
        self.scale = scale
        self.rotation = rotation
        self.object = None
        self.modifier = Modifier(
            self.object,
        )

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

    def became_the_child_of(self, parent_obj):
        ''''''
        au.deactivate_all()
        if parent_obj is str:
            au.activate_object_by_name(parent_obj)
        else:
            au.activate_object(parent_obj)
        self.select_object()
        bpy.ops.object.parent_no_inverse_set(keep_transform=True)
        
    def create_emission_material(self, material_name='emission_material', emission_color=(1, 1, 1, 1), strength=1):
        # Create a new material
        mat = bpy.data.materials.new(name=material_name)
        mat.use_nodes = True

        # Clear default nodes
        nodes = mat.node_tree.nodes
        for node in nodes:
            nodes.remove(node)

        # Create emission node
        emission_node = nodes.new(type='ShaderNodeEmission')
        emission_node.inputs['Color'].default_value = emission_color
        emission_node.inputs['Strength'].default_value = strength

        # Create output node
        output_node = nodes.new(type='ShaderNodeOutputMaterial')
        
        # Link nodes
        mat.node_tree.links.new(emission_node.outputs['Emission'], output_node.inputs['Surface'])

        # Assign material to object
        if self.object.data.materials:
            self.object.data.materials[0] = mat
        else:
            self.object.data.materials.append(mat)
        
        bpy.context.scene.eevee.use_bloom = True
        
    def shade_smooth(self):
        '''Shade Smooth'''
        au.deselect_all()
        self.select_object()
        bpy.ops.object.shade_smooth()
        
    def add_lamp_inside(self, name='lamp', lamp_type='POINT', energy=1000, color=(1, 1, 1, 1), shadow=False):
        '''Add lamp inside object'''
        # au.deselect_all()
        # au.deactivate_all()
        lamp = Lamp(name, lamp_type, energy, color, shadow, self.location, self.scale, self.rotation)
        lamp.became_the_child_of(self.object)
        return lamp