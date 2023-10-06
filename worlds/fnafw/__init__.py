import os

import BaseClasses
from .Items import FNaFWItem, item_table, start_anim_table, strong_anim_table, halloween_anim_table
from .Locations import FNaFWLocations, location_table, exclusion_table
from .Regions import FNaFW_regions, link_FNaFW_structures
from .Rules import set_rules, set_completion_rules

from BaseClasses import Region, Entrance, Item, Tutorial
from .Options import FNaFW_options
from worlds.AutoWorld import World, WebWorld
from worlds.AutoWorld import World, WebWorld
from worlds.LauncherComponents import Component, components, Type
from multiprocessing import Process
import math


def run_client():
    print('running fnafw client')
    from .FNaFWorldClient import main  # lazy import
    p = Process(target=main)
    p.start()


# components.append(Component("FNaF World Client", "FNaFWorldClient"))
components.append(Component("FNaF World Client", func=run_client))

client_version = 7


class FNaFWWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Tutorial",
        "A guide to setting up the Archipelago FNaFW software on your computer. This guide covers "
        "single-player, multiworld, and related software.",
        "English",
        "fnafw_en.md",
        "fnafw/en",
        ["Mewlif"]
    )]


class FNaFWWorld(World):
    """
    Freddy Fazbear's Pizzeria Simulator is a horror game where animatronics come through vents into your office
    to kill you. You win if you complete night 5 with all 4 animatronics obtained in your world to get the true ending.
    """
    game = "FNaFW"
    web = FNaFWWeb()
    option_definitions = FNaFW_options
    topology_present = True

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.id for name, data in location_table.items()}

    data_version = 4

    def _get_FNaFW_data(self):
        return {
            'world_seed': self.multiworld.per_slot_randoms[self.player].getrandbits(32),
            'seed_name': self.multiworld.seed_name,
            'player_name': self.multiworld.get_player_name(self.player),
            'player_id': self.player,
            'client_version': client_version,
            'race': self.multiworld.is_race
        }

    def create_items(self):
        # Generate item pool
        itempool = []

        # Add all required progression items
        for name, item in item_table.items():
            itempool += [name]
        itempool += ["Progressive Endoskeleton"] * 2

        chosen_anim = self.multiworld.random.choice([item for item in start_anim_table if item in itempool])
        self.multiworld.get_location("Freddy", self.player).place_locked_item(self.create_item(itempool.pop(itempool.index(chosen_anim))))
        chosen_anim = self.multiworld.random.choice([item for item in start_anim_table if item in itempool])
        self.multiworld.get_location("Bonnie", self.player).place_locked_item(self.create_item(itempool.pop(itempool.index(chosen_anim))))
        chosen_anim = self.multiworld.random.choice([item for item in start_anim_table if item in itempool])
        self.multiworld.get_location("Chica", self.player).place_locked_item(self.create_item(itempool.pop(itempool.index(chosen_anim))))
        chosen_anim = self.multiworld.random.choice([item for item in start_anim_table if item in itempool])
        self.multiworld.get_location("Foxy", self.player).place_locked_item(self.create_item(itempool.pop(itempool.index(chosen_anim))))
        chosen_anim = self.multiworld.random.choice([item for item in start_anim_table if item in itempool])
        self.multiworld.get_location("Toy Bonnie", self.player).place_locked_item(self.create_item(itempool.pop(itempool.index(chosen_anim))))
        chosen_anim = self.multiworld.random.choice([item for item in start_anim_table if item in itempool])
        self.multiworld.get_location("Toy Chica", self.player).place_locked_item(self.create_item(itempool.pop(itempool.index(chosen_anim))))
        chosen_anim = self.multiworld.random.choice([item for item in start_anim_table if item in itempool])
        self.multiworld.get_location("Toy Freddy", self.player).place_locked_item(self.create_item(itempool.pop(itempool.index(chosen_anim))))
        chosen_anim = self.multiworld.random.choice([item for item in start_anim_table if item in itempool])
        self.multiworld.get_location("Mangle", self.player).place_locked_item(self.create_item(itempool.pop(itempool.index(chosen_anim))))

        # Convert itempool into real items

        self.multiworld.random.shuffle(itempool)
        itempool = [item for item in map(lambda name: self.create_item(name), itempool)]
        self.multiworld.itempool += itempool

    def set_rules(self):
        set_rules(self.multiworld, self.player)
        set_completion_rules(self.multiworld, self.player)

    def create_regions(self):
        def FNaFWRegion(region_name: str, exits=[]):
            ret = Region(region_name, self.player, self.multiworld)
            ret.locations = [FNaFWLocations(self.player, loc_name, loc_data.id, ret)
                             for loc_name, loc_data in location_table.items()
                             if loc_data.region == region_name]
            for exit in exits:
                ret.exits.append(Entrance(self.player, exit, ret))
            return ret

        self.multiworld.regions += [FNaFWRegion(*r) for r in FNaFW_regions]
        link_FNaFW_structures(self.multiworld, self.player)

    def fill_slot_data(self):
        slot_data = self._get_FNaFW_data()
        for option_name in FNaFW_options:
            option = getattr(self.multiworld, option_name)[self.player]
            if slot_data.get(option_name, None) is None and type(option.value) in {str, int}:
                slot_data[option_name] = int(option.value)
        return slot_data

    def create_item(self, name: str) -> Item:
        item_data = item_table[name]
        item = FNaFWItem(name, item_data.classification, item_data.code, self.player)
        return item
