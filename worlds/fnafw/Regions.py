
def link_FNaFW_structures(world, player):
    for (exit, region) in mandatory_connections:
        world.get_entrance(exit, player).connect(world.get_region(region, player))


# (Region name, list of exits)
FNaFW_regions = [
    ("Menu", ["New Game"]),
    ("World", []),
    # ("Fazbear Hills South", ["Fazbear Hills South -> Choppy's Woods", "Fazbear Hills South -> Lilygear Lake"]),
    # ("Choppy's Woods", ["Choppy's Woods -> Mysterious Mine South", "Choppy's Woods -> Dusting Fields"]),
    # ("Lilygear Lake", ["Lilygear Lake -> Fazbear Hills North", "Lilygear Lake -> Blacktomb Yard", "Lilygear Lake -> Pinwheel Circus South"]),
    # ("Pinwheel Circus South", []),
    # ("Pinwheel Circus North", ["Pinwheel Circus North -> Pinwheel Circus South", "Pinwheel Circus North -> Pinwheel Funhouse"]),
    # ("Pinwheel Funhouse", []),
    # ("Mysterious Mine South", []),
    # ("Mysterious Mine North", []),
    # ("Mysterious Mine West", []),
    # ("Blacktomb Yard", ["Blacktomb Yard -> Deep-Metal Mine"]),
    # ("Deep-Metal Mine", ["Deep-Metal Mine -> Pinwheel Circus North"]),
    # ("Fazbear Hills North", ["Fazbear Hills North -> Mysterious Mine North"]),
    # ("Dusting Fields", ["Dusting Fields -> Mysterious Mine West"]),
]

# (Entrance, region pointed to)
mandatory_connections = [
    ("New Game", "World"),
    # ("New Game", "Fazbear Hills"),
    # ("Fazbear Hills South -> Choppy's Woods", "Choppy's Woods"),
    # ("Fazbear Hills South -> Lilygear Lake", "Lilygear Lake"),
    # ("Choppy's Woods -> Mysterious Mine South", "Mysterious Mine South"),
    # ("Choppy's Woods -> Dusting Fields", "Dusting Fields"),
    # ("Lilygear Lake -> Fazbear Hills North", "Fazbear Hills North"),
    # ("Lilygear Lake -> Blacktomb Yard", "Blacktomb Yard"),
    # ("Lilygear Lake -> Pinwheel Circus South", "Pinwheel Circus South"),
    # ("Pinwheel Circus North -> Pinwheel Circus South", "Pinwheel Circus South"),
    # ("Pinwheel Circus North -> Pinwheel Funhouse", "Pinwheel Funhouse"),
    # ("Blacktomb Yard -> Deep-Metal Mine", "Deep-Metal Mine"),
    # ("Deep-Metal Mine -> Pinwheel Circus North", "Pinwheel Circus North"),
    # ("Fazbear Hills North -> Mysterious Mine North", "Mysterious Mine North"),
    # ("Dusting Fields -> Mysterious Mine West", "Mysterious Mine West"),
]
