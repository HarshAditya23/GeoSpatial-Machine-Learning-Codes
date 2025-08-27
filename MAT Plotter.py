# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 22:41:47 2025

@author: gaurh
"""

import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
import earthpy.plot as ep

data = sio.loadmat(r'sub.mat')
print(data.keys())
print(type(data))

data = data['HSI']
print(data.shape)
print(f"Data Shape: {data.shape[1:]}\nNumber of Bands: {data.shape[2]}")

fig = plt.figure(figsize = (20, 12))
ax = fig.subplots(2, 5)

for i in range(2):
  for j in range(5):
    c = np.random.randint(23)
    ax[i][j].imshow(data[:,:,c], cmap='nipy_spectral')
    ax[i][j].axis('off')
    ax[i][j].title.set_text(f"Band - {c}")
    c += 1

plt.tight_layout()
plt.show()

mdata = np.moveaxis(data, -1, 0)
ep.plot_rgb(mdata, (14, 4, 1), figsize=(15, 15))
plt.show()