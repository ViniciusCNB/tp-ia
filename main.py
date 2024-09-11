# from constants import carl_position, daryl_position, exit_position, glen_position, maggie_position, rick_position, terrain_mapping
# from utils import carregar_mapa_a_partir_do_txt, criar_mapa, marcar_caminho, encontrar_caminho, traduzir_caminho


# # 1º passo: carregar o mapa da prisão em uma matriz
# prison_map = carregar_mapa_a_partir_do_txt('prison_map.txt', terrain_mapping)

# # 2º passo: definir a ordem de visitação dos personagens, com a posição de início e fim fixos
# pontos_a_visitar = [rick_position, carl_position, daryl_position, glen_position, maggie_position, exit_position]

# # 3º passo: encontrar o caminho entre os pontos de visitação, retornando o caminho como um dicionário e o custo total
# caminho, custo = encontrar_caminho(prison_map, pontos_a_visitar)

# print(f'> Custo total do caminho encontrado: {custo}')
# traduzir_caminho(caminho)

# # Marca o caminho no mapa
# marcar_caminho(prison_map, caminho)

# # Plota o mapa com o caminho
# criar_mapa(prison_map)

from constants import carl_position, daryl_position, exit_position, glen_position, maggie_position, rick_position, terrain_mapping
from utils import carregar_mapa_a_partir_do_txt, criar_mapa, marcar_caminho, encontrar_caminho, traduzir_caminho

# 1º passo: carregar o mapa da prisão em uma matriz
prison_map = carregar_mapa_a_partir_do_txt('prison_map.txt', terrain_mapping)

# 2º passo: definir a ordem de visitação dos personagens, com a posição de início e fim fixos
pontos_a_visitar = [rick_position, carl_position, daryl_position, glen_position, maggie_position, exit_position]

# 3º passo: encontrar o caminho entre os pontos de visitação, retornando o caminho como um dicionário e o custo total
caminho_completo, custo_total = encontrar_caminho(prison_map, pontos_a_visitar)

# Inicializar o mapa para cada caminho individual
mapa_atual = carregar_mapa_a_partir_do_txt('prison_map.txt', terrain_mapping)

# Iterar pelos trechos, marcando e criando um mapa separado para cada caminho
for i in range(len(pontos_a_visitar) - 1):
    ponto_inicial = pontos_a_visitar[i]
    ponto_final = pontos_a_visitar[i + 1]
    
    # Encontrar o caminho entre os dois pontos
    trecho, custo = encontrar_caminho(mapa_atual, [ponto_inicial, ponto_final])
    
    # Traduzir e imprimir o caminho
    print(f'> Gerando mapa para o caminho de {ponto_inicial} até {ponto_final}')
    traduzir_caminho(trecho)
    
    # Marcar o caminho no mapa
    marcar_caminho(mapa_atual, trecho)
    
    # Criar e mostrar o mapa para esse trecho
    criar_mapa(mapa_atual)

# Exibir o custo total do caminho completo
print(f'> Custo total do caminho completo: {custo_total}')

