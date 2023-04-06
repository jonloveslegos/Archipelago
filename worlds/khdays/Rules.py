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

    def days_crowns_obatianable(self, state: CollectionState, player: int):
        obtainable = 0
        if self.days_mission_to_day(93):
            obtainable += 1
        return obtainable

    def days_challenges_completable(self, state: CollectionState, player: int):
        completable = 0
        if self.days_mission_to_day(93):
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

    def days_has_day_access(self, state: CollectionState, day_number: int, player: int):
        can_do = True
        if day_number >= 193:
            can_do = can_do and state.has_any({"Glide 3", "Glide 5"}, player)
        if day_number >= 11:
            can_do = can_do and self.days_has_magic(state, player)
        if day_number > 7:
            days = [7, 8, 9, 10, 11, 12, 13, 14, 15, 22, 23, 24, 25, 26, 51, 71, 72, 73, 74, 75, 94, 95, 96, 97, 117, 118,
                119, 149, 150, 151, 152, 171, 172, 173, 193, 194, 224, 225, 255, 256, 277, 296, 297, 298, 299, 300, 301,
                321, 322, 352, 353, 354, 355, 357, 358]
            temp_number = day_number
            while temp_number not in days:
                temp_number += 1
            can_do = can_do and state.has("Day "+str(days[days.index(temp_number)-1]), player)
        return can_do

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

    def days_has_count_access(self, state: CollectionState, item_name: str, req_count: int, player: int):
        total = 0
        if item_name == "Potion":
            if self.days_has_day_access(state, 8, player):
                total += 1
            if self.days_has_day_access(state, 14, player):
                total += 4
            if self.days_has_day_access(state, 353, player):
                total += 2
            if self.days_has_day_access(state, 354, player):
                total += 1
            if self.days_has_day_access(state, 11, player):
                total += 1
            if self.days_has_day_access(state, 15, player):
                total += 6
            if self.days_has_day_access(state, 22, player):
                total += 3
            if self.days_has_day_access(state, 23, player):
                total += 2
            if self.days_has_day_access(state, 25, player):
                total += 3
            if self.days_has_day_access(state, 26, player):
                total += 3
            if self.days_has_day_access(state, 51, player):
                total += 5
            if self.days_has_day_access(state, 72, player):
                total += 5
            if self.days_has_day_access(state, 73, player):
                total += 1
            if self.days_has_day_access(state, 75, player):
                total += 12
            if self.days_has_day_access(state, 94, player):
                total += 2
            if self.days_has_day_access(state, 95, player):
                total += 3
            if self.days_has_day_access(state, 97, player):
                total += 9
            if self.days_has_day_access(state, 152, player):
                total += 2
            if self.days_shop_status(state, player) >= 1:
                total += 20
            if self.days_has_day_access(state, 358, player):
                total += 10
        elif item_name == "Thunder":
            if self.days_has_day_access(state, 117, player):
                total += 2
            if self.days_has_day_access(state, 301, player):
                if self.days_can_get_materials(state, "Lightning Shard", player) and self.days_shop_status(state, player) >= 1:
                    total += 1
            if self.days_has_day_access(state, 277, player):
                if self.days_can_get_materials(state, "Lightning Shard", player) and self.days_shop_status(state, player) >= 1:
                    total += 1
            if self.days_has_day_access(state, 119, player):
                total += 1
                if self.days_can_get_materials(state, "Lightning Shard", player) and self.days_shop_status(state, player) >= 1:
                    total += 3
            if self.days_has_day_access(state, 152, player):
                total += 1
                if self.days_can_get_materials(state, "Lightning Shard", player) and self.days_shop_status(state, player) >= 1:
                    total += 2
            if self.days_has_day_access(state, 151, player):
                if self.days_can_get_materials(state, "Lightning Shard", player) and self.days_shop_status(state, player) >= 1:
                    total += 1
            if self.days_has_day_access(state, 173, player):
                if self.days_can_get_materials(state, "Lightning Shard", player) and self.days_shop_status(state, player) >= 1:
                    total += 2
            if self.days_has_day_access(state, 193, player):
                if self.days_can_get_materials(state, "Lightning Shard", player) and self.days_shop_status(state, player) >= 1:
                    total += 2
            if self.days_has_day_access(state, 194, player):
                if self.days_can_get_materials(state, "Lightning Shard", player) and self.days_shop_status(state, player) >= 1:
                    total += 1
            if self.days_has_day_access(state, 225, player):
                if self.days_can_get_materials(state, "Lightning Shard", player) and self.days_shop_status(state, player) >= 1:
                    total += 1
            if self.days_shop_status(state, player) >= 2:
                total += 2
            if self.days_has_day_access(state, 358, player):
                total += 3
        elif item_name == "Thundara":
            if self.days_has_day_access(state, 193, player):
                total += 1
            if self.days_shop_status(state, player) >= 4:
                total += 2
            if self.days_has_day_access(state, 256, player) and self.days_shop_status(state, player) >= 1 and state.has("Thunder", player, 4) and self.days_can_get_materials(state, "Lightning Gem", player):
                total += 1
            if self.days_has_day_access(state, 277, player) and self.days_shop_status(state, player) >= 1 and state.has("Thunder", player, 4) and self.days_can_get_materials(state, "Lightning Gem", player):
                total += 2
            if self.days_has_day_access(state, 355, player) and self.days_shop_status(state, player) >= 1 and state.has("Thunder", player, 4) and self.days_can_get_materials(state, "Lightning Gem", player):
                total += 1
            if self.days_has_day_access(state, 358, player):
                total += 2
        elif item_name == "Thundaga":
            if self.days_has_day_access(state, 277, player):
                total += 1
            if self.days_has_day_access(state, 256, player) and self.days_shop_status(state, player) >= 1 and state.has("Thundara", player, 4) and self.days_can_get_materials(state, "Lightning Crystal", player):
                total += 1
            if self.days_has_day_access(state, 300, player) and self.days_shop_status(state, player) >= 1 and state.has("Thundara", player, 4) and self.days_can_get_materials(state, "Lightning Crystal", player):
                total += 1
            if self.days_has_day_access(state, 351, player) and self.days_shop_status(state, player) >= 1 and state.has("Thundara", player, 4) and self.days_can_get_materials(state, "Lightning Crystal", player):
                total += 2

        elif item_name == "Guard Unit":
            if self.days_has_day_access(state, 71, player):
                total += 1
            if self.days_shop_status(state, player) >= 2:
                total += 1
            if self.days_shop_status(state, player) >= 4:
                total += 1
            if self.days_shop_status(state, player) >= 6:
                total += 1
            if self.days_has_day_access(state, 358, player):
                total += 1
        elif item_name == "Magic Unit":
            if self.days_has_day_access(state, 296, player):
                total += 1
            if self.days_shop_status(state, player) >= 2:
                total += 1
            if self.days_shop_status(state, player) >= 4:
                total += 1
            if self.days_shop_status(state, player) >= 6:
                total += 1
            if self.days_has_day_access(state, 358, player):
                total += 1
        elif item_name == "Cure":
            if self.days_has_day_access(state, 71, player):
                total += 2
            if self.days_has_day_access(state, 358, player):
                total += 3
            if self.days_has_day_access(state, 75, player):
                total += 1
            if self.days_has_day_access(state, 97, player):
                total += 1
            if self.days_has_day_access(state, 152, player):
                total += 1
                if self.days_can_get_materials(state, "Shining Shard", player) and self.days_shop_status(state, player) >= 1:
                    total += 2
            if self.days_has_day_access(state, 150, player):
                if self.days_can_get_materials(state, "Shining Shard", player) and self.days_shop_status(state, player) >= 1:
                    total += 1
            if self.days_has_day_access(state, 255, player):
                if self.days_can_get_materials(state, "Shining Shard", player) and self.days_shop_status(state, player) >= 1:
                    total += 1
            if self.days_has_day_access(state, 194, player):
                total += 1
            if self.days_has_day_access(state, 74, player):
                if self.days_can_get_materials(state, "Shining Shard", player) and self.days_shop_status(state, player) >= 1:
                    total += 1
            if self.days_has_day_access(state, 225, player):
                if self.days_can_get_materials(state, "Shining Shard", player) and self.days_shop_status(state, player) >= 1:
                    total += 1
            if self.days_has_day_access(state, 119, player):
                if self.days_can_get_materials(state, "Shining Shard", player) and self.days_shop_status(state, player) >= 1:
                    total += 2
            if self.days_has_day_access(state, 149, player):
                if self.days_can_get_materials(state, "Shining Shard", player) and self.days_shop_status(state, player) >= 1:
                    total += 1
            if self.days_has_day_access(state, 171, player):
                if self.days_can_get_materials(state, "Shining Shard", player) and self.days_shop_status(state, player) >= 1:
                    total += 1
            if self.days_has_day_access(state, 173, player):
                if self.days_can_get_materials(state, "Shining Shard", player) and self.days_shop_status(state, player) >= 1:
                    total += 1
            if self.days_shop_status(state, player) >= 2:
                total += 2
        elif item_name == "Duel Gear+ 4":
            if self.days_has_day_access(state, 194, player):
                total += 1
        elif item_name == "Dodge Roll 3":
            if self.days_has_day_access(state, 172, player):
                total += 1
        elif item_name == "Cura":
            if self.days_has_day_access(state, 171, player):
                total += 1
            if self.days_has_day_access(state, 172, player) and self.days_shop_status(state, player) >= 1 and state.has("Cure", player, 7) and self.days_can_get_materials(state, "Shining Gem", player):
                total += 1
            if self.days_has_day_access(state, 173, player) and self.days_shop_status(state, player) >= 1 and state.has("Cure", player, 7) and self.days_can_get_materials(state, "Shining Gem", player):
                total += 2
            if self.days_has_day_access(state, 194, player) and self.days_shop_status(state, player) >= 1 and state.has("Cure", player, 7) and self.days_can_get_materials(state, "Shining Gem", player):
                total += 1
            if self.days_has_day_access(state, 224, player) and self.days_shop_status(state, player) >= 1 and state.has("Cure", player, 7) and self.days_can_get_materials(state, "Shining Gem", player):
                total += 1
            if self.days_has_day_access(state, 255, player) and self.days_shop_status(state, player) >= 1 and state.has("Cure", player, 7) and self.days_can_get_materials(state, "Shining Gem", player):
                total += 2
            if self.days_shop_status(state, player) >= 3:
                total += 2
            if self.days_has_day_access(state, 358, player):
                total += 2
        elif item_name == "Curaga":
            if self.days_has_day_access(state, 256, player) and state.has("High Jump 3", player) and state.has(
                    "High Jump LV+", player) and state.has("High Jump LV+", player):
                total += 1
            if self.days_has_day_access(state, 256, player) and self.days_shop_status(state, player) >= 1 and state.has("Cura", player, 4) and self.days_can_get_materials(state, "Shining Crystal", player):
                total += 1
            if self.days_has_day_access(state, 299, player) and self.days_shop_status(state, player) >= 1 and state.has("Cura", player, 4) and self.days_can_get_materials(state, "Shining Crystal", player):
                total += 1
            if self.days_has_day_access(state, 322, player) and self.days_shop_status(state, player) >= 1 and state.has("Cura", player, 4) and self.days_can_get_materials(state, "Shining Crystal", player):
                total += 2
        elif item_name == "Magic LV2 4":
            if self.days_has_day_access(state, 71, player):
                total += 1
        elif item_name == "Final Limit":
            if self.days_has_day_access(state, 225, player):
                total += 1
        elif item_name == "Magic LV2 4B":
            if self.days_shop_status(state, player) >= 2:
                total += 1
        elif item_name == "Magic LV2 4C":
            if self.days_shop_status(state, player) >= 5:
                total += 1
        elif item_name == "Magic LV3 4":
            if self.days_shop_status(state, player) >= 3:
                total += 1
        elif item_name == "Magic LV3 4B":
            if self.days_shop_status(state, player) >= 4:
                total += 1
        elif item_name == "Magic LV4 4":
            if self.days_has_day_access(state, 297, player):
                total += 1
        elif item_name == "Hi-Potion":
            if self.days_has_day_access(state, 15, player):
                total += 1
            if self.days_has_day_access(state, 354, player):
                total += 2
            if self.days_has_day_access(state, 353, player):
                total += 1
            if self.days_has_day_access(state, 322, player):
                total += 2
            if self.days_has_day_access(state, 277, player):
                total += 1
            if self.days_has_day_access(state, 256, player):
                total += 4
            if self.days_has_day_access(state, 75, player):
                total += 4
            if self.days_has_day_access(state, 95, player):
                total += 2
            if self.days_has_day_access(state, 152, player):
                total += 3
            if self.days_has_day_access(state, 255, player):
                total += 1
            if self.days_has_day_access(state, 151, player):
                total += 1
            if self.days_has_day_access(state, 321, player):
                total += 1
            if self.days_has_day_access(state, 73, player):
                total += 1
            if self.days_has_day_access(state, 97, player):
                total += 3
            if self.days_has_day_access(state, 119, player):
                total += 2
            if self.days_has_day_access(state, 225, player):
                total += 1
            if self.days_has_day_access(state, 152, player):
                total += 1
            if self.days_has_day_access(state, 171, player):
                total += 1
            if self.days_has_day_access(state, 172, player):
                total += 1
            if self.days_has_day_access(state, 194, player):
                total += 1
            if self.days_shop_status(state, player) >= 3:
                total += 10
            if self.days_has_day_access(state, 358, player):
                total += 10
        elif item_name == "Hi-Ether":
            if self.days_has_day_access(state, 301, player):
                total += 2
            if self.days_has_day_access(state, 321, player):
                total += 1
            if self.days_has_day_access(state, 277, player):
                total += 1
            if self.days_has_day_access(state, 256, player):
                total += 2
            if self.days_has_day_access(state, 322, player):
                total += 1
            if self.days_has_day_access(state, 353, player):
                total += 3
            if self.days_shop_status(state, player) >= 3:
                total += 10
            if self.days_has_day_access(state, 358, player):
                total += 10
        elif item_name == "Mega-Ether":
            if self.days_shop_status(state, player) >= 5:
                total += 5
            if self.days_has_day_access(state, 358, player):
                total += 10
        elif item_name == "Megalixir":
            if self.days_has_day_access(state, 225, player):
                total += 1
            if self.days_has_day_access(state, 358, player):
                total += 5
        elif item_name == "Mega-Potion":
            if self.days_shop_status(state, player) >= 5:
                total += 5
            if self.days_has_day_access(state, 358, player):
                total += 10
        elif item_name == "Blizzara":
            if self.days_has_day_access(state, 152, player):
                total += 1
            if self.days_has_day_access(state, 193, player):
                total += 1
            if self.days_has_day_access(state, 256, player) and self.days_shop_status(state, player) >= 1 and state.has("Blizzard", player, 4) and self.days_can_get_materials(state, "Frost Gem", player):
                total += 1
            if self.days_has_day_access(state, 194, player):
                total += 1
            if self.days_has_day_access(state, 173, player) and self.days_shop_status(state, player) >= 1 and state.has("Blizzard", player, 4) and self.days_can_get_materials(state, "Frost Gem", player):
                total += 1
            if self.days_has_day_access(state, 225, player) and self.days_shop_status(state, player) >= 1 and state.has("Blizzard", player, 4) and self.days_can_get_materials(state, "Frost Gem", player):
                total += 1
            if self.days_has_day_access(state, 225, player):
                total += 2
            if self.days_has_day_access(state, 322, player) and self.days_shop_status(state, player) >= 1 and state.has("Blizzard", player, 4) and self.days_can_get_materials(state, "Frost Gem", player):
                total += 1
            if self.days_shop_status(state, player) >= 3:
                total += 2
            if self.days_has_day_access(state, 358, player):
                total += 2
        elif item_name == "Blizzaga":
            if self.days_has_day_access(state, 301, player) and self.days_shop_status(state, player) >= 1 and state.has("Blizzara", player, 4) and self.days_can_get_materials(state, "Frost Crystal", player):
                total += 1
            if self.days_has_day_access(state, 301, player):
                total += 1
            if self.days_has_day_access(state, 322, player) and self.days_shop_status(state, player) >= 1 and state.has("Blizzara", player, 4) and self.days_can_get_materials(state, "Frost Crystal", player):
                total += 1
            if self.days_has_day_access(state, 352, player) and self.days_shop_status(state, player) >= 1 and state.has("Blizzara", player, 4) and self.days_can_get_materials(state, "Frost Crystal", player):
                total += 2
        elif item_name == "Pack Extender":
            if self.days_has_day_access(state, 96, player):
                total += 1
        elif item_name == "Aero":
            if self.days_has_day_access(state, 97, player):
                total += 1
            if self.days_has_day_access(state, 225, player):
                if self.days_can_get_materials(state, "Gust Shard", player) and self.days_shop_status(state, player) >= 1:
                    total += 2
            if self.days_has_day_access(state, 256, player):
                if self.days_can_get_materials(state, "Gust Shard", player) and self.days_shop_status(state, player) >= 1:
                    total += 2
            if self.days_has_day_access(state, 119, player):
                total += 1
                if self.days_can_get_materials(state, "Gust Shard", player) and self.days_shop_status(state, player) >= 1:
                    total += 3
            if self.days_shop_status(state, player) >= 2:
                total += 2
            if self.days_has_day_access(state, 150, player):
                if self.days_can_get_materials(state, "Gust Shard", player) and self.days_shop_status(state, player) >= 1:
                    total += 1
            if self.days_has_day_access(state, 152, player):
                if self.days_can_get_materials(state, "Gust Shard", player) and self.days_shop_status(state, player) >= 1:
                    total += 1
            if self.days_has_day_access(state, 172, player):
                if self.days_can_get_materials(state, "Gust Shard", player) and self.days_shop_status(state, player) >= 1:
                    total += 1
            if self.days_has_day_access(state, 194, player):
                if self.days_can_get_materials(state, "Gust Shard", player) and self.days_shop_status(state, player) >= 1:
                    total += 1
            if self.days_has_day_access(state, 255, player):
                if self.days_can_get_materials(state, "Gust Shard", player) and self.days_shop_status(state, player) >= 1:
                    total += 1
            if self.days_has_day_access(state, 358, player):
                total += 3
        elif item_name == "Aerora":
            if self.days_has_day_access(state, 119, player) and self.days_shop_status(state, player) >= 1 and state.has("Aero", player, 6) and self.days_can_get_materials(state, "Gust Gem", player):
                total += 1
            if self.days_has_day_access(state, 321, player) and self.days_shop_status(state, player) >= 1 and state.has("Aero", player, 6) and self.days_can_get_materials(state, "Gust Gem", player):
                total += 1
            if self.days_has_day_access(state, 256, player) and self.days_shop_status(state, player) >= 1 and state.has("Aero", player, 6) and self.days_can_get_materials(state, "Gust Gem", player):
                total += 1
            if self.days_has_day_access(state, 225, player) and self.days_shop_status(state, player) >= 1 and state.has("Aero", player, 6) and self.days_can_get_materials(state, "Gust Gem", player):
                total += 1
            if self.days_has_day_access(state, 277, player) and self.days_shop_status(state, player) >= 1 and state.has("Aero", player, 6) and self.days_can_get_materials(state, "Gust Gem", player):
                total += 1
            if self.days_has_day_access(state, 355, player) and self.days_shop_status(state, player) >= 1 and state.has("Aero", player, 6) and self.days_can_get_materials(state, "Gust Gem", player):
                total += 1
            if self.days_has_day_access(state, 358, player):
                total += 3
        elif item_name == "Aeroga":
            if self.days_has_day_access(state, 297, player) and self.days_shop_status(state, player) >= 1 and state.has("Aerora", player, 3) and self.days_can_get_materials(state, "Gust Crystal", player):
                total += 1
            if self.days_has_day_access(state, 322, player) and self.days_shop_status(state, player) >= 1 and state.has("Aerora", player, 3) and self.days_can_get_materials(state, "Gust Crystal", player):
                total += 2
            if self.days_has_day_access(state, 358, player):
                total += 1
        elif item_name == "LV Doubler 6":
            if self.days_has_day_access(state, 149, player):
                total += 1
        elif item_name == "LV Doubler 6B":
            if self.days_has_day_access(state, 193, player):
                total += 1
        elif item_name == "LV Doubler 6C":
            if self.days_has_day_access(state, 358, player):
                total += 1
        elif item_name == "LV Doubler 6D":
            if self.days_has_day_access(state, 358, player):
                total += 1
        elif item_name == "Sliding Dash":
            if self.days_has_day_access(state, 149, player):
                total += 1
        elif item_name == "Sliding Dash 3":
            if self.days_has_day_access(state, 256, player) and state.has("High Jump 3", player) and state.has("High Jump LV+", player) and state.has("High Jump LV+", player):
                total += 1
        elif item_name == "Sliding Dash LV+":
            if self.days_has_day_access(state, 321, player):
                total += 1
            if self.days_has_day_access(state, 358, player):
                total += 1
        elif item_name == "Fira":
            if self.days_has_day_access(state, 149, player):
                total += 1
            if self.days_has_day_access(state, 150, player):
                total += 1
            if self.days_has_day_access(state, 173, player):
                total += 1
            if self.days_has_day_access(state, 151, player) and self.days_shop_status(state, player) >= 1 and state.has("Fire", player, 3) and self.days_can_get_materials(state, "Blazing Gem",
                                                                                             player):
                total += 1
            if self.days_shop_status(state, player) >= 3:
                total += 2
            if self.days_has_day_access(state, 298, player) and self.days_shop_status(state, player) >= 1 and state.has("Fire", player, 3) and self.days_can_get_materials(state, "Blazing Gem",
                                                                                             player):
                total += 1
            if self.days_has_day_access(state, 322, player) and self.days_shop_status(state, player) >= 1 and state.has("Fire", player, 3) and self.days_can_get_materials(state, "Blazing Gem",
                                                                                             player):
                total += 1
            if self.days_has_day_access(state, 358, player):
                total += 2
        elif item_name == "Firaga":
            if self.days_has_day_access(state, 224, player) and self.days_shop_status(state, player) >= 1 and state.has("Fira", player, 3) and self.days_can_get_materials(state, "Blazing Crystal",
                                                                                             player):
                total += 1
            if self.days_has_day_access(state, 322, player) and self.days_shop_status(state, player) >= 1 and state.has("Fira", player, 3) and self.days_can_get_materials(state, "Blazing Crystal",
                                                                                             player):
                total += 2
        elif item_name == "High Jump":
            if self.days_has_day_access(state, 151, player):
                total += 1
        elif item_name == "High Jump LV+":
            if self.days_shop_status(state, player) >= 5:
                total += 1
            if self.days_shop_status(state, player) >= 6:
                total += 1
        elif item_name == "High Jump 3":
            if self.days_has_day_access(state, 297, player):
                total += 1
        elif item_name == "Treasure Magnet":
            if self.days_has_day_access(state, 94, player):
                total += 1
        elif item_name == "Treasure Magnet 3":
            if self.days_shop_status(state, player) >= 4:
                total += 1
        elif item_name == "Treasure Magnet LV+":
            if self.days_shop_status(state, player) >= 5:
                total += 2
        elif item_name == "Auto-Life 3":
            if self.days_shop_status(state, player) >= 2:
                total += 1
        elif item_name == "Auto-Life LV+":
            if self.days_shop_status(state, player) >= 3:
                total += 1
            if self.days_shop_status(state, player) >= 5:
                total += 1
        elif item_name == "Limit Boost":
            if self.days_shop_status(state, player) >= 3:
                total += 1
        elif item_name == "Limit Recharge":
            if self.days_has_day_access(state, 358, player):
                total += 5
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Blazing Shard", player) and self.days_can_get_materials(state, "Moonstone", player) and self.days_can_get_materials(state, "Shining Shard", player):
                total += 5
        elif item_name == "Range Extender":
            if self.days_shop_status(state, player) >= 2:
                total += 1
        elif item_name == "Auto-Lock":
            if self.days_shop_status(state, player) >= 3:
                total += 1
        elif item_name == "Valor Gear 2":
            if self.days_has_day_access(state, 94, player):
                total += 1
        elif item_name == "Fire":
            if self.days_has_day_access(state, 10, player):
                total += 2
            if self.days_has_day_access(state, 322, player):
                if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Blazing Shard",
                                                                                             player):
                    total += 1
            if self.days_has_day_access(state, 298, player):
                if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Blazing Shard",
                                                                                             player):
                    total += 1
            if self.days_has_day_access(state, 296, player):
                if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Blazing Shard",
                                                                                             player):
                    total += 1
            if self.days_has_day_access(state, 256, player):
                if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Blazing Shard",
                                                                                             player):
                    total += 1
            if self.days_has_day_access(state, 14, player):
                total += 2
            if self.days_has_day_access(state, 15, player):
                total += 1
                if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Blazing Shard",
                                                                                             player):
                    total += 2
            if self.days_has_day_access(state, 23, player):
                if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Blazing Shard",
                                                                                             player):
                    total += 2
            if self.days_shop_status(state, player) >= 1:
                total += 1
            if self.days_shop_status(state, player) >= 2:
                total += 1
            if self.days_has_day_access(state, 75, player):
                total += 1
                if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Blazing Shard",
                                                                                             player):
                    total += 1
            if self.days_has_day_access(state, 173, player):
                total += 1
                if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Blazing Shard",
                                                                                             player):
                    total += 1
            if self.days_has_day_access(state, 97, player):
                if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Blazing Shard",
                                                                                             player):
                    total += 1
            if self.days_has_day_access(state, 152, player):
                if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Blazing Shard",
                                                                                             player):
                    total += 1
            if self.days_has_day_access(state, 358, player):
                total += 3
        elif item_name == "Doublecast 4":
            if self.days_has_day_access(state, 22, player):
                total += 1
        elif item_name == "Triplecast 3":
            if self.days_shop_status(state, player) >= 1:
                total += 1
        elif item_name == "Quadcast 3":
            if self.days_shop_status(state, player) >= 4:
                total += 1
        elif item_name == "Aerial Recovery":
            if self.days_shop_status(state, player) >= 1:
                total += 1
        elif item_name == "Aerial Recovery 3":
            if self.days_shop_status(state, player) >= 3:
                total += 1
        elif item_name == "A. Recovery LV+":
            if self.days_has_day_access(state, 173, player) and state.has_any({"Glide 3", "Glide 5"}, player):
                total += 2
        elif item_name == "Technical Gear 3":
            if self.days_shop_status(state, player) >= 1:
                total += 1
        elif item_name == "Chrono Gear 3":
            if self.days_shop_status(state, player) >= 1:
                total += 1
        elif item_name == "Lift Gear 3":
            if self.days_shop_status(state, player) >= 1:
                total += 1
        elif item_name == "Nimble Gear 4":
            if self.days_shop_status(state, player) >= 2:
                total += 1
        elif item_name == "Fearless Gear 3":
            if self.days_shop_status(state, player) >= 2:
                total += 1
        elif item_name == "Prestige Gear 4":
            if self.days_shop_status(state, player) >= 3:
                total += 1
        elif item_name == "Champion Gear+ 5":
            if self.days_shop_status(state, player) >= 5:
                total += 1
        elif item_name == "Pandora's Gear 5":
            if self.days_shop_status(state, player) >= 6:
                total += 1
        elif item_name == "Zero Gear 5":
            if self.days_shop_status(state, player) >= 6:
                total += 1
        elif item_name == "Wild Gear 3":
            if self.days_shop_status(state, player) >= 1:
                total += 1
        elif item_name == "Loaded Gear":
            if self.days_has_day_access(state, 22, player):
                total += 1
        elif item_name == "Sign of Resolve":
            if self.days_has_day_access(state, 23, player):
                total += 1
        elif item_name == "Skill Gear+ 2":
            if self.days_has_day_access(state, 24, player):
                total += 1
        elif item_name == "Blizzard":
            if self.days_has_day_access(state, 25, player):
                total += 2
            if self.days_has_day_access(state, 26, player):
                total += 1
            if self.days_shop_status(state, player) >= 1:
                total += 2
            if self.days_has_day_access(state, 51, player):
                total += 1
            if self.days_has_day_access(state, 95, player) and self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Frost Shard", player):
                total += 1
            if self.days_has_day_access(state, 225, player) and self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Frost Shard", player):
                total += 1
            if self.days_has_day_access(state, 75, player):
                total += 1
            if self.days_has_day_access(state, 97, player) and self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Frost Shard", player):
                total += 2
            if self.days_has_day_access(state, 149, player) and self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Frost Shard", player):
                total += 1
            if self.days_has_day_access(state, 152, player) and self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Frost Shard", player):
                total += 5
            if self.days_has_day_access(state, 256, player) and self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Frost Shard", player):
                total += 2
            if self.days_has_day_access(state, 358, player):
                total += 3
        elif item_name == "Power Unit":
            if self.days_has_day_access(state, 24, player):
                total += 1
            if self.days_shop_status(state, player) >= 1:
                total += 1
            if self.days_shop_status(state, player) >= 3:
                total += 1
            if self.days_shop_status(state, player) >= 6:
                total += 1
            if self.days_has_day_access(state, 358, player):
                total += 1
        elif item_name == "Brawl Ring":
            if self.days_shop_status(state, player) >= 1:
                total += 1
        elif item_name == "Soldier Ring":
            if self.days_shop_status(state, player) >= 1:
                total += 1
        elif item_name == "Flower Charm":
            if self.days_shop_status(state, player) >= 2:
                total += 1
        elif item_name == "Blizzard Charm":
            if self.days_shop_status(state, player) >= 2:
                total += 1
        elif item_name == "Knight's Defense":
            if self.days_shop_status(state, player) >= 3:
                total += 1
        elif item_name == "Rainforce Ring":
            if self.days_shop_status(state, player) >= 3:
                total += 1
        elif item_name == "Critical Ring":
            if self.days_shop_status(state, player) >= 4:
                total += 1
        elif item_name == "Lucky Star":
            if self.days_shop_status(state, player) >= 5:
                total += 1
        elif item_name == "Princess's Crown":
            if self.days_shop_status(state, player) >= 6:
                total += 1
        elif item_name == "Deep Sky":
            if self.days_shop_status(state, player) >= 6:
                total += 1
        elif item_name == "Critical Sun":
            if self.days_shop_status(state, player) >= 6:
                total += 1
        elif item_name == "Ability Unit":
            if self.days_has_day_access(state, 26, player):
                total += 1
            if self.days_has_day_access(state, 95, player):
                total += 1
            if self.days_shop_status(state, player) >= 2:
                total += 1
        elif item_name == "Sight Unit":
            if self.days_has_day_access(state, 97, player) and state.has_any({"High Jump", "High Jump 3"}, player):
                total += 1
            if self.days_has_day_access(state, 151, player):
                total += 1
            if self.days_has_day_access(state, 321, player):
                total += 1
            if self.days_has_day_access(state, 354, player):
                total += 1
            if self.days_has_day_access(state, 152, player) and state.has("High Jump 3", player) and state.has("High Jump LV+", player) and state.has_any({"Glide 3", "Glide 5"}, player) and state.has("High Jump LV+", player):
                total += 1
        elif item_name == "Phantom Gear 4":
            if self.days_has_day_access(state, 152, player):
                total += 1
        elif item_name == "Ether":
            if self.days_has_day_access(state, 11, player):
                total += 1
            if self.days_has_day_access(state, 14, player):
                total += 3
            if self.days_has_day_access(state, 15, player):
                total += 1
            if self.days_has_day_access(state, 51, player):
                total += 3
            if self.days_has_day_access(state, 73, player):
                total += 1
            if self.days_has_day_access(state, 74, player):
                total += 1
            if self.days_has_day_access(state, 75, player):
                total += 4
            if self.days_has_day_access(state, 94, player):
                total += 1
            if self.days_has_day_access(state, 95, player):
                total += 1
            if self.days_has_day_access(state, 96, player):
                total += 6
            if self.days_has_day_access(state, 97, player):
                total += 2
            if self.days_has_day_access(state, 119, player):
                total += 1
            if self.days_has_day_access(state, 172, player):
                total += 1
            if self.days_has_day_access(state, 358, player):
                total += 10
            if self.days_shop_status(state, player) >= 1:
                total += 20
        elif item_name == "Scan":
            if self.days_has_day_access(state, 11, player):
                total += 1
        elif item_name == "Elixir":
            if self.days_has_day_access(state, 51, player) and state.has_any({"High Jump", "High Jump 3", "Air Slide 2", "Air Slide 5"}, player):
                total += 1
            if self.days_has_day_access(state, 119, player):
                total += 1
            if self.days_has_day_access(state, 150, player):
                total += 1
            if self.days_has_day_access(state, 152, player):
                total += 2
            if self.days_has_day_access(state, 322, player):
                total += 4
            if self.days_has_day_access(state, 48, player) and state.has("High Jump 3", player) and state.has("High Jump LV+", player) and state.has("High Jump LV+", player):
                total += 1
            if self.days_has_day_access(state, 358, player):
                total += 10
        elif item_name == "Dodge Roll":
            if self.days_has_day_access(state, 12, player):
                total += 1
        elif item_name == "Dodge Roll LV+":
            if self.days_shop_status(state, player) >= 3:
                total += 1
        elif item_name == "Dodge Rush":
            if self.days_shop_status(state, player) >= 2 and self.days_can_get_materials(state, "Premium Orb", player) and self.days_can_get_materials(state, "Power Tech+", player) and self.days_can_get_materials(state, "Combo Tech", player) and self.days_can_get_materials(state, "Moonstone", player):
                total += 1
        elif item_name == "Dodging Deflect":
            if self.days_shop_status(state, player) >= 2 and self.days_can_get_materials(state, "Range Tech+", player) and self.days_can_get_materials(state, "Diamond", player):
                total += 1
        elif item_name == "Dodge Combo":
            if self.days_shop_status(state, player) >= 2 and self.days_can_get_materials(state, "Adamantite", player) and self.days_can_get_materials(state, "Combo Tech+", player):
                total += 1
        elif item_name == "Auto-Dodge":
            if self.days_shop_status(state, player) >= 2 and self.days_can_get_materials(state, "Combo Tech++", player) and self.days_can_get_materials(state, "Diamond", player):
                total += 1
        elif item_name == "Perfect Block":
            if self.days_shop_status(state, player) >= 2 and self.days_can_get_materials(state, "Shield Tech", player) and self.days_can_get_materials(state, "Moonstone", player):
                total += 1
        elif item_name == "Block-Counter":
            if self.days_shop_status(state, player) >= 2 and self.days_can_get_materials(state, "Shield Tech+", player) and self.days_can_get_materials(state, "Shield Tech", player) and self.days_can_get_materials(state, "Moonstone", player):
                total += 1
        elif item_name == "Block-Retreat":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Shield Tech", player) and self.days_can_get_materials(state, "Moonstone", player) and state.has("Block-Counter", player):
                total += 1
        elif item_name == "Sliding Block":
            if self.days_shop_status(state, player) >= 2 and self.days_can_get_materials(state, "Range Tech+", player) and self.days_can_get_materials(state, "Shield Tech+", player) and self.days_can_get_materials(state, "Diamond", player):
                total += 1
        elif item_name == "Block-Jump":
            if self.days_shop_status(state, player) >= 2 and self.days_can_get_materials(state, "Aerial Tech+", player) and self.days_can_get_materials(state, "Shield Tech+", player) and self.days_can_get_materials(state, "Diamond", player):
                total += 1
        elif item_name == "Fire Block":
            if self.days_shop_status(state, player) >= 2 and self.days_can_get_materials(state, "Rune Tech", player) and self.days_can_get_materials(state, "Blazing Shard", player) and self.days_can_get_materials(state, "Shield Tech", player) and self.days_can_get_materials(state, "Moonstone", player):
                total += 1
        elif item_name == "Blizzard Block":
            if self.days_shop_status(state, player) >= 2 and self.days_can_get_materials(state, "Rune Tech", player) and self.days_can_get_materials(state, "Frost Shard", player) and self.days_can_get_materials(state, "Shield Tech", player) and self.days_can_get_materials(state, "Moonstone", player):
                total += 1
        elif item_name == "Thunder Block":
            if self.days_shop_status(state, player) >= 2 and self.days_can_get_materials(state, "Rune Tech+", player) and self.days_can_get_materials(state, "Lightning Gem", player) and self.days_can_get_materials(state, "Shield Tech", player) and self.days_can_get_materials(state, "Diamond", player):
                total += 1
        elif item_name == "Aero Block":
            if self.days_shop_status(state, player) >= 2 and self.days_can_get_materials(state, "Rune Tech+", player) and self.days_can_get_materials(state, "Gust Gem", player) and self.days_can_get_materials(state, "Shield Tech+", player) and self.days_can_get_materials(state, "Diamond", player):
                total += 1
        elif item_name == "Block Bonus":
            if self.days_shop_status(state, player) >= 2 and self.days_can_get_materials(state, "Luck Tech", player) and self.days_can_get_materials(state, "Shield Tech", player) and self.days_can_get_materials(state, "Adamantite", player):
                total += 1
        elif item_name == "Round Block":
            if self.days_shop_status(state, player) >= 2 and self.days_can_get_materials(state, "Shield Tech+", player) and self.days_can_get_materials(state, "Moonstone", player):
                total += 1
        elif item_name == "Auto-Block":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Shield Tech+", player) and self.days_can_get_materials(state, "Adamantite", player) and state.has("Round Block", player):
                total += 1
        elif item_name == "Quick Recovery":
            if self.days_shop_status(state, player) >= 2 and self.days_can_get_materials(state, "Rune Tech+", player) and self.days_can_get_materials(state, "Moonstone", player):
                total += 1
        elif item_name == "Aerial Payback":
            if self.days_shop_status(state, player) >= 2 and self.days_can_get_materials(state, "Combo Tech+", player) and self.days_can_get_materials(state, "Diamond", player):
                total += 1
        elif item_name == "Smash Recovery":
            if self.days_shop_status(state, player) >= 2 and self.days_can_get_materials(state, "Power Tech++", player) and self.days_can_get_materials(state, "Adamantite", player):
                total += 1
        elif item_name == "Air Rush":
            if self.days_shop_status(state, player) >= 2 and self.days_can_get_materials(state, "Aerial Tech+", player) and self.days_can_get_materials(state, "Moonstone", player):
                total += 1
        elif item_name == "Homing Glide":
            if self.days_shop_status(state, player) >= 2 and self.days_can_get_materials(state, "Range Tech++", player) and self.days_can_get_materials(state, "Aerial Tech++", player) and self.days_can_get_materials(state, "Adamantite", player):
                total += 1
        elif item_name == "Rocket Glide":
            if self.days_shop_status(state, player) >= 2 and self.days_can_get_materials(state, "Range Tech", player) and self.days_can_get_materials(state, "Combo Tech++", player) and self.days_can_get_materials(state, "Aerial Tech++", player) and self.days_can_get_materials(state, "Adamantite", player):
                total += 1
        elif item_name == "Float":
            if self.days_shop_status(state, player) >= 2 and self.days_can_get_materials(state, "Aerial Tech++", player) and self.days_can_get_materials(state, "Adamantite", player):
                total += 1
        elif item_name == "Duel Gear 4":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Bronze", player) and self.days_can_get_materials(state, "Combo Tech", player) and self.days_can_get_materials(state, "Gear Component A", player):
                total += 1
        elif item_name == "Duel Gear++ 5":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Dark Ingot", player) and self.days_can_get_materials(state, "Combo Tech", player) and self.days_can_get_materials(state, "Gear Component B", player):
                total += 1
        elif item_name == "Chrono Gear+ 3":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Bronze", player) and self.days_can_get_materials(state, "Rune Tech", player) and self.days_can_get_materials(state, "Gear Component A", player):
                total += 1
        elif item_name == "Phantom Gear++ 5":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Dark Ingot", player) and self.days_can_get_materials(state, "Rune Tech+", player) and self.days_can_get_materials(state, "Gear Component B", player):
                total += 1
        elif item_name == "Nimble Gear+ 4":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Bronze", player) and self.days_can_get_materials(state, "Aerial Tech", player) and self.days_can_get_materials(state, "Gear Component A", player):
                total += 1
        elif item_name == "Ominous Gear+ 4":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Range Tech", player) and self.days_can_get_materials(state, "Gear Component A", player) and self.days_can_get_materials(state, "Bronze", player):
                total += 1
        elif item_name == "Fearless Gear+ 3":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Power Tech", player) and self.days_can_get_materials(state, "Bronze", player) and self.days_can_get_materials(state, "Gear Component A", player):
                total += 1
        elif item_name == "Prestige Gear+ 4":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Gear Component B", player) and self.days_can_get_materials(state, "Power Tech", player) and self.days_can_get_materials(state, "Dark Ingot", player):
                total += 1
        elif item_name == "Crisis Gear 5":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Dark Ingot", player) and self.days_can_get_materials(state, "Power Tech+", player) and self.days_can_get_materials(state, "Rune Tech+", player) and self.days_can_get_materials(state, "Gear Component B", player):
                total += 1
        elif item_name == "Crisis Gear+ 5":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Rune Tech+", player) and self.days_can_get_materials(state, "Power Tech+", player) and self.days_can_get_materials(state, "Silver", player) and self.days_can_get_materials(state, "Gear Component C", player):
                total += 1
        elif item_name == "Omega Gear+ 6":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Mithril", player) and self.days_can_get_materials(state, "Power Tech++", player) and self.days_can_get_materials(state, "Rune Tech++", player) and self.days_can_get_materials(state, "Gear Component D", player):
                total += 1
        elif item_name == "Hazard Gear 5":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Silver", player) and self.days_can_get_materials(state, "Range Tech+", player) and self.days_can_get_materials(state, "Rune Tech+", player) and self.days_can_get_materials(state, "Gear Component C", player):
                total += 1
        elif item_name == "Hazard Gear+ 5":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Range Tech++", player) and self.days_can_get_materials(state, "Rune Tech++", player) and self.days_can_get_materials(state, "Gold", player) and self.days_can_get_materials(state, "Gear Component D", player):
                total += 1
        elif item_name == "Rage Gear+ 5":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Silver", player) and self.days_can_get_materials(state, "Aerial Tech+", player) and self.days_can_get_materials(state, "Combo Tech+", player) and self.days_can_get_materials(state, "Gear Component C", player):
                total += 1
        elif item_name == "Champion Gear 5":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Silver", player) and self.days_can_get_materials(state, "Power Tech+", player) and self.days_can_get_materials(state, "Combo Tech+", player) and self.days_can_get_materials(state, "Gear Component C", player):
                total += 1
        elif item_name == "Ultimate Gear+ 6":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Orichalcum", player) and self.days_can_get_materials(state, "Power Tech++", player) and self.days_can_get_materials(state, "Combo Tech++", player) and self.days_can_get_materials(state, "Gear Component D", player):
                total += 1
        elif item_name == "Pandora's Gear+ 5":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Mithril", player) and self.days_can_get_materials(state, "Premium Orb", player) and self.days_can_get_materials(state, "Luck Tech", player) and self.days_can_get_materials(state, "Gear Component D", player):
                total += 1
        elif item_name == "Magic Ring":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Iron", player) and self.days_can_get_materials(state, "Moonstone", player):
                total += 1
        elif item_name == "Fencer's Ring":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Shining Shard", player) and self.days_can_get_materials(state, "Iron", player) and self.days_can_get_materials(state, "Moonstone", player):
                total += 1
        elif item_name == "Fire Charm":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Blazing Shard", player) and self.days_can_get_materials(state, "Aerial Tech", player) and self.days_can_get_materials(state, "Iron", player) and self.days_can_get_materials(state, "Moonstone", player):
                total += 1
        elif item_name == "Strike Ring":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Combo Tech", player) and self.days_can_get_materials(state, "Bronze", player) and self.days_can_get_materials(state, "Iron", player) and self.days_can_get_materials(state, "Moonstone", player):
                total += 1
        elif item_name == "Lucky Ring":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Shield Tech", player) and self.days_can_get_materials(state, "Bronze", player) and self.days_can_get_materials(state, "Iron", player) and self.days_can_get_materials(state, "Moonstone", player):
                total += 1
        elif item_name == "White Ring":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Power Tech", player) and self.days_can_get_materials(state, "Bronze", player) and self.days_can_get_materials(state, "Iron", player) and self.days_can_get_materials(state, "Moonstone", player):
                total += 1
        elif item_name == "Raider's Ring":
            if self.days_shop_status(state, player) >= 1 and state.has("Lucky Ring", player) and self.days_can_get_materials(state, "Moonstone", player) and self.days_can_get_materials(state, "Dark Ingot", player):
                total += 1
        elif item_name == "Thunder Charm":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Aerial Tech", player) and self.days_can_get_materials(state, "Lightning Gem", player) and self.days_can_get_materials(state, "Moonstone", player) and self.days_can_get_materials(state, "Dark Ingot", player):
                total += 1
        elif item_name == "Recovery Ring":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Combo Tech+", player) and self.days_can_get_materials(state, "Dark Ingot", player) and self.days_can_get_materials(state, "Moonstone", player):
                total += 1
        elif item_name == "Vitality Ring":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Combo Tech++", player) and self.days_can_get_materials(state, "Moonstone", player) and self.days_can_get_materials(state, "Dark Ingot", player):
                total += 1
        elif item_name == "Double Up":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Luck Tech", player) and self.days_can_get_materials(state, "Diamond", player) and self.days_can_get_materials(state, "Silver", player):
                total += 1
        elif item_name == "Storm's Eye":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Gust Gem", player) and self.days_can_get_materials(state, "Diamond", player) and self.days_can_get_materials(state, "Silver", player):
                total += 1
        elif item_name == "Fairy Circle":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Aerial Tech+", player) and self.days_can_get_materials(state, "Range Tech+", player) and self.days_can_get_materials(state, "Diamond", player) and self.days_can_get_materials(state, "Silver", player):
                total += 1
        elif item_name == "Full Circle":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Shield Tech+", player) and self.days_can_get_materials(state, "Shield Tech", player) and self.days_can_get_materials(state, "Diamond", player) and self.days_can_get_materials(state, "Silver", player):
                total += 1
        elif item_name == "Charge Ring":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Diamond", player) and state.has("Full Circle", player) and self.days_can_get_materials(state, "Gold", player):
                total += 1
        elif item_name == "Eternal Ring":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Diamond", player) and self.days_can_get_materials(state, "Gold", player) and state.has("Recovery Ring", player):
                total += 1
        elif item_name == "Carmine Blight":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Ankharite", player) and self.days_can_get_materials(state, "Power Tech++", player) and self.days_can_get_materials(state, "Adamantite", player) and self.days_can_get_materials(state, "Gold", player):
                total += 1
        elif item_name == "Frozen Blight":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Diamond", player) and self.days_can_get_materials(state, "Rune Tech++", player) and self.days_can_get_materials(state, "Gold", player):
                total += 1
        elif item_name == "Safety Ring":
            if self.days_shop_status(state, player) >= 1 and self.days_can_get_materials(state, "Shield Tech+", player) and self.days_can_get_materials(state, "Diamond", player) and self.days_can_get_materials(state, "Gold", player):
                total += 1
        elif item_name == "Lunar Strike":
            if self.days_shop_status(state, player) >= 6 and self.days_can_get_materials(state, "Premium Orb", player) and self.days_can_get_materials(state, "Adamantite", player) and self.days_can_get_materials(state, "Mithril", player):
                total += 1
        elif item_name == "Protect Ring":
            if self.days_shop_status(state, player) >= 6 and self.days_can_get_materials(state, "Shield Tech++", player) and self.days_can_get_materials(state, "Adamantite", player) and self.days_can_get_materials(state, "Mithril", player):
                total += 1
        elif item_name == "Might Crown":
            if self.days_shop_status(state, player) >= 6 and self.days_can_get_materials(state, "Combo Tech++", player) and self.days_can_get_materials(state, "Adamantite", player) and self.days_can_get_materials(state, "Mithril", player):
                total += 1
        elif item_name == "Three Stars":
            if self.days_shop_status(state, player) >= 6 and self.days_can_get_materials(state, "Luck Tech", player) and self.days_can_get_materials(state, "Adamantite", player) and self.days_can_get_materials(state, "Mithril", player):
                total += 1
        elif item_name == "Imperial Crown":
            if self.days_shop_status(state, player) >= 6 and self.days_can_get_materials(state, "Premium Orb", player) and self.days_can_get_materials(state, "Ankharite", player) and self.days_can_get_materials(state, "Adamantite", player) and self.days_can_get_materials(state, "Mithril", player):
                total += 1
        elif item_name == "Witch's Chaos":
            if self.days_shop_status(state, player) >= 6 and self.days_can_get_materials(state, "Premium Orb", player) and self.days_can_get_materials(state, "Shield Tech++", player) and self.days_can_get_materials(state, "Adamantite", player) and self.days_can_get_materials(state, "Mithril", player):
                total += 1
        elif item_name == "Extreme":
            if self.days_shop_status(state, player) >= 6 and self.days_can_get_materials(state, "Luck Tech", player) and self.days_can_get_materials(state, "Dark Ingot", player) and self.days_can_get_materials(state, "Moonstone", player) and self.days_can_get_materials(state, "Orichalcum", player):
                total += 1
        elif item_name == "Nothing to Fear":
            if self.days_shop_status(state, player) >= 6 and self.days_can_get_materials(state, "Orichalcum", player) and self.days_can_get_materials(state, "Adamantite", player) and state.has("Frozen Blight", player):
                total += 1
        elif item_name == "Space in Its Place":
            if self.days_shop_status(state, player) >= 6 and self.days_can_get_materials(state, "Combo Tech++", player) and self.days_can_get_materials(state, "Aerial Tech++", player) and self.days_can_get_materials(state, "Moonstone", player) and self.days_can_get_materials(state, "Orichalcum", player):
                total += 1
        elif item_name == "Flagging Winds":
            if self.days_shop_status(state, player) >= 6 and self.days_can_get_materials(state, "Gust Crystal", player) and self.days_can_get_materials(state, "Gust Shard", player) and self.days_can_get_materials(state, "Moonstone", player) and self.days_can_get_materials(state, "Orichalcum", player):
                total += 1
        elif item_name == "Ice Breaker":
            if self.days_shop_status(state, player) >= 6 and self.days_can_get_materials(state, "Frost Gem", player) and self.days_can_get_materials(state, "Frost Crystal", player) and self.days_can_get_materials(state, "Moonstone", player) and self.days_can_get_materials(state, "Orichalcum", player):
                total += 1
        elif item_name == "Down to Earth":
            if self.days_shop_status(state, player) >= 6 and self.days_can_get_materials(state, "Moonstone", player) and self.days_can_get_materials(state, "Orichalcum", player) and state.has("Eternal Ring", player):
                total += 1
        elif item_name == "Lose Your Illusion":
            if self.days_shop_status(state, player) >= 6 and self.days_can_get_materials(state, "Adamantite", player) and self.days_can_get_materials(state, "Orichalcum", player) and state.has("Charge Ring", player):
                total += 1
        elif item_name == "Sighing of the Moon":
            if self.days_shop_status(state, player) >= 6 and state.has("Strike Ring", player) and self.days_can_get_materials(state, "Orichalcum", player) and self.days_can_get_materials(state, "Diamond", player):
                total += 1
        elif item_name == "Tears of Flame":
            if self.days_shop_status(state, player) >= 6 and self.days_can_get_materials(state, "Blazing Gem", player) and self.days_can_get_materials(state, "Blazing Crystal", player) and self.days_can_get_materials(state, "Diamond", player) and self.days_can_get_materials(state, "Orichalcum", player):
                total += 1
        elif item_name == "Parting of Waters":
            if self.days_shop_status(state, player) >= 6 and self.days_can_get_materials(state, "Orichalcum", player) and self.days_can_get_materials(state, "Diamond", player) and state.has("Storm's Eye", player):
                total += 1
        elif item_name == "Test of Time":
            if self.days_shop_status(state, player) >= 6 and self.days_can_get_materials(state, "Adamantite", player) and self.days_can_get_materials(state, "Orichalcum", player) and state.has("Fairy Circle", player):
                total += 1
        elif item_name == "Flowers Athirst":
            if self.days_shop_status(state, player) >= 6 and self.days_can_get_materials(state, "Moonstone", player) and self.days_can_get_materials(state, "Orichalcum", player) and state.has("Double Up", player):
                total += 1
        elif item_name == "Stolen Thunder":
            if self.days_shop_status(state, player) >= 6 and self.days_can_get_materials(state, "Lightning Shard", player) and self.days_can_get_materials(state, "Lightning Crystal", player) and self.days_can_get_materials(state, "Moonstone", player) and self.days_can_get_materials(state, "Orichalcum", player):
                total += 1
        elif item_name == "Dying of the Light":
            if self.days_shop_status(state, player) >= 6 and self.days_can_get_materials(state, "Shining Gem", player) and self.days_can_get_materials(state, "Moonstone", player) and self.days_can_get_materials(state, "Orichalcum", player) and state.has("Imperial Crown", player):
                total += 1
        elif item_name == "Skill Gear":
            if self.days_has_day_access(state, 13, player):
                total += 1
        elif item_name == "Block 2":
            if self.days_has_day_access(state, 14, player):
                total += 1
        elif item_name == "Block 4":
            if self.days_shop_status(state, player) >= 5:
                total += 1
        elif item_name == "Block LV+":
            if self.days_has_day_access(state, 73, player):
                total += 1
            if self.days_shop_status(state, player) >= 5:
                total += 1
            if self.days_shop_status(state, player) >= 6:
                total += 1
        elif item_name == "Panel Slot":
            if self.days_has_day_access(state, 25, player):
                total += 1
            if self.days_has_day_access(state, 26, player):
                total += 1
            if self.days_has_day_access(state, 51, player):
                total += 4
                if state.has_any({"High Jump", "High Jump 3"}, player):
                    total += 1
            if self.days_has_day_access(state, 71, player):
                total += 1
            if self.days_has_day_access(state, 72, player):
                total += 1
            if self.days_has_day_access(state, 73, player):
                total += 1
            if self.days_has_day_access(state, 74, player):
                total += 1
            if self.days_has_day_access(state, 75, player):
                total += 5
            if self.days_has_day_access(state, 94, player):
                total += 1
            if self.days_has_day_access(state, 95, player):
                total += 1
            if self.days_has_day_access(state, 96, player):
                total += 1
            if self.days_has_day_access(state, 97, player):
                total += 5
            if self.days_has_day_access(state, 117, player):
                total += 1
            if self.days_has_day_access(state, 119, player):
                total += 4
            if self.days_has_day_access(state, 149, player):
                total += 1
            if self.days_has_day_access(state, 150, player):
                total += 1
            if self.days_has_day_access(state, 151, player):
                total += 1
            if self.days_has_day_access(state, 152, player):
                total += 6
            if self.days_has_day_access(state, 171, player):
                total += 1
            if self.days_has_day_access(state, 172, player):
                total += 1
            if self.days_has_day_access(state, 173, player):
                total += 4
            if self.days_has_day_access(state, 193, player):
                total += 2
            if self.days_has_day_access(state, 194, player):
                total += 4
            if self.days_has_day_access(state, 224, player):
                total += 2
            if self.days_has_day_access(state, 225, player):
                total += 3
            if self.days_has_day_access(state, 255, player):
                total += 1
            if self.days_has_day_access(state, 256, player):
                total += 3
            if self.days_has_day_access(state, 277, player):
                total += 5
            if self.days_has_day_access(state, 296, player):
                total += 1
            if self.days_has_day_access(state, 297, player):
                total += 1
            if self.days_has_day_access(state, 298, player):
                total += 1
            if self.days_has_day_access(state, 299, player):
                total += 1
            if self.days_has_day_access(state, 300, player):
                total += 1
            if self.days_has_day_access(state, 301, player):
                total += 5
            if self.days_has_day_access(state, 321, player):
                total += 1
            if self.days_has_day_access(state, 322, player):
                total += 6
            if self.days_has_day_access(state, 352, player):
                total += 2
            if self.days_has_day_access(state, 353, player):
                total += 1
            if self.days_has_day_access(state, 354, player):
                total += 1
            if self.days_has_day_access(state, 358, player):
                total += 13
            if self.days_shop_status(state, player) >= 1:
                total += 1
            if self.days_shop_status(state, player) >= 2:
                total += 1
            if self.days_shop_status(state, player) >= 3:
                total += 1
            if self.days_shop_status(state, player) >= 4:
                total += 1
            if self.days_shop_status(state, player) >= 5:
                total += 1
            if self.days_shop_status(state, player) >= 6:
                total += 2
        elif item_name == "Glide 3":
            if self.days_has_day_access(state, 173, player):
                total += 1
        elif item_name == "Glide 5":
            if self.days_has_day_access(state, 358, player):
                total += 1
        elif item_name == "Glide LV+":
            if self.days_has_day_access(state, 256, player):
                total += 1
            if self.days_has_day_access(state, 299, player):
                total += 1
            if self.days_shop_status(state, player) >= 4:
                total += 1
            if self.days_has_day_access(state, 358, player):
                total += 1
        elif item_name == "Level Up":
            if self.days_shop_status(state, player) >= 1:
                total += 1
            if self.days_shop_status(state, player) >= 2:
                total += 1
            if self.days_shop_status(state, player) >= 4:
                total += 1
            if self.days_has_day_access(state, 74, player):
                total += 8
            if self.days_has_day_access(state, 152, player):
                total += 8
            if self.days_has_day_access(state, 277, player):
                total += 8
            if self.days_has_day_access(state, 357, player):
                total += 8
            if self.days_has_day_access(state, 358, player):
                total += 4
        elif item_name == "Ominous Gear 4":
            if self.days_has_day_access(state, 26, player) and ((state.has("Air Slide LV+", player) and state.has_any({"Air Slide 5", "Air Slide 2"}, player) and state.has("High Jump", player)) or (state.has("High Jump 3", player) and state.has("High Jump LV+", player))):
                total += 1
        elif item_name == "Panacea":
            if self.days_has_day_access(state, 51, player):
                total += 3
            if self.days_has_day_access(state, 26, player):
                total += 1
            if self.days_has_day_access(state, 71, player):
                total += 2
            if self.days_shop_status(state, player) >= 1:
                total += 15
            if self.days_has_day_access(state, 358, player):
                total += 10
        elif item_name == "Loaded Gear+ 2":
            if self.days_has_day_access(state, 51, player):
                total += 1
        elif item_name == "LV Doubler 5":
            if self.days_has_day_access(state, 51, player):
                total += 1
        elif item_name == "LV Tripler 4":
            if self.days_has_day_access(state, 255, player):
                total += 1
        elif item_name == "LV Tripler 4B":
            if self.days_has_day_access(state, 300, player):
                total += 1
        elif item_name == "LV Tripler 4C":
            if self.days_has_day_access(state, 358, player):
                total += 1
        elif item_name == "LV Quadrupler 3":
            if self.days_has_day_access(state, 352, player):
                total += 1
        elif item_name == "LV Quadrupler 3B":
            if self.days_shop_status(state, player) >= 6:
                total += 1
        elif item_name == "LV Quadrupler 3C":
            if self.days_has_day_access(state, 358, player):
                total += 1
        elif item_name == "Backpack":
            if self.days_has_day_access(state, 73, player):
                total += 1
            if self.days_has_day_access(state, 97, player) and state.has_any({"High Jump", "High Jump 3"}, player):
                total += 1
            if self.days_shop_status(state, player) >= 2:
                total += 1
        elif item_name == "Air Slide 2":
            if self.days_has_day_access(state, 74, player):
                total += 1
        elif item_name == "Air Slide 5":
            if self.days_has_day_access(state, 255, player):
                total += 1
        elif item_name == "Air Slide LV+":
            if self.days_has_day_access(state, 119, player):
                total += 1
            if self.days_has_day_access(state, 256, player):
                total += 1
            if self.days_shop_status(state, player) >= 5:
                total += 1
            if self.days_shop_status(state, player) >= 6:
                total += 1
        elif item_name == "Technical Gear+ 3":
            if self.days_has_day_access(state, 119, player):
                total += 1
        elif item_name == "Haste":
            if self.days_has_day_access(state, 358, player):
                total += 1
        elif item_name == "Haste 3":
            if self.days_has_day_access(state, 358, player):
                total += 1
        elif item_name == "Haste LV+":
            if self.days_has_day_access(state, 358, player):
                total += 2
        elif item_name == "Ultima Weapon":
            if self.days_has_day_access(state, 358, player):
                total += 1
        elif item_name == "Phantom Gear+ 4":
            if self.days_has_day_access(state, 358, player):
                total += 1
        elif item_name == "Lift Gear+ 3":
            if self.days_has_day_access(state, 358, player):
                total += 1
        elif item_name == "Wild Gear+ 3":
            if self.days_has_day_access(state, 358, player):
                total += 1
        elif item_name == "Valor Gear+ 2":
            if self.days_has_day_access(state, 358, player):
                total += 1
        elif item_name == "Omega Gear 6":
            if self.days_has_day_access(state, 358, player):
                total += 1
        elif item_name == "Rage Gear 5":
            if self.days_has_day_access(state, 358, player):
                total += 1
        elif item_name == "Ultimate Gear 6":
            if self.days_has_day_access(state, 358, player):
                total += 1
        elif item_name == "Casual Gear 2":
            if self.days_has_day_access(state, 358, player):
                total += 1
        elif item_name == "Mystery Gear 3":
            if self.days_has_day_access(state, 358, player):
                total += 1
        elif item_name == "Crimson Blood":
            if self.days_has_day_access(state, 358, player):
                total += 1
        elif item_name == "Rune Ring":
            if self.days_has_day_access(state, 358, player):
                total += 1
        elif item_name == "Master's Circle":
            if self.days_has_day_access(state, 358, player):
                total += 1
        if total > worlds.khdays.Items.item_table[item_name].khdaysamount:
            print(item_name)
            print(total-worlds.khdays.Items.item_table[item_name].khdaysamount)
        return total >= req_count


def set_rules(world: MultiWorld, player: int):
    for loc in location_table:
        if location_table[loc] is None:
            day_number = int(str(loc).split(" ")[len(str(loc).split(" "))-1])
            set_rule(world.get_location(loc, player), lambda state, day_number=day_number: state.days_has_day_access(state, day_number, player))
        elif location_table[loc] >= 25000:
            item_string = ''.join([i+" " for i in str(loc).split(" ")[:-1]])[:-1]
            item_count = int(str(loc).split(" ")[len(str(loc).split(" "))-1])
            set_rule(world.get_location(loc, player), lambda state, item_string=item_string, item_count=item_count: state.days_has_count_access(state, item_string, item_count, player))


def set_completion_rules(world: MultiWorld, player: int):
    world.completion_condition[player] = lambda state, world=world, player=player: state.days_has_day_access(state, world.DayRequirement[player].value, player)
