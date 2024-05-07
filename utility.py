import bpy

'''
Utility untuk menghapus object
'''

def clear_mesh():
    '''
    Menghapus semua object yang aktif \n
    Contoh penggunaan: clear()
    '''
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()


'''
Utility untuk mengaktifkan dan memilih object
'''


def deselect_all():
    """
    Deselect all objects in the scene.
    """
    bpy.ops.object.select_all(action='DESELECT')


def select_object(context):
    context.select_set(True)


def select_object_by_name(name):
    bpy.data.objects[name].select_set(True)


def deactive_all():
    """
    Deactive all objects in the scene.
    """
    for obj in bpy.context.scene.objects:
        obj.select_set(False)
        # obj.hide_set(True)


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


def join_objects(objs, name=None):
    """
    Menggabungkan objek objek dengan nama tertentu 
    dan yang akan dijadikan parent adalah objek pertama \n
    """
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