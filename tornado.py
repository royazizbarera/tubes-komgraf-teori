import bpy
from math import radians


def parent_objects(parent_obj, child_obj):
    """
    Set one object as the parent of another.
    """
    # Simpan posisi global sebelum objek menjadi parent
    global_position_child_obj = child_obj.matrix_world.translation
    child_obj.parent = parent_obj
    child_obj.matrix_world.translation = global_position_child_obj


def clear_scene():
    '''
    '''
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()


def create_plane(name, location, size=2, scale=(10, 10, 10), rotation=(0, 0, 0)):
    bpy.ops.mesh.primitive_plane_add(
        size=size, enter_editmode=False, align='WORLD', location=location)
    plane_object = bpy.context.object
    plane_object.name = name
    plane_object.scale = scale
    plane_object.rotation_euler = rotation
    return plane_object


def create_cube(name, location, size=2, scale=(1, 1, 1), rotation=(0, 0, 0)):
    bpy.ops.mesh.primitive_cube_add(
        size=size, enter_editmode=False, align='WORLD', location=location)
    cube_object = bpy.context.object
    cube_object.name = name
    cube_object.scale = scale
    cube_object.rotation_euler = rotation
    return cube_object


def create_cylinder(name, location, radius=1, depth=2, scale=(1, 1, 1), rotation=(0, 0, 0)):
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=32, radius=radius, depth=depth, end_fill_type='NGON', align='WORLD', location=location)
    cylinder_object = bpy.context.object
    cylinder_object.name = name
    cylinder_object.scale = scale
    cylinder_object.rotation_euler = rotation
    return cylinder_object


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
        # obj.hide_set(True)\


def set_limit_rotation(obj, x=False, y=False, z=False):
    deactive_all()
    set_active_object(obj)
    bpy.ops.object.constraint_add(type='LIMIT_ROTATION')
    bpy.context.object.constraints["Limit Rotation"].use_limit_x = x
    bpy.context.object.constraints["Limit Rotation"].use_limit_y = y
    bpy.context.object.constraints["Limit Rotation"].use_limit_z = z
    deactive_all()


def parent_objects(parent_obj, child_objs):
    deactive_all()
    set_active_object(parent_obj)
    select_object(parent_obj)
    for child_obj in child_objs:
        select_object(child_obj)
    set_parent_actived_object()
    deactive_all()
    return parent_obj


def set_active_object(context_obj):
    bpy.context.view_layer.objects.active = context_obj


def set_parent_actived_object():
    bpy.ops.object.parent_set(type='OBJECT', keep_transform=False)


def change_name(obj, name):
    obj.name = name


def join_objects(context_objs, name=None):
    """
    Join multiple objects into one.
    """
    if name is not None:
        context_objs[0].name = name
    set_active_object(context_objs[0])
    for obj in context_objs:
        obj.select_set(True)
    bpy.ops.object.join()
    return context_objs[0]


def create():
    '''
    '''
    # Pondasi
    # Alas
    alas = create_plane(name='alas', location=(
        0, 0, 0), size=2, scale=(10, 10, 10))
    tihang_kiri = create_cube(name='tihang_kiri', location=(
        0, -8.5, 10), size=2, scale=(1, 0.5, 10))
    tihang_kanan = create_cube(name='tihang_kanan', location=(
        0, 8.5, 10), size=2, scale=(1, 0.5, 10))
    
    # Join alas, tihang_kiri, tihang_kanan
    alas = join_objects([alas, tihang_kiri, tihang_kanan], name='alas')

    # Tihang utama
    tihang_kiri_atas = create_cube(name='tihang_kiri_atas', location=(
        0, -7.5, 19), size=2, scale=(1, 0.5, 10), rotation=(radians(0), radians(90), radians(0)))
    tihang_kanan_atas = create_cube(name='tihang_kanan_atas', location=(
        0, 7.5, 19), size=2, scale=(1, 0.5, 10), rotation=(radians(0), radians(90), radians(0)))
    tihang_utama = create_cylinder(name='tihang_utama', location=(0, 0, 19), scale=(
        0.250, 0.250, 8), rotation=(radians(-90), radians(0), radians(0)))

    # Join tihang_kiri_atas, tihang_kanan_atas, tihang_utama
    tihang_utama = join_objects([tihang_kiri_atas, tihang_kanan_atas, tihang_utama], name='tihang_utama')

    # # Menjadikan parent object
    # tihang_kiri_atas.select_set(True)
    # tihang_kanan_atas.select_set(True)
    # tihang_utama.select_set(True)
    # bpy.ops.object.parent_set(type='OBJECT', keep_transform=False)

    # Kursi
    tihang_kursi = create_cylinder(name='tihang_kursi', location=(9, 0, 19), scale=(
        0.250, 0.250, 8), rotation=(radians(-90), radians(0), radians(0)))
    kursi1 = create_cube(name='kursi1', location=(10, -5, 19))
    kursi2 = create_cube(name='kursi2', location=(10, -2.5, 19))
    kursi3 = create_cube(name='kursi3', location=(10, 0, 19))
    kursi4 = create_cube(name='kursi4', location=(10, 2.5, 19))
    kursi5 = create_cube(name='kursi5', location=(10, 5, 19))

    kursi = join_objects(
        [tihang_kursi, kursi1, kursi2, kursi3, kursi4, kursi5], name='kursi')
    # parent_objects(tihang_kursi, [kursi])

    # parent_objects(alas, [tihang_kiri, tihang_kanan])

    set_limit_rotation(kursi, y=True, z=True)

    parent_objects(tihang_utama, [kursi])
    
    
    # set_active_object(tihang_utama)
    
    
    # bpy.context.scene.frame_current = 1
    # bpy.context.scene.frame_start = 1
    # bpy.context.scene.frame_end = 180
    # bpy.context.scene.frame_current = 1
    # bpy.context.scene.tool_settings.use_keyframe_insert_auto = True
    # bpy.ops.transform.rotate(value=-1.5708, orient_axis='Y', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
    # bpy.context.scene.frame_end = 180
    # bpy.context.scene.frame_current = 180
    # bpy.ops.transform.rotate(value=-4.71239, orient_axis='Y', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)



def animate():
    
    bpy.context.scene.frame_current = 1
    bpy.context.scene.frame_start = 1
    bpy.context.scene.frame_end = 180
    bpy.context.scene.frame_current = 1
    bpy.context.scene.tool_settings.use_keyframe_insert_auto = True
    bpy.ops.transform.rotate(value=-1.5708, orient_axis='Y', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
    bpy.context.scene.frame_end = 180
    bpy.context.scene.frame_current = 180
    bpy.ops.transform.rotate(value=-4.71239, orient_axis='Y', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)


def main():
    clear_scene()
    create()


main()
