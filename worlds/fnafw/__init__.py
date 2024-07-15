from .Items import *
from .Locations import FNaFWLocations, location_table, exclusion_table, location_groups
from .Regions import FNaFW_regions, link_FNaFW_structures
from .Rules import set_rules, set_completion_rules

from BaseClasses import Region, Entrance, Item
from .Options import FNaFWOptions
from worlds.AutoWorld import World, WebWorld
from worlds.LauncherComponents import Component, components
from multiprocessing import Process
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
    options_dataclass = FNaFWOptions
    options: FNaFWOptions

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

    fnafw_world_identifier = []

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
            'vanilla_halloween': bool(self.options.vanilla_halloween.value),
            'initial_characters': self.options.initial_characters.current_key,
            'hard_logic': bool(self.options.hard_logic.value),
            'require_find_char': bool(self.options.require_find_char.value),
            'progressive_anims': bool(self.options.progressive_anims.value),
            'progressive_bytes': bool(self.options.progressive_bytes.value),
            'progressive_chips': bool(self.options.progressive_chips.value),
            'vanilla_lasers': bool(self.options.vanilla_lasers.value),
            'cheap_endo': bool(self.options.cheap_endo.value),
            'vanilla_pearl': bool(self.options.vanilla_pearl.value),
            'fazcoin_chests': self.options.fazcoin_chests.value,
            'ending_goal': self.options.ending_goal.current_key,
            'area_warping': self.options.area_warping.current_key,
        }

    def get_filler_item_name(self) -> str:
        choice_and_weight = {"50 Tokens": 5,
                             "100 Tokens": 40,
                             "250 Tokens": 30,
                             "500 Tokens": 20,
                             "1000 Tokens": 5}
        chosen_item_name = self.multiworld.random.choices(list(choice_and_weight.keys()), weights=list(choice_and_weight.values()))[0]
        return chosen_item_name

    def create_items(self):

        # Generate item pool
        itempool = []

        # Add all required progression items
        for name, count in to_add_to_pool.items():
            itempool += [name] * count

        if self.options.initial_characters == "vanilla":
            for item in start_anim_table:
                self.multiworld.get_location(item, self.player).place_locked_item(
                    self.create_item(itempool.pop(itempool.index(item))))
        elif self.options.initial_characters == "limited_random":
            chooseable_anim_table = []
            chooseable_anim_table += start_anim_table + fazbear_hills_anim_table + choppys_woods_anim_table
            for item in start_anim_table:
                chosen_anim = self.random.choice(chooseable_anim_table)
                self.multiworld.get_location(item, self.player).place_locked_item(
                    self.create_item(itempool.pop(itempool.index(chosen_anim))))
                chooseable_anim_table.remove(chosen_anim)
        elif self.options.initial_characters == "true_random":
            chooseable_anim_table = []
            chooseable_anim_table += start_anim_table + fazbear_hills_anim_table + choppys_woods_anim_table + \
                                     dusting_fields_anim_table + lilygear_lake_anim_table + \
                                     mysterious_mine_anim_table + blacktomb_yard_anim_table + \
                                     deep_metal_mine_anim_table + pinwheel_circus_anim_table + \
                                     top_layer_anim_table + pinwheel_funhouse_anim_table
            if not self.options.ending_goal.current_key == "universe_end":
                chooseable_anim_table += ["Fredbear"]
            for item in start_anim_table:
                chosen_anim = self.random.choice(chooseable_anim_table)
                self.multiworld.get_location(item, self.player).place_locked_item(
                    self.create_item(itempool.pop(itempool.index(chosen_anim))))
                chooseable_anim_table.remove(chosen_anim)

        if self.options.progressive_anims:
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
            if not self.options.ending_goal.current_key == "universe_end":
                self.anims_10 += ["Fredbear"]
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

        if self.options.vanilla_halloween:
            for item in halloween_anim_table:
                if self.options.progressive_anims:
                    self.multiworld.get_location(item, self.player).place_locked_item(
                        self.create_item(itempool.pop(itempool.index("Progressive Animatronic"))))
                else:
                    self.multiworld.get_location(item, self.player).place_locked_item(
                        self.create_item(itempool.pop(itempool.index(item))))

        if self.options.vanilla_pearl:
            self.multiworld.get_location("Fazbear Hills: Pearl", self.player).place_locked_item(
                self.create_item(itempool.pop(itempool.index("Pearl"))))

        if self.options.area_warping.current_key == "warp_item":
            itempool += ["Warp Access"]

        if self.options.vanilla_lasers:
            self.multiworld.get_location("Dusting Fields: Laser Switch", self.player).place_locked_item(
                self.create_item(itempool.pop(itempool.index("Laser Switch 1"))))
            self.multiworld.get_location("Fazbear Hills: Laser Switch", self.player).place_locked_item(
                self.create_item(itempool.pop(itempool.index("Laser Switch 2"))))
            self.multiworld.get_location("Lilygear Lake: Laser Switch", self.player).place_locked_item(
                self.create_item(itempool.pop(itempool.index("Laser Switch 3"))))
            self.multiworld.get_location("Deep-Metal Mine: Laser Switch", self.player).place_locked_item(
                self.create_item(itempool.pop(itempool.index("Laser Switch 4"))))

        if self.options.progressive_chips:
            self.chips_1 = [item for item in itempool if item in green_chip_table]
            self.chips_2 = [item for item in itempool if item in orange_chip_table]
            if not self.options.require_find_char:
                self.chips_2 += ["Find Characters"]
            self.chips_3 = [item for item in itempool if item in red_chip_table]
            self.random.shuffle(self.chips_1)
            self.random.shuffle(self.chips_2)
            self.random.shuffle(self.chips_3)
            self.all_chips = self.chips_1 + self.chips_2 + self.chips_3
            itempool = ["Progressive Chip" if item in self.all_chips else item for item in itempool]

        if self.options.progressive_bytes:
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

        while len(itempool) < len(self.multiworld.get_unfilled_locations(self.player)):
            itempool += [self.create_filler()]

        self.multiworld.itempool += itempool

    def generate_basic(self) -> None:
        self.fnafw_world_identifier = [self.random.randint(0, 65535) for i in range(10)]

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
        set_rules(self.multiworld, self.player, self.options)
        set_completion_rules(self.multiworld, self.player, self.options)

    def create_regions(self):
        def FNaFWRegion(region_name: str, exits: list):
            ret = Region(region_name, self.player, self.multiworld)
            if region_name != "Menu":
                ret.locations = [FNaFWLocations(self.player, loc_name, loc_data.id, ret)
                                 for loc_name, loc_data in location_table.items()
                                 if loc_data.region == region_name
                                 and (loc_data.id < 797302 or loc_data.id > 797337)]
                ret.locations += [FNaFWLocations(self.player, "Fazbear Hills: Fazcoin Chest "+str(i+1), 797302+i, ret) for i in range(self.options.fazcoin_chests.value)]
                ret.locations += [FNaFWLocations(self.player, "Choppy's Woods: Fazcoin Chest "+str(i+1), 797306+i, ret) for i in range(self.options.fazcoin_chests.value)]
                ret.locations += [FNaFWLocations(self.player, "Dusting Fields: Fazcoin Chest "+str(i+1), 797310+i, ret) for i in range(self.options.fazcoin_chests.value)]
                ret.locations += [FNaFWLocations(self.player, "Lilygear Lake: Fazcoin Chest "+str(i+1), 797314+i, ret) for i in range(self.options.fazcoin_chests.value)]
                ret.locations += [FNaFWLocations(self.player, "Mysterious Mine: Fazcoin Chest "+str(i+1), 797318+i, ret) for i in range(self.options.fazcoin_chests.value)]
                ret.locations += [FNaFWLocations(self.player, "Blacktomb Yard: Fazcoin Chest "+str(i+1), 797322+i, ret) for i in range(self.options.fazcoin_chests.value)]
                ret.locations += [FNaFWLocations(self.player, "Deep-Metal Mine: Fazcoin Chest "+str(i+1), 797326+i, ret) for i in range(self.options.fazcoin_chests.value)]
                ret.locations += [FNaFWLocations(self.player, "Pinwheel Circus: Fazcoin Chest "+str(i+1), 797330+i, ret) for i in range(self.options.fazcoin_chests.value)]
                ret.locations += [FNaFWLocations(self.player, "Pinwheel Funhouse: Fazcoin Chest "+str(i+1), 797334+i, ret) for i in range(self.options.fazcoin_chests.value)]
            for exit in exits:
                ret.exits.append(Entrance(self.player, exit, ret))
            return ret

        self.multiworld.regions += [FNaFWRegion(*r) for r in FNaFW_regions]
        link_FNaFW_structures(self.multiworld, self.player)

    def fill_slot_data(self):
        slot_data = self._get_FNaFW_data()
        for option_name in self.options.as_dict():
            option = getattr(self.multiworld, option_name)[self.player]
            if slot_data.get(option_name, None) is None and type(option.value) in {str, int}:
                slot_data[option_name] = int(option.value)
        slot_data["Progressive Animatronics Order"] = self.all_anims
        slot_data["Progressive Chips Order"] = self.all_chips
        slot_data["Progressive Bytes Order"] = self.all_bytes
        slot_data["fnafw_world_identifier"] = self.fnafw_world_identifier

        return slot_data

    def create_item(self, name: str) -> Item:
        item_data = item_table[name]
        item = FNaFWItem(name, item_data.classification, item_data.code, self.player)
        return item
