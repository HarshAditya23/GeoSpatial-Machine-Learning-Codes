# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 22:41:47 2025

@author: gaurh
"""


import h5py as h5 #From v7.3 matlab files

data = h5.File(r'Houston13.mat')['ori_data']
# print(mat_v7.keys())
# #print(type(mat_v7))
# print(len(mat_v7))
print(data.shape)
# from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt

# data = loadmat(r'C:\Users\gaurh\Desktop\cube2.mat')['data']
# #gt = loadmat('GT.mat')['gt']



print(f"Data Shape: {data.shape[1:]}\nNumber of Bands: {data.shape[0]}")

fig = plt.figure(figsize = (20, 12))

ax = fig.subplots(2, 5)

for i in range(2):
  for j in range(5):
    c = np.random.randint(45)
    ax[i][j].imshow(data[c,:,:], cmap='nipy_spectral')
    ax[i][j].axis('off')
    ax[i][j].title.set_text(f"Band - {c}")
    c += 1

plt.tight_layout()
plt.show()

mdata = np.moveaxis(data, -1, 0)

ep.plot_rgb(mdata, (29, 23, 2), figsize=(15, 15))

plt.show()

def plot_data(data):
  fig = plt.figure(figsize=(12, 12))
  plt.imshow(data, cmap='nipy_spectral')
  plt.colorbar()
  plt.axis('on')
  plt.show()

plot_data(gt)