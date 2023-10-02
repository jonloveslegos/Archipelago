
def link_FNaFW_structures(world, player):
    for (exit, region) in mandatory_connections:
        world.get_entrance(exit, player).connect(world.get_region(region, player))


# (Region name, list of exits)
FNaFW_regions = [
    ('Menu', ['New Game']),
    ('World', []),
]

# (Entrance, region pointed to)
mandatory_connections = [
    ('New Game', 'World'),
]
