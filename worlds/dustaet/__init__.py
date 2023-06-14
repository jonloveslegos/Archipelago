from BaseClasses import Region, Entrance, Item, Tutorial, ItemClassification
from .Items import DustAETItem, item_table, required_items, lookup_game_id_to_name
from .Locations import DustAETAdvancement, advancement_table, exclusion_table
from .Options import dustaet_options
from .Rules import set_rules
from ..AutoWorld import World, WebWorld
from worlds.LauncherComponents import Component, components
from multiprocessing import Process

import Utils

client_version = 7


def data_path(file_name: str):
    import pkgutil
    return pkgutil.get_data(__name__, "data/" + file_name)


def run_client():
    print('running dust aet client')
    from .DustAETClient import main  # lazy import
    p = Process(target=main)
    p.start()


components.append(Component("Dust AET Client", func=run_client))


class DustAETWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Tutorial",
        "A guide to setting up the Archipelago DustAET software on your computer. This guide covers "
        "single-player, multiworld, and related software.",
        "English",
        "dustaet_en.md",
        "dustaet/en",
        ["Mewlif"]
    )]


class DustAETWorld(World):
    """
    DustAET is a game where you avoid mines and find checks inside the board
    with the mines! You win when you get all your items and beat the board!
    """
    game: str = "DustAET"
    option_definitions = dustaet_options
    topology_present = True
    web = DustAETWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.id for name, data in advancement_table.items()}

    data_version = 4

    def _get_dustaet_data(self):
        return {
            'world_seed': self.multiworld.per_slot_randoms[self.player].getrandbits(32),
            'seed_name': self.multiworld.seed_name,
            'player_name': self.multiworld.get_player_name(self.player),
            'player_id': self.player,
            'client_version': client_version,
            'race': self.multiworld.is_race,
        }

    def create_items(self):

        # Generate item pool
        itempool = []
        # Add all required progression items
        for name in advancement_table:
            if advancement_table[name].id is not None:
                itempool += [lookup_game_id_to_name[advancement_table[name].vanilla_item_id]]
        # Convert itempool into real items
        itempool = [item for item in map(lambda name: self.create_item(name), itempool)]
        self.multiworld.itempool += itempool

    def create_event(self, name: str, classification: ItemClassification) -> Item:
        return DustAETItem(name, classification, None, self.player)

    def generate_basic(self) -> None:
        self.multiworld.get_location("General Gaius", self.player).place_locked_item(
            self.create_event("Victory", ItemClassification.progression))
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    set_rules = set_rules

    def create_region(self, name: str, to=None):
        if to is None:
            to = []
        reg = Region(name, self.player, self.multiworld)
        for item_name, location_data in advancement_table.items():
            if str(location_data.region) == name:
                reg.locations.append(DustAETAdvancement(self.player, item_name, location_data.id, reg))
        for itm in to:
            reg.exits.append(Entrance(self.player, "To "+itm.name+" from "+name, reg))
        self.multiworld.regions.append(reg)
        for itm in to:
            self.multiworld.get_entrance("To "+itm.name+" from "+name, self.player) \
                .connect(self.multiworld.get_region(itm.name, self.player))
        return reg

    def create_regions(self):
        sanctuary = self.create_region("The Sanctuary")
        farm = self.create_region("Geehan's Farm")
        archer_pass = self.create_region("Archers' Pass")
        glen = self.create_region("Ivydale Glen")
        cove = self.create_region("Hidden Cove")
        basin = self.create_region("Everdawn Basin")
        mountain = self.create_region("Blackmoor Mountains", [basin])
        meadow = self.create_region("The Sorrowing Meadow", [mountain])
        caverns2 = self.create_region("Cirromon Caverns P2", [meadow, cove])
        caverns1 = self.create_region("Cirromon Caverns P1", [caverns2, glen])
        forest = self.create_region("Abadis Forest", [caverns1])
        village = self.create_region("Aurora Village", [forest, farm, archer_pass, sanctuary])
        glade2 = self.create_region("The Glade P2", [village])
        glade1 = self.create_region("The Glade P1", [glade2])
        menu = self.create_region("Menu", [glade1])

    def fill_slot_data(self):
        slot_data = self._get_dustaet_data()
        for option_name in dustaet_options:
            option = getattr(self.multiworld, option_name)[self.player]
            if slot_data.get(option_name, None) is None and type(option.value) in {str, int}:
                slot_data[option_name] = int(option.value)
        return slot_data

    def create_item(self, name: str) -> Item:
        item_data = item_table[name]
        item = DustAETItem(name,
                                ItemClassification.progression if item_data.progression else ItemClassification.filler,
                                item_data.code, self.player)
        return item
