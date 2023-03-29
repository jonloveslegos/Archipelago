from typing import TYPE_CHECKING
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
            else:
                total = 0
        elif item_name == "Thunder":
            if self.days_has_day_access(state, 117, player):
                total += 2
            if self.days_has_day_access(state, 301, player):
                total += 1
            if self.days_has_day_access(state, 277, player):
                total += 1
            if self.days_has_day_access(state, 119, player):
                total += 4
            if self.days_has_day_access(state, 152, player):
                total += 3
            if self.days_has_day_access(state, 151, player):
                total += 1
            if self.days_has_day_access(state, 173, player):
                total += 2
            if self.days_has_day_access(state, 193, player):
                total += 2
            if self.days_has_day_access(state, 194, player):
                total += 1
            if self.days_has_day_access(state, 225, player):
                total += 1
            if self.days_shop_status(state, player) >= 2:
                total += 2
        elif item_name == "Thundara":
            if self.days_has_day_access(state, 193, player):
                total += 1
            if self.days_shop_status(state, player) >= 4:
                total += 2
            if self.days_has_day_access(state, 256, player):
                total += 1
            if self.days_has_day_access(state, 277, player):
                total += 2
            if self.days_has_day_access(state, 355, player):
                total += 1
        elif item_name == "Thundaga":
            if self.days_has_day_access(state, 277, player):
                total += 1
            if self.days_has_day_access(state, 256, player):
                total += 1
            if self.days_has_day_access(state, 300, player):
                total += 1
            if self.days_has_day_access(state, 322, player):
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
        elif item_name == "Magic Unit":
            if self.days_has_day_access(state, 296, player):
                total += 1
            if self.days_shop_status(state, player) >= 2:
                total += 1
            if self.days_shop_status(state, player) >= 4:
                total += 1
            if self.days_shop_status(state, player) >= 6:
                total += 1
        elif item_name == "Cure":
            if self.days_has_day_access(state, 71, player):
                total += 2
            if self.days_has_day_access(state, 75, player):
                total += 1
            if self.days_has_day_access(state, 97, player):
                total += 1
            if self.days_has_day_access(state, 152, player):
                total += 3
            if self.days_has_day_access(state, 150, player):
                total += 1
            if self.days_has_day_access(state, 255, player):
                total += 1
            if self.days_has_day_access(state, 194, player):
                total += 1
            if self.days_has_day_access(state, 74, player):
                total += 1
            if self.days_has_day_access(state, 225, player):
                total += 1
            if self.days_has_day_access(state, 119, player):
                total += 2
            if self.days_has_day_access(state, 149, player):
                total += 1
            if self.days_has_day_access(state, 171, player):
                total += 1
            if self.days_has_day_access(state, 173, player):
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
            if self.days_has_day_access(state, 172, player):
                total += 1
            if self.days_has_day_access(state, 173, player):
                total += 2
            if self.days_has_day_access(state, 194, player):
                total += 1
            if self.days_has_day_access(state, 224, player):
                total += 1
            if self.days_has_day_access(state, 255, player):
                total += 2
            if self.days_shop_status(state, player) >= 3:
                total += 2
        elif item_name == "Curaga":
            if self.days_has_day_access(state, 256, player) and state.has("High Jump 3", player) and state.has(
                    "High Jump LV+", player) and state.has("High Jump LV+", player):
                total += 1
            if self.days_has_day_access(state, 256, player):
                total += 1
            if self.days_has_day_access(state, 299, player):
                total += 1
            if self.days_has_day_access(state, 322, player):
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
            else:
                total = 0
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
            else:
                total = 0
        elif item_name == "Mega-Ether":
            if self.days_shop_status(state, player) >= 5:
                total += 5
            else:
                total = 0
        elif item_name == "Megalixir":
            if self.days_has_day_access(state, 225, player):
                total += 1
        elif item_name == "Mega-Potion":
            if self.days_shop_status(state, player) >= 5:
                total += 5
            else:
                total = 0
        elif item_name == "Blizzara":
            if self.days_has_day_access(state, 152, player):
                total += 1
            if self.days_has_day_access(state, 193, player):
                total += 1
            if self.days_has_day_access(state, 256, player):
                total += 1
            if self.days_has_day_access(state, 194, player):
                total += 1
            if self.days_has_day_access(state, 173, player):
                total += 1
            if self.days_has_day_access(state, 225, player):
                total += 3
            if self.days_shop_status(state, player) >= 3:
                total += 2
        elif item_name == "Blizzaga":
            if self.days_has_day_access(state, 301, player):
                total += 2
            if self.days_has_day_access(state, 322, player):
                total += 2
            if self.days_has_day_access(state, 352, player):
                total += 2
        elif item_name == "Pack Extender":
            if self.days_has_day_access(state, 96, player):
                total += 1
        elif item_name == "Aero":
            if self.days_has_day_access(state, 97, player):
                total += 1
            if self.days_has_day_access(state, 225, player):
                total += 2
            if self.days_has_day_access(state, 256, player):
                total += 2
            if self.days_has_day_access(state, 119, player):
                total += 4
            if self.days_shop_status(state, player) >= 2:
                total += 2
            if self.days_has_day_access(state, 150, player):
                total += 1
            if self.days_has_day_access(state, 152, player):
                total += 1
            if self.days_has_day_access(state, 172, player):
                total += 1
            if self.days_has_day_access(state, 194, player):
                total += 1
            if self.days_has_day_access(state, 255, player):
                total += 1
        elif item_name == "Aerora":
            if self.days_has_day_access(state, 119, player):
                total += 1
            if self.days_has_day_access(state, 321, player):
                total += 1
            if self.days_has_day_access(state, 256, player):
                total += 1
            if self.days_has_day_access(state, 225, player):
                total += 1
            if self.days_has_day_access(state, 277, player):
                total += 1
            if self.days_has_day_access(state, 355, player):
                total += 1
        elif item_name == "Aeroga":
            if self.days_has_day_access(state, 297, player):
                total += 1
            if self.days_has_day_access(state, 322, player):
                total += 2
        elif item_name == "LV Doubler 6":
            if self.days_has_day_access(state, 149, player):
                total += 1
        elif item_name == "LV Doubler 6B":
            if self.days_has_day_access(state, 193, player):
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
        elif item_name == "Fira":
            if self.days_has_day_access(state, 149, player):
                total += 1
            if self.days_has_day_access(state, 150, player):
                total += 1
            if self.days_has_day_access(state, 173, player):
                total += 1
            if self.days_has_day_access(state, 151, player):
                total += 1
            if self.days_shop_status(state, player) >= 3:
                total += 2
            if self.days_has_day_access(state, 298, player):
                total += 1
            if self.days_has_day_access(state, 322, player):
                total += 1
        elif item_name == "Firaga":
            if self.days_has_day_access(state, 224, player):
                total += 1
            if self.days_has_day_access(state, 322, player):
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
                total += 1
            if self.days_has_day_access(state, 298, player):
                total += 1
            if self.days_has_day_access(state, 296, player):
                total += 1
            if self.days_has_day_access(state, 256, player):
                total += 1
            if self.days_has_day_access(state, 14, player):
                total += 2
            if self.days_has_day_access(state, 15, player):
                total += 3
            if self.days_has_day_access(state, 23, player):
                total += 2
            if self.days_shop_status(state, player) >= 1:
                total += 1
            if self.days_shop_status(state, player) >= 2:
                total += 1
            if self.days_has_day_access(state, 75, player):
                total += 2
            if self.days_has_day_access(state, 173, player):
                total += 2
            if self.days_has_day_access(state, 97, player):
                total += 1
            if self.days_has_day_access(state, 152, player):
                total += 1
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
        elif item_name == "Aerial Recovery LV+":
            if self.days_has_day_access(state, 173, player) and state.has_any({"Glide 3", "Glide 5"}, player):
                total += 1
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
            if self.days_has_day_access(state, 75, player):
                total += 1
            if self.days_has_day_access(state, 97, player):
                total += 2
            if self.days_has_day_access(state, 149, player):
                total += 1
            if self.days_has_day_access(state, 152, player):
                total += 5
            if self.days_has_day_access(state, 256, player):
                total += 2
        elif item_name == "Power Unit":
            if self.days_has_day_access(state, 24, player):
                total += 1
            if self.days_shop_status(state, player) >= 1:
                total += 1
            if self.days_shop_status(state, player) >= 3:
                total += 1
            if self.days_shop_status(state, player) >= 6:
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
            if self.days_shop_status(state, player) >= 1:
                total += 20
            else:
                total = 0
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
        elif item_name == "Dodge Roll":
            if self.days_has_day_access(state, 12, player):
                total += 1
        elif item_name == "Dodge Roll LV+":
            if self.days_shop_status(state, player) >= 3:
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
        elif item_name == "Glide LV+":
            if self.days_has_day_access(state, 256, player):
                total += 1
            if self.days_has_day_access(state, 299, player):
                total += 1
            if self.days_has_day_access(state, 300, player):
                total += 1
            if self.days_shop_status(state, player) >= 4:
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
        elif item_name == "Loaded Gear+ 2":
            if self.days_has_day_access(state, 51, player):
                total += 1
        elif item_name == "LV Doubler 5":
            if self.days_has_day_access(state, 51, player):
                total += 1
        elif item_name == "LV Tripler 4":
            if self.days_has_day_access(state, 255, player):
                total += 1
        elif item_name == "LV Quadrupler 3":
            if self.days_has_day_access(state, 352, player):
                total += 1
        elif item_name == "LV Quadrupler 3B":
            if self.days_shop_status(state, player) >= 6:
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
        if total < req_count:
            if self.days_shop_status(state, player) >= 6:
                total += req_count
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
