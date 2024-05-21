# ===================================

from importlib import reload

import library_object.uv_sphere

reload(library_object.uv_sphere)
from library_object.uv_sphere import UvSphere



class Moon():
    def __init__(self, name='moon', color=(0.8, 0.8, 0.8, 1), location=(0, 0, 0), scale=(1, 1, 1), rotation=(0, 0, 0)):
        self.name = name
        self.location = location
        self.scale = scale
        self.rotation = rotation
        self.color = color
        self.create_object()

    def create_object(self):
        self.sun = UvSphere(self.name, scale=self.scale,
                            location=self.location, rotation=self.rotation)
        self.sun.modifier.add_subdivision_surface(levels=2, render_levels=2)
        self.sun.shade_smooth()
        self.sun.material.create_emission_material(emission_color=self.color)
        self.sun.add_lamp_inside(lamp_type='SUN', energy=5, color=self.color)
        self.sun.set_shadow_mode('NONE')
