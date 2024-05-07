import bpy
# from math import radians

def _set_parameter_new_object(obj_context, name, location, scale, rotation):
    obj_context.name = name
    obj_context.location = location
    obj_context.scale = scale
    obj_context.rotation_euler = rotation
    return obj_context

def create_plane(name, location, size=2, scale=(10, 10, 10), rotation=(0, 0, 0)):
    '''
    Membuat object plane \n
    Contoh penggunaan: create_plane(name='alas', location=(0, 0, 0), size=2, scale=(10, 10, 10))
    '''
    bpy.ops.mesh.primitive_plane_add(
        size=size, enter_editmode=False, align='WORLD')
    return _set_parameter_new_object(bpy.context.object, name, location, scale, rotation)

def create_cube(name, location, size=2, scale=(1, 1, 1), rotation=(0, 0, 0)):
    '''
    Membuat object cube \n
    Contoh penggunaan: create_cube(name='tihang_kiri', location=(0, -8.5, 10), size=2, scale=(1, 0.5, 10))
    '''
    bpy.ops.mesh.primitive_cube_add(
        size=size, enter_editmode=False, align='WORLD', location=location)
    return _set_parameter_new_object(bpy.context.object, name, location, scale, rotation)

def create_cylinder(name, location, radius=1, depth=2, scale=(1, 1, 1), rotation=(0, 0, 0)):
    '''
    Membuat object cylinder \n
    Contoh penggunaan: create_cylinder(name='tihang_utama', location=(0, 0, 19), scale=(0.250, 0.250, 8))
    '''
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=32, radius=radius, depth=depth, end_fill_type='NGON', align='WORLD', location=location)
    return _set_parameter_new_object(bpy.context.object, name, location, scale, rotation)

