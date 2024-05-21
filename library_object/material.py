import bpy

class Material:
    def __init__(self, object):
        self.self_object = object

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
        mat.node_tree.links.new(
            emission_node.outputs['Emission'], output_node.inputs['Surface'])

        # Assign material to object
        if self.self_object.object.data.materials:
            self.self_object.object.data.materials[0] = mat
        else:
            self.self_object.object.data.materials.append(mat)

        bpy.context.scene.eevee.use_bloom = True
