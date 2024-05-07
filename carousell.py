import bpy
import math
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdir)


import custom_object
import utility
from math import radians


class BasicElement:
    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates
        self.mainObject = None
        self.allObjects = None

        self.create()
        self.mainObject.name = name
        self.translate(coordinates)
        
    def create(self):
        pass
    
    def translate(self, coordinates):
        self.coordinates = coordinates
        self.mainObject.location = coordinates
        
    def rotate(self, angle):
        self.mainObject.rotation_euler = (math.radians(
            angle[0]), math.radians(angle[1]), math.radians(angle[2]))
        
    def scale(self, size):
        self.mainObject.scale = size
        
    def mirror(self, axis):
        utility.select_object(self.mainObject)
        bpy.ops.object.modifier_add(type='MIRROR')
        bpy.context.object.modifiers["Mirror"].use_axis[0] = axis[0]
        bpy.context.object.modifiers["Mirror"].use_axis[1] = axis[1]
        bpy.context.object.modifiers["Mirror"].use_axis[2] = axis[2]

class Seat(BasicElement):
    def __init__(self, location):
        self.location = location
        self.seat = None
        self.animation_offset = 0

        self.create()

    def create(self):
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
        horseFoundation = custom_object.create_cylinder(name="foundation", location=(0, 0, 8.8), scale=(0.121, 0.213, 9.958),
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

        self.mainObject = horseBody





class Carousell(BasicElement):
    def __init__(self, coordinates):
        self.coordinates = (coordinates[0], coordinates[1], coordinates[2])
        self.seats = []
        self.roof = None
        self.roofparts = None
        self.floormain = None
        self.basefloor = None
        self.anotherMain = None

        # self.create()
        self.plot_seats()
        self.animate()


    def plot_seats(self):
        seat_1 = Seat((-15, 0,2))
        seat_1.rotate((-65, 90, 0))
        seat_1.translate((-15, 0,2))
        self.seats.append(seat_1)

        seat_2 = Seat((15, 0,2))
        seat_2.rotate((115, 90, 0))
        seat_2.translate((15, 0,2))
        self.seats.append(seat_2)

        seat_3 = Seat((0, -15,2))
        seat_3.rotate((200, 90, 0))
        seat_3.translate((0, -15,2))
        self.seats.append(seat_3)

        seat_4 = Seat((0, 15,2))
        seat_4.rotate((-4, 90, 0))
        seat_4.translate((0, 15, 2))
        self.seats.append(seat_4)

        seat_5 = Seat((-9, 10,2))
        seat_5.rotate((-35, 90, 0))
        seat_5.translate((-9, 10,2))
        self.seats.append(seat_5)

        seat_6 = Seat((9, 10, 2))
        seat_6.rotate((35, 90, 0))
        seat_6.translate((9, 10, 2))
        self.seats.append(seat_6) 

        seat_7 = Seat((9, -10, 2))
        seat_7.rotate((135, 90, 0))
        seat_7.translate((9, -10, 2))
        self.seats.append(seat_7)

        seat_8 = Seat((-9, -10, 2))
        seat_8.rotate((-150, 90, 0))
        seat_8.translate((-9, -10, 2))
        self.seats.append(seat_8)

        seat_9 = Seat((-17,8,2))
        seat_9.rotate((-50, 90, 0))
        seat_9.translate((-17,8,2))
        self.seats.append(seat_9)

        seat_10 = Seat((-8, 18,2))
        seat_10.rotate((-35, 90, 0))
        seat_10.translate((-8, 18,2))
        self.seats.append(seat_10)

        seat_11 = Seat((8, 18, 2))
        seat_11.rotate((35, 90, 0))
        seat_11.translate((8, 18,2))
        self.seats.append(seat_11)

        seat_12 = Seat((17, 8, 2))
        seat_12.rotate((65, 90, 0))
        seat_12.translate((17,8,2))
        self.seats.append(seat_12)

        seat_13 = Seat((17, -8, 2))
        seat_13.rotate((110, 90, 0))
        seat_13.translate((17, -8, 2))
        self.seats.append(seat_13)

        seat_14 = Seat((8,-18,2))
        seat_14.rotate((-215, 90, 0))
        seat_14.translate((8,-18,2))
        self.seats.append(seat_14)

        seat_15 = Seat((-8, -18, 2))
        seat_15.rotate((215, 90,0))
        seat_15.translate((-8, -18, 2))
        self.seats.append(seat_15)

        seat_16 = Seat((-17, -8, 2))
        seat_16.rotate((-130, 90, 0))
        seat_16.translate((-17, -8, 2))
        self.seats.append(seat_16)




        mainPole = custom_object.create_cylinder(name="pole", location=(0,0,5), scale=(1,1,15))

        roof = custom_object.create_cone(name="roof", location=(0,0,25.06), scale=(30,30,8.915))
        self.roof = roof
        roofparts = custom_object.create_cylinder(name="roofpart", location=(0,0,14), scale=(25,26,3))
        self.roofparts = roofparts
        
        floorMain = custom_object.create_cylinder(name="floor", location=(0,0,-5), scale=(25,26,1))
        self.floormain = floorMain
        floorbase = custom_object.create_cylinder(name="floorbase", location=(0,0,0), scale=(28,28,1))
        self.basefloor = floorbase

        poleMini = custom_object.create_cylinder(name="pole", location=(0,0,10), scale=(1,1,1))
        
        self.mainObject = mainPole
        self.anotherMain = poleMini



        utility.parent_objects(self.mainObject, [seat_1.mainObject, seat_2.mainObject, seat_3.mainObject, seat_4.mainObject, seat_5.mainObject, seat_6.mainObject, seat_7.mainObject, seat_8.mainObject, seat_9.mainObject, seat_10.mainObject, seat_11.mainObject, seat_12.mainObject, seat_13.mainObject, seat_14.mainObject, seat_15.mainObject, seat_16.mainObject,   roof, roofparts, floorMain])
        utility.parent_objects(self.anotherMain, [floorbase])




    def animate(self):
        frames = 100 
        bpy.context.scene.frame_end = frames  
        for frame in range(frames + 1): 
            angle = 360 - (frame / frames) * 360  
            self.rotate((0, 0, angle))
            self.mainObject.keyframe_insert(data_path="rotation_euler", index=2, frame=frame) 
            
            for i, seat in enumerate(self.seats):
                vertical_offset = math.sin(math.radians(frame / frames * 360 + i * 45)) * 2
                seat.translate((seat.location[0], seat.location[1], seat.location[2] + vertical_offset))
                seat.mainObject.keyframe_insert(data_path="location", index=2, frame=frame)

def main():
    korsel = Carousell(coordinates=(10,10,8))
    korsel.translate((0,0,13))


main()
