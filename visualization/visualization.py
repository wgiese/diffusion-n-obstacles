#! /usr/bin/env python

import hl
import numpy as np

# Dimensions
nx, ny, nz = 2, 2, 2
lx, ly, lz = 1.0, 1.0, 1.0
dx, dy, dz = lx/nx, ly/ny, lz/nz

ncells = nx * ny * nz
npoints = (nx + 1) * (ny + 1) * (nz + 1)

# Coordinates
x = np.arange(0, lx + dx, dx, dtype='float64')
y = np.arange(0, ly + dy, dy, dtype='float64')
z = np.arange(0, lz + dz, dz, dtype='float64')

# Variables
point_data = np.zeros((nx + 1, ny + 1, nz + 1))
cell_data = np.zeros((nx, ny, nz))

cell_data[1][1][1] = 1.0

point_data[2][1][1] = 1.0 

hl.gridToVTK("./visualization", x, y, z, cellData = {"pressure" : cell_data}, pointData = {"temp" : point_data})
