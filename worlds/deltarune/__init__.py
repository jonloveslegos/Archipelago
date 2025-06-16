from .Items import DeltaruneItem, item_table, non_key_items, key_items, \
    junk_weights_all, warp_doors, super_boss_rewards
from .Locations import DeltaruneAdvancement, advancement_table, exclusion_table
from .Regions import deltarune_regions, link_deltarune_areas
from .Rules import set_rules, set_completion_rules
from worlds.generic.Rules import exclusion_rules
from BaseClasses import Region, Entrance, Tutorial, Item, ItemClassification
from .Options import DeltaruneOptions
from worlds.AutoWorld import World, WebWorld
from worlds.LauncherComponents import Component, components
from multiprocessing import Process


def run_client():
    print('running deltarune client')
    from .DeltaruneClient import main  # lazy import
    p = Process(target=main)
    p.start()


# components.append(Component("Deltarune Client", "DeltaruneClient"))
components.append(Component("Deltarune Client", func=run_client))


def data_path(file_name: str):
    import pkgutil
    return pkgutil.get_data(__name__, "data/" + file_name)


class DeltaruneWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Archipelago Deltarune software on your computer. This guide covers "
        "single-player, multiworld, and related software.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Mewlif"]
    )]


class DeltaruneWorld(World):
    """
    Deltarune is an RPG.
    """
    game = "Deltarune"
    options_dataclass = DeltaruneOptions
    options: DeltaruneOptions
    web = DeltaruneWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.id for name, data in advancement_table.items()}

    def _get_deltarune_data(self):
        return {
            "world_seed": self.random.getrandbits(32),
            "seed_name": self.multiworld.seed_name,
            "player_name": self.multiworld.get_player_name(self.player),
            "player_id": self.player,
            "client_version": self.required_client_version,
            "race": self.multiworld.is_race,
            "randomize_warp_doors": bool(self.options.randomize_warp_doors.value),
            "randomize_super_bosses": bool(self.options.randomize_super_bosses.value),
            "goal_macguffin_amount": int(self.options.goal_macguffin_amount.value),
        }

    def get_filler_item_name(self):
        junk_pool = junk_weights_all
        return self.random.choices(list(junk_pool.keys()), weights=list(junk_pool.values()))[0]

    def create_items(self):
        # Generate item pool
        itempool: list[str] = []
        # Add all required progression items
        itempool += ["King-Shaped Key Piece"] * self.options.goal_macguffin_amount
        for name, num in key_items.items():
            itempool += [name] * num
        for name, num in non_key_items.items():
            itempool += [name] * num
        if not self.options.randomize_warp_doors:
            itempool = [item for item in itempool if item not in warp_doors]
            self.multiworld.get_location("CH1: Fields Warp Door", self.player).place_locked_item(self.create_item("Fields Warp"))
            self.multiworld.get_location("CH1: Forest Warp Door", self.player).place_locked_item(self.create_item("Forest Warp"))
            self.multiworld.get_location("CH1: Bake Sale Warp Door", self.player).place_locked_item(self.create_item("Bake Sale Warp"))
            self.multiworld.get_location("CH1: Castle Warp Door", self.player).place_locked_item(self.create_item("Castle Warp"))
        if not self.options.randomize_super_bosses:
            itempool = [item for item in itempool if item not in super_boss_rewards]
            self.multiworld.get_location("CH1: JevilsTail", self.player).place_locked_item(self.create_item("JevilsTail"))
            self.multiworld.get_location("CH1: ShadowCrystal", self.player).place_locked_item(self.create_item("ShadowCrystal"))
            self.multiworld.get_location("CH1: DevilsKnife", self.player).place_locked_item(self.create_item("DevilsKnife"))

        # Choose locations to automatically exclude based on settings
        exclusion_checks = set()
        exclusion_rules(self.multiworld, self.player, exclusion_checks)

        # Convert itempool into real items
        itempool_converted = [item for item in map(lambda name: self.create_item(name), itempool)]
        # Remove random junk items if the item pool overflows
        if len(itempool_converted) > len(self.multiworld.get_unfilled_locations(self.player)):
            print(len(itempool_converted) - len(self.multiworld.get_unfilled_locations(self.player)))
        while len(itempool_converted) > len(self.multiworld.get_unfilled_locations(self.player)):
            itempool_converted.remove(self.random.choice([item for item in itempool_converted if item.classification == ItemClassification.filler]))
        # Fill remaining items with randomly generated junk
        while len(itempool_converted) < len(self.multiworld.get_unfilled_locations(self.player)):
            itempool_converted.append(self.create_filler())

        self.multiworld.itempool += itempool_converted

    def set_rules(self):
        set_rules(self)
        set_completion_rules(self)

    def create_regions(self):
        def DeltaruneRegion(region_name: str, exits=None):
            if exits is None:
                exits = []
            ret = Region(region_name, self.player, self.multiworld)
            ret.locations += [DeltaruneAdvancement(self.player, loc_name, loc_data.id, ret)
                              for loc_name, loc_data in advancement_table.items()
                              if loc_data.region == region_name]
            for exit in exits:
                ret.exits.append(Entrance(self.player, exit, ret))
            return ret

        self.multiworld.regions += [DeltaruneRegion(*r) for r in deltarune_regions]
        link_deltarune_areas(self.multiworld, self.player)

    def fill_slot_data(self):
        return self._get_deltarune_data()

    def create_item(self, name: str) -> Item:
        item_data = item_table[name]
        item = DeltaruneItem(name, item_data.classification, item_data.code, self.player)
        return item
