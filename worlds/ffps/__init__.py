from .Items import FFPSItem, item_table, shop_table
from .Locations import FFPSLocations, location_table, exclusion_table, money_table
from .Regions import FFPS_regions, link_FFPS_structures
from .Rules import set_rules, set_completion_rules

from BaseClasses import Region, Entrance, Item, Tutorial
from .Options import FFPSOptions
from ..AutoWorld import World, WebWorld
from worlds.LauncherComponents import Component, components
from multiprocessing import Process


def run_client():
    print('running FFPS client')
    from .FFPSClient import main  # lazy import
    p = Process(target=main)
    p.start()


# components.append(Component("FFPS Client", "FFPSClient"))
components.append(Component("FFPS Client", func=run_client))


def data_path(file_name: str):
    import pkgutil
    return pkgutil.get_data(__name__, "data/" + file_name)


class FFPSWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Tutorial",
        "A guide to setting up the Archipelago FFPS software on your computer. This guide covers "
        "single-player, multiworld, and related software.",
        "English",
        "ffps_en.md",
        "ffps/en",
        ["Mewlif"]
    )]


class FFPSWorld(World):
    """
    Freddy Fazbear's Pizzeria Simulator is a horror game where animatronics come through vents into your office
    to kill you. You win if you complete night 5 with all 4 animatronics obtained in your world to get the true ending.
    """
    game = "FFPS"
    web = FFPSWeb()
    options_dataclass = FFPSOptions
    options: FFPSOptions

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.id for name, data in location_table.items()}

    def _get_FFPS_data(self):
        return {
            'world_seed': self.random.getrandbits(32),
            'seed_name': self.multiworld.seed_name,
            'player_name': self.multiworld.get_player_name(self.player),
            'player_id': self.player,
            'race': self.multiworld.is_race,
            'max_anim_appears': int(self.options.max_animatronics_appearing),
            'catalogue_rando': bool(self.options.catalogue_rando),
            'night_difficulty': int(self.options.night_difficulty),
            'upgrade_rando': bool(self.options.upgrade_rando),
            'easier_money_grinding': bool(self.options.easier_money_grinding),
            'wallet_sanity': bool(self.options.wallet_sanity),
            'full_wallet': bool(self.options.full_wallet),
            'day_sanity': bool(self.options.day_sanity),
            'skipable_night': bool(self.options.skipable_night),
        }

    def generate_basic(self):
        # Generate item pool
        itempool = []

        # Add all required progression items
        for name, item in self.item_name_to_id.items():
            itempool += [name]
        itempool += ["Stage Upgrade"] * 4
        itempool += ["Cup Upgrade"] * 3
        itempool += ["Speaker Upgrade"] * 1
        itempool += ["Wallet Capacity Increase"] * 11

        if not self.options.day_sanity:
            itempool = [item for item in itempool if item != "Tuesday Unlock" and item != "Wednesday Unlock" and
                        item != "Thursday Unlock" and item != "Friday Unlock" and item != "Saturday Unlock"]

        if not self.options.wallet_sanity:
            itempool = [item for item in itempool if item != "Wallet Capacity Increase"]

        # Convert itempool into real items
        if not self.options.catalogue_rando:
            self.multiworld.get_location("Unlocked Catalogue 2", self.player).place_locked_item(
                self.create_item("Catalogue 2 Unlock"))
            self.multiworld.get_location("Unlocked Catalogue 3", self.player).place_locked_item(
                self.create_item("Catalogue 3 Unlock"))
            self.multiworld.get_location("Unlocked Catalogue 4", self.player).place_locked_item(
                self.create_item("Catalogue 4 Unlock"))
            itempool.remove("Catalogue 2 Unlock")
            itempool.remove("Catalogue 3 Unlock")
            itempool.remove("Catalogue 4 Unlock")

        if not self.options.upgrade_rando:
            self.multiworld.get_location("Bought Printer Upgrade", self.player).place_locked_item(
                self.create_item("Printer Upgrade"))
            self.multiworld.get_location("Bought Handyman Upgrade", self.player).place_locked_item(
                self.create_item("Handyman Upgrade"))
            self.multiworld.get_location("Bought Internet Upgrade", self.player).place_locked_item(
                self.create_item("Internet Upgrade"))
            itempool.remove("Printer Upgrade")
            itempool.remove("Handyman Upgrade")
            itempool.remove("Internet Upgrade")

        complete_item_pool = [item for item in map(lambda name: self.create_item(name), itempool)]

        while len(complete_item_pool) < len(self.multiworld.get_unfilled_locations(self.player)):
            complete_item_pool.append(self.create_filler())

        self.multiworld.itempool += complete_item_pool

    def set_rules(self):
        set_rules(self, self.player)
        set_completion_rules(self, self.player)

    def create_regions(self):
        def FFPSRegion(region_name: str, exits):
            ret = Region(region_name, self.player, self.multiworld)
            ret.locations = [FFPSLocations(self.player, loc_name, loc_data.id, ret)
                             for loc_name, loc_data in location_table.items()
                             if loc_data.region == region_name]
            for exit in exits:
                ret.exits.append(Entrance(self.player, exit, ret))
            return ret

        self.multiworld.regions += [FFPSRegion(*r) for r in FFPS_regions]
        link_FFPS_structures(self.multiworld, self.player)

    def fill_slot_data(self):
        slot_data = self._get_FFPS_data()
        for option_name in self.options.as_dict():
            option = getattr(self.options, option_name)
            if slot_data.get(option_name, None) is None and type(option.value) in {str, int}:
                slot_data[option_name] = int(option.value)
        return slot_data

    def create_item(self, name: str) -> Item:
        item_data = item_table[name]
        item = FFPSItem(name, item_data.classification, item_data.code, self.player)
        return item

    def get_filler_item_name(self):
        return "250 Money"
