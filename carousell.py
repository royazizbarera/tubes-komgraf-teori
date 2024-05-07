import bpy
import math
import custom_object
import utility
from math import radians

class Seat():
    def __init__(self, location=(0, 0, 0)):
        self.location = location
        self.seat = None
        self.animation_offset = 0
        self.create_carousel()

    def create_carousel(self):
        '''
        Create carousel seat
        '''

        # Create seat (main body)
        horseBody = custom_object.create_cylinder(name='mainBody', location=(0, 0, 2), scale=(1, 1, 1),
                                                  rotation=(radians(0), radians(90), radians(0)))
        horseNeck = custom_object.create_cylinder(name="neck", location=(1.408, 0, 2.361), scale=(0.8, 0.9, 0.7),
                                                  rotation=(radians(0), radians(50), radians(0)))
        horseHead = custom_object.create_cylinder(name="head", location=(2.264, 0, 2.810), scale=(0.6, 0.7, 0.8),
                                                  rotation=(radians(0), radians(92.42), radians(0)))
        horseFoundation = custom_object.create_cylinder(name="foundation", location=(0, 0, -0.7), scale=(1, 0.5, 3),
                                                        rotation=(radians(0), radians(0), radians(0)))
        horseGrip = custom_object.create_cylinder(name="grip", location=(2.264, 0, 2.807), scale=(0.2, 0.3, 1.5),
                                                  rotation=(radians(0), radians(92.42), radians(-88.78)))
        horseHair = custom_object.create_cylinder(name="hair", location=(2.385, 0, 3.126), scale=(1, 0.1, 0.3),
                                                  rotation=(radians(0), radians(92.42), radians(0)))
        horseTail = custom_object.create_cylinder(name="tail", location=(-1.467, 0, 2.373),
                                                  scale=(0.707, 0.572, 0.616), rotation=(radians(0), radians(126.3),
                                                                                     radians(0)))
        horseFoot = custom_object.create_cylinder(name="footrest", location=(0, 0, -1), scale=(0.3, 0.9, 1),
                                                  rotation=(radians(-90), radians(90), radians(0)))

        utility.parent_objects(horseBody, [horseNeck, horseHead, horseGrip, horseFoundation, horseFoot, horseTail,
                                           horseHair])

        self.seat = horseBody


def main():

    seat = Seat((0,0,0))
    pass

main()
