from BaseClasses import MultiWorld


def link_deltarune_areas(world: MultiWorld, player: int):
    for (exit, region) in mandatory_connections:
        world.get_entrance(exit, player).connect(world.get_region(region, player))


# (Region name, list of exits)
deltarune_regions = [
    ("Menu", ["New Game", "??? Exit"]),
    ("???", []),
]

# (Entrance, region pointed to)
mandatory_connections = [
    ("??? Exit", "???"),
]
