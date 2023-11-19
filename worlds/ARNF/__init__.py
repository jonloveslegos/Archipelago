import string
import logging

from typing import List, Dict

from BaseClasses import Region, Entrance, Item, ItemClassification, MultiWorld, Tutorial
from worlds.AutoWorld import WebWorld, World
from .Items import ARNFItem, item_table, item_pool_weights
from .Locations import ARNFLocation, location_table
from .Options import ARNFOptions
from .Regions import region_data_table
#from .Rules import get_button_rule



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
        logger = logging.getLogger()
        logger.info(f'self.player: {self.player}')
        item = ARNFItem(name, classification, item_id, self.player)
        return item

    def create_items(self) -> None:
        # Generate item pool
        itempool: List = []
        
        total_locations = self.options.total_locations.value
        
        # Create junk items
        self.junk_pool = self.create_junk_pool()
        
        # Fill remaining items with randomly generated junk
        while len(itempool) < total_locations:
            itempool.append(self.get_filler_item_name())

        # Convert itempool into real items
        itempool = list(map(lambda name: self.create_item(name), itempool))
        self.multiworld.itempool += itempool
        
        # total_locations = self.options.total_locations.value
        # itempool: List = []
        # item_pool: List[ARNFItem] = []
        # while len(item_pool) < total_locations:
            # item_pool.append(self.get_filler_item_name())
        # for i in range(1, 47):
            # item_pool.append(self.create_item(i))
        # self.multiworld.item_pool += item_pool

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
        # Create regions.
        for region_name in region_data_table.keys():
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        # Create locations.
        # for region_name, region_data in region_data_table.items():
            # region = self.multiworld.get_region(region_name, self.player)
            # region.add_locations({
                # location_name: location_data.address for location_name, location_data in location_data_table.items()
                # if location_data.region == region_name and location_data.can_create(self.multiworld, self.player)
            # }, CliqueLocation)
            # region.add_exits(region_data_table[region_name].connecting_regions)

    # def set_rules(self) -> None:
        # set_rules(self.multiworld, self.player)

    def fill_slot_data(self):
        return {
            "color": getattr(self.multiworld, "color")[self.player].current_key
        }

class ARNFItem(Item):
    game = "A Robot Named Fight!"
    type: str

    def __init__(self, name, classification, type: str, code, player: int):
        super(ARNFItem, self).__init__(name, classification, code, player)
        self.type = type
