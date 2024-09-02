import BaseClasses
from worlds.generic.Rules import exclusion_rules
from BaseClasses import Tutorial, Item, ItemClassification
from .Options import PangeaOptions
try:
    import custom_worlds.undertale as ut_world
except ModuleNotFoundError:
    import worlds.undertale as ut_world
from worlds.AutoWorld import WebWorld
from worlds.LauncherComponents import Component, components
from multiprocessing import Process
from .entrance_rando import *
from typing import NamedTuple, List


def run_client():
    print('running Pangea client')
    # from .PangeaClient import main  # lazy import
    # p = Process(target=main)
    # p.start()


class PangeaItem(Item):
    game: str = "Pangea"


class Portal(NamedTuple):
    mod_string: str


# components.append(Component("Pangea Client", "PangeaClient"))
components.append(Component("Pangea Client", func=run_client))


class PangeaWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Archipelago Pangea software on your computer. This guide covers "
        "single-player, multiworld, and related software.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Mewlif"]
    )]


class PangeaWorld(World):
    """
    Undertale is an RPG where every choice you make matters. You could choose to hurt all the enemies, eventually
    causing genocide of the monster species. Or you can spare all the enemies, befriending them and freeing them
    from their underground prison.
    """
    game = "Pangea"
    options_dataclass = PangeaOptions
    options: PangeaOptions
    web = PangeaWeb()
    multiworld_pangea: MultiWorld

    undertale: World

    item_name_to_id = {name: data for name, data in ut_world.UndertaleWorld.item_name_to_id.items()}
    location_name_to_id = {name: data for name, data in ut_world.UndertaleWorld.location_name_to_id.items()}

    topology_present = True

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)

    def _get_pangea_data(self):
        return {
            "world_seed": self.random.getrandbits(32),
            "seed_name": self.multiworld.seed_name,
            "player_name": self.multiworld.get_player_name(self.player),
            "player_id": self.player,
            "client_version": self.required_client_version,
            "race": self.multiworld.is_race,
            "include_undertale": bool(self.options.include_undertale.value),
        }

    def get_filler_item_name(self):
        possible_filler = []
        if bool(self.options.include_undertale.value):
            possible_filler += self.undertale.get_filler_item_name()

        return self.random.choice(possible_filler)

    def pre_fill(self):
        if bool(self.options.include_undertale.value):
            if self.undertale.options.entrance_rando:
                portal_mapping_temp = [item.destination_string() for item in ut_world.er_scripts.portal_mapping]

                for item in portal_mapping_temp:
                    temp = self.multiworld.get_entrance(item, self.player)
                    temp.name = "Undertale: "+temp.name
                    disconnect_entrance_for_randomization(temp)

        place_state = randomize_entrances(self, True, {0: [0]}).pairings

    def generate_early(self):

        self.multiworld_pangea = MultiWorld(1)
        self.undertale = ut_world.UndertaleWorld(self.multiworld_pangea, 1)
        self.undertale.options = self.undertale.options_dataclass(**{option_key: self.undertale.options_dataclass.type_hints[option_key]
                                                               for option_key in self.undertale.options_dataclass.type_hints})
        self.multiworld_pangea.worlds.update({1: self.undertale})
        self.multiworld_pangea.state = CollectionState(self.multiworld_pangea)

        if bool(self.options.include_undertale.value):
            for item in self.options_dataclass.type_hints:
                for und_item in self.undertale.options_dataclass.type_hints:
                    if item == und_item:
                        self.undertale.options.__setattr__(item, self.options.__getattribute__(item))
            self.undertale.generate_early()

    def create_items(self):
        # Generate item pool
        itempool = []
        if bool(self.options.include_undertale.value):
            self.undertale.create_items()
            for item in self.multiworld_pangea.precollected_items[self.undertale.player]:
                item.player = self.player
                self.multiworld.push_precollected(item)
        for item in self.multiworld_pangea.itempool:
            item.player = self.player
            itempool += [item]
        # Choose locations to automatically exclude based on settings
        exclusion_checks = set()
        for ply in range(self.multiworld_pangea.players):
            for item in self.multiworld_pangea.get_locations(ply+1):
                if item.progress_type == BaseClasses.LocationProgressType.EXCLUDED:
                    exclusion_checks.update([item.name])

        exclusion_rules(self.multiworld, self.player, exclusion_checks)

        # Fill remaining items with randomly generated junk or Temmie Flakes
        while len(itempool) < len(self.multiworld.get_unfilled_locations(self.player)):
            itempool.append(self.create_filler())

        self.multiworld.itempool += itempool

    def set_rules(self) -> None:
        if bool(self.options.include_undertale.value):
            ut_world.set_er_location_rules(self)

    def create_regions(self):
        regions_mapping: List[Entrance] = []

        if bool(self.options.include_undertale.value):
            self.undertale.create_regions()
            portal_mapping_temp = [item for item in self.multiworld_pangea.get_regions(self.undertale.player)]

            for item in portal_mapping_temp:
                item.player = self.player
                item.multiworld = self.multiworld
                self.multiworld.regions.append(item)
                self.multiworld.regions.region_cache[self.player].update({item.name: item})
                for loc in item.locations:
                    self.multiworld.regions.location_cache[self.player].update({loc.name: loc})
                for ent in item.entrances:
                    self.multiworld.regions.entrance_cache[self.player].update({ent.name: ent})

        for item in regions_mapping:
            item.player = self.player

    def fill_slot_data(self):
        slot_data = self._get_pangea_data()
        for option_name in self.options.as_dict():
            option = getattr(self.multiworld, option_name)[self.player]
            if slot_data.get(option_name, None) is None and type(option.value) in {str, int}:
                slot_data[option_name] = int(option.value)
        return slot_data

    def create_item(self, name: str) -> Item:
        if bool(self.options.include_undertale.value):
            if name in self.undertale.item_names:
                item_data = self.undertale.create_item(name)
                item = PangeaItem(name, item_data.classification, item_data.code, self.player)
                return item

        return PangeaItem("None", ItemClassification.filler, 9999999999, self.player)
