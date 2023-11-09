from typing import List

from BaseClasses import Region, Tutorial
from worlds.AutoWorld import WebWorld, World
from .Items import ARNFItem, item_data_table, item_table
from .Locations import ARNFLocation, location_data_table, location_table, locked_locations
from .Options import arnf_options
from .Regions import region_data_table
from .Rules import get_button_rule


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
    data_version = 3
    web = ARNFWebWorld()
    option_definitions = arnf_options
    location_name_to_id = location_table
    item_name_to_id = item_table

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)

    def create_item(self, name: str) -> ARNFItem:
        return ARNFItem(name, item_data_table[name].type, item_data_table[name].code, self.player)

    def create_items(self) -> None:
        item_pool: List[ARNFItem] = []
        for name, item in item_data_table.items():
            if item.code and item.can_create(self.multiworld, self.player):
                item_pool.append(self.create_item(name))

        self.multiworld.itempool += item_pool

    def create_regions(self) -> None:
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
            }, CliqueLocation)
            region.add_exits(region_data_table[region_name].connecting_regions)

    def get_filler_item_name(self) -> str:
        return "A Cool Filler Item (No Satisfaction Guaranteed)"

    def set_rules(self) -> None:
        set_rules(self.multiworld, self.player)

    def fill_slot_data(self):
        return {
            "color": getattr(self.multiworld, "color")[self.player].current_key
        }

class ARNFItem(Item):
    game = "A Robot Named Fight!"
    type: int

    def __init__(self, name, classification, type: str, code, player: int):
        super(SMItem, self).__init__(name, classification, code, player)
        self.type = type
