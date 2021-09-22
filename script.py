import bpy
from random import randint
    
def spheres(number, x, y, z, startKF, n):
    newX = 0
    newY = 0
    newZ = 0
    for i in range(0,number):    
        bpy.ops.mesh.primitive_ico_sphere_add(enter_editmode=False)
        sphere = bpy.context.object
        sphere.hide_viewport = True
        sphere.hide_render = True
        sphere.keyframe_insert(data_path="hide_viewport", frame=0, index=-1)
        sphere.keyframe_insert(data_path="hide_render", frame=0, index=-1)
        sphere.hide_viewport = False
        sphere.hide_render = False
        sphere.keyframe_insert(data_path="hide_viewport", frame=startKF, index=-1)
        sphere.keyframe_insert(data_path="hide_render", frame=startKF, index=-1)
        sphere.location = (x,y,z)
        sphere.keyframe_insert(data_path="location", frame=startKF, index=-1)
        addX = (randint (-4,4))
        addY = (randint (-4,4))
        addZ = (randint (-4,4))
        newX = x + addX 
        newY = y + addY
        newZ = z + addZ
        sphere.location = (newX,newY,newZ)
        sphere.keyframe_insert(data_path="location", frame=startKF+20, index=-1)
    
    if n < 3:
        spheres(10, newX, newY, newZ, startKF+20, n+1)
        
bpy.ops.mesh.primitive_cube_add()

count = 10

for c in range(0,count):
    x = randint(-10,10)
    y = randint(-10,10)
    z = randint(-10,10)
    bpy.ops.mesh.primitive_cube_add(location=(x,y,z))        
    
spheres(10, 0, 0, 0, 20, 0)

bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=4, radius=1,  location=(0, 0, 0))
bpy.ops.object.shade_smooth()
            
obj = bpy.context.object
        
obj.hide_viewport = True
obj.hide_render = True
obj.keyframe_insert(data_path="hide_viewport", frame=0, index=-1)
obj.keyframe_insert(data_path="hide_render", frame=0, index=-1)