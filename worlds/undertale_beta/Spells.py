from dataclasses import dataclass
import math
import typing


@dataclass
class _undertale_procedural_spell:
    effect_one: str = "none"
    effect_two: str = "none"
    atk_add: float = 0.0
    atk_sub: float = 0.0
    atk_mult: float = 0.0
    atk_div: float = 1.0
    def_add: float = 0.0
    def_sub: float = 0.0
    def_mult: float = 0.0
    def_div: float = 1.0
    hp_add: float = 0.0
    hp_sub: float = 0.0
    hp_mult: float = 0.0
    hp_div: float = 1.0
    lv_add: float = 0.0
    lv_sub: float = 0.0
    lv_mult: float = 0.0
    lv_div: float = 1.0
    total_add: float = 0.0
    total_sub: float = 0.0
    total_mult: float = 0.0
    total_div: float = 1.0
    soul_mode_length: int = 0
    target_def_add: float = 0.0
    target_def_sub: float = 0.0
    target_def_mult: float = 0.0
    target_def_div: float = 1.0
    tp_cost: float = 0.0

class under_Expected_Spell_Stats(typing.NamedTuple):
    tension_mod: int
    lv_1_value: int
    lv_19_value: int

spell_effects = {
    "heal": under_Expected_Spell_Stats(80, 10, 46),
    "over_heal": under_Expected_Spell_Stats(120, 5, 23),
    "damage_target": under_Expected_Spell_Stats(100, 44, 202),
    "damage_all": under_Expected_Spell_Stats(175, 44, 202),
    "target_defense_reduction": under_Expected_Spell_Stats(100, 10, 10),
    "brave_defense": under_Expected_Spell_Stats(125, 3, 3),
    "patient_regen": under_Expected_Spell_Stats(100, 2, 2),
    "pacify_target": under_Expected_Spell_Stats(187, 1, 1),
    "self_defense_reduction": under_Expected_Spell_Stats(-260, 30, 30),
}

targeting_spell_effects = [
    "damage_target",
    "damage_all",
]

numerical_spell_effects = [
    "heal",
    "over_heal",
    "damage_target",
    "damage_all",
    "target_defense_reduction",
    "self_defense_reduction",
]

soul_spell_effects = [
    "brave_defense",
    "patient_regen",
]

unaffected_by_secondary = [
    "pacify_target",
]
