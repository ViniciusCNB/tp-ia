import constants
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from utils import aestrela, load_map_from_file
from matplotlib.colors import ListedColormap

prison_map = load_map_from_file('prison_map.txt', constants.terrain_mapping)

# Exibe o mapa no terminal como uma matriz
for row in prison_map:
    print(row)

# Função para marcar o caminho no mapa
def mark_path_on_map(prison_map, path):
    for (x, y) in path:
        prison_map[x][y] = -1  # Marca o caminho com um valor específico, por exemplo, -1

# Exibe o mapa em uma imagem como um heatmap
# def plot_map(prison_map):
#     """
#     Plota a matriz do mapa como um heatmap usando matplotlib e seaborn.
#     """
#     plt.figure(figsize=(15, 15))  # Define o tamanho do gráfico
#     cmap = sns.color_palette("YlOrRd", as_cmap=True)
#     cmap.set_under('blue')  # Define a cor para o caminho
#     sns.heatmap(prison_map, cmap=cmap, annot=True, cbar=True, square=True, linewidths=0.5, linecolor='black', vmin=0)
#     plt.title("Mapa de Prisão com Custos e Caminho")
#     plt.show()


def plot_map(prison_map, caminho=None):
    """
    Plota a matriz do mapa como um heatmap usando matplotlib e seaborn, com cores personalizadas.
    """
    # Definir o mapeamento de cores de acordo com os valores
    colors = ['yellow','darkgray', 'brown', 'green', 'lightgray', 'blue']  # cores para os valores
    cmap = ListedColormap(colors)

    # Definir os limites para o colorbar (cada limite corresponde a uma cor)
    bounds = [-1, 1, 3, 5, 10, float('inf')]  # limites baseados nos valores
    norm = plt.Normalize(vmin= -1, vmax=10)  # Normaliza os valores de 0 a 10

    # Plota o mapa com o colormap personalizado
    plt.figure(figsize=(20, 20))  # Define o tamanho do gráfico
    sns.heatmap(prison_map, cmap=cmap, annot=True, cbar=True, square=True, linewidths=0.5, linecolor='black',
                norm=norm, cbar_kws={'ticks': [-1, 1, 3, 5, 10]})  # Define os ticks do colorbar

    plt.title("Mapa de Prisão com Custos e Cores Personalizadas")
    plt.show()


# Teste A* com a posição do Rick e do Carl
caminho = aestrela(prison_map, (20, 12), (5, 32))

# Marca o caminho no mapa
mark_path_on_map(prison_map, caminho)

# Plota o mapa com o caminho
plot_map(prison_map)

print(caminho)