from math import radians
import os
import sys
import bpy
from importlib import reload


currentdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdir)
# ===================================


import custom_object.sun
import library_object.uv_sphere
import library_object.empty
import library_object.plane
import import_object.import_object
import library_object.new_object
import library_object.cube
import library_object.aditional_utility as au


reload(library_object.cube)
reload(au)
reload(library_object.new_object)
reload(import_object.import_object)
reload(library_object.plane)
reload(library_object.empty)
reload(library_object.uv_sphere)
reload(custom_object.sun)

# ===================================
from custom_object.sun import Sun
from library_object.empty import Empty
from library_object.plane import Plane
from import_object.import_object import import_object_obj
from library_object.new_object import NewObject
from library_object.cube import Cube

au.delete_all()
plane = Plane('alas', scale=(100, 100, 1))
poros = Empty(name='poros')
sun = Sun(name='sun', scale=(50, 50, 50), location=(0, 0, 500))
sun.sun.became_the_child_of(poros.object)


def poros_animation():
    au.deactive_all()
    min_frame = 1
    max_frame = 360
    bpy.context.scene.frame_start = min_frame
    bpy.context.scene.frame_end = max_frame

    # Animasi
    frame_per_rotate = 360
    # rotate_times = 2

    # start animation
    bpy.context.scene.tool_settings.use_keyframe_insert_auto = True

    # for i in range(rotate_times):
    poros.set_rotation((0, 0, 0))
    poros.animation.keyframe_insert(data_path="rotation_euler", frame=min_frame)
    poros.set_rotation((radians(frame_per_rotate), 0, 0))
    poros.animation.keyframe_insert(data_path="rotation_euler", frame=max_frame)

    bpy.context.scene.tool_settings.use_keyframe_insert_auto = False

    bpy.ops.screen.animation_play()


def main():
    poros_animation()


if __name__ == '__main__':
    main()
