# ===================================
from math import radians
import os
import sys
import bpy
from importlib import reload


currentdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdir)
# ===================================

import custom_object.aditional_utility as au
import custom_object.cube
import custom_object.new_object
import import_object.import_object
import custom_object.plane
import custom_object.empty
import custom_object.uv_sphere
import custom_object.sun

reload(custom_object.cube)
reload(custom_object.aditional_utility)
reload(custom_object.new_object)
reload(import_object.import_object)
reload(custom_object.plane)
reload(custom_object.empty)
reload(custom_object.uv_sphere)
reload(custom_object.sun)

from custom_object.cube import Cube
from custom_object.new_object import NewObject
from import_object.import_object import import_object_obj
from custom_object.plane import Plane
from custom_object.empty import Empty
from custom_object.sun import Sun


au.delete_all()
plane = Plane('alas',scale=(100,100,1))
poros = Empty(name='poros')
sun = Sun(name='sun', scale=(50,50,50), location=(0,0,500))
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
    poros.keyframe_insert(data_path="rotation_euler", frame=min_frame)
    print(poros.rotation)
    poros.set_rotation((radians(frame_per_rotate), 0, 0))
    poros.keyframe_insert(data_path="rotation_euler", frame=max_frame)

    bpy.context.scene.tool_settings.use_keyframe_insert_auto = False

    bpy.ops.screen.animation_play()

def main():
    poros_animation()
    
if __name__ == '__main__':
    main()