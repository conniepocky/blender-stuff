import bpy
import random

def fractal(n, x, y, z):
    scaleLevel = n-0.5 #random.randint(n, 10)
    bpy.ops.mesh.primitive_cube_add(size=random.randint(2,50), enter_editmode=False, align='WORLD', location=(x, y, z), scale=(1, 1, 1))
    if n  > 0:
        # face 1
        nx = x + scaleLevel*2 # ???
        ny = y + 0
        nz = z + 0
        fractal(n-1, nx, ny, nz)
        
        # face 2
        nx = x - 1
        ny = y + 0
        nz = z + 0
        fractal(n-1, nx, ny, nz)
        
        # face 3
        nx = x + 2
        ny = y + 2
        nz = z + 2
        fractal(n-1, nx, ny, nz)
        
        #face 4
        
        #face 5
        
        #face 6


fractal(3, 0, 0, 0)