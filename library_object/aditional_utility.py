import bpy

def delete_all():
    '''
    Menghapus semua object di scene
    '''
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

def deactivate_all():
    '''
    Deactive semua objek di scene
    '''
    for obj in bpy.context.scene.objects:
        obj.select_set(False)
    bpy.context.view_layer.objects.active = None


def deselect_all():
    '''
    Deselect semua objek di scene
    '''
    bpy.ops.object.select_all(action='DESELECT')


def clear_mesh():
    '''
    Menghapus semua object yang aktif \n
    Contoh penggunaan: clear()
    '''
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()


def set_parameter_new_object(obj, name, location, scale, rotation):
    '''
    Menambahkan parameter pada objek baru
    '''
    obj.name = name
    obj.location = location
    obj.scale = scale
    obj.rotation_euler = rotation
    return obj


def activate_object(context_obj):
    ''''''
    bpy.context.view_layer.objects.active = context_obj


def activate_object_by_name(name):
    ''''''
    bpy.context.view_layer.objects.active = bpy.data.objects[name]


def select_object(context):
    context.select_set(True)
    
def select_object_by_name(name):
    bpy.data.objects[name].select_set(True)

def get_object_by_name(name):
    ''''''
    return bpy.data.objects[name]


def set_parameter_new_object(obj, name, location, scale, rotation):
    obj.name = name
    obj.location = location
    obj.scale = scale
    obj.rotation_euler = rotation
    return obj


'''
Utility untuk mengaktifkan dan memilih object
'''


def deselect_all():
    '''
    Deselect all objects in the scene.
    '''
    bpy.ops.object.select_all(action='DESELECT')


def select_object(context):
    context.select_set(True)


def select_object_by_name(name):
    bpy.data.objects[name].select_set(True)


def deactive_all():
    '''
    Deactive all objects in the scene.
    '''
    for obj in bpy.context.scene.objects:
        obj.select_set(False)


def set_active_object(context_obj):
    bpy.context.view_layer.objects.active = context_obj


def set_active_object_by_name(name):
    bpy.context.view_layer.objects.active = bpy.data.objects[name]


def change_name(obj, name):
    obj.name = name


def set_limit_rotation(obj, x=False, y=False, z=False):
    deactive_all()
    set_active_object(obj)
    bpy.ops.object.constraint_add(type='LIMIT_ROTATION')
    bpy.context.object.constraints["Limit Rotation"].use_limit_x = x
    bpy.context.object.constraints["Limit Rotation"].use_limit_y = y
    bpy.context.object.constraints["Limit Rotation"].use_limit_z = z
    deactive_all()


'''
=================================================
'''


def _set_parent_actived_object():
    bpy.ops.object.parent_set(type='OBJECT', keep_transform=False)


def parent_objects(parent_obj, child_objs: list, name=None):
    '''
    Parenting object \n
    '''
    if name is not None:
        parent_obj.name = name
    deactive_all()
    set_active_object(parent_obj)
    select_object(parent_obj)
    for child_obj in child_objs:
        select_object(child_obj)
    _set_parent_actived_object()
    deactive_all()
    return parent_obj


def parent_objects_inverted(parent_obj, child_obj):
    child_obj.parent = parent_obj
    child_obj.matrix_parent_inverse = parent_obj.matrix_world.inverted()
    bpy.context.view_layer.update()


def parent_objects_empty(child_objs: list, name=None):
    '''
    Masih error
    '''
    empty_cube = create_empty_cube(
        name, (0, 0, 0), scale=(1, 1, 1), rotation=(0, 0, 0))
    set_active_object(empty_cube)
    for child_obj in child_objs:
        select_object(child_obj)
    bpy.ops.object.parent_no_inverse_set(keep_transform=True)


def join_objects(objs, name=None):
    '''
    Menggabungkan objek objek dengan nama tertentu 
    dan yang akan dijadikan parent adalah objek pertama \n
    '''
    if name is not None:
        objs[0].name = name
    set_active_object(objs[0])
    for obj in objs:
        obj.select_set(True)
    bpy.ops.object.join()
    return objs[0]


'''
=================================================
'''


def get_object_by_name(name):
    return bpy.data.objects[name]


def create_empty_cube(name, location, scale=(1, 1, 1), rotation=(0, 0, 0)):
    '''
    Membuat object empty cube \n
    Contoh penggunaan: create_empty_cube(name='parent_alas', location=(0, -8.5, 10), scale=(1, 0.5, 10))
    '''
    bpy.ops.object.empty_add(type='CUBE', align='WORLD', location=location)
    return set_parameter_new_object(bpy.context.object, name, location, scale, rotation)


def duplicate_object(obj):
    '''
    Menduplikasi object \n
    Contoh penggunaan: duplicate_object(obj=alas.object, name='alas', location=(0, -8.5, 10), scale=(1, 0.5, 10))
    '''
    deactive_all()
    deselect_all()
    obj.select_set(True)
    activate_object(obj)
    bpy.ops.object.duplicate()
    return bpy.context.object