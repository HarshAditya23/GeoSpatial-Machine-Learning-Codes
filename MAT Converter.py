# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 21:12:14 2025

@author: gaurh
"""

from spectral import *
import numpy as np
from scipy.io import savemat

# Step 1: Load the hyperspectral image
cube = open_image(r'subquac.hdr')

print("Image shape:", cube.shape)

# assumes ENVI format
data = cube.load()  # This will be a 3D numpy array: (rows, cols, bands)

# Step 2: Optionally, convert to (bands, rows, cols) like Pavia University format
#data = np.transpose(data, (2, 0, 1))  # Shape: (bands, rows, cols)

# Step 3: Save to .mat file
savemat(r'C:\Users\gaurh\Desktop\cube4.mat', {'data': data})
