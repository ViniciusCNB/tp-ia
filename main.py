from constants import carl_position, daryl_position, exit_position, glen_position, maggie_position, rick_position, terrain_mapping
from utils import load_map_from_file, plot_map, mark_path_on_map, encontrar_caminho

prison_map = load_map_from_file('prison_map.txt', terrain_mapping)

# Exibe o mapa no terminal como uma matriz
# for row in prison_map:
#     print(row)

pontos_a_visitar = [rick_position, carl_position, daryl_position, glen_position, maggie_position, exit_position]

caminho, custo = encontrar_caminho(prison_map, pontos_a_visitar)

# Marca o caminho no mapa
mark_path_on_map(prison_map, caminho)

# Plota o mapa com o caminho
plot_map(prison_map)

print(f'> Custo total do caminho encontrado: {custo}')
print(caminho)