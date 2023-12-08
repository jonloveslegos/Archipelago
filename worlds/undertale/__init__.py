from .Items import UndertaleItem, item_table, required_armor, required_weapons, non_key_items, key_items, \
    junk_weights_all, plot_items, junk_weights_neutral, junk_weights_pacifist, junk_weights_genocide, junk_weights_cut_items
from .Locations import UndertaleAdvancement, advancement_table, exclusion_table
from .er_rules import set_er_location_rules
from .er_scripts import create_er_regions, create_er_regions_vanilla
from .Rules import set_rules, set_completion_rules
from worlds.generic.Rules import exclusion_rules
from BaseClasses import Region, Entrance, Tutorial, Item
from .Options import undertale_options
from worlds.AutoWorld import World, WebWorld
from worlds.LauncherComponents import Component, components, Type
from multiprocessing import Process
from typing import Dict, List, Any
import Utils
import math


def run_client():
    print('running undertale client')
    from .UndertaleClient import main  # lazy import
    p = Process(target=main)
    p.start()


# components.append(Component("Undertale Client", "UndertaleClient"))
components.append(Component("Undertale Client", func=run_client))


def data_path(file_name: str):
    import pkgutil
    return pkgutil.get_data(__name__, "data/" + file_name)


class UndertaleWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Tutorial",
        "A guide to setting up the Archipelago Undertale software on your computer. This guide covers "
        "single-player, multiworld, and related software.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Mewlif"]
    )]


