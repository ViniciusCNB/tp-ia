from constants import carl_position, daryl_position, exit_position, glen_position, maggie_position, rick_position, terrain_mapping
from utils import carregar_mapa_a_partir_do_txt, criar_mapa, marcar_caminho, encontrar_caminho, traduzir_caminho


# 1º passo: carregar o mapa da prisão em uma matriz
prison_map = carregar_mapa_a_partir_do_txt('prison_map.txt', terrain_mapping)

# 2º passo: definir a ordem de visitação dos personagens, com a posição de início e fim fixos
pontos_a_visitar = [rick_position, carl_position, daryl_position, glen_position, maggie_position, exit_position]

# 3º passo: encontrar o caminho entre os pontos de visitação, retornando o caminho como um dicionário e o custo total
caminho, custo = encontrar_caminho(prison_map, pontos_a_visitar)

print(f'> Custo total do caminho encontrado: {custo}')
traduzir_caminho(caminho)

# Marca o caminho no mapa
marcar_caminho(prison_map, caminho)

# Plota o mapa com o caminho
criar_mapa(prison_map)


