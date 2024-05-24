from math import radians
import bpy
from importlib import reload

import library_object.aditional_utility as au
import custom_object.sun
import library_object.empty
import library_object.plane
import custom_object.moon

reload(au)
reload(library_object.plane)
reload(library_object.empty)
reload(custom_object.sun)
reload(custom_object.moon)

from custom_object.sun import Sun
from library_object.empty import Empty
from library_object.plane import Plane
from custom_object.moon import Moon

class Environment:
    def __init__(self):
        self.sun_color = (1, 0.880267, 0.06236, 1)
        self.moon_color = (0.8, 0.8, 0.8, 1)
        self.sun_color_at_sunrise = (1, 0.2, 0.0, 1)
        self.sun_color_at_sunset = (1, 0.2, 0.0, 1)
        self.tinggi_matahari = 700
        self.tinggi_bulan = ((self.tinggi_matahari) - (self.tinggi_matahari // 3)) * -1
        au.delete_all()
        self.plane = Plane('alas', scale=(300, 300, 1))
        self.poros = Empty(name='poros_enviroment')
        self.sun_object = Sun(name='sun', color=self.sun_color, scale=(50, 50, 50), location=(0, 0, self.tinggi_matahari))
        self.moon_object = Moon(name='moon', color=self.moon_color, scale=(20, 20, 20), location=(0, 0, self.tinggi_bulan), rotation=(radians(180), 0, 0))
        
        self.sun_object.sun.became_the_child_of(self.poros.object)
        self.moon_object.moon.became_the_child_of(self.poros.object)

    def animation(self):
        au.deactive_all()
        min_frame = 1
        max_frame = 360 * 2
        initial_rotate = 90
        bpy.context.scene.frame_start = min_frame
        bpy.context.scene.frame_end = max_frame

        frame_per_rotate = 360

        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True

        ''' Rotasi poros'''
        # Set rotasi awal
        self.poros.set_rotation((radians(initial_rotate), 0, 0))
        self.poros.animation.keyframe_insert(data_path="rotation_euler", frame=min_frame)
        # Set rotasi akhir
        self.poros.set_rotation((radians(frame_per_rotate + initial_rotate), 0, 0))
        self.poros.animation.keyframe_insert(data_path="rotation_euler", frame=max_frame)

        ''' Color sun '''
        # Tambahkan keyframe untuk warna matahari saat matahari terbit
        bpy.context.scene.frame_set((max_frame - (max_frame // 2)))
        self.sun_object.lamp.object.data.color = self.sun_color_at_sunrise[:3]
        self.sun_object.lamp.object.data.keyframe_insert(data_path="color", frame=(max_frame - (max_frame // 2)))
        
        # Tambahkan keyframe untuk warna matahari saat matahari ditengah
        bpy.context.scene.frame_set((max_frame - (max_frame // 4)))
        self.sun_object.lamp.object.data.color = self.sun_color[:3]
        self.sun_object.lamp.object.data.keyframe_insert(data_path="color", frame=(max_frame - (max_frame // 4)))

        # Tambahkan keyframe untuk warna matahari saat matahari terbenam
        bpy.context.scene.frame_set(max_frame)
        self.sun_object.lamp.object.data.color = self.sun_color_at_sunset[:3]
        self.sun_object.lamp.object.data.keyframe_insert(data_path="color", frame=(max_frame))

        
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = False

    def play_animation(self):
        bpy.ops.screen.animation_play()