class UndertaleWorld(World):
    """
    Undertale is an RPG where every choice you make matters. You could choose to hurt all the enemies, eventually
    causing genocide of the monster species. Or you can spare all the enemies, befriending them and freeing them
    from their underground prison.
    """
    game = "Undertale"
    option_definitions = undertale_options
    web = UndertaleWeb()

    topology_present = True

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.id for name, data in advancement_table.items()}

    data_version = 7
    undertale_portal_pairs: Dict[str, str]
    er_portal_hints: Dict[int, str]

    def _get_undertale_data(self):
        return {
            "world_seed": self.multiworld.per_slot_randoms[self.player].getrandbits(32),
            "seed_name": self.multiworld.seed_name,
            "player_name": self.multiworld.get_player_name(self.player),
            "player_id": self.player,
            "client_version": self.required_client_version,
            "race": self.multiworld.is_race,
            "route_required": self.multiworld.route_required[self.player].current_key,
            "starting_area": self.multiworld.starting_area[self.player].current_key,
            "temy_include": bool(self.multiworld.temy_include[self.player].value),
            "only_flakes": bool(self.multiworld.only_flakes[self.player].value),
            "no_equips": bool(self.multiworld.no_equips[self.player].value),
            "key_hunt": bool(self.multiworld.key_hunt[self.player].value),
            "key_pieces": self.multiworld.key_pieces[self.player].value,
            "rando_love": bool(self.multiworld.rando_love[self.player].value),
            "rando_stats": bool(self.multiworld.rando_stats[self.player].value),
            "prog_armor": bool(self.multiworld.prog_armor[self.player].value),
            "prog_weapons": bool(self.multiworld.prog_weapons[self.player].value),
            "rando_item_button": bool(self.multiworld.rando_item_button[self.player].value),
            "kill_sanity": bool(self.multiworld.kill_sanity[self.player].value),
            "rando_jump": bool(self.multiworld.rando_jump[self.player].value),
            "cut_items": bool(self.multiworld.cut_items[self.player].value),
            "kill_sanity_pack_size": self.multiworld.kill_sanity_pack_size[self.player].value,
            "ice_traps": self.multiworld.ice_traps[self.player].value,
            "spare_sanity": bool(self.multiworld.spare_sanity[self.player].value),
            "entrance_rando": bool(self.multiworld.entrance_rando[self.player].value),
            "spare_sanity_max": self.multiworld.spare_sanity_max[self.player].value,
            "spare_sanity_pack_size": self.multiworld.spare_sanity_pack_size[self.player].value,
            "Entrance Rando": self.undertale_portal_pairs
        }

    def get_filler_item_name(self):
        if self.multiworld.route_required[self.player] == "all_routes":
            junk_pool = junk_weights_all.copy()
        elif self.multiworld.route_required[self.player] == "genocide":
            junk_pool = junk_weights_genocide.copy()
        elif self.multiworld.route_required[self.player] == "neutral":
            junk_pool = junk_weights_neutral.copy()
        elif self.multiworld.route_required[self.player] == "pacifist":
            junk_pool = junk_weights_pacifist.copy()
        else:
            junk_pool = junk_weights_all.copy()
        if self.multiworld.cut_items[self.player]:
            junk_pool = junk_pool | junk_weights_cut_items.copy()
        if not self.multiworld.only_flakes[self.player]:
            return self.multiworld.random.choices(list(junk_pool.keys()), weights=list(junk_pool.values()))[0]
        else:
            return "Temmie Flakes"

    def create_items(self):
        exclusion_pool = set()
        # Generate item pool
        itempool = []
        # Add all required progression items
        for name, num in key_items.items():
            itempool += [name] * num
        for name, num in required_armor.items():
            itempool += [name] * num
        for name, num in required_weapons.items():
            itempool += [name] * num
        for name, num in non_key_items.items():
            itempool += [name] * num
        if self.multiworld.rando_item_button[self.player]:
            itempool += ["ITEM"]
        else:
            self.multiworld.push_precollected(self.create_item("ITEM"))
        if not self.multiworld.rando_jump[self.player]:
            itempool.remove("Jump")
            self.multiworld.push_precollected(self.create_item("Jump"))
        self.multiworld.push_precollected(self.create_item("FIGHT"))
        self.multiworld.push_precollected(self.create_item("ACT"))
        self.multiworld.push_precollected(self.create_item("MERCY"))
        if self.multiworld.route_required[self.player] == "genocide":
            itempool = [item for item in itempool if item != "Popato Chisps" and item != "Stained Apron" and
                        item != "Nice Cream" and item != "Hot Cat" and item != "Hot Dog...?" and item != "Punch Card"]
        elif self.multiworld.route_required[self.player] == "neutral":
            itempool = [item for item in itempool if item != "Popato Chisps" and item != "Hot Cat" and
                        item != "Hot Dog...?"]
        if self.multiworld.route_required[self.player] == "pacifist" or \
                self.multiworld.route_required[self.player] == "all_routes":
            itempool += ["Undyne Letter EX"]
        else:
            itempool.remove("Complete Skeleton")
            itempool.remove("Fish")
            itempool.remove("DT Extractor")
            itempool.remove("Hush Puppy")
        if self.multiworld.key_hunt[self.player]:
            itempool += ["Key Piece"] * self.multiworld.key_pieces[self.player].value
        else:
            itempool += ["Left Home Key"]
            itempool += ["Right Home Key"]
        if not self.multiworld.rando_love[self.player] or \
                (self.multiworld.route_required[self.player] != "genocide" and
                 self.multiworld.route_required[self.player] != "all_routes"):
            itempool = [item for item in itempool if not item == "LOVE"]
        if self.multiworld.spare_sanity[self.player] and self.multiworld.route_required[self.player] != "genocide":
            itempool += ["Ruins Spare"] * math.ceil(self.multiworld.spare_sanity_max[self.player].value/self.multiworld.spare_sanity_pack_size[self.player].value)
            itempool += ["Snowdin Spare"] * math.ceil(self.multiworld.spare_sanity_max[self.player].value/self.multiworld.spare_sanity_pack_size[self.player].value)
            itempool += ["Waterfall Spare"] * math.ceil(self.multiworld.spare_sanity_max[self.player].value/self.multiworld.spare_sanity_pack_size[self.player].value)
            itempool += ["Hotland Spare"] * math.ceil(self.multiworld.spare_sanity_max[self.player].value/self.multiworld.spare_sanity_pack_size[self.player].value)
        if not self.multiworld.kill_sanity[self.player] or \
                (self.multiworld.route_required[self.player] != "genocide" and
                 self.multiworld.route_required[self.player] != "all_routes"):
            self.multiworld.precollected_items[self.player] += [self.create_item("Ruins Population Pack")]
            self.multiworld.precollected_items[self.player] += [self.create_item("Snowdin Population Pack")]
            self.multiworld.precollected_items[self.player] += [self.create_item("Waterfall Population Pack")]
            self.multiworld.precollected_items[self.player] += [self.create_item("Hotland Population Pack")]
            exclusion_pool.update(exclusion_table["NoKills"])
        else:
            itempool += ["Ruins Population Pack"] * math.ceil(20/self.multiworld.kill_sanity_pack_size[self.player].value)
            itempool += ["Snowdin Population Pack"] * math.ceil(16/self.multiworld.kill_sanity_pack_size[self.player].value)
            itempool += ["Waterfall Population Pack"] * math.ceil(18/self.multiworld.kill_sanity_pack_size[self.player].value)
            itempool += ["Hotland Population Pack"] * math.ceil(40/self.multiworld.kill_sanity_pack_size[self.player].value)
        if self.multiworld.ice_traps[self.player].value > 0:
            itempool += ["Ice Trap"] * self.multiworld.ice_traps[self.player].value
        if not self.multiworld.rando_stats[self.player] or \
                (self.multiworld.route_required[self.player] != "genocide" and
                 self.multiworld.route_required[self.player] != "all_routes"):
            itempool = [item for item in itempool if not (item == "ATK Up" or item == "DEF Up" or item == "HP Up")]
        if self.multiworld.temy_include[self.player]:
            itempool += ["temy armor"]
        if self.multiworld.no_equips[self.player]:
            itempool = [item for item in itempool if item not in required_armor and item not in required_weapons]
        else:
            if self.multiworld.prog_armor[self.player]:
                itempool = [item if (item not in required_armor and not item == "temy armor") else
                            "Progressive Armor" for item in itempool]
            if self.multiworld.prog_weapons[self.player]:
                itempool = [item if item not in required_weapons else "Progressive Weapons" for item in itempool]
        if self.multiworld.route_required[self.player] == "genocide" or \
                self.multiworld.route_required[self.player] == "all_routes":
            if not self.multiworld.only_flakes[self.player]:
                itempool += ["Snowman Piece"] * 2
            if not self.multiworld.no_equips[self.player]:
                itempool = ["Real Knife" if item == "Worn Dagger" else "The Locket"
                            if item == "Heart Locket" else item for item in itempool]
        if self.multiworld.only_flakes[self.player]:
            itempool = [item for item in itempool if item not in non_key_items]

        starting_key = self.multiworld.starting_area[self.player].current_key.title() + " Key"
        itempool.remove(starting_key)
        self.multiworld.push_precollected(self.create_item(starting_key))
        # Choose locations to automatically exclude based on settings
        exclusion_pool.update(exclusion_table[self.multiworld.route_required[self.player].current_key])
        if not self.multiworld.rando_love[self.player] or \
                (self.multiworld.route_required[self.player] != "genocide" and
                 self.multiworld.route_required[self.player] != "all_routes"):
            exclusion_pool.update(exclusion_table["NoLove"])
        if not self.multiworld.rando_stats[self.player] or \
                (self.multiworld.route_required[self.player] != "genocide" and
                 self.multiworld.route_required[self.player] != "all_routes"):
            exclusion_pool.update(exclusion_table["NoStats"])

        # Choose locations to automatically exclude based on settings
        exclusion_checks = set()
        exclusion_checks.update(["Nicecream Punch Card", "Hush Trade"])
        exclusion_rules(self.multiworld, self.player, exclusion_checks)

        # Convert itempool into real items
        itempool = [item for item in map(lambda name: self.create_item(name), itempool)]
        # Fill remaining items with randomly generated junk or Temmie Flakes
        while len(itempool) < len(self.multiworld.get_unfilled_locations(self.player)):
            itempool += [self.create_filler()]

        self.multiworld.itempool += itempool
    def set_rules(self) -> None:
        set_er_location_rules(self)

    def extend_hint_information(self, hint_data: Dict[int, Dict[int, str]]):
        if self.multiworld.entrance_rando[self.player]:
            hint_data[self.player] = self.er_portal_hints

    def create_regions(self):
        def UndertaleRegion(region_name: str, exits=[]):
            ret = Region(region_name, self.player, self.multiworld)
            ret.locations += [UndertaleAdvancement(self.player, loc_name, loc_data.id, ret)
                             for loc_name, loc_data in advancement_table.items()
                             if loc_data.region == region_name and
                             (loc_name not in exclusion_table["NoKills"] or
                              (self.multiworld.kill_sanity[self.player] and
                               (self.multiworld.route_required[self.player] == "genocide" or
                                self.multiworld.route_required[self.player] == "all_routes"))) and
                             (loc_name not in exclusion_table["NoStats"] or
                              (self.multiworld.rando_stats[self.player] and
                               (self.multiworld.route_required[self.player] == "genocide" or
                                self.multiworld.route_required[self.player] == "all_routes"))) and
                             (loc_name not in exclusion_table["NoLove"] or
                              (self.multiworld.rando_love[self.player] and
                               (self.multiworld.route_required[self.player] == "genocide" or
                                self.multiworld.route_required[self.player] == "all_routes"))) and
                             (loc_name not in exclusion_table["NoSpare"]) and
                             loc_name not in exclusion_table[self.multiworld.route_required[self.player].current_key]]

            if self.multiworld.spare_sanity[self.player] and self.multiworld.route_required[self.player] != "genocide":
                if region_name == "Ruins":
                    ret.locations += [UndertaleAdvancement(self.player, "Ruins Spare "+str(i+1), 78013+i, ret) for i in range(self.multiworld.spare_sanity_max[self.player].value)]
                elif region_name == "Snowdin Forest":
                    ret.locations += [UndertaleAdvancement(self.player, "Snowdin Spare "+str(i+1), 78113+i, ret) for i in range(self.multiworld.spare_sanity_max[self.player].value)]
                elif region_name == "Waterfall":
                    ret.locations += [UndertaleAdvancement(self.player, "Waterfall Spare "+str(i+1), 78213+i, ret) for i in range(self.multiworld.spare_sanity_max[self.player].value)]
                elif region_name == "???":
                    ret.locations += [UndertaleAdvancement(self.player, "Hotland Spare "+str(i+1), 78313+i, ret) for i in range(self.multiworld.spare_sanity_max[self.player].value)]

            for exit in exits:
                ret.exits.append(Entrance(self.player, exit, ret))
            return ret

        self.undertale_portal_pairs = {}
        self.er_portal_hints = {}
        if self.multiworld.entrance_rando[self.player]:
            portal_pairs, portal_hints = create_er_regions(self)
            for portal1, portal2 in portal_pairs.items():
                self.undertale_portal_pairs[portal1.scene_destination()] = portal2.scene_destination()
            self.er_portal_hints = portal_hints
        else:
            portal_pairs = create_er_regions_vanilla(self)
            for portal1, portal2 in portal_pairs.items():
                self.undertale_portal_pairs[portal1.scene_destination()] = portal2.scene_destination()

    def fill_slot_data(self):
        slot_data = self._get_undertale_data()
        for option_name in undertale_options:
            option = getattr(self.multiworld, option_name)[self.player]
            if (option_name == "rando_love" or option_name == "rando_stats" or option_name == "kill_sanity") and \
                    self.multiworld.route_required[self.player] != "genocide" and \
                    self.multiworld.route_required[self.player] != "all_routes":
                option.value = False
                slot_data[option_name] = int(option.value)
            elif (option_name == "spare_sanity") and \
                    self.multiworld.route_required[self.player] == "genocide":
                option.value = False
                slot_data[option_name] = int(option.value)
            elif (option_name == "kill_sanity_pack_size" and ((
                    self.multiworld.route_required[self.player] != "genocide" and
                    self.multiworld.route_required[self.player] != "all_routes") or not bool(self.multiworld.kill_sanity[self.player].value))):
                option.value = 40
                slot_data[option_name] = int(option.value)
            elif slot_data.get(option_name, None) is None and type(option.value) in {str, int}:
                slot_data[option_name] = int(option.value)

        state = self.multiworld.get_all_state(False)
        state.update_reachable_regions(self.player)
        Utils.visualize_regions(self.multiworld.get_region("Menu", self.player), "undertale_check.puml", show_entrance_names=True, highlight_regions=state.reachable_regions[self.player])
        return slot_data

    def create_item(self, name: str) -> Item:
        from .Items import item_table
        item_data = item_table[name]
        item = UndertaleItem(name, item_data.classification, item_data.code, self.player)
        return item
