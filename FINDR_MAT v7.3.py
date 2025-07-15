# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 22:26:15 2025

@author: gaurh
"""

import h5py as h5
from nfindr import run_nfindr
from utils import plot_endmembers
import numpy as np

data = h5.File(r'Houston18.mat')
print("Loaded keys in .mat:", data.keys())

data = data['ori_data']
data = np.array(data)

bands = 48
hyp_data = data.reshape((bands, -1))
print("Hyperspectral image shape:", hyp_data.shape)


pixels = hyp_data
bands, N = pixels.shape
num_endmembers = 15
print(f"Running N-FINDR to find {num_endmembers} endmembers...")

endmembers = run_nfindr(pixels, num_endmembers, max_iter=20)
print("N-FINDR completed.")

plot_endmembers(endmembers)