import constants
from utils import aestrela, load_map_from_file, plot_map, mark_path_on_map

prison_map = load_map_from_file('prison_map.txt', constants.terrain_mapping)

# Exibe o mapa no terminal como uma matriz
for row in prison_map:
    print(row)

# Teste A* com a posição do Rick e do Carl
caminho = aestrela(prison_map, (20, 12), (5, 32))

# Marca o caminho no mapa
mark_path_on_map(prison_map, caminho)

# Plota o mapa com o caminho
plot_map(prison_map)

print(caminho)