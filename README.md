# Projeto de Visualização de Mapa de Calor de Microplástico

## Integrantes do Projeto
- **Leonardo Baldaia**
  - RM: 557416
- **Lorran dos Santos**
  - RM: 558982
- **Gabriel Caetano**
  - RM: 557582

## Objetivo

O principal objetivo deste projeto é criar um mapa de calor para visualizar a quantidade de microplásticos na água. Esta visualização visa fornecer uma representação clara e informativa da distribuição e concentração de microplásticos em diferentes locais geográficos.

## Descrição do Projeto

O projeto utiliza dados contidos no arquivo "SEA_MICRO.csv" para gerar o mapa de calor. Os passos principais incluem:

### 1. Leitura dos Dados

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sea_micro = pd.read_csv("SEA_MICRO.csv")
### 2. Extração das Coordenadas e Quantidade de Microplásticos

x = sea_micro['Longitude']
y = sea_micro['Latitude']
z = sea_micro['Pieces_KM2']

### 3. Criação das Grades para o Mapa de Calor

xi = np.linspace(x.min(), x.max(), 100)
yi = np.linspace(y.min(), y.max(), 100)

### 4. Geração da Matriz para o Mapa de Calor

zi, xedges, yedges = np.histogram2d(x, y, bins=(xi, yi), weights=z)

### 5. Plotagem do Mapa de Calor

plt.figure(figsize=(8, 6))
plt.pcolormesh(xedges, yedges, zi.T, cmap='hot')
plt.colorbar(label='Microplástico')
plt.title('Mapa de Calor de Microplástico por Localização Geográfica')
plt.ylabel('Latitude')
plt.show()

### Conclusão

Este projeto demonstra uma abordagem eficiente para visualizar a distribuição de microplásticos na água através de um mapa de calor, permitindo uma análise mais profunda e visualmente intuitiva dos dados geográficos.

### Ferramentas Utilizadas

Python
Pandas
NumPy
Matplotlib
###
