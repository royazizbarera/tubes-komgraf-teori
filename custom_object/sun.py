# ===================================

from importlib import reload

import custom_object.uv_sphere

reload(custom_object.uv_sphere)

from custom_object.uv_sphere import UvSphere

class Sun():
    def __init__(self, name, color = (1,0.880267,0.06236,1), location=(0, 0, 0), scale=(1, 1, 1), rotation=(0, 0, 0)):
        self.name = name
        self.location = location
        self.scale = scale
        self.rotation = rotation
        self.color = color
        self.create_object()

    def create_object(self):
        self.sun = UvSphere(self.name, scale=self.scale, location=self.location, rotation=self.rotation)
        self.sun.shade_smooth()
        self.sun.create_emission_material(emission_color=self.color)
        self.sun.add_lamp_inside(lamp_type='SUN', energy=5, color=self.color)
        self.sun.set_shadow_mode('NONE')
