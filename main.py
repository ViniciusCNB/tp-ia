# GRUPO 10: Davi Ribeiro de Almeida, Maria Eduarda Santos Timiraos e Vinícius Correa Nobre Borges

from constants import carl_position, daryl_position, exit_position, glen_position, maggie_position, rick_position, terrain_mapping
from utils import carregar_mapa_a_partir_do_txt, encontrar_caminho

# 1º passo: carregar o mapa da prisão em uma matriz
prison_map = carregar_mapa_a_partir_do_txt('prison_map.txt', terrain_mapping)

# 2º passo: definir a ordem de visitação dos personagens, com a posição de início e fim fixos
pontos_a_visitar = [rick_position, carl_position, daryl_position, glen_position, maggie_position, exit_position]

# 3º passo: encontrar o caminho entre os pontos de visitação, exibindo as etapas do caminho com seus custos e custo final
encontrar_caminho(prison_map, pontos_a_visitar)