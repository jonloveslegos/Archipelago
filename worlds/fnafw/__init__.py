import os

import BaseClasses
from .Items import *
from .Locations import FNaFWLocations, location_table, exclusion_table
from .Regions import FNaFW_regions, link_FNaFW_structures
from .Rules import set_rules, set_completion_rules

from BaseClasses import Region, Entrance, Item, Tutorial
from .Options import FNaFW_options
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


def data_path(file_name: str):
    import pkgutil
    return pkgutil.get_data(__name__, "data/" + file_name)


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
    FNaF World is a rpg where the goal is to beat hard mode in any way. (Only the Scott and Clock endings are valid.)
    """
    game = "FNaFW"
    web = FNaFWWeb()
    option_definitions = FNaFW_options

    anims_0 = []
    anims_1 = []
    anims_2 = []
    anims_3 = []
    anims_4 = []
    anims_5 = []
    anims_6 = []
    anims_7 = []
    anims_8 = []
    anims_9 = []
    anims_10 = []
    anims_11 = []
    chips_1 = []
    chips_2 = []
    chips_3 = []
    bytes_1 = []
    bytes_2 = []
    bytes_3 = []

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
            'race': self.multiworld.is_race,
            'exclude_halloween': bool(self.multiworld.exclude_halloween[self.player].value),
            'exclude_initial_characters': bool(self.multiworld.initial_characters[self.player].value),
            'hard_logic': bool(self.multiworld.hard_logic[self.player].value),
            'progressive_anims': bool(self.multiworld.progressive_anims[self.player].value),
            'progressive_bytes': bool(self.multiworld.progressive_bytes[self.player].value),
            'progressive_chips': bool(self.multiworld.progressive_chips[self.player].value)
        }

    def create_items(self):

        # Generate item pool
        itempool = []

        # Add all required progression items
        for name, item in item_table.items():
            itempool += [name]
        itempool += ["Progressive Endoskeleton"] * 2

        if not self.multiworld.initial_characters[self.player]:
            for item in start_anim_table:
                self.multiworld.get_location(item, self.player).place_locked_item(self.create_item(itempool.pop(itempool.index(item))))
        else:
            chooseable_anim_table = []
            chooseable_anim_table += start_anim_table+fazbear_hills_anim_table+choppys_woods_anim_table
            for item in start_anim_table:
                chosen_anim = self.random.choice(chooseable_anim_table)
                self.multiworld.get_location(item, self.player).place_locked_item(self.create_item(itempool.pop(itempool.index(chosen_anim))))
                chooseable_anim_table.remove(chosen_anim)

        if self.multiworld.progressive_anims[self.player]:
            self.anims_0 = [item for item in itempool if item in start_anim_table]
            self.anims_1 = [item for item in itempool if item in fazbear_hills_anim_table]
            self.anims_2 = [item for item in itempool if item in choppys_woods_anim_table]
            self.anims_3 = [item for item in itempool if item in dusting_fields_anim_table]
            self.anims_4 = [item for item in itempool if item in lilygear_lake_anim_table]
            self.anims_5 = [item for item in itempool if item in mysterious_mine_anim_table]
            self.anims_6 = [item for item in itempool if item in blacktomb_yard_anim_table]
            self.anims_7 = [item for item in itempool if item in deep_metal_mine_anim_table]
            self.anims_8 = [item for item in itempool if item in pinwheel_circus_anim_table]
            self.anims_9 = [item for item in itempool if item in top_layer_anim_table]
            self.anims_10 = [item for item in itempool if item in pinwheel_funhouse_anim_table]
            self.anims_11 = [item for item in itempool if item in halloween_anim_table]
            self.random.shuffle(self.anims_0)
            self.random.shuffle(self.anims_1)
            self.random.shuffle(self.anims_2)
            self.random.shuffle(self.anims_3)
            self.random.shuffle(self.anims_4)
            self.random.shuffle(self.anims_5)
            self.random.shuffle(self.anims_6)
            self.random.shuffle(self.anims_7)
            self.random.shuffle(self.anims_8)
            self.random.shuffle(self.anims_9)
            self.random.shuffle(self.anims_10)
            self.random.shuffle(self.anims_11)
            itempool = ["Progressive Animatronic" if item in start_anim_table+fazbear_hills_anim_table+choppys_woods_anim_table+dusting_fields_anim_table+lilygear_lake_anim_table+mysterious_mine_anim_table+blacktomb_yard_anim_table+deep_metal_mine_anim_table+pinwheel_circus_anim_table+top_layer_anim_table+pinwheel_funhouse_anim_table+halloween_anim_table else item for item in itempool]

        if self.multiworld.exclude_halloween[self.player]:
            for item in halloween_anim_table:
                if self.multiworld.progressive_anims[self.player]:
                    self.multiworld.get_location(item, self.player).place_locked_item(self.create_item(itempool.pop(itempool.index("Progressive Animatronic"))))
                else:
                    self.multiworld.get_location(item, self.player).place_locked_item(self.create_item(itempool.pop(itempool.index(item))))

        if self.multiworld.progressive_chips[self.player]:
            self.chips_1 = [item for item in itempool if item in green_chip_table]
            self.chips_2 = [item for item in itempool if item in orange_chip_table]
            self.chips_3 = [item for item in itempool if item in red_chip_table]
            self.random.shuffle(self.chips_1)
            self.random.shuffle(self.chips_2)
            self.random.shuffle(self.chips_3)
            itempool = ["Progressive Chip" if item in green_chip_table+orange_chip_table+red_chip_table else item for item in itempool]

        if self.multiworld.progressive_bytes[self.player]:
            self.bytes_1 = [item for item in itempool if item in weak_byte_table]
            self.bytes_2 = [item for item in itempool if item in byte_table]
            self.bytes_3 = [item for item in itempool if item in strong_byte_table]
            self.random.shuffle(self.bytes_1)
            self.random.shuffle(self.bytes_2)
            self.random.shuffle(self.bytes_3)
            itempool = ["Progressive Byte" if item in weak_byte_table+byte_table+strong_byte_table else item for item in itempool]

        # Convert itempool into real items

        self.random.shuffle(itempool)
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
        slot_data["Progressive Animatronics Order"] = self.anims_0+self.anims_1+self.anims_2+self.anims_3+self.anims_4+self.anims_5+self.anims_6+self.anims_7+self.anims_8+self.anims_9+self.anims_10+self.anims_11
        slot_data["Progressive Chips Order"] = self.chips_1+self.chips_2+self.chips_3
        slot_data["Progressive Bytes Order"] = self.bytes_1+self.bytes_2+self.bytes_3

        return slot_data

    def create_item(self, name: str) -> Item:
        item_data = item_table[name]
        item = FNaFWItem(name, item_data.classification, item_data.code, self.player)
        return item
