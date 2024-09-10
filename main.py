from constants import carl_position, daryl_position, exit_position, glen_position, maggie_position, rick_position, terrain_mapping
from utils import carregar_mapa_de_arquivo, criar_mapa, marcar_caminho, encontrar_caminho, traduzir_caminho

prison_map = carregar_mapa_de_arquivo('prison_map.txt', terrain_mapping)

# Exibe o mapa no terminal como uma matriz
# for row in prison_map:
#     print(row)

pontos_a_visitar = [rick_position, carl_position, daryl_position, glen_position, maggie_position, exit_position]

caminho, custo = encontrar_caminho(prison_map, pontos_a_visitar)

print(f'> Custo total do caminho encontrado: {custo}')
traduzir_caminho(caminho)

# Marca o caminho no mapa
marcar_caminho(prison_map, caminho)

# Plota o mapa com o caminho
criar_mapa(prison_map)


