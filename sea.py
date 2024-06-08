# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 21:18:23 2024

@author: leona
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sea_micro = pd.read_csv("SEA_MICRO.csv")


x = sea_micro['Longitude']
y = sea_micro['Latitude']
z = sea_micro['Pieces_KM2']


xi = np.linspace(x.min(), x.max(), 100)
yi = np.linspace(y.min(), y.max(), 100)


zi, xedges, yedges = np.histogram2d(x, y, bins=(xi, yi), weights=z)


plt.figure(figsize=(8, 6))
plt.pcolormesh(xedges, yedges, zi.T, cmap='hot')
plt.colorbar(label='Microplástico')
plt.title('Mapa de Calor de Microplástico por Localização Geográfica')
plt.ylabel('Latitude')
plt.show()
