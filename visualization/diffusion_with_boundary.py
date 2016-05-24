#! /usr/bin/env python

import hl
import numpy as np

# Dimensions
nx, ny, nz = 100, 50, 50
lx, ly, lz = 20.0, 10.0, 10.0
dx, dy, dz = lx/nx, ly/ny, lz/nz

ncells = nx * ny * nz


# Coordinates
x = np.arange(0, lx + dx, dx, dtype='float64')
y = np.arange(0, ly + dy, dy, dtype='float64')
z = np.arange(0, lz + dz, dz, dtype='float64')

# Variables

Diffusion_coeff = 1.0

rate = 6*Diffusion_coeff/(lx*lx)


molecule = np.zeros((nx, ny, nz))
density = np.zeros((nx, ny, nz))
boundary = np.zeros((nx, ny, nz))


# Define two spheres
R1 = 3.0
R2 = 2.5
center1 = [5.0,5.0,5.0]
center2 = [9.0,5.0,5.0]

for i in range(0,nx):
  for j in range(0,ny):
    for k in range(0,nz):

      dist1 = (x[i] - center1[0])**2 + (y[j] - center1[1])**2 + (z[k] - center1[2])**2
     
      if (dist1 < R1**2 ):
	boundary[i][j][k] = 1
  
      dist2 = (x[i] - center2[0])**2 + (y[j] - center2[1])**2 + (z[k] - center2[2])**2
     
      if (dist2 < R2**2 ):
	boundary[i][j][k] = 1  


pos_x = nx/2
pos_y = ny/2
pos_z = nz/2

molecule[pos_x][pos_y][pos_z] = 1.0
density[pos_x][pos_y][pos_z] = 1.0


time = 0.0


for i in range(0,100):

  tau = np.random.exponential(1.0 / rate)

  time += tau
  
  temp = density/np.sum(density)
  
  rand_num = np.random.uniform()
  
  if ( rand_num < 1.0/6.0):
    if (pos_x < nx - 1):
      if (boundary[pos_x+1][pos_y][pos_z] == 1):
	molecule[pos_x][pos_y][pos_z] = 0.0
	pos_x += 1 
	molecule[pos_x][pos_y][pos_z] = 1.0
    density[pos_x][pos_y][pos_z] += 1.0      
  elif ( rand_num < 2.0/6.0):
    if ( 0 < pos_x):
      if (boundary[pos_x-1][pos_y][pos_z] == 1):
	molecule[pos_x][pos_y][pos_z] = 0.0
	pos_x -= 1 
	molecule[pos_x][pos_y][pos_z] = 1.0
    density[pos_x][pos_y][pos_z] += 1.0 
  elif ( rand_num < 3.0/6.0):
    if (pos_y < ny - 1):
      if (boundary[pos_x][pos_y+1][pos_z] == 1):
	molecule[pos_x][pos_y][pos_z] = 0.0
	pos_y += 1 
	molecule[pos_x][pos_y][pos_z] = 1.0
    density[pos_x][pos_y][pos_z] += 1.0      
  elif ( rand_num < 4.0/6.0):
    if ( 0 < pos_y):
      if (boundary[pos_x][pos_y-1][pos_z] == 1):
	molecule[pos_x][pos_y][pos_z] = 0.0
	pos_y -= 1 
	molecule[pos_x][pos_y][pos_z] = 1.0
    density[pos_x][pos_y][pos_z] += 1.0 
  elif ( rand_num < 5.0/6.0):    
    if (pos_z < nz - 1):
      if (boundary[pos_x][pos_y][pos_z+1] == 1):
	molecule[pos_x][pos_y][pos_z] = 0.0
	pos_z += 1 
	molecule[pos_x][pos_y][pos_z] = 1.0
    density[pos_x][pos_y][pos_z] += 1.0      
  else:
    if ( 0 < pos_z):
      if (boundary[pos_x][pos_y][pos_z-1] == 1):
	molecule[pos_x][pos_y][pos_z] = 0.0
	pos_z -= 1 
	molecule[pos_x][pos_y][pos_z] = 1.0
    density[pos_x][pos_y][pos_z] += 1.0 
  
  hl.gridToVTK("output/diffusion_obstacle" + str(i), x, y, z, cellData = {"particle" : molecule, "density" : density, "boundary" : boundary})
