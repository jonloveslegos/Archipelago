import logging
import random
import string

from typing import List, Dict

from BaseClasses import Region, Entrance, Item, ItemClassification, MultiWorld, Tutorial
from worlds.AutoWorld import WebWorld, World
from worlds.generic.Rules import set_rule
from .Items import ARNFItem, item_table, item_data_table
from .Locations import ARNFLocation, location_data_table, location_table, locked_locations
from .Constants import normal_item_prefix, progression_item_prefix, normal_total_locations
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


    def create_item(self, name: str) -> ARNFItem:
        return ARNFItem(name = name, classification = item_data_table[name].type, code = item_data_table[name].code, player = self.player)
        # item_id = item_table[name]
        # classification = ItemClassification.filler
        # item = ARNFItem(name, classification, item_id, self.player)
        # return item


    def create_items(self) -> None:
        #Initialize item pool
        item_pool: List[ARNFItem] = []
        logger = logging.getLogger()
        
        #Generate the items
        for name, item in item_data_table.items():
            if (    (name.startswith(normal_item_prefix) and self.options.game_mode.value == 1) or
                    (name.startswith(progression_item_prefix) ) ):
                # or
                # (name.startswith(classic_boss_rush_item_prefix) and self.options.game_mode.value == 2) or 
                # (name.startswith(exterminator_item_prefix) and self.options.game_mode.value == 4)):
                item_pool.append(self.create_item(name))
        
        self.multiworld.itempool += item_pool


    def get_filler_item_name(self) -> str:
        return "FillerItem"


    def create_junk_pool(self) -> Dict:
        pool_option = self.options.item_weights.value
        junk_pool: Dict[str, int] = {}
        junk_pool = item_pool_weights[pool_option].copy()
        return junk_pool


    def create_regions(self) -> None:
        logger = logging.getLogger()
        
        # Create regions.
        for region_name in region_data_table.keys():
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        # Create locations.
        for region_name, region_data in region_data_table.items():
            region = self.multiworld.get_region(region_name, self.player)
            region.add_locations({
                location_name: location_data.address for location_name, location_data in location_data_table.items()
                if location_data.region == region_name and location_data.can_create(self.multiworld, self.player)
            }, ARNFLocation)
            region.add_exits(region_data_table[region_name].connecting_regions)

        # logger.info(f"locked_locations: {locked_locations}")

        # Place locked locations.
        for location_name, location_data in locked_locations.items():
            # Ignore locations we never created.
            if not location_data.can_create(self.multiworld, self.player):
                continue

            locked_item = self.create_item(location_data_table[location_name].locked_item)
            logger.info(f"locked_item: {locked_item}")
            self.multiworld.get_location(location_name, self.player).place_locked_item(locked_item)
        
        # logger.info(f"location_data_table: {location_data_table}")
        
        # menu = create_region(self.multiworld, self.player, "Menu")
        # self.multiworld.regions.append(menu)
        # # By using a victory region, we can define it as being connected to by several regions
        # #   which can then determine the availability of the victory.
        # victory_region = create_region(self.multiworld, self.player, "Victory")
        # self.multiworld.regions.append(victory_region)
        # ace_items = get_ordered_item_pickups(self.options.game_mode.value)
        # logger = logging.getLogger()
        # logger.info(ace_items)
        # planet = create_region(self.multiworld, self.player, "NormalMode", ace_items)
        # self.multiworld.regions.append(planet)

        # # can get to victory from the beginning of the game
        # to_victory = Entrance(self.player, "beating game", planet)
        # planet.exits.append(to_victory)
        # to_victory.connect(victory_region)

        # connection = Entrance(self.player, "Lobby", menu)
        # menu.exits.append(connection)
        # connection.connect(planet)
        
        # create_events(self.multiworld, self.player)


    def fill_slot_data(self):
        options_dict = self.options.as_dict("game_mode", "grant_achievements_mode", "start_with_explorb", "start_with_master_map", "start_with_wall_jump", "death_link", casing="camel")
        logger = logging.getLogger()
        logger.info(options_dict)
        return options_dict


    def set_rules(self) -> None:
        # set_rule(self.multiworld.get_location("Victory", self.player),
             # lambda state: state.can_reach(f"VictoryCheck", "Location", self.player))
        
        # Win Condition
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)


# def create_events(world: MultiWorld, player: int) -> None:
    # world_region = world.get_region("NormalMode", player)
    # victory_region = world.get_region("Victory", player)
    # victory_event = ARNFLocation(player, "Victory", None, victory_region)
    # victory_event.place_locked_item(ARNFItem("Victory", ItemClassification.progression, None, player))
    # world_region.locations.append(victory_event)


# def create_region(world: MultiWorld, player: int, name: str, locations: Dict[str, int] = {}) -> Region:
    # ret = Region(name, player, world)
    # for location_name, location_id in locations.items():
        # ret.locations.append(ARNFLocation(player, location_name, location_id, ret))
    # return ret