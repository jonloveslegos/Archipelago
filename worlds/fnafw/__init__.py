import os

import BaseClasses
from .Items import *
from .Locations import FNaFWLocations, location_table, exclusion_table, location_groups
from .Regions import FNaFW_regions, link_FNaFW_structures
from .Rules import set_rules, set_completion_rules

from BaseClasses import Region, Entrance, Item, Tutorial
from .Options import FNaFW_options
from worlds.AutoWorld import World, WebWorld
from worlds.LauncherComponents import Component, components, Type
from multiprocessing import Process
import math
import typing


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
    tutorials = []


class FNaFWWorld(World):
    """
    FNaF World is a rpg where the goal is to beat hard mode in any way. (Only the Scott and Clock endings are valid.)
    """
    game = "FNaFW"
    web = FNaFWWeb()
    item_name_groups = item_groups
    location_name_groups = location_groups
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

    all_anims = []
    all_chips = []
    all_bytes = []

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
            'require_find_char': bool(self.multiworld.require_find_char[self.player].value),
            'progressive_anims': bool(self.multiworld.progressive_anims[self.player].value),
            'progressive_bytes': bool(self.multiworld.progressive_bytes[self.player].value),
            'progressive_chips': bool(self.multiworld.progressive_chips[self.player].value),
            'vanilla_lasers': bool(self.multiworld.vanilla_lasers[self.player].value),
            'cheap_endo': bool(self.multiworld.cheap_endo[self.player].value),
            'vanilla_pearl': bool(self.multiworld.vanilla_pearl[self.player].value),
        }

    def get_filler_item_name(self) -> str:
        choice_and_weight = {"25 Tokens": 15,
                             "50 Tokens": 20,
                             "100 Tokens": 25,
                             "250 Tokens": 15,
                             "500 Tokens": 10,
                             "1000 Tokens": 10,
                             "2500 Tokens": 5}
        chosen_item_name = self.random.choices(choice_and_weight)
        return chosen_item_name

    def create_items(self):

        # Generate item pool
        itempool = []

        # Add all required progression items
        for name, count in to_add_to_pool.items():
            itempool += [name] * count

        if not self.multiworld.initial_characters[self.player]:
            for item in start_anim_table:
                self.multiworld.get_location(item, self.player).place_locked_item(
                    self.create_item(itempool.pop(itempool.index(item))))
        else:
            chooseable_anim_table = []
            chooseable_anim_table += start_anim_table + fazbear_hills_anim_table + choppys_woods_anim_table
            for item in start_anim_table:
                chosen_anim = self.random.choice(chooseable_anim_table)
                self.multiworld.get_location(item, self.player).place_locked_item(
                    self.create_item(itempool.pop(itempool.index(chosen_anim))))
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
            self.all_anims = self.anims_0 + self.anims_1 + self.anims_2 + self.anims_3 + self.anims_4 + self.anims_5 + self.anims_6 + self.anims_7 + self.anims_8 + self.anims_9 + self.anims_10 + self.anims_11
            itempool = ["Progressive Animatronic" if item in self.all_anims else item for item in itempool]

        if self.multiworld.exclude_halloween[self.player]:
            for item in halloween_anim_table:
                if self.multiworld.progressive_anims[self.player]:
                    self.multiworld.get_location(item, self.player).place_locked_item(
                        self.create_item(itempool.pop(itempool.index("Progressive Animatronic"))))
                else:
                    self.multiworld.get_location(item, self.player).place_locked_item(
                        self.create_item(itempool.pop(itempool.index(item))))

        if self.multiworld.vanilla_pearl[self.player]:
            self.multiworld.get_location("Fazbear Hills: Pearl", self.player).place_locked_item(
                self.create_item(itempool.pop(itempool.index("Pearl"))))

        if self.multiworld.vanilla_lasers[self.player]:
            self.multiworld.get_location("Dusting Fields: Laser Switch", self.player).place_locked_item(
                self.create_item(itempool.pop(itempool.index("Laser Switch 1"))))
            self.multiworld.get_location("Fazbear Hills: Laser Switch", self.player).place_locked_item(
                self.create_item(itempool.pop(itempool.index("Laser Switch 2"))))
            self.multiworld.get_location("Lilygear Lake: Laser Switch", self.player).place_locked_item(
                self.create_item(itempool.pop(itempool.index("Laser Switch 3"))))
            self.multiworld.get_location("Deep-Metal Mine: Laser Switch", self.player).place_locked_item(
                self.create_item(itempool.pop(itempool.index("Laser Switch 4"))))

        if self.multiworld.progressive_chips[self.player]:
            self.chips_1 = [item for item in itempool if item in green_chip_table]
            self.chips_2 = [item for item in itempool if item in orange_chip_table]
            if not self.multiworld.require_find_char[self.player]:
                self.chips_2 += ["Find Characters"]
            self.chips_3 = [item for item in itempool if item in red_chip_table]
            self.random.shuffle(self.chips_1)
            self.random.shuffle(self.chips_2)
            self.random.shuffle(self.chips_3)
            self.all_chips = self.chips_1 + self.chips_2 + self.chips_3
            itempool = ["Progressive Chip" if item in self.all_chips else item for item in itempool]

        if self.multiworld.progressive_bytes[self.player]:
            self.bytes_1 = [item for item in itempool if item in weak_byte_table]
            self.bytes_2 = [item for item in itempool if item in byte_table]
            self.bytes_3 = [item for item in itempool if item in strong_byte_table]
            self.random.shuffle(self.bytes_1)
            self.random.shuffle(self.bytes_2)
            self.random.shuffle(self.bytes_3)
            self.all_bytes = self.bytes_1 + self.bytes_2 + self.bytes_3
            itempool = ["Progressive Byte" if item in self.all_bytes else item for item in itempool]

        # Convert itempool into real items

        self.random.shuffle(itempool)
        itempool = [item for item in map(lambda name: self.create_item(name), itempool)]
        self.multiworld.itempool += itempool

    def write_spoiler(self, spoiler_handle: typing.TextIO) -> None:
        player_name = self.multiworld.get_player_name(self.player)
        spoiler_handle.write(f"\n\nProgressive Animatronics ({player_name}): ")
        for item in self.all_anims:
            spoiler_handle.write(f"{self.all_anims.index(item) + 1}={item}, ")
        spoiler_handle.write(f"\nProgressive Chips ({player_name}): ")
        for item in self.all_chips:
            spoiler_handle.write(f"{self.all_chips.index(item) + 1}={item}, ")
        spoiler_handle.write(f"\nProgressive Bytes ({player_name}): ")
        for item in self.all_bytes:
            spoiler_handle.write(f"{self.all_bytes.index(item) + 1}={item}, ")

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
        slot_data["Progressive Animatronics Order"] = self.all_anims
        slot_data["Progressive Chips Order"] = self.all_chips
        slot_data["Progressive Bytes Order"] = self.all_bytes

        return slot_data

    def create_item(self, name: str) -> Item:
        item_data = item_table[name]
        item = FNaFWItem(name, item_data.classification, item_data.code, self.player)
        return item
