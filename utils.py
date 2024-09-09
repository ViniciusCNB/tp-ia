import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from queue import PriorityQueue
from matplotlib.colors import ListedColormap


def load_map_from_file(filename, terrain_mapping):
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    # Inicializa a matriz do mapa
    map_matrix = np.zeros((len(lines), len(lines[0].strip())), dtype=float)
    
    for i, line in enumerate(lines):
        for j, char in enumerate(line.strip()):
            map_matrix[i, j] = terrain_mapping[char]
    
    return map_matrix


def h_score(atual, destino):
    # Função heurística: distância Manhattan 
    return abs(atual[0] - destino[0]) + abs(atual[1] - destino[1])


def aestrela(matriz, inicio, destino):
    rows = len(matriz)
    cols = len(matriz[0])
    
    # Inicializar f_score e g_score com valores infinitos
    f_score = { (i, j): float('inf') for i in range(rows) for j in range(cols) }
    g_score = { (i, j): float('inf') for i in range(rows) for j in range(cols) }
    
    # Configurar valores iniciais
    g_score[inicio] = 0
    f_score[inicio] = h_score(inicio, destino)
    
    # Inicializar a fila de prioridade
    fila = PriorityQueue()
    fila.put((f_score[inicio], inicio))
    
    # Para armazenar o caminho
    caminho = {}
    
    while not fila.empty():
        _, atual = fila.get()

        # Verifica se o destino foi alcançado
        if atual == destino:
            break

        # Explorar vizinhos (cima, baixo, esquerda, direita)
        vizinhos = [
            (atual[0] - 1, atual[1]), # cima
            (atual[0] + 1, atual[1]), # baixo
            (atual[0], atual[1] - 1), # esquerda
            (atual[0], atual[1] + 1)  # direita
        ]
        
        for vizinho in vizinhos:
            linha, coluna = vizinho
            # Verificar se a posição do vizinho é válida e acessível
            if 0 <= linha < rows and 0 <= coluna < cols and matriz[linha][coluna] != float('inf'):
                # Calcular g_score do vizinho
                custo = matriz[linha][coluna]
                novo_g_score = g_score[atual] + custo
                
                if novo_g_score < g_score[vizinho]:
                    g_score[vizinho] = novo_g_score
                    f_score[vizinho] = novo_g_score + h_score(vizinho, destino)
                    fila.put((f_score[vizinho], vizinho))
                    caminho[vizinho] = atual

    # Reconstruir o caminho do destino ao início
    caminho_final = {}
    celula_analisada = destino
    if celula_analisada in caminho:
        while celula_analisada != inicio:
            caminho_final[caminho[celula_analisada]] = celula_analisada
            celula_analisada = caminho[celula_analisada]

    # Retornar tanto o caminho quanto o custo total do caminho
    custo_total = g_score[destino] if destino in g_score else float('inf')
    return caminho_final, custo_total


def encontrar_caminho(prison_map, pontos):
    caminho_completo = {}
    custo_total = 0
    

    # Itera sobre os pontos na ordem especificada
    for i in range(len(pontos) - 1):
        ponto_inicial = pontos[i]
        ponto_final = pontos[i + 1]

        # Chama a função A* para cada trecho entre os pontos consecutivos
        trecho, custo = aestrela(prison_map, ponto_inicial, ponto_final)

        # Adiciona o trecho ao caminho completo
        # O trecho é um dicionário onde a chave é a célula atual e o valor é a célula anterior
        caminho_completo.update(trecho)
        custo_total += custo
        
    return caminho_completo, custo_total


# Plota a matriz do mapa como um heatmap usando matplotlib e seaborn, com cores personalizadas.
def plot_map(prison_map, caminho=None):
    # Definir o mapeamento de cores de acordo com os valores
    colors = ['yellow', '#7f7f7f', '#948a54', '#9bbb59','#d9d9d9', '#d9d9d9']  # cores para os valores
    cmap = ListedColormap(colors)

    # Definir os limites para o colorbar (cada limite corresponde a uma cor)
    bounds = [-1, 1, 3, 5, 10, float('inf')]  # limites baseados nos valores
    norm = plt.Normalize(vmin= -1, vmax=10)  # Normaliza os valores de 0 a 10

    # Plota o mapa com o colormap personalizado
    plt.figure(figsize=(20, 20))  # Define o tamanho do gráfico
    sns.heatmap(prison_map, cmap=cmap, annot=True, cbar=False, square=True, linewidths=0.5, linecolor='black',
                norm=norm, cbar_kws={'ticks': [-1, 1, 3, 5, 10]})  # Define os ticks do colorbar

    plt.title("Mapa de Prisão com Custos e Cores Personalizadas")
    plt.show()


# Função para marcar o caminho no mapa
def mark_path_on_map(prison_map, path):
    for (x, y) in path:
        prison_map[x][y] = -1


def trace_path(path_dict):
    # Encontrar o ponto de partida: aquele que não é valor de nenhum par
    start = None
    for key in path_dict:
        if key not in path_dict.values():
            start = key
            break

    # Caso não encontre um ponto inicial
    if start is None:
        print("Caminho inválido: não foi possível encontrar um ponto inicial.")
        return

    # Traçar o caminho
    path = [start]
    while start in path_dict:
        start = path_dict[start]
        path.append(start)

    # Exibir o caminho de forma legível
    for i, step in enumerate(path):
        print(f"Passo {i + 1}: {step}")
