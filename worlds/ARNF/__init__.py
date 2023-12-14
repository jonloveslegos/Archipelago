import logging
import random
import string

from typing import List, Dict

from BaseClasses import Region, Entrance, Item, ItemClassification, MultiWorld, Tutorial
from worlds.AutoWorld import WebWorld, World
from worlds.generic.Rules import set_rule
from .Items import ARNFItem, item_table, item_data_table, normal_item_prefix, classic_boss_rush_item_prefix
from .Locations import ARNFLocation, location_table, get_ordered_item_pickups, normal_total_locations, classic_boss_rush_total_locations
from .Options import ARNFOptions
from .Regions import region_data_table


class ARNFWebWorld(WebWorld):
    theme = "dirt"
    tutorials = [
        Tutorial(
            tutorial_name="Start Guide",
            description="A guide to playing A Robot Named Fight!",
            language="English",
            file_name="guide_en.md",
            link="guide/en",
            authors=["Beta Sprite"]
        )
    ]


class ARNFWorld(World):
    """A Robot Named Fight is a Metroidvania roguelike focused on exploration and item collection.
    Explore a different, procedurally-generated labyrinth each time you play and discover randomized
    power-ups to traverse obstacles, find secrets and explode meat beasts."""

    game = "A Robot Named Fight!"
    web = ARNFWebWorld()
    options_dataclass = ARNFOptions
    options: ARNFOptions
    topology_present = False
    
    item_name_to_id = item_table
    location_name_to_id = location_table


    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)


    def create_item(self, name: int) -> ARNFItem:
        item_id = item_table[name]
        classification = ItemClassification.filler
        item = ARNFItem(name, classification, item_id, self.player)
        return item


    def create_items(self) -> None:
        #Initialize item pool
        item_pool: List[ARNFItem] = []
        logger = logging.getLogger()
        
        #Generate the items
        for name, item in item_data_table.items():
            if (    (name.startswith(normal_item_prefix) and self.options.normal_included.value == 1) or
                    (name.startswith(classic_boss_rush_item_prefix) and self.options.classic_boss_rush_included.value == 1)):
                item_pool.append(self.create_item(name))
        
        logger.info(item_pool)
        
        self.multiworld.itempool += item_pool


    def get_filler_item_name(self) -> str:
        if not self.junk_pool:
            self.junk_pool = self.create_junk_pool()
        weights = [data for data in self.junk_pool.values()]
        filler = self.multiworld.random.choices([filler for filler in self.junk_pool.keys()], weights,
                                                k=1)[0]
        return filler


    def create_junk_pool(self) -> Dict:
        pool_option = self.options.item_weights.value
        junk_pool: Dict[str, int] = {}
        junk_pool = item_pool_weights[pool_option].copy()
        return junk_pool


    def create_regions(self) -> None:
        menu = create_region(self.multiworld, self.player, "Menu")
        self.multiworld.regions.append(menu)
        # By using a victory region, we can define it as being connected to by several regions
        #   which can then determine the availability of the victory.
        victory_region = create_region(self.multiworld, self.player, "Victory")
        self.multiworld.regions.append(victory_region)
        ace_items = get_ordered_item_pickups(self.options.normal_included.value, self.options.classic_boss_rush_included.value)
        # shuffled = list(ace_items.values())
        # random.shuffle(shuffled)
        # shuffled_items = dict(zip(ace_items, shuffled))
        logger = logging.getLogger()
        logger.info(ace_items)
        planet = create_region(self.multiworld, self.player, "NormalMode", ace_items)
        self.multiworld.regions.append(planet)

        # can get to victory from the beginning of the game
        to_victory = Entrance(self.player, "beating game", planet)
        planet.exits.append(to_victory)
        to_victory.connect(victory_region)

        connection = Entrance(self.player, "Lobby", menu)
        menu.exits.append(connection)
        connection.connect(planet)
        
        create_events(self.multiworld, self.player)


    def fill_slot_data(self):
        options_dict = self.options.as_dict("normal_included", "classic_boss_rush_included", "start_with_explorb", "death_link", casing="camel")
        logger = logging.getLogger()
        logger.info(options_dict)
        return options_dict


    def set_rules(self) -> None:
        # set_rule(self.multiworld.get_location("Victory", self.player),
             # lambda state: state.can_reach(f"VictoryCheck", "Location", self.player))
        
        # Win Condition
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)


def create_events(world: MultiWorld, player: int) -> None:
    world_region = world.get_region("NormalMode", player)
    victory_region = world.get_region("Victory", player)
    victory_event = ARNFLocation(player, "Victory", None, victory_region)
    victory_event.place_locked_item(ARNFItem("Victory", ItemClassification.progression, None, player))
    world_region.locations.append(victory_event)


def create_region(world: MultiWorld, player: int, name: str, locations: Dict[str, int] = {}) -> Region:
    ret = Region(name, player, world)
    for location_name, location_id in locations.items():
        ret.locations.append(ARNFLocation(player, location_name, location_id, ret))
    return ret