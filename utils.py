import heapq
import numpy as np
from constants import EDIFICIO

def load_map_from_file(filename, terrain_mapping):
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    # Inicializa a matriz do mapa
    map_matrix = np.zeros((len(lines), len(lines[0].strip())), dtype=float)
    
    for i, line in enumerate(lines):
        for j, char in enumerate(line.strip()):
            map_matrix[i, j] = terrain_mapping[char]
    
    return map_matrix


def heuristic(a, b):
    # Distância Manhattan
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star_search(map, start, goal):
    # Inicializando a fronteira com o nó de início
    frontier = []
    heapq.heappush(frontier, (0, start))
    
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while frontier:
        current_cost, current = heapq.heappop(frontier)
        
        if current == goal:
            break
        
        for next in get_neighbors(map, current):
            new_cost = cost_so_far[current] + map[next[0]][next[1]]
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                heapq.heappush(frontier, (priority, next))
                came_from[next] = current
    
    return came_from, cost_so_far


def get_neighbors(map, current):
    neighbors = []
    x, y = current
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Movimentos verticais e horizontais
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < map.shape[0] and 0 <= ny < map.shape[1]:
            if map[nx, ny] != EDIFICIO:  # Rick não pode atravessar edifícios
                neighbors.append((nx, ny))
    
    return neighbors