import logging
import os
import threading
import pkgutil
from typing import NamedTuple, Union, Dict, Any

import bsdiff4

import Utils
from BaseClasses import Item, Location, Region, Entrance, MultiWorld, ItemClassification, Tutorial
from .Items import item_table, KHDaysItem
from .Locations import location_table, KHDaysLocation
from .Options import khdays_options
from .Rules import set_rules
from worlds.AutoWorld import World, WebWorld
from worlds.generic.Rules import add_rule


class KHDaysWeb(WebWorld):
    theme = "stone"
    setup = Tutorial(
        "Multiworld Setup Tutorial",
        "A guide to setting up Kingdom Hearts Days for Archipelago on your computer.",
        "English",
        "multiworld_en.md",
        "multiworld/en",
        ["Mewlif"]
    )

    tutorials = [setup]


class KHDaysWorld(World):
    """
    Kingdom Hearts Days is a game for the Nintendo DS! Complete tasks for the Organization, to get rewards!
    You objective is to beat the final day and win the game!
    """
    option_definitions = khdays_options
    game = "Kingdom Hearts Days"
    topology_present = False
    data_version = 1
    base_id = 7000
    web = KHDaysWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = location_table

    def __init__(self, world: MultiWorld, player: int):
        super().__init__(world, player)
        self.generator_in_use = threading.Event()
        self.rom_name_available_event = threading.Event()
        self.levels = None
        self.filler_items = None

    def create_item(self, name: str):
        return KHDaysItem(name, item_table[name].classification, self.item_name_to_id[name], self.player)

    def create_event(self, event: str):
        return KHDaysItem(event, ItemClassification.progression, None, self.player)

    def create_location(self, name, id, parent, event=False):
        return_location = KHDaysLocation(self.player, name, id, parent)
        return_location.event = event
        return return_location

    def create_regions(self):
        menu = Region("Menu", self.player, self.multiworld)
        missions = Region("Missions", self.player, self.multiworld)

        for location in location_table:
            missions.locations.append(
                self.create_location(location, location_table[location], missions))
        begin_game = Entrance(self.player, "Begin Game", menu)
        menu.exits.append(begin_game)
        begin_game.connect(missions)
        self.multiworld.regions.append(menu)
        self.multiworld.regions.append(missions)

    def create_items(self):
        item_pool = []
        for (name) in item_table:
            for i in range(item_table[name].khdaysamount):
                item_pool += {self.create_item(name)}
        self.multiworld.itempool += item_pool

    # refer to Rules.py
    set_rules = set_rules

    def get_filler_item_name(self) -> str:
        if self.filler_items is None:
            self.filler_items = [item for item in item_table if item_table[item].classification == ItemClassification.filler]
        return self.multiworld.random.choice(self.filler_items)

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data = {}
        return slot_data
