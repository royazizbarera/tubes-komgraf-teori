import bpy
import math

# Clear
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

class Wahana:
    def __init__(self,koordinatX,koordinatY):
        self.koordinatX = koordinatX
        self.koordinatY = koordinatY
    
    def draw(self):
        # Membuat Alas Utama
        bpy.ops.mesh.primitive_cylinder_add(radius=30, depth=1, location=(self.koordinatX, self.koordinatY, 0))
        alasUtama = bpy.context.object

        # Membuat Alas masing masing kumpulan cangkir 1
        bpy.ops.mesh.primitive_cylinder_add(radius=10, depth=1, location=(0, 17, 1))
        alas1 = bpy.context.object

        # Membuat alas masing masing kumpulan cangkir 2
        bpy.ops.mesh.primitive_cylinder_add(radius=10, depth=1, location=(0, 17, 1))
        alas2 = bpy.context.object
        # Memindahkan posisi alas 2
        bpy.context.view_layer.objects.active = alas2
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
        bpy.ops.transform.rotate(value=math.radians(120), orient_axis='Z')

        # Membuat alas masing masing kumpulan cangkir 3
        bpy.ops.mesh.primitive_cylinder_add(radius=10, depth=1, location=(0, 17, 1))
        alas3 = bpy.context.object
        # Memindahkan posisi alas 3
        bpy.context.view_layer.objects.active = alas3
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
        bpy.ops.transform.rotate(value=math.radians(240), orient_axis='Z')

        self.alasCangkir = [alas1, alas2, alas3]
        
        # Penggabungan objek menjadi parent child
        for alas in self.alasCangkir:
            alas.parent = alasUtama

        # Membuat bola pada alas 1
        bpy.ops.mesh.primitive_uv_sphere_add(radius=4, location=(0, 5, 4))
        bola1 = bpy.context.object
        bola1.parent = alas1
        
        bpy.ops.mesh.primitive_uv_sphere_add(radius=4, location=(0, 5, 4))
        bola2 = bpy.context.object
        bpy.context.view_layer.objects.active = bola2
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
        bpy.ops.transform.rotate(value=math.radians(120), orient_axis='Z')
        bola2.parent = alas1
        
        bpy.ops.mesh.primitive_uv_sphere_add(radius=4, location=(0, 5, 4))
        bola3 = bpy.context.object
        bpy.context.view_layer.objects.active = bola3
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
        bpy.ops.transform.rotate(value=math.radians(240), orient_axis='Z')
        bola3.parent = alas1
        
        # Membuat bola pada alas 2
        bpy.ops.mesh.primitive_uv_sphere_add(radius=4, location=(0, 5, 5))
        bola4 = bpy.context.object
        bola4.location.y += 17
        bola4.parent = alas2
        
        bpy.ops.mesh.primitive_uv_sphere_add(radius=4, location=(0, 5, 5))
        bola5 = bpy.context.object
        bpy.context.view_layer.objects.active = bola5
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
        bpy.ops.transform.rotate(value=math.radians(120), orient_axis='Z')
        bola5.location.y += 17
        bola5.parent = alas2
        
        bpy.ops.mesh.primitive_uv_sphere_add(radius=4, location=(0, 5, 5))
        bola6 = bpy.context.object
        bpy.context.view_layer.objects.active = bola6
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
        bpy.ops.transform.rotate(value=math.radians(240), orient_axis='Z')
        bola6.location.y += 17
        bola6.parent = alas2
        
        # Membuat bola pada alas 3
        bpy.ops.mesh.primitive_uv_sphere_add(radius=4, location=(0, 5, 5))
        bola7 = bpy.context.object
        bola7.location.y += 17
        bola7.parent = alas3
        
        bpy.ops.mesh.primitive_uv_sphere_add(radius=4, location=(0, 5, 5))
        bola8 = bpy.context.object
        bpy.context.view_layer.objects.active = bola8
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
        bpy.ops.transform.rotate(value=math.radians(120), orient_axis='Z')
        bola8.location.y += 17
        bola8.parent = alas3
        
        bpy.ops.mesh.primitive_uv_sphere_add(radius=4, location=(0, 5, 5))
        bola9 = bpy.context.object
        bpy.context.view_layer.objects.active = bola9
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
        bpy.ops.transform.rotate(value=math.radians(240), orient_axis='Z')
        bola9.location.y += 17
        bola9.parent = alas3
        
        bolaBawah = [bola1, bola2, bola3, bola4, bola5, bola6, bola7, bola8, bola9]
        
        # Membentuk cangkir dari setiap bola
        # Pembuatan bola pemotong dan penerapan fungsi boolean pada alas 1
        bpy.ops.mesh.primitive_uv_sphere_add(radius=4, location=(0, 5, 6))
        bolaPemotong1 = bpy.context.object
        bolaPemotong1.parent = alas1
        
        bpy.ops.mesh.primitive_uv_sphere_add(radius=4, location=(0, 5, 6))
        bolaPemotong2 = bpy.context.object
        bpy.context.view_layer.objects.active = bolaPemotong2
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
        bpy.ops.transform.rotate(value=math.radians(120), orient_axis='Z')
        bolaPemotong2.parent = alas1
        
        bpy.ops.mesh.primitive_uv_sphere_add(radius=4, location=(0, 5, 6))
        bolaPemotong3 = bpy.context.object
        bpy.context.view_layer.objects.active = bolaPemotong3
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
        bpy.ops.transform.rotate(value=math.radians(240), orient_axis='Z')
        bolaPemotong3.parent = alas1
        
        bpy.ops.mesh.primitive_uv_sphere_add(radius=4, location=(0, 5, 7))
        bolaPemotong4 = bpy.context.object
        bolaPemotong4.location.y += 17
        bolaPemotong4.parent = alas2
        
        bpy.ops.mesh.primitive_uv_sphere_add(radius=4, location=(0, 5, 7))
        bolaPemotong5 = bpy.context.object
        bpy.context.view_layer.objects.active = bolaPemotong5
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
        bpy.ops.transform.rotate(value=math.radians(120), orient_axis='Z')
        bolaPemotong5.location.y += 17
        bolaPemotong5.parent = alas2
        
        bpy.ops.mesh.primitive_uv_sphere_add(radius=4, location=(0, 5, 7))
        bolaPemotong6 = bpy.context.object
        bpy.context.view_layer.objects.active = bolaPemotong6
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
        bpy.ops.transform.rotate(value=math.radians(240), orient_axis='Z')
        bolaPemotong6.location.y += 17
        bolaPemotong6.parent = alas2
        
        bpy.ops.mesh.primitive_uv_sphere_add(radius=4, location=(0, 5, 7))
        bolaPemotong7 = bpy.context.object
        bolaPemotong7.location.y += 17
        bolaPemotong7.parent = alas3
        
        bpy.ops.mesh.primitive_uv_sphere_add(radius=4, location=(0, 5, 7))
        bolaPemotong8 = bpy.context.object
        bpy.context.view_layer.objects.active = bolaPemotong8
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
        bpy.ops.transform.rotate(value=math.radians(120), orient_axis='Z')
        bolaPemotong8.location.y += 17
        bolaPemotong8.parent = alas3
        
        bpy.ops.mesh.primitive_uv_sphere_add(radius=4, location=(0, 5, 7))
        bolaPemotong9 = bpy.context.object
        bpy.context.view_layer.objects.active = bolaPemotong9
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
        bpy.ops.transform.rotate(value=math.radians(240), orient_axis='Z')
        bolaPemotong9.location.y += 17
        bolaPemotong9.parent = alas3
        
        bolaPemotong = [bolaPemotong1, bolaPemotong2, bolaPemotong3, bolaPemotong4, bolaPemotong5, bolaPemotong6, bolaPemotong7, bolaPemotong8, bolaPemotong9]

        for i in range(9):
                bpy.context.view_layer.objects.active = bolaBawah[i]
                bolaPemotong[i].select_set(True)
                bpy.ops.object.modifier_add(type='BOOLEAN')
                bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
                bpy.context.object.modifiers["Boolean"].object = bolaPemotong[i]
                bpy.ops.object.modifier_apply(modifier="Boolean")

        # Menghapus bola pemotong
        for bola in bolaPemotong:
            bpy.data.objects.remove(bola)
            
        # Memindahkan bola ke variabel cangkir
        self.cangkir = bolaBawah
        
    def animate(self):
        bpy.ops.object.select_all(action='DESELECT')
        for alas in self.alasCangkir:
            alas.select_set(True)
        bpy.context.view_layer.objects.active = self.alasCangkir[0]
        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS', center='MEDIAN')

        # Set keyframe buat animasi alas
        for alas in self.alasCangkir:
            alas.rotation_euler = (0, 0, math.radians(0))
            alas.keyframe_insert(data_path="rotation_euler", index=2, frame=1)
            alas.rotation_euler = (0, 0, math.radians(360))
            alas.keyframe_insert(data_path="rotation_euler", index=2, frame=60)
            alas.rotation_euler = (0, 0, math.radians(0))
            alas.keyframe_insert(data_path="rotation_euler", index=2, frame=120)
            
        bpy.ops.object.select_all(action='DESELECT')
        for cangkir in self.cangkir:
            cangkir.select_set(True)
        bpy.context.view_layer.objects.active = self.cangkir[0]
        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS', center='MEDIAN')

        # Set keyframe buat animasi alas
        for cangkir in self.cangkir:
            cangkir.rotation_euler = (0, 0, math.radians(0))
            cangkir.keyframe_insert(data_path="rotation_euler", index=2, frame=1)
            cangkir.rotation_euler = (0, 0, math.radians(180))
            cangkir.keyframe_insert(data_path="rotation_euler", index=2, frame=60)
            cangkir.rotation_euler = (0, 0, math.radians(0))
            cangkir.keyframe_insert(data_path="rotation_euler", index=2, frame=120)
            
        
            
Wahana = Wahana(0,0)
Wahana.draw()
Wahana.animate()