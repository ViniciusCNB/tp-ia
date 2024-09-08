import constants
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from utils import aestrela, load_map_from_file

prison_map = load_map_from_file('prison_map.txt', constants.terrain_mapping)

# Exibe o mapa no terminal como uma matriz
for row in prison_map:
    print(row)

# Exibe o mapa em uma imagem como um heatmap
def plot_map(prison_map):
    """
    Plota a matriz do mapa como um heatmap usando matplotlib e seaborn.
    """
    plt.figure(figsize=(15, 15))  # Define o tamanho do gráfico
    sns.heatmap(prison_map, cmap="YlOrRd", annot=True, cbar=True, square=True, linewidths=0.5, linecolor='black')
    plt.title("Mapa de Prisão com Custos")
    plt.show()

plot_map(prison_map)

# Teste A* com a posição do Rick e do Carl
caminho = aestrela(prison_map, (20, 12), (5, 32))

print(caminho)