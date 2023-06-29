from typing import TYPE_CHECKING

import worlds.khdays.Items
from BaseClasses import CollectionState, MultiWorld

from ..generic.Rules import add_rule, set_rule

from .Locations import location_table

if TYPE_CHECKING:
    from . import KHDaysWorld

from ..AutoWorld import LogicMixin

from .Options import khdays_options


class KHDaysLogic(LogicMixin):

    def days_has_magic(self, state: CollectionState, player: int):
        return state.has_any({"Fire"}, player)

    def days_can_get_materials(self, state: CollectionState, material_name: str, player: int):
        if material_name == "Gold":
            return self.days_has_day_access(state, self.days_mission_to_day(73), player)
        if material_name == "Blazing Shard":
            return self.days_has_day_access(state, 14, player)
        if material_name == "Blazing Gem":
            return self.days_has_day_access(state, self.days_mission_to_day(51), player)
        if material_name == "Blazing Crystal":
            return self.days_has_day_access(state, self.days_mission_to_day(63), player)
        if material_name == "Frost Shard":
            return self.days_has_day_access(state, self.days_mission_to_day(21), player)
        if material_name == "Frost Gem":
            return self.days_has_day_access(state, self.days_mission_to_day(51), player)
        if material_name == "Frost Crystal":
            return self.days_has_day_access(state, self.days_mission_to_day(73), player)
        if material_name == "Lightning Shard":
            return self.days_has_day_access(state, self.days_mission_to_day(38), player)
        if material_name == "Lightning Gem":
            return self.days_has_day_access(state, self.days_mission_to_day(52), player)
        if material_name == "Lightning Crystal":
            return self.days_has_day_access(state, self.days_mission_to_day(77), player)
        if material_name == "Gust Shard":
            return self.days_has_day_access(state, self.days_mission_to_day(38), player)
        if material_name == "Gust Gem":
            return self.days_has_day_access(state, self.days_mission_to_day(62), player)
        if material_name == "Gust Crystal":
            return self.days_has_day_access(state, self.days_mission_to_day(73), player)
        if material_name == "Shining Shard":
            return self.days_has_day_access(state, self.days_mission_to_day(13), player)
        if material_name == "Shining Gem":
            return self.days_has_day_access(state, self.days_mission_to_day(53), player)
        if material_name == "Shining Crystal":
            return self.days_has_day_access(state, self.days_mission_to_day(73), player)
        if material_name == "Combo Tech":
            return self.days_has_day_access(state, self.days_mission_to_day(31), player)
        if material_name == "Combo Tech+":
            return self.days_has_day_access(state, self.days_mission_to_day(67), player)
        if material_name == "Combo Tech++":
            return self.days_has_day_access(state, self.days_mission_to_day(63), player)
        if material_name == "Power Tech":
            return self.days_has_day_access(state, self.days_mission_to_day(38), player)
        if material_name == "Power Tech+":
            return self.days_has_day_access(state, self.days_mission_to_day(58), player)
        if material_name == "Power Tech++":
            return self.days_has_day_access(state, self.days_mission_to_day(83), player)
        if material_name == "Moonstone":
            return self.days_has_day_access(state, 14, player)
        if material_name == "Premium Orb":
            return self.days_has_day_access(state, self.days_mission_to_day(73), player)
        if material_name == "Diamond":
            return self.days_has_day_access(state, self.days_mission_to_day(82), player)
        if material_name == "Range Tech":
            return self.days_has_day_access(state, self.days_mission_to_day(40), player)
        if material_name == "Range Tech+":
            return self.days_has_day_access(state, self.days_mission_to_day(63), player)
        if material_name == "Range Tech++":
            return self.days_has_day_access(state, self.days_mission_to_day(79), player)
        if material_name == "Adamantite":
            return self.days_has_day_access(state, self.days_mission_to_day(73), player)
        if material_name == "Combo Tech":
            return self.days_has_day_access(state, self.days_mission_to_day(29), player)
        if material_name == "Combo Tech+":
            return self.days_has_day_access(state, self.days_mission_to_day(67), player)
        if material_name == "Combo Tech++":
            return self.days_has_day_access(state, self.days_mission_to_day(63), player)
        if material_name == "Shield Tech":
            return self.days_has_day_access(state, self.days_mission_to_day(39), player)
        if material_name == "Shield Tech+":
            return self.days_has_day_access(state, self.days_mission_to_day(65), player)
        if material_name == "Shield Tech++":
            return self.days_has_day_access(state, self.days_mission_to_day(74), player)
        if material_name == "Aerial Tech":
            return self.days_has_day_access(state, self.days_mission_to_day(47), player)
        if material_name == "Aerial Tech+":
            return self.days_has_day_access(state, self.days_mission_to_day(65), player)
        if material_name == "Aerial Tech++":
            return self.days_has_day_access(state, self.days_mission_to_day(81), player)
        if material_name == "Luck Tech":
            return self.days_has_day_access(state, self.days_mission_to_day(77), player)
        if material_name == "Rune Tech":
            return self.days_has_day_access(state, self.days_mission_to_day(47), player)
        if material_name == "Rune Tech+":
            return self.days_has_day_access(state, self.days_mission_to_day(65), player)
        if material_name == "Rune Tech++":
            return self.days_has_day_access(state, self.days_mission_to_day(85), player)
        if material_name == "Gear Component A":
            return self.days_has_day_access(state, self.days_mission_to_day(36), player)
        if material_name == "Gear Component B":
            return self.days_has_day_access(state, self.days_mission_to_day(51), player)
        if material_name == "Gear Component C":
            return self.days_has_day_access(state, self.days_mission_to_day(62), player)
        if material_name == "Gear Component D":
            return self.days_has_day_access(state, self.days_mission_to_day(82), player)
        if material_name == "Dark Ingot":
            return self.days_has_day_access(state, self.days_mission_to_day(52), player)
        if material_name == "Bronze":
            return self.days_has_day_access(state, self.days_mission_to_day(49), player)
        if material_name == "Mithril":
            return self.days_has_day_access(state, self.days_mission_to_day(85), player)
        if material_name == "Silver":
            return self.days_has_day_access(state, self.days_mission_to_day(64), player)
        if material_name == "Orichalcum":
            return self.days_has_day_access(state, self.days_mission_to_day(82), player)
        if material_name == "Iron":
            return self.days_has_day_access(state, self.days_mission_to_day(16), player)
        if material_name == "Ankharite":
            return self.days_has_day_access(state, self.days_mission_to_day(73), player)
        print("not found: "+material_name)
        return False

    def days_check_panels(self, state: CollectionState, player: int):
        panel_count = state.count("Panel Slot", player)
        slot_space_1 = [[1 for y in range(8)] for x in range(5)]
        slot_space_2 = [[1 for y in range(8)] for x in range(5)]
        slot_space_3 = [[1 for y in range(8)] for x in range(5)]
        for y in range(3):
            for x in range(5):
                slot_space_1[x][y] = 0
        x = 0
        y = 3
        space = 0
        for i in range(panel_count):
            if space == 0:
                slot_space_1[x][y] = 0
            elif space == 1:
                slot_space_2[x][y] = 0
            elif space == 2:
                slot_space_3[x][y] = 0
            x += 1
            if x >= 5:
                x = 0
                y += 1
            if y >= 8:
                y = 0
                x = 0
                space += 1
            if space >= 3:
                break
        return slot_space_1, slot_space_2, slot_space_3

    def days_levels_obtainable(self, state: CollectionState, player: int):
        obtainable = 0
        if self.days_has_day_access(state, self.days_mission_to_day(10), player):
            obtainable += 5
        if self.days_has_day_access(state, self.days_mission_to_day(25), player):
            obtainable += 6
        if self.days_has_day_access(state, self.days_mission_to_day(50), player):
            obtainable += 6
        if self.days_has_day_access(state, self.days_mission_to_day(75), player):
            obtainable += 7
        if self.days_has_day_access(state, self.days_mission_to_day(90), player):
            obtainable += 8
        if self.days_shop_status(state, player) >= 1:
            obtainable += 1
        if self.days_shop_status(state, player) >= 2:
            obtainable += 1
        if self.days_shop_status(state, player) >= 4:
            obtainable += 1
        if self.days_challenges_completable(state, player) >= 90:
            obtainable += 1
        if self.days_challenges_completable(state, player) >= 140:
            obtainable += 1
        if self.days_challenges_completable(state, player) >= 210:
            obtainable += 1
        if self.days_challenges_completable(state, player) >= 230:
            obtainable += 1
        return obtainable

    def days_crowns_obtainable(self, state: CollectionState, player: int):
        obtainable = 0
        if self.days_has_day_access(state, self.days_mission_to_day(93), player):
            obtainable += 1
        return obtainable

    def days_challenges_completable(self, state: CollectionState, player: int):
        completable = 0
        if self.days_has_day_access(state, self.days_mission_to_day(93), player):
            completable += 1
        return completable

    def days_mission_to_day(self, mission_number: int):
        day_number = 7
        for i in range(mission_number):
            if 17 <= day_number < 22:
                day_number = 22
            elif 26 <= day_number < 51:
                day_number = 51
            elif 54 <= day_number < 71:
                day_number = 71
            elif 79 <= day_number < 94:
                day_number = 94
            elif 100 <= day_number < 117:
                day_number = 117
            elif 122 <= day_number < 149:
                day_number = 149
            elif 156 <= day_number < 171:
                day_number = 171
            elif 176 <= day_number < 193:
                day_number = 193
            elif 197 <= day_number < 224:
                day_number = 224
            elif 227 <= day_number < 255:
                day_number = 255
            elif 258 <= day_number < 277:
                day_number = 277
            elif 280 <= day_number < 296:
                day_number = 296
            elif 304 <= day_number < 321:
                day_number = 321
            elif 326 <= day_number < 352:
                day_number = 352
            elif 355 <= day_number < 357:
                day_number = 357
            else:
                day_number += 1
        return day_number

    def days_day_to_mission(self, day_number_2: int):
        day_number = 7
        mission_number = 0
        while day_number_2 > day_number:
            mission_number += 1
            if 17 <= day_number < 22:
                day_number = 22
            elif 26 <= day_number < 51:
                day_number = 51
            elif 54 <= day_number < 71:
                day_number = 71
            elif 79 <= day_number < 94:
                day_number = 94
            elif 100 <= day_number < 117:
                day_number = 117
            elif 122 <= day_number < 149:
                day_number = 149
            elif 156 <= day_number < 171:
                day_number = 171
            elif 176 <= day_number < 193:
                day_number = 193
            elif 197 <= day_number < 224:
                day_number = 224
            elif 227 <= day_number < 255:
                day_number = 255
            elif 258 <= day_number < 277:
                day_number = 277
            elif 280 <= day_number < 296:
                day_number = 296
            elif 304 <= day_number < 321:
                day_number = 321
            elif 326 <= day_number < 352:
                day_number = 352
            elif 355 <= day_number < 357:
                day_number = 357
            else:
                day_number += 1
        return mission_number

    def days_has_day_access(self, state: CollectionState, day_number: int, player: int):
        can_do = True
        if day_number >= 193:
            can_do = can_do and state.has_any({"Glide 3", "Glide 5"}, player)
        if day_number >= 11:
            can_do = can_do and self.days_has_magic(state, player)
        return can_do and state.has("Panel Slot", player, max(0, self.days_day_to_mission(day_number)-5))

    def days_shop_status(self, state: CollectionState, player: int):
        if self.days_has_day_access(state, 358, player):
            return 6  # Legend
        if self.days_has_day_access(state, 296, player):
            return 5  # Master
        if self.days_has_day_access(state, 225, player):
            return 4  # Expert
        if self.days_has_day_access(state, 172, player):
            return 3  # Agent
        if self.days_has_day_access(state, 117, player):
            return 2  # Rookie
        if self.days_has_day_access(state, 26, player):
            return 1  # Novice
        return 0


