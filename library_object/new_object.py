
from importlib import reload  # top
import library_object.object3D  # top

reload(library_object.object3D)  # mid
from library_object.object3D import Object3D



class NewObject(Object3D):
    def __init__(self, name, object, location, scale=(1, 1, 1), rotation=(0, 0, 0)):
        super().__init__(name, location, scale, rotation)
        super().create_object(object)
