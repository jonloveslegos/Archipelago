from BaseClasses import MultiWorld


def link_deltarune_areas(world: MultiWorld, player: int):
    for (exit, region) in mandatory_connections:
        world.get_entrance(exit, player).connect(world.get_region(region, player))


# (Region name, list of exits)
deltarune_regions = [
    ("Menu", ["New Game"]),
    ("Hub", ["Chapter 1 Entrance", "Chapter 2 Entrance", "Chapter 3 Entrance", "Chapter 4 Entrance"]),
    ("Chapter 1", ["CH1: Castle Town Entrance"]),
    ("CH1: Castle Town", ["CH1: Fields Entrance"]),
    ("CH1: Fields", ["CH1: Forest Entrance", "CH1: Fields Warp"]),
    ("CH1: Forest", ["CH1: Bake Sale Entrance", "CH1: Forest Warp"]),
    ("CH1: Bake Sale", ["CH1: Card Castle Entrance", "CH1: Bake Sale Warp", "CH1: Castle Warp"]),
    ("CH1: Card Castle", []),
    ("CH1: Warp Hub", ["CH1: Fields Warp Hub", "CH1: Forest Warp Hub", "CH1: Bake Sale Warp Hub", "CH1: Castle Warp Hub"]),
    ("Chapter 2", []),
    ("Chapter 3", []),
    ("Chapter 4", []),
]

# (Entrance, region pointed to)
mandatory_connections = [
    ("New Game", "Hub"),
    ("Chapter 1 Entrance", "Chapter 1"),
    ("Chapter 2 Entrance", "Chapter 2"),
    ("Chapter 3 Entrance", "Chapter 3"),
    ("Chapter 4 Entrance", "Chapter 4"),
    ("CH1: Castle Town Entrance", "CH1: Castle Town"),
    ("CH1: Fields Entrance", "CH1: Fields"),
    ("CH1: Forest Entrance", "CH1: Forest"),
    ("CH1: Bake Sale Entrance", "CH1: Bake Sale"),
    ("CH1: Card Castle Entrance", "CH1: Card Castle"),
    ("CH1: Castle Warp", "CH1: Warp Hub"),
    ("CH1: Fields Warp", "CH1: Warp Hub"),
    ("CH1: Forest Warp", "CH1: Warp Hub"),
    ("CH1: Bake Sale Warp", "CH1: Warp Hub"),
    ("CH1: Castle Warp Hub", "CH1: Bake Sale"),
    ("CH1: Fields Warp Hub", "CH1: Fields"),
    ("CH1: Forest Warp Hub", "CH1: Forest"),
    ("CH1: Bake Sale Warp Hub", "CH1: Bake Sale"),
]