def set_rules(world: MultiWorld, player: int):
    for i in world.get_locations(player):
        if i.name.startswith("Mission "):
            set_rule(i, lambda state, i=i: state.days_has_day_access(state, max(11, state.days_mission_to_day(int(i.name.removeprefix("Mission ").split(":")[0]))), player))
        else:
            set_rule(i, lambda state: state.days_has_day_access(state, 11, player))
    for i in range(93):
        set_rule(world.get_location("Mission "+str(i+1)+": Reward 1", player), lambda state, i=i: state.days_has_day_access(state, state.days_mission_to_day(i+1), player))
        set_rule(world.get_location("Mission "+str(i+1)+": Reward 2", player), lambda state, i=i: state.days_has_day_access(state, state.days_mission_to_day(i+1), player))
        set_rule(world.get_location("Mission "+str(i+1)+": Reward 3", player), lambda state, i=i: state.days_has_day_access(state, state.days_mission_to_day(i+1), player))
        set_rule(world.get_location("Mission "+str(i+1)+": Reward 4", player), lambda state, i=i: state.days_has_day_access(state, max(11, state.days_mission_to_day(i+1)), player))
        set_rule(world.get_location("Mission "+str(i+1)+": Reward 5", player), lambda state, i=i: state.days_has_day_access(state, max(11, state.days_mission_to_day(i+1)), player))
    set_rule(world.get_location("Mission 1: Potion 1", player), lambda state: True)
    for i in range(20):
        set_rule(world.get_location("Moogle: Potion "+str(i+1), player), lambda state: state.days_shop_status(state, player) >= 1)
        set_rule(world.get_location("Moogle: Ether "+str(i+1), player), lambda state: state.days_shop_status(state, player) >= 1)
    for i in range(39):
        set_rule(world.get_location("Hub: Level Up "+str(i+1), player), lambda state: state.days_levels_obtainable(state, player) >= i+1)
    set_rule(world.get_location("Moogle: Panel Slot 1", player), lambda state: state.days_shop_status(state, player) >= 1)
    set_rule(world.get_location("Moogle: Aerial Recovery 1", player), lambda state: state.days_shop_status(state, player) >= 1)
    set_rule(world.get_location("Moogle: Power Unit 1", player), lambda state: state.days_shop_status(state, player) >= 1)
    set_rule(world.get_location("Moogle: Brawl Ring 1", player), lambda state: state.days_shop_status(state, player) >= 1)
    set_rule(world.get_location("Moogle: Fire 1", player), lambda state: state.days_shop_status(state, player) >= 1)
    set_rule(world.get_location("Moogle: Fire 2", player), lambda state: state.days_shop_status(state, player) >= 1)
    for i in range(10):
        set_rule(world.get_location("Moogle: Fire "+str(i+3), player), lambda state: state.days_shop_status(state, player) >= 1 and state.has("Fire Recipe", player, i+1) and state.days_can_get_materials(state, "Blazing Shard", player))
    for i in range(10):
        set_rule(world.get_location("Moogle: Limit Recharge " + str(i + 1), player),
                 lambda state: state.days_shop_status(state, player) >= 1 and state.days_can_get_materials(state, "Blazing Shard", player) and state.days_can_get_materials(state, "Shining Shard", player) and state.days_can_get_materials(state, "Moonstone", player))

    set_rule(world.get_location("Moogle: Blizzard 1", player), lambda state: state.days_shop_status(state, player) >= 1)
    set_rule(world.get_location("Moogle: Blizzard 2", player), lambda state: state.days_shop_status(state, player) >= 1)
    set_rule(world.get_location("Moogle: Soldier Ring 1", player), lambda state: state.days_shop_status(state, player) >= 1)
    set_rule(world.get_location("Moogle: Wild Gear 3 1", player), lambda state: state.days_shop_status(state, player) >= 1)
    set_rule(world.get_location("Moogle: Lift Gear 3 1", player), lambda state: state.days_shop_status(state, player) >= 1)
    set_rule(world.get_location("Moogle: Chrono Gear 3 1", player), lambda state: state.days_shop_status(state, player) >= 1)
    set_rule(world.get_location("Moogle: Technical Gear 3 1", player), lambda state: state.days_shop_status(state, player) >= 1)
    set_rule(world.get_location("Moogle: Triplecast 3 1", player), lambda state: state.days_shop_status(state, player) >= 1)
    set_rule(world.get_location("Mission 1: Reward 4", player), lambda state: state.days_has_day_access(state, state.days_mission_to_day(1), player))
    set_rule(world.get_location("Mission 1: Reward 5", player), lambda state: state.days_has_day_access(state, state.days_mission_to_day(1), player))
    set_rule(world.get_location("Mission 2: Reward 4", player), lambda state: state.days_has_day_access(state, state.days_mission_to_day(2), player))
    set_rule(world.get_location("Mission 2: Reward 5", player), lambda state: state.days_has_day_access(state, state.days_mission_to_day(2), player))
    set_rule(world.get_location("Mission 4: Reward 4", player), lambda state: state.days_has_day_access(state, state.days_mission_to_day(4), player))
    set_rule(world.get_location("Mission 4: Reward 5", player), lambda state: state.days_has_day_access(state, state.days_mission_to_day(4), player))
    add_rule(world.get_location("Mission 9: Reward 4", player), lambda state: state.has("Level Up", player, 5))
    add_rule(world.get_location("Mission 9: Reward 5", player), lambda state: state.has("Level Up", player, 5))


def set_completion_rules(world: MultiWorld, player: int):
    world.completion_condition[player] = lambda state, world=world: state.days_has_day_access(state, world.DayRequirement[player].value, player)
