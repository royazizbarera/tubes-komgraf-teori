# from math import radians
# import os
# import sys
# import bpy
# from importlib import reload


# currentdir = os.path.dirname(os.path.realpath(__file__))
# sys.path.append(currentdir)
# # ===================================


# import library_object.aditional_utility as au
# import custom_object.sun
# import library_object.empty
# import library_object.plane
# import custom_object.moon


# reload(au)
# reload(library_object.plane)
# reload(library_object.empty)
# reload(custom_object.sun)
# reload(custom_object.moon)

# # ===================================
# from custom_object.sun import Sun
# from library_object.empty import Empty
# from library_object.plane import Plane
# from custom_object.moon import Moon

# tinggi_matahari = 700
# tinggi_bulan = ((tinggi_matahari)-(tinggi_matahari//3))*-1
# au.delete_all()
# plane = Plane('alas', scale=(100, 100, 1))
# poros = Empty(name='poros')
# sun = Sun(name='sun', scale=(50, 50, 50), location=(0, 0, tinggi_matahari))
# sun.sun.became_the_child_of(poros.object)
# moon = Moon(name='moon', scale=(20, 20, 20), location=(0, 0, tinggi_bulan), rotation=(radians(180), 0, 0))
# moon.moon.became_the_child_of(poros.object)
# # poros.set_rotation((radians(-90), None, None))

# def poros_animation():
#     au.deactive_all()
#     min_frame = 1
#     max_frame = 360*2
#     initial_rotate = 90
#     bpy.context.scene.frame_start = min_frame
#     bpy.context.scene.frame_end = max_frame

#     # Animasi
#     frame_per_rotate = 360
#     # rotate_times = 2

#     # start animation
#     bpy.context.scene.tool_settings.use_keyframe_insert_auto = True

#     # for i in range(rotate_times):
#     poros.set_rotation((radians(initial_rotate), 0, 0))
#     poros.animation.keyframe_insert(data_path="rotation_euler", frame=min_frame)
    
#     poros.set_rotation((radians(frame_per_rotate+initial_rotate), 0, 0))
#     poros.animation.keyframe_insert(data_path="rotation_euler", frame=max_frame)

#     bpy.context.scene.tool_settings.use_keyframe_insert_auto = False

#     bpy.ops.screen.animation_play()


# def main():
#     poros_animation()


# if __name__ == '__main__':
#     main()

import os
import sys
from importlib import reload


currentdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdir)
# ===================================


import custom_object.environment
import custom_object.wahana.ferris_wheel

reload(custom_object.environment)
reload(custom_object.wahana.ferris_wheel)

# ===================================
from custom_object.environment import Environment
from custom_object.wahana.ferris_wheel import FerrisWheel

def main():
    env = Environment()
    env.animation()
    '''Test aja'''  
    # from library_object.aditional_utility import delete_all
    # delete_all()
    fw = FerrisWheel()
    fw.animation()
    
    env.play_animation()

if __name__ == '__main__':
    main()
