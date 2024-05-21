# ===================================
import os
import sys
from importlib import reload

currentdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdir)
# ===================================
import custom_object.cube
import custom_object.aditional_utility
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
from custom_object.aditional_utility import delete_all
from custom_object.new_object import NewObject
from import_object.import_object import import_object_obj
from custom_object.plane import Plane
from custom_object.empty import Empty
from custom_object.sun import Sun

def craete_object():
    delete_all()
    plane = Plane('alas',scale=(100,100,1))
    poros = Empty(name='poros')
    sun = Sun(name='sun', scale=(50,50,50), location=(0,0,100))
    sun.sun.became_the_child_of(poros.object)

def animation():
    pass

def main():
    craete_object()
    animation()
    
if __name__ == '__main__':
    main()