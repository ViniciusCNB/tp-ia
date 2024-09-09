import constants
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from utils import aestrela, load_map_from_file

prison_map = load_map_from_file('prison_map.txt', constants.terrain_mapping)

# Exibe o mapa no terminal como uma matriz
for row in prison_map:
    print(row)

# Função para marcar o caminho no mapa
def mark_path_on_map(prison_map, path):
    for (x, y) in path:
        prison_map[x][y] = -1  # Marca o caminho com um valor específico, por exemplo, -1

# Exibe o mapa em uma imagem como um heatmap
def plot_map(prison_map):
    """
    Plota a matriz do mapa como um heatmap usando matplotlib e seaborn.
    """
    plt.figure(figsize=(15, 15))  # Define o tamanho do gráfico
    cmap = sns.color_palette("YlOrRd", as_cmap=True)
    cmap.set_under('blue')  # Define a cor para o caminho
    sns.heatmap(prison_map, cmap=cmap, annot=True, cbar=True, square=True, linewidths=0.5, linecolor='black', vmin=0)
    plt.title("Mapa de Prisão com Custos e Caminho")
    plt.show()

# Teste A* com a posição do Rick e do Carl
caminho = aestrela(prison_map, (20, 12), (5, 32))

# Marca o caminho no mapa
mark_path_on_map(prison_map, caminho)

# Plota o mapa com o caminho
plot_map(prison_map)

print(caminho)