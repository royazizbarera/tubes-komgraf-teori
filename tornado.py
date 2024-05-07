import bpy
from math import radians
import custom_object
import utility
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdir)


def create_tornado():
    '''
    Membuat wahana tornado
    '''
    # Pondasi
    # Alas
    alas = custom_object.create_plane(name='alas', location=(
        0, 0, 0), size=2, scale=(10, 10, 10))
    tihang_kiri = custom_object.create_cube(name='tihang_kiri', location=(
        0, -8.5, 10), size=2, scale=(1, 0.5, 10))
    tihang_kanan = custom_object.create_cube(name='tihang_kanan', location=(
        0, 8.5, 10), size=2, scale=(1, 0.5, 10))

    # Join alas, tihang_kiri, tihang_kanan
    alas = utility.join_objects([alas, tihang_kiri, tihang_kanan], name='alas')

    # Tihang utama
    tihang_kiri_atas = custom_object.create_cube(name='tihang_kiri_atas', location=(
        0, -7.5, 19), size=2, scale=(1, 0.5, 10), rotation=(radians(0), radians(90), radians(0)))
    tihang_kanan_atas = custom_object.create_cube(name='tihang_kanan_atas', location=(
        0, 7.5, 19), size=2, scale=(1, 0.5, 10), rotation=(radians(0), radians(90), radians(0)))
    tihang_utama = custom_object.create_cylinder(name='tihang_utama', location=(0, 0, 19), scale=(
        0.250, 0.250, 8), rotation=(radians(-90), radians(0), radians(0)))

    # Join tihang_kiri_atas, tihang_kanan_atas, tihang_utama
    tihang_utama = utility.join_objects(
        objs=[tihang_utama, tihang_kiri_atas, tihang_kanan_atas], name='tihang_utama')

    # Kursi
    tihang_kursi = custom_object.create_cylinder(name='tihang_kursi', location=(9, 0, 19), scale=(
        0.250, 0.250, 8), rotation=(radians(-90), radians(0), radians(0)))
    kursi1 = custom_object.create_cube(name='kursi1', location=(10, -5, 19))
    kursi2 = custom_object.create_cube(name='kursi2', location=(10, -2.5, 19))
    kursi3 = custom_object.create_cube(name='kursi3', location=(10, 0, 19))
    kursi4 = custom_object.create_cube(name='kursi4', location=(10, 2.5, 19))
    kursi5 = custom_object.create_cube(name='kursi5', location=(10, 5, 19))

    utility.parent_objects(
        tihang_kursi, [kursi1, kursi2, kursi3, kursi4, kursi5])
    kursi = utility.join_objects(
        objs=[tihang_kursi, kursi1, kursi2, kursi3, kursi4, kursi5], name='kursi')

    # Membuat ketika di rotasi dia tidak ikut rotasi
    utility.set_limit_rotation(kursi, x=False, y=False, z=False)

    # Parenting
    utility.parent_objects(tihang_utama, [kursi])


def animate_tornado():
    utility.deactive_all()
    min_frame = 1
    max_frame = 90
    bpy.context.scene.frame_start = min_frame
    bpy.context.scene.frame_end = max_frame

    # Animasi
    frame_per_rotate = 360
    rotate_times = 2

    for i in range(rotate_times):
        tihang_utama = utility.get_object_by_name('tihang_utama')
        tihang_utama.rotation_euler[1] = radians(frame_per_rotate)
        tihang_utama.keyframe_insert(
            data_path="rotation_euler", frame=max_frame)
        tihang_utama.rotation_euler[1] = radians(0)
        tihang_utama.keyframe_insert(
            data_path="rotation_euler", frame=min_frame)

        kursi = utility.get_object_by_name('kursi')
        kursi.rotation_euler[1] = radians(0)
        kursi.keyframe_insert(data_path="rotation_euler", frame=min_frame)
        kursi.rotation_euler[1] = radians(-1*frame_per_rotate)
        kursi.keyframe_insert(data_path="rotation_euler", frame=max_frame)

    bpy.ops.screen.animation_play()


def main():
    utility.clear_mesh()
    create_tornado()
    animate_tornado()


main()
