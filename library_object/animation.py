import bpy



class Animation:
    def __init__(self, object):
        self.self_object = object

    def keyframe_insert(self, data_path, frame):
        '''Keyframe insert'''
        self.self_object.object.keyframe_insert(
            data_path=data_path, frame=frame)
