import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from queue import PriorityQueue
from matplotlib.colors import ListedColormap


def carregar_mapa_a_partir_do_txt(nome_arquivo, mapeamento_do_terreno):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        
    # Inicializa a matriz do mapa
    matriz_do_mapa = np.zeros((len(linhas), len(linhas[0].strip())), dtype=float)
    
    for i, linha in enumerate(linhas):
        for j, char in enumerate(linha.strip()):
            matriz_do_mapa[i, j] = mapeamento_do_terreno[char]
    
    return matriz_do_mapa


def h_score(atual, destino):
    # Função heurística: distância Manhattan 
    return abs(atual[0] - destino[0]) + abs(atual[1] - destino[1])


def a_estrela(matriz, inicio, destino):
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


def encontrar_caminho(mapa_prisao, pontos):
    caminho_completo = {}
    custo_total = 0
    
    for i in range(len(pontos) - 1):
        ponto_inicial = pontos[i]
        ponto_final = pontos[i + 1]

        # Chama a função A* para cada trecho entre os pontos consecutivos
        trecho_invertido, custo = a_estrela(mapa_prisao, ponto_inicial, ponto_final)
        
        trecho = inverter_dicionario(trecho_invertido)

        # Adiciona o trecho ao caminho completo
        caminho_completo.update(trecho)
        custo_total += custo
        
        # Marca o caminho e cria o mapa
        mapa_com_caminho = mapa_prisao.copy()  # Cria uma cópia do mapa
        marcar_caminho(mapa_com_caminho, trecho)
        
        # Criar título com o custo total do trecho
        titulo = f"Mapa do trecho {i + 1}, de {ponto_inicial} até {ponto_final} (Custo: {custo})"
        criar_mapa(mapa_com_caminho, titulo)  # Agora está passando o título

        # Printando os passos do caminho e o custo
        print(f"\n\n> Passos do trecho {i + 1}, de {ponto_inicial} até {ponto_final} (Custo: {custo})\n")
        custo_parcial = 0
        chaves_trecho = list(trecho.keys())
        for index, passo in enumerate(chaves_trecho[1:]):
            custo_parcial += mapa_prisao[passo[0], passo[1]]
            print(f"Passo {index + 1}: {passo}, Custo Acumulado: {custo_parcial}")
        
        # Para obter a última casa do caminho:
        print(f"Passo {len(trecho)}: {list(trecho.values())[-1]}, Custo Acumulado: {custo_parcial + mapa_prisao[chaves_trecho[-1][0], chaves_trecho[-1][1]]}")
    
    print(f"\n> Custo Total: {custo_total}")
    
    plt.show()  # Exibe todos os mapas ao final
    

def criar_mapa(mapa_prisao, titulo):
    # Definir o mapeamento de cores de acordo com os valores
    cores = ['yellow', '#7f7f7f', '#948a54', '#9bbb59', '#d9d9d9', '#d9d9d9']  # cores para os valores
    cmap = ListedColormap(cores)

    # Definir os limites para o colorbar (cada limite corresponde a uma cor)
    norm = plt.Normalize(vmin=-1, vmax=10)  # Normaliza os valores de 0 a 10

    # Plota o mapa com o colormap personalizado
    plt.figure(figsize=(10, 10))  # Define o tamanho do gráfico
    sns.heatmap(mapa_prisao, 
                cmap=cmap,
                annot=True, 
                cbar=False, 
                square=True, 
                linewidths=0.5, 
                linecolor='black',
                norm=norm, 
                annot_kws={'fontsize': 7})  # Define os ticks do colorbar

    plt.title(titulo)


# Função para marcar o caminho no mapa
def marcar_caminho(mapa_prisao, caminho):
    for (x, y) in list(caminho.keys())[1:]:
        mapa_prisao[x][y] = -1
    # Para marcar a última casa do trecho
    mapa_prisao[list(caminho.values())[-1][0]][list(caminho.values())[-1][1]] = -1


def inverter_dicionario(dicionario):
    # Converte o dicionário em uma lista de tuplas (chave, valor)
    lista_itens = list(dicionario.items())
    
    # Inverte a ordem da lista
    lista_invertida = lista_itens[::-1]
    
    # Reconstrói o dicionário a partir da lista invertida
    dicionario_invertido = dict(lista_invertida)
    
    return dicionario_invertido