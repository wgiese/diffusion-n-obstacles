#! /usr/bin/env python

import hl
import numpy as np

# Dimensions
nx, ny, nz = 10, 10, 10
lx, ly, lz = 1.0, 1.0, 1.0
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
      molecule[pos_x][pos_y][pos_z] = 0.0
      pos_x += 1 
      molecule[pos_x][pos_y][pos_z] = 1.0
    density[pos_x][pos_y][pos_z] += 1.0      
  elif ( rand_num < 2.0/6.0):
    if ( 0 < pos_x):
      molecule[pos_x][pos_y][pos_z] = 0.0
      pos_x -= 1 
      molecule[pos_x][pos_y][pos_z] = 1.0
    density[pos_x][pos_y][pos_z] += 1.0 
  elif ( rand_num < 3.0/6.0):
    if (pos_y < ny - 1):
      molecule[pos_x][pos_y][pos_z] = 0.0
      pos_y += 1 
      molecule[pos_x][pos_y][pos_z] = 1.0
    density[pos_x][pos_y][pos_z] += 1.0      
  elif ( rand_num < 4.0/6.0):
    if ( 0 < pos_y):
      molecule[pos_x][pos_y][pos_z] = 0.0
      pos_y -= 1 
      molecule[pos_x][pos_y][pos_z] = 1.0
    density[pos_x][pos_y][pos_z] += 1.0 
  elif ( rand_num < 5.0/6.0):    
    if (pos_z < nz - 1):
      molecule[pos_x][pos_y][pos_z] = 0.0
      pos_z += 1 
      molecule[pos_x][pos_y][pos_z] = 1.0
    density[pos_x][pos_y][pos_z] += 1.0      
  else:
    if ( 0 < pos_z):
      molecule[pos_x][pos_y][pos_z] = 0.0
      pos_z -= 1 
      molecule[pos_x][pos_y][pos_z] = 1.0
    density[pos_x][pos_y][pos_z] += 1.0 
  
  hl.gridToVTK("output/diffusion_" + str(i), x, y, z, cellData = {"particle" : molecule, "density" : temp})
