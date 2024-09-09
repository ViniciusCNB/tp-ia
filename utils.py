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

    return caminho_final


# Plota a matriz do mapa como um heatmap usando matplotlib e seaborn, com cores personalizadas.
def plot_map(prison_map, caminho=None):
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


# Função para marcar o caminho no mapa
def mark_path_on_map(prison_map, path):
    for (x, y) in path:
        prison_map[x][y] = -1