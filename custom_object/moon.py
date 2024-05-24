# ===================================
from importlib import reload

import library_object.uv_sphere
import library_object.lamp

reload(library_object.uv_sphere)
reload(library_object.lamp)
from library_object.uv_sphere import UvSphere
from library_object.lamp import Lamp


class Moon():
    def __init__(self, name='moon', color=(0.8, 0.8, 0.8, 1), location=(0, 0, 0), scale=(1, 1, 1), rotation=(0, 0, 0)):
        self.name = name
        self.location = location
        self.scale = scale
        self.rotation = rotation
        self.color = color
        self.create_object()

    def create_object(self):
        self.moon = UvSphere(self.name, scale=self.scale,
                            location=self.location, rotation=self.rotation)
        self.moon.modifier.add_subdivision_surface(levels=2, render_levels=2)
        self.moon.shade_smooth()
        self.moon.material.create_emission_material(emission_color=self.color)
        self.moon.set_shadow_mode('NONE')
        
        self.lamp = Lamp(self.name, lamp_type='SUN', energy=5, color=self.color, shadow=False,
                    location=self.location, scale=self.scale, rotation=self.rotation)
        self.lamp.became_the_child_of(self.moon.object)