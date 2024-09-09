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
rick_position = (20, 12)  # Posição de início - Refeitório
carl_position = (5, 32)
daryl_position = (35, 35)
glen_position = (32, 8)
maggie_position = (13, 31)
exit_position = (41, 21)  # Porta de saída