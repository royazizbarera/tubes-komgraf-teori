
# import library_object.circle

from importlib import reload

# reload(library_object.circle)

# from library_object.circle import Circle

import bpy
from math import radians

import import_object.import_object
import library_object.aditional_utility as au
from library_object.object3D import Object3D

reload(import_object.import_object)
reload(au)


from import_object.import_object import import_obj

class FerrisWheel:
    def __init__(self) -> None:
        self.create_object()
        pass
    
    def create_object(self):
        # ferris_wheel = import_object_obj('model/obj/ferris.obj')
        # NewObject('ferris_wheel', ferris_wheel, (0, 0, 0), (1, 1, 1), (0, 0, 0))
        import_obj(
            filepath="D:\\1Kuliah\\Semester 4\\Komputer Grafik\\Tubes Teori\\tornado\\model\\obj\\ferris\\ferris_wheel.obj", 
            directory="D:\\1Kuliah\\Semester 4\\Komputer Grafik\\Tubes Teori\\tornado\\model\\obj\\ferris\\", 
            files=[{"name":"ferris_wheel.obj", "name":"ferris_wheel.obj"}]
        )
        import_obj(
            filepath="D:\\1Kuliah\\Semester 4\\Komputer Grafik\\Tubes Teori\\tornado\\model\\obj\\ferris\\kabin_ferris_wheel.obj", 
            directory="D:\\1Kuliah\\Semester 4\\Komputer Grafik\\Tubes Teori\\tornado\\model\\obj\\ferris\\", 
            files=[{"name":"kabin_ferris_wheel.obj", "name":"kabin_ferris_wheel.obj"}]
        )
        au.deselect_all()
        au.deactivate_all()
        # poros_ferris_wheel = au.get_object_by_name('poros_ferris_wheel')
        # kabin_ferris_wheel = au.get_object_by_name('kabin_ferris_wheel')
        # tihang_ferris_wheel = au.get_object_by_name('tihang_ferris_wheel')
        # p = NewObject('poros_ferris_wheel_2', au.get_object_by_name('poros_ferris_wheel'), poros_ferris_wheel.location, poros_ferris_wheel.scale, poros_ferris_wheel.rotation_euler)
        self.poros_ferris_wheel = Object3D('poros_ferris_wheel', new_object=au.get_object_by_name('poros_ferris_wheel'))
        self.kabin_ferris_wheel = Object3D('kabin_ferris_wheel', new_object=au.get_object_by_name('kabin_ferris_wheel'))
        self.tihang_ferris_wheel = Object3D('tihang_ferris_wheel', new_object=au.get_object_by_name('tihang_ferris_wheel'))
        
        self.poros_ferris_wheel.became_the_child_of(self.tihang_ferris_wheel.object)
        
        self.create_kabin_ferris_wheel()
        self.tihang_ferris_wheel.set_location((0, 0, 30))
    
    def create_kabin_ferris_wheel(self):    
        # membuat kabin menjadi banyak mengelilingi poros dengan radius 20 menggunakan rumus lingkaran dengan maksimal 10 kabin
        self.kabin_ferris_wheel_1 = Object3D('kabin_ferris_wheel_1', new_object=au.duplicate_object(self.kabin_ferris_wheel.object))
        self.kabin_ferris_wheel_2 = Object3D('kabin_ferris_wheel_2', new_object=au.duplicate_object(self.kabin_ferris_wheel.object))
        self.kabin_ferris_wheel_3 = Object3D('kabin_ferris_wheel_3', new_object=au.duplicate_object(self.kabin_ferris_wheel.object))
        self.kabin_ferris_wheel_4 = Object3D('kabin_ferris_wheel_4', new_object=au.duplicate_object(self.kabin_ferris_wheel.object))
        self.kabin_ferris_wheel_5 = Object3D('kabin_ferris_wheel_5', new_object=au.duplicate_object(self.kabin_ferris_wheel.object))
        self.kabin_ferris_wheel_6 = Object3D('kabin_ferris_wheel_6', new_object=au.duplicate_object(self.kabin_ferris_wheel.object))
        self.kabin_ferris_wheel_7 = Object3D('kabin_ferris_wheel_7', new_object=au.duplicate_object(self.kabin_ferris_wheel.object))
        self.kabin_ferris_wheel_8 = Object3D('kabin_ferris_wheel_8', new_object=au.duplicate_object(self.kabin_ferris_wheel.object))
        self.kabin_ferris_wheel_9 = Object3D('kabin_ferris_wheel_9', new_object=au.duplicate_object(self.kabin_ferris_wheel.object))
        
        # set location kabin
        self.kabin_ferris_wheel.set_location((0, 0, 20))
        self.kabin_ferris_wheel_1.set_location((0, 11.7348, 16.1563))
        self.kabin_ferris_wheel_2.set_location((0, 18.7461, 6.1563))
        self.kabin_ferris_wheel_3.set_location((0, 18.9125, -5.86647))
        self.kabin_ferris_wheel_4.set_location((0, 11.7232, -15.8109))
        self.kabin_ferris_wheel_5.set_location((0, 0, -20))
        self.kabin_ferris_wheel_6.set_location((0, -11.5873, -15.7749))
        self.kabin_ferris_wheel_7.set_location((0, -18.8651, -5.86701))
        self.kabin_ferris_wheel_8.set_location((0, -18.793, 6.34669))
        self.kabin_ferris_wheel_9.set_location((0, -11.5513, 16.2185))
        
        # became the child of poros
        self.kabin_ferris_wheel.became_the_child_of(self.poros_ferris_wheel.object)
        self.kabin_ferris_wheel_1.became_the_child_of(self.poros_ferris_wheel.object)
        self.kabin_ferris_wheel_2.became_the_child_of(self.poros_ferris_wheel.object)
        self.kabin_ferris_wheel_3.became_the_child_of(self.poros_ferris_wheel.object)
        self.kabin_ferris_wheel_4.became_the_child_of(self.poros_ferris_wheel.object)
        self.kabin_ferris_wheel_5.became_the_child_of(self.poros_ferris_wheel.object)
        self.kabin_ferris_wheel_6.became_the_child_of(self.poros_ferris_wheel.object)
        self.kabin_ferris_wheel_7.became_the_child_of(self.poros_ferris_wheel.object)
        self.kabin_ferris_wheel_8.became_the_child_of(self.poros_ferris_wheel.object)
        self.kabin_ferris_wheel_9.became_the_child_of(self.poros_ferris_wheel.object)
        
        # set limit rotation
        self.kabin_ferris_wheel.limit_rotation( x=True, min_x=radians(90), max_x=radians(90) )
        self.kabin_ferris_wheel_1.limit_rotation( x=True, min_x=radians(90), max_x=radians(90) )
        self.kabin_ferris_wheel_2.limit_rotation( x=True, min_x=radians(90), max_x=radians(90) )
        self.kabin_ferris_wheel_3.limit_rotation( x=True, min_x=radians(90), max_x=radians(90) )
        self.kabin_ferris_wheel_4.limit_rotation( x=True, min_x=radians(90), max_x=radians(90) )
        self.kabin_ferris_wheel_5.limit_rotation( x=True, min_x=radians(90), max_x=radians(90) )
        self.kabin_ferris_wheel_6.limit_rotation( x=True, min_x=radians(90), max_x=radians(90) )
        self.kabin_ferris_wheel_7.limit_rotation( x=True, min_x=radians(90), max_x=radians(90) )
        self.kabin_ferris_wheel_8.limit_rotation( x=True, min_x=radians(90), max_x=radians(90) )
        self.kabin_ferris_wheel_9.limit_rotation( x=True, min_x=radians(90), max_x=radians(90) )
        
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
        self.poros_ferris_wheel.set_rotation((radians(initial_rotate), 0, 0))
        self.poros_ferris_wheel.animation.keyframe_insert(data_path="rotation_euler", frame=min_frame)
        # Set rotasi akhir
        self.poros_ferris_wheel.set_rotation((radians(frame_per_rotate + initial_rotate), 0, 0))
        self.poros_ferris_wheel.animation.keyframe_insert(data_path="rotation_euler", frame=max_frame)

        bpy.context.scene.tool_settings.use_keyframe_insert_auto = False

    def play_animation(self):
        bpy.ops.screen.animation_play()
