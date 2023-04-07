import logging
import os
import threading
import pkgutil
from typing import NamedTuple, Union, Dict, Any

import bsdiff4

import Utils
from BaseClasses import Item, Location, Region, Entrance, MultiWorld, ItemClassification, Tutorial
from .Items import item_table, KHDaysItem, character_list
from .Locations import location_table, KHDaysLocation
from .Options import khdays_options
from .Rules import set_rules, set_completion_rules
from worlds.AutoWorld import World, WebWorld
from worlds.generic.Rules import add_rule
from worlds.LauncherComponents import Component, components

components.append(Component("KHDays Client", "KingdomHeartsDaysClient"))


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
    Your objective is to beat the final day and win the game!
    """
    option_definitions = khdays_options
    game = "Kingdom Hearts Days"
    topology_present = False
    data_version = 0
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

    def create_regions(self):
        menu = Region("Menu", self.player, self.multiworld)
        missions = Region("Missions", self.player, self.multiworld)

        missions.locations = [KHDaysLocation(self.player, loc_name, loc_data, missions)
                           for loc_name, loc_data in location_table.items()]
        for item in missions.locations:
            if "Block-Retreat" in item.name:
                item.progress_type = Location.progress_type.EXCLUDED
            if "Auto-Block" in item.name:
                item.progress_type = Location.progress_type.EXCLUDED
            if "Charge Ring" in item.name:
                item.progress_type = Location.progress_type.EXCLUDED
            if "Eternal Ring" in item.name:
                item.progress_type = Location.progress_type.EXCLUDED
            if "Nothing to Fear" in item.name:
                item.progress_type = Location.progress_type.EXCLUDED
            if "Down to Earth" in item.name:
                item.progress_type = Location.progress_type.EXCLUDED
            if "Lose Your Illusion" in item.name:
                item.progress_type = Location.progress_type.EXCLUDED
            if "Sighing of the Moon" in item.name:
                item.progress_type = Location.progress_type.EXCLUDED
            if "Parting of Waters" in item.name:
                item.progress_type = Location.progress_type.EXCLUDED
            if "Test of Time" in item.name:
                item.progress_type = Location.progress_type.EXCLUDED
            if "Flowers Athirst" in item.name:
                item.progress_type = Location.progress_type.EXCLUDED
            if "Dying of the Light" in item.name:
                item.progress_type = Location.progress_type.EXCLUDED
        begin_game = Entrance(self.player, "Begin Game", menu)
        menu.exits.append(begin_game)
        begin_game.connect(missions)
        self.multiworld.regions.append(menu)
        self.multiworld.regions.append(missions)

    def generate_basic(self):
        item_pool = []
        chosen_char = character_list[self.multiworld.StartingCharacter[self.player]]
        for (name) in item_table:
            if name == "Potion":
                for i in range(item_table[name].khdaysamount - 19):
                    item_pool += [self.create_item(name)]
            elif name != chosen_char:
                for i in range(item_table[name].khdaysamount):
                    item_pool += [self.create_item(name)]
        
        for (name) in location_table:
            if location_table[name] is None:
                event_item = self.create_event(name)
                self.multiworld.get_location(name, self.player).place_locked_item(event_item)

        self.multiworld.push_precollected(self.create_item(chosen_char))
        for i in range(len(location_table) - len(item_pool) - len(Items.days) - len(self.multiworld.precollected_items[self.player])):
            item_pool += [self.create_item("Potion")]
        self.multiworld.itempool += item_pool

    def set_rules(self):
        set_rules(self.multiworld, self.player)
        set_completion_rules(self.multiworld, self.player)

    def get_filler_item_name(self) -> str:
        if self.filler_items is None:
            self.filler_items = [item for item in item_table if item_table[item].classification == ItemClassification.filler]
        return self.multiworld.random.choice(self.filler_items)

    def fill_slot_data(self) -> Dict[str, Any]:
        return {
            "day_requirement": self.multiworld.DayRequirement[self.player].value,
            'starting_character': self.multiworld.StartingCharacter[self.player].current_key,
        }
