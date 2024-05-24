import bpy



class Animation:
    def __init__(self, object):
        self.self_object = object

    def keyframe_insert(self, data_path, frame):
        '''Keyframe insert'''
        '''
        Options about data_path
        - location
        - rotation_euler
        - scale
        '''
        self.self_object.object.keyframe_insert(
            data_path=data_path, frame=frame)

    def frame_set(self, frame):
        self.self_object.scene.frame_set(frame)