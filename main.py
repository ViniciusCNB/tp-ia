from utils import load_map_from_file
import constants


prison_map = load_map_from_file('prison_map.txt', constants.terrain_mapping)

for row in prison_map:
    print(row)
