from aocd import get_data

inp = get_data(day=20, year=2020)

import dataclasses
import enum
import functools
import math


Side = enum.IntEnum('Side', ['UP', 'RIGHT', 'DOWN', 'LEFT'], start=0)


@dataclasses.dataclass(frozen=True)
class Config:
  tile_id: int
  rotation: int
  h_flipped: bool
  v_flipped: bool


def generate_configs(tile_id: int):
  configs = []
  for rotation in range(4):
    for h_flipped in [False, True]:
      for v_flipped in [False, True]:
        configs.append(Config(tile_id, rotation, h_flipped, v_flipped))
  return configs


@functools.cache
def get_active(config: Config):
  tile_definition = tiles[config.tile_id]
  if config.h_flipped:
    tile_definition = [line[::-1] for line in tile_definition]
  if config.v_flipped:
    tile_definition = tile_definition[::-1]
  for _ in range(config.rotation):
    tile_definition = list(zip(*(line[::-1] for line in tile_definition)))
    
  return frozenset({(row, col) for row, line in enumerate(tile_definition) for col, c in enumerate(line) if c == '#'})


@functools.cache
def get_edges(config: Config):
  active = get_active(config)
  return (
    frozenset({col for row, col in active if row == 0}), # Up
    frozenset({row for row, col in active if col == 9}), # Right
    frozenset({col for row, col in active if row == 9}), # Down
    frozenset({row for row, col in active if col == 0})  # Left
  )


tiles = {}
for tile_string in inp.split('\n\n'):
  tile_id, *tile_definition = tile_string.splitlines()
  tile_id = int(tile_id[5:-1])
  tiles[tile_id] = tile_definition

connectivity = {} # tile_id: (max number of sides that could be connected at once)
for tile_id in tiles:
  edges = get_edges(Config(tile_id, 0, False, False))
  
  edges_other = set()
  for tile_id_other in tiles:
    if tile_id_other == tile_id:
      continue

    for config_other in generate_configs(tile_id_other):
      edges_other.update(get_edges(config_other))
    
  connectivity[tile_id] = sum(edge in edges_other for edge in edges)

corner_tile_ids = {tile_id for tile_id, connections in connectivity.items() if connections == 2}
answer = math.prod(corner_tile_ids)
print(answer)

def place(row, col, remaining_tile_ids, arrangement):
  if row == len(arrangement):
    return True

  col2 = col + 1
  row2 = row
  if col2 == len(arrangement[0]):
    col2 = 0
    row2 += 1
    
  possible_tiles = set(remaining_tile_ids)
  
  # Corner position must be a corner tile ID
  if row in [0, len(arrangement) - 1] and col in [0, len(arrangement[0]) - 1]:
    possible_tiles.intersection_update(corner_tile_ids)

  possible_configs = {config for tile_id in possible_tiles for config in generate_configs(tile_id)}
  
  # Sides must align with the tile above and the tile to the left
  if col > 0:
    possible_configs.intersection_update(side_to_config[(get_edges(arrangement[row][col - 1])[Side.RIGHT], Side.LEFT)])
  if row > 0:
    possible_configs.intersection_update(side_to_config[(get_edges(arrangement[row - 1][col])[Side.DOWN], Side.UP)])

  for config in possible_configs:
    arrangement[row][col] = config
    if place(row2, col2, remaining_tile_ids - {config.tile_id}, arrangement):
      return True

  return False


side_to_config = {} # (edge, side): [config, ...]
for tile_id in tiles:
  for config in generate_configs(tile_id):
    for edges, side in zip(get_edges(config), Side):
      side_to_config[(edges, side)] = side_to_config.get((edges, side), frozenset()).union({config})

tiles_per_side = int(math.sqrt(len(tiles)))
arrangement = [[None for _ in range(tiles_per_side)] for _ in range(tiles_per_side)]
place(0, 0, frozenset(tiles), arrangement) # < 1 second

active = set()
for row, line in enumerate(arrangement):
  for col, config in enumerate(line):
    active.update({(r - 1 + 8 * row, c - 1 + 8 * col) for r, c in get_active(config) if r not in [0, 9] and c not in [0, 9]})

tiles['monster'] = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''.splitlines()

target_configs = generate_configs('monster')
target_actives = [get_active(config) for config in target_configs]

monster = set()
for row in range(tiles_per_side * 8):
  for col in range(tiles_per_side * 8):
    for target in target_actives:
      offset_target = {(r + row, c + col) for r, c in target}
      if offset_target.issubset(active):
        monster.update(offset_target)

answer = len(active) - len(monster)
print(answer)
