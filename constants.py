# Constantes de terreno
ASFALTO = 1
TERRA = 3
GRAMA = 5
PARALELEPIPEDO = 10
EDIFICIO = float('inf')

# Mapeamento dos caracteres para os custos
terrain_mapping = {
    '1': ASFALTO,
    '3': TERRA,
    '5': GRAMA,
    '9': PARALELEPIPEDO,
    'X': EDIFICIO
}

# Posições dos personagens e saída
rick_position = (21, 13)  # Posição de início - Refeitório
carl_position = (6, 33)
daryl_position = (36, 36)
glen_position = (33, 9)
maggie_position = (14, 32)
exit_position = (41, 13)  # Porta de saída