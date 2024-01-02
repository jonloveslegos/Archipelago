from typing import Dict, NamedTuple, List, Tuple
from enum import IntEnum


class Portal(NamedTuple):
    region: str  # AP region
    destination: str  # vanilla destination scene
    origin_letter: str  # vanilla origin tag
    name: str = ""  # human-readable name

    def scene(self) -> str:  # the actual scene name in Undertale
        return undertale_er_regions[self.region].game_scene

    def scene_destination(self) -> str:  # full, nonchanging name to interpret by the mod
        return self.scene() + self.origin_letter


portal_mapping: List[Portal] = [
    Portal(region="Ruins Entrance", destination="room_area1_2", origin_letter="B"),
    Portal(region="Snowdin Entrance", destination="room_tundra1", origin_letter="A"),
    Portal(region="Waterfall Entrance", destination="room_water1", origin_letter="D"),
    Portal(region="Hotland Entrance", destination="room_fire_prelab", origin_letter="C"),
    Portal(region="New Home Entrance", destination="room_castle_elevatorout", origin_letter="X"),

    Portal(region="room_fire_prelab", destination="Hotland Entrance", origin_letter="A"),
    Portal(region="room_fire_prelab", destination="room_fire_lab1", origin_letter="D"),
    Portal(region="room_fire_prelab", destination="room_fire_dock", origin_letter="B"),
    Portal(region="room_fire_prelab", destination="room_fire_elevator_l1", origin_letter="T"),

    Portal(region="room_fire_elevator_l1", destination="room_fire_prelab", origin_letter="T"),

    Portal(region="room_fire_dock", destination="room_fire_prelab", origin_letter="A"),

    Portal(region="room_fire_lab1", destination="room_fire_prelab", origin_letter="C"),
    Portal(region="room_fire_lab1", destination="room_fire_lab2", origin_letter="B"),
    Portal(region="room_fire_lab1", destination="room_fire3", origin_letter="D"),

    Portal(region="room_fire_lab2", destination="room_fire_lab1", origin_letter="A"),

    Portal(region="room_fire3", destination="room_fire_lab1", origin_letter="C"),
    Portal(region="room_fire3", destination="room_fire5", origin_letter="B"),

    Portal(region="room_fire5", destination="room_fire3", origin_letter="A"),
    Portal(region="room_fire5", destination="room_fire6", origin_letter="B"),

    Portal(region="room_fire6", destination="room_fire5", origin_letter="A"),
    Portal(region="room_fire6", destination="room_fire6A", origin_letter="B"),
    Portal(region="room_fire6", destination="room_fire_lasers1", origin_letter="D"),

    Portal(region="room_fire_lasers1", destination="room_fire6", origin_letter="C"),
    Portal(region="room_fire_lasers1", destination="room_fire7", origin_letter="B"),

    Portal(region="room_fire7", destination="room_fire_lasers1", origin_letter="A"),
    Portal(region="room_fire7", destination="room_fire8", origin_letter="B"),
    Portal(region="room_fire7", destination="room_fire9", origin_letter="U"),

    Portal(region="Fire Door 1", destination="room_fire_turn", origin_letter="T"),

    Portal(region="room_fire_turn", destination="Fire Door 1", origin_letter="T"),
    Portal(region="Fire Turn Part 2", destination="room_fire_cookingshow", origin_letter="B"),

    Portal(region="room_fire_cookingshow", destination="Fire Turn Part 2", origin_letter="A"),
    Portal(region="room_fire_cookingshow", destination="room_fire_savepoint1", origin_letter="B"),

    Portal(region="room_fire_savepoint1", destination="room_fire_cookingshow", origin_letter="A"),
    Portal(region="room_fire_savepoint1", destination="room_fire_elevator_r1", origin_letter="B"),

    Portal(region="room_fire_elevator_r1", destination="room_fire_savepoint1", origin_letter="A"),

    Portal(region="room_fire_elevator_r2", destination="room_fire_hotdog", origin_letter="B"),

    Portal(region="room_fire_hotdog", destination="room_fire_elevator_r2", origin_letter="A"),
    Portal(region="room_fire_hotdog", destination="room_fire_walkandbranch", origin_letter="B"),

    Portal(region="room_fire_walkandbranch", destination="room_fire_hotdog", origin_letter="A"),
    Portal(region="room_fire_walkandbranch", destination="room_fire10", origin_letter="T"),
    Portal(region="room_fire_walkandbranch", destination="room_fire_sorry", origin_letter="B"),
    Portal(region="room_fire_walkandbranch", destination="room_fire_apron", origin_letter="D"),

    Portal(region="room_fire_sorry", destination="room_fire_walkandbranch", origin_letter="A"),

    Portal(region="room_fire_apron", destination="room_fire_walkandbranch", origin_letter="C"),

    Portal(region="room_fire10", destination="room_fire_walkandbranch", origin_letter="T"),
    Portal(region="room_fire10", destination="room_fire_rpuzzle", origin_letter="B"),

    Portal(region="room_fire_rpuzzle", destination="room_fire10", origin_letter="A"),
    Portal(region="room_fire_rpuzzle", destination="room_fire_mewmew2", origin_letter="B"),

    Portal(region="room_fire_mewmew2", destination="room_fire_rpuzzle", origin_letter="A"),
    Portal(region="room_fire_mewmew2", destination="room_fire_boysnightout", origin_letter="B"),

    Portal(region="room_fire_boysnightout", destination="room_fire_mewmew2", origin_letter="A"),
    Portal(region="room_fire_boysnightout", destination="room_fire_newsreport", origin_letter="B"),

    Portal(region="room_fire_newsreport", destination="room_fire_boysnightout", origin_letter="A"),
    Portal(region="room_fire_newsreport", destination="room_fire_coreview2", origin_letter="B"),

    Portal(region="room_fire_coreview2", destination="room_fire_newsreport", origin_letter="A"),
    Portal(region="room_fire_coreview2", destination="room_fire_elevator_l2", origin_letter="B"),

    Portal(region="room_fire_elevator_l2", destination="room_fire_coreview2", origin_letter="A"),

    Portal(region="room_fire_elevator_l3", destination="room_fire_spidershop", origin_letter="B"),

    Portal(region="room_fire_spidershop", destination="room_fire_elevator_l3", origin_letter="A"),
    Portal(region="room_fire_spidershop", destination="room_fire_walkandbranch2", origin_letter="B"),

    Portal(region="room_fire_walkandbranch2", destination="room_fire_spidershop", origin_letter="A"),
    Portal(region="room_fire_walkandbranch2", destination="room_fire_preshootguy4", origin_letter="T"),
    Portal(region="room_fire_walkandbranch2", destination="room_fire_conveyorlaser", origin_letter="B"),

    Portal(region="room_fire_conveyorlaser", destination="room_fire_walkandbranch2", origin_letter="A"),
    Portal(region="room_fire_conveyorlaser", destination="room_fire_shootguy_3", origin_letter="B"),

    Portal(region="room_fire_shootguy_3", destination="room_fire_conveyorlaser", origin_letter="A"),

    Portal(region="room_fire_preshootguy4", destination="room_fire_walkandbranch2", origin_letter="T"),
    Portal(region="room_fire_preshootguy4", destination="room_fire_shootguy_4", origin_letter="B"),

    Portal(region="room_fire_shootguy_4", destination="room_fire_preshootguy4", origin_letter="A"),

    Portal(region="Fire Door 2", destination="room_fire_savepoint2", origin_letter="X"),

    Portal(region="room_fire_savepoint2", destination="Fire Door 2", origin_letter="X"),
    Portal(region="room_fire_savepoint2", destination="room_fire_spider", origin_letter="B"),

    Portal(region="room_fire_spider", destination="room_fire_savepoint2", origin_letter="A"),
    Portal(region="room_fire_spider", destination="room_fire_pacing", origin_letter="B"),

    Portal(region="room_fire_pacing", destination="room_fire_spider", origin_letter="A"),
    Portal(region="room_fire_pacing", destination="room_fire_operatest", origin_letter="B"),

    Portal(region="room_fire_operatest", destination="room_fire_pacing", origin_letter="A"),
    Portal(region="room_fire_operatest", destination="room_fire_hotelfront_1", origin_letter="D"),

    Portal(region="room_fire_hotelfront_1", destination="room_fire_operatest", origin_letter="C"),
    Portal(region="room_fire_hotelfront_1", destination="room_fire_multitile", origin_letter="A"),
    Portal(region="room_fire_hotelfront_1", destination="room_fire_hotelfront_2", origin_letter="B"),
    Portal(region="room_fire_hotelfront_1", destination="room_fire_elevator_r3", origin_letter="X"),

    Portal(region="room_fire_multitile", destination="room_fire_hotelfront_1", origin_letter="B"),

    Portal(region="room_fire_elevator_r3", destination="room_fire_hotelfront_1", origin_letter="X"),

    Portal(region="room_fire_hotelfront_2", destination="room_fire_hotelfront_1", origin_letter="A"),
    Portal(region="room_fire_hotelfront_2", destination="room_fire_hotellobby", origin_letter="B"),
    Portal(region="room_fire_hotelfront_2", destination="room_shop3", origin_letter="X"),

    Portal(region="room_fire_hotellobby", destination="room_fire_hotelfront_2", origin_letter="A"),
    Portal(region="room_fire_hotellobby", destination="room_fire_restaurant", origin_letter="B"),
    Portal(region="room_fire_hotellobby", destination="room_fire_hoteldoors", origin_letter="D"),
    Portal(region="room_fire_hotellobby", destination="room_fire_precore", origin_letter="X"),
    Portal(region="room_fire_hotellobby", destination="room_shop4", origin_letter="T"),

    Portal(region="room_shop4", destination="room_fire_hotellobby", origin_letter="T"),

    Portal(region="room_fire_restaurant", destination="room_fire_hotellobby", origin_letter="A"),

    Portal(region="room_fire_hoteldoors", destination="room_fire_hotellobby", origin_letter="C"),

    Portal(region="Bed Door One-way", destination="room_fire_hotelbed", origin_letter="B"),

    Portal(region="room_fire_hotelbed", destination="Bed Door One-way", origin_letter="A"),

    Portal(region="room_fire_precore", destination="room_fire_hotellobby", origin_letter="X"),
    Portal(region="room_fire_precore", destination="room_fire_core1", origin_letter="B"),

    Portal(region="room_fire_core1", destination="room_fire_precore", origin_letter="A"),
    Portal(region="room_fire_core1", destination="room_fire_core2", origin_letter="B"),
    Portal(region="room_fire_core1", destination="room_fire_core3", origin_letter="D"),
    Portal(region="room_fire_core1", destination="room_fire_core_premett", origin_letter="U"),

    Portal(region="room_fire_core2", destination="room_fire_core1", origin_letter="A"),

    Portal(region="room_fire_core3", destination="room_fire_core1", origin_letter="C"),
    Portal(region="room_fire_core3", destination="room_fire_core4", origin_letter="B"),

    Portal(region="room_fire_core4", destination="room_fire_core3", origin_letter="A"),
    Portal(region="room_fire_core4", destination="room_fire_core5", origin_letter="B"),

    Portal(region="room_fire_core5", destination="room_fire_core4", origin_letter="A"),
    Portal(region="room_fire_core5", destination="room_fire_core_freebattle", origin_letter="B"),
    Portal(region="room_fire_core5", destination="room_fire_core_laserfun", origin_letter="D"),

    Portal(region="room_fire_core_freebattle", destination="room_fire_core5", origin_letter="A"),

    Portal(region="room_fire_core_laserfun", destination="room_fire_core5", origin_letter="C"),
    Portal(region="room_fire_core_laserfun", destination="room_fire_core_branch", origin_letter="B"),

    Portal(region="room_fire_core_branch", destination="room_fire_core_laserfun", origin_letter="A"),
    Portal(region="room_fire_core_branch", destination="room_fire_core_bottomleft", origin_letter="B"),
    Portal(region="room_fire_core_branch", destination="room_fire_core_center", origin_letter="X"),
    Portal(region="room_fire_core_branch", destination="room_fire_core_bottomright", origin_letter="U"),

    Portal(region="room_fire_core_bottomleft", destination="room_fire_core_branch", origin_letter="A"),
    Portal(region="room_fire_core_bottomleft", destination="room_fire_core_left", origin_letter="B"),

    Portal(region="room_fire_core_center", destination="room_fire_core_branch", origin_letter="X"),
    Portal(region="room_fire_core_center", destination="room_fire_core_right", origin_letter="C"),
    Portal(region="room_fire_core_center", destination="room_fire_core_top", origin_letter="U"),

    Portal(region="room_fire_core_left", destination="room_fire_core_bottomleft", origin_letter="A"),
    Portal(region="room_fire_core_left", destination="room_fire_core_topleft", origin_letter="B"),
    Portal(region="room_fire_core_left", destination="room_fire_shootguy_5", origin_letter="X"),

    Portal(region="room_fire_core_topleft", destination="room_fire_core_left", origin_letter="A"),
    Portal(region="room_fire_core_topleft", destination="room_fire_core_top", origin_letter="B"),
    Portal(region="room_fire_core_topleft", destination="room_fire_core_treasureleft", origin_letter="X"),

    Portal(region="room_fire_core_treasureleft", destination="room_fire_core_topleft", origin_letter="X"),

    Portal(region="room_fire_shootguy_5", destination="room_fire_core_left", origin_letter="X"),

    Portal(region="room_fire_core_top", destination="room_fire_core_center", origin_letter="U"),
    Portal(region="room_fire_core_top", destination="room_fire_core_topleft", origin_letter="A"),
    Portal(region="room_fire_core_top", destination="room_fire_core_warrior", origin_letter="X"),
    Portal(region="room_fire_core_top", destination="room_fire_core_topright", origin_letter="B"),

    Portal(region="room_fire_core_warrior", destination="room_fire_core_top", origin_letter="X"),

    Portal(region="room_fire_core_right", destination="room_fire_core_center", origin_letter="D"),
    Portal(region="room_fire_core_right", destination="room_fire_core_bottomright", origin_letter="B"),
    Portal(region="room_fire_core_right", destination="room_fire_core_topright", origin_letter="A"),
    Portal(region="room_fire_core_right", destination="room_fire_core_bridge", origin_letter="X"),

    Portal(region="room_fire_core_topright", destination="room_fire_core_top", origin_letter="A"),
    Portal(region="room_fire_core_topright", destination="room_fire_core_right", origin_letter="B"),
    Portal(region="room_fire_core_topright", destination="room_fire_core_treasureright", origin_letter="X"),

    Portal(region="room_fire_core_treasureright", destination="room_fire_core_topright", origin_letter="X"),

    Portal(region="room_fire_core_bottomright", destination="room_fire_core_branch", origin_letter="U"),
    Portal(region="room_fire_core_bottomright", destination="room_fire_core_right", origin_letter="A"),

    Portal(region="room_fire_core_bridge", destination="room_fire_core_right", origin_letter="X"),
    Portal(region="room_fire_core_bridge", destination="room_fire_core_premett", origin_letter="B"),

    Portal(region="room_fire_core_premett", destination="room_fire_core_bridge", origin_letter="A"),
    Portal(region="room_fire_core_premett", destination="room_fire_core1", origin_letter="U"),

    Portal(region="Metta Entrance", destination="room_fire_core_metttest", origin_letter="B"),

    Portal(region="room_fire_core_metttest", destination="Metta Entrance", origin_letter="A"),

    Portal(region="room_castle_elevatorout", destination="New Home Entrance", origin_letter="S"),
    Portal(region="room_castle_elevatorout", destination="room_castle_precastle", origin_letter="B"),

    Portal(region="room_castle_precastle", destination="room_castle_elevatorout", origin_letter="A"),
    Portal(region="room_castle_precastle", destination="room_castle_hook", origin_letter="B"),

    Portal(region="room_castle_hook", destination="room_castle_precastle", origin_letter="A"),
    Portal(region="room_castle_hook", destination="room_castle_front", origin_letter="B"),

    Portal(region="room_castle_front", destination="room_castle_hook", origin_letter="A"),
    Portal(region="room_castle_front", destination="room_asghouse1", origin_letter="B"),

    Portal(region="room_asghouse1", destination="room_castle_front", origin_letter="A"),
    Portal(region="room_asghouse1", destination="room_asghouse2", origin_letter="B"),
    Portal(region="room_asghouse1", destination="room_asghouse3", origin_letter="D"),

    Portal(region="room_asghouse2", destination="room_asghouse1", origin_letter="A"),
    Portal(region="room_asghouse2", destination="room_kitchen_final", origin_letter="X"),

    Portal(region="room_kitchen_final", destination="room_asghouse2", origin_letter="X"),

    Portal(region="room_asghouse3", destination="room_asghouse1", origin_letter="C"),
    Portal(region="room_asghouse3", destination="room_asrielroom_final", origin_letter="D"),
    Portal(region="room_asghouse3", destination="room_asgoreroom", origin_letter="B"),

    Portal(region="room_asrielroom_final", destination="room_asghouse3", origin_letter="C"),

    Portal(region="room_asgoreroom", destination="room_asghouse3", origin_letter="A"),

    Portal(region="room_shop3", destination="room_fire_hotelfront_2", origin_letter="X"),

    Portal(region="room_fire8", destination="room_fire7", origin_letter="A"),
    Portal(region="room_fire8", destination="room_fire_shootguy_2", origin_letter="B"),

    Portal(region="room_fire_shootguy_2", destination="room_fire8", origin_letter="A"),

    Portal(region="room_fire9", destination="room_fire7", origin_letter="U"),
    Portal(region="room_fire9", destination="room_fire_shootguy_1", origin_letter="B"),

    Portal(region="room_fire_shootguy_1", destination="room_fire9", origin_letter="A"),

    Portal(region="room_fire6A", destination="room_fire6", origin_letter="A"),

    Portal(region="room_water1", destination="Waterfall Entrance", origin_letter="A"),
    Portal(region="room_water1", destination="room_water2", origin_letter="B"),

    Portal(region="room_water2", destination="room_water1", origin_letter="A"),
    Portal(region="room_water2", destination="room_water3", origin_letter="B"),

    Portal(region="room_water3", destination="room_water2", origin_letter="A"),
    Portal(region="room_water3", destination="room_water3A", origin_letter="B"),
    Portal(region="room_water3", destination="room_water4", origin_letter="D"),

    Portal(region="room_water3A", destination="room_water3", origin_letter="A"),

    Portal(region="room_water4", destination="room_water3", origin_letter="C"),
    Portal(region="room_water4", destination="room_water_bridgepuzz1", origin_letter="B"),

    Portal(region="room_water_bridgepuzz1", destination="room_water4", origin_letter="A"),
    Portal(region="water bridge puzzle after", destination="room_water5", origin_letter="B"),

    Portal(region="room_water5", destination="water bridge puzzle after", origin_letter="A"),
    Portal(region="room_water5", destination="room_water5A", origin_letter="B"),
    Portal(region="water bridge puzzle 2 after", destination="room_water6", origin_letter="D"),

    Portal(region="room_water5A", destination="room_water5", origin_letter="A"),

    Portal(region="room_water6", destination="water bridge puzzle 2 after", origin_letter="C"),
    Portal(region="room_water6", destination="room_water7", origin_letter="B"),

    Portal(region="room_water7", destination="room_water6", origin_letter="A"),
    Portal(region="Room Water 7 One Way", destination="room_water8", origin_letter="B"),

    Portal(region="room_water8", destination="Room Water 7 One Way", origin_letter="A"),
    Portal(region="room_water8", destination="room_water9", origin_letter="B"),

    Portal(region="room_water9", destination="room_water8", origin_letter="A"),
    Portal(region="room_water9", destination="room_water_savepoint1", origin_letter="B"),

    Portal(region="room_water_savepoint1", destination="room_water9", origin_letter="A"),
    Portal(region="room_water_savepoint1", destination="room_water11", origin_letter="X"),

    Portal(region="room_water11", destination="room_water_savepoint1", origin_letter="X"),
    Portal(region="room_water11", destination="room_water_nicecream", origin_letter="B"),
    Portal(region="room_water11", destination="room_water_bird", origin_letter="T"),
    Portal(region="room_water11", destination="room_water12", origin_letter="D"),

    Portal(region="room_water_nicecream", destination="room_water11", origin_letter="A"),

    Portal(region="room_water12", destination="room_water11", origin_letter="C"),
    Portal(region="room_water12", destination="room_water_shoe", origin_letter="B"),
    Portal(region="room_water12", destination="room_water_onionsan", origin_letter="W"),

    Portal(region="room_water_shoe", destination="room_water12", origin_letter="A"),

    Portal(region="room_water_bird", destination="room_water11", origin_letter="T"),
    Portal(region="room_water_bird", destination="room_water_friendlyhub", origin_letter="S"),

    Portal(region="room_water_onionsan", destination="room_water12", origin_letter="W"),
    Portal(region="room_water_onionsan", destination="room_water14", origin_letter="B"),

    Portal(region="room_water14", destination="room_water_onionsan", origin_letter="A"),
    Portal(region="room_water14", destination="room_water_piano", origin_letter="B"),
    Portal(region="room_water14", destination="room_water_statue", origin_letter="S"),

    Portal(region="room_water_piano", destination="room_water14", origin_letter="A"),

    Portal(region="room_water_statue", destination="room_water14", origin_letter="S"),
    Portal(region="room_water_statue", destination="room_water_prewaterfall", origin_letter="B"),

    Portal(region="room_water_prewaterfall", destination="room_water_statue", origin_letter="A"),
    Portal(region="room_water_prewaterfall", destination="room_water_waterfall", origin_letter="B"),

    Portal(region="room_water_waterfall", destination="room_water_prewaterfall", origin_letter="A"),
    Portal(region="room_water_waterfall", destination="room_water_waterfall2", origin_letter="B"),

    Portal(region="room_water_waterfall2", destination="room_water_waterfall", origin_letter="A"),
    Portal(region="room_water_waterfall2", destination="room_water_waterfall3", origin_letter="B"),

    Portal(region="room_water_waterfall3", destination="room_water_waterfall2", origin_letter="A"),
    Portal(region="room_water_waterfall3", destination="room_water_waterfall4", origin_letter="B"),

    Portal(region="room_water_waterfall4", destination="room_water_waterfall3", origin_letter="A"),

    Portal(region="Monster Kid Raised Ledge", destination="room_water_preundyne", origin_letter="B"),

    Portal(region="room_water_preundyne", destination="Monster Kid Raised Ledge", origin_letter="A"),
    Portal(region="room_water_preundyne", destination="room_water_undynebridge", origin_letter="B"),

    Portal(region="room_water_undynebridge", destination="room_water_preundyne", origin_letter="A"),

    Portal(region="room_water_trashzone1", destination="room_water_trashsavepoint", origin_letter="B"),

    Portal(region="room_water_trashsavepoint", destination="room_water_trashzone1", origin_letter="A"),
    Portal(region="room_water_trashsavepoint", destination="room_water_trashzone2", origin_letter="B"),

    Portal(region="room_water_trashzone2", destination="room_water_trashsavepoint", origin_letter="A"),
    Portal(region="room_water_trashzone2", destination="room_water_friendlyhub", origin_letter="B"),

    Portal(region="room_water_friendlyhub", destination="room_water_trashzone2", origin_letter="A"),
    Portal(region="room_water_friendlyhub", destination="room_water_bird", origin_letter="S"),
    Portal(region="room_water_friendlyhub", destination="room_water_blookyard", origin_letter="W"),
    Portal(region="room_water_friendlyhub", destination="room_water_farm", origin_letter="V"),
    Portal(region="room_water_friendlyhub", destination="room_water_shop", origin_letter="T"),

    Portal(region="Undyne Rocks", destination="room_water_undyneyard", origin_letter="B"),

    Portal(region="room_water_blookyard", destination="room_water_friendlyhub", origin_letter="W"),
    Portal(region="room_water_blookyard", destination="room_water_farm", origin_letter="S"),
    Portal(region="room_water_blookyard", destination="room_water_blookhouse", origin_letter="B"),

    Portal(region="hapsta door", destination="room_water_hapstablook", origin_letter="D"),

    Portal(region="room_water_blookhouse", destination="room_water_blookyard", origin_letter="A"),

    Portal(region="room_water_hapstablook", destination="hapsta door", origin_letter="C"),

    Portal(region="room_water_farm", destination="room_water_friendlyhub", origin_letter="V"),
    Portal(region="room_water_farm", destination="room_water_blookyard", origin_letter="S"),

    Portal(region="room_water_shop", destination="room_water_friendlyhub", origin_letter="T"),
    Portal(region="room_water_shop", destination="room_shop2", origin_letter="X"),
    Portal(region="room_water_shop", destination="room_water_dock", origin_letter="B"),
    Portal(region="room_water_shop", destination="room_water15", origin_letter="D"),

    Portal(region="room_water_dock", destination="room_water_shop", origin_letter="A"),

    Portal(region="room_water15", destination="room_water_shop", origin_letter="C"),
    Portal(region="room_water15", destination="room_water16", origin_letter="B"),

    Portal(region="room_water16", destination="room_water15", origin_letter="A"),
    Portal(region="room_water16", destination="room_water_temvillage", origin_letter="B"),
    Portal(region="room_water16", destination="room_water17", origin_letter="D"),

    Portal(region="room_water_temvillage", destination="room_water16", origin_letter="A"),
    Portal(region="room_water_temvillage", destination="room_shop5", origin_letter="X"),

    Portal(region="room_water17", destination="room_water16", origin_letter="C"),
    Portal(region="room_water17", destination="room_water18", origin_letter="B"),

    Portal(region="room_water18", destination="room_water17", origin_letter="A"),
    Portal(region="room_water18", destination="room_water19", origin_letter="B"),

    Portal(region="room_water19", destination="room_water18", origin_letter="A"),
    Portal(region="room_water19", destination="room_water20", origin_letter="B"),

    Portal(region="room_water20", destination="room_water19", origin_letter="A"),

    Portal(region="room_shop5", destination="room_water_temvillage", origin_letter="X"),

    Portal(region="room_shop2", destination="room_water_shop", origin_letter="X"),

    Portal(region="room_water_undyneyard", destination="Undyne Rocks", origin_letter="A"),

    Portal(region="room_area1_2", destination="Ruins Entrance", origin_letter="A"),
    Portal(region="room_area1_2", destination="room_ruins1", origin_letter="B"),

    Portal(region="room_ruins1", destination="room_area1_2", origin_letter="A"),
    Portal(region="room_ruins1", destination="room_ruins2", origin_letter="B"),

    Portal(region="room_ruins2", destination="room_ruins1", origin_letter="A"),
    Portal(region="room_ruins2", destination="room_ruins3", origin_letter="B"),

    Portal(region="room_ruins3", destination="room_ruins2", origin_letter="A"),
    Portal(region="Ruins 3 Past Puzzles", destination="room_ruins4", origin_letter="B"),

    Portal(region="room_ruins4", destination="Ruins 3 Past Puzzles", origin_letter="A"),
    Portal(region="room_ruins4", destination="room_ruins5", origin_letter="B"),

    Portal(region="room_ruins5", destination="room_ruins4", origin_letter="A"),
    Portal(region="room_ruins5", destination="room_ruins6", origin_letter="B"),

    Portal(region="room_ruins6", destination="room_ruins5", origin_letter="A"),
    Portal(region="room_ruins6", destination="room_ruins7", origin_letter="B"),

    Portal(region="room_ruins7", destination="room_ruins6", origin_letter="A"),
    Portal(region="room_ruins7", destination="room_ruins7A", origin_letter="B"),
    Portal(region="room_ruins7", destination="room_ruins8", origin_letter="D"),

    Portal(region="room_ruins7A", destination="room_ruins7", origin_letter="A"),

    Portal(region="room_ruins8", destination="room_ruins7", origin_letter="C"),
    Portal(region="room_ruins8", destination="room_ruins9", origin_letter="B"),

    Portal(region="room_ruins9", destination="room_ruins8", origin_letter="A"),
    Portal(region="Ruins 9 Past Puzzles", destination="room_ruins10", origin_letter="B"),

    Portal(region="room_ruins10", destination="Ruins 9 Past Puzzles", origin_letter="A"),
    Portal(region="room_ruins10", destination="room_ruins11", origin_letter="B"),

    Portal(region="room_ruins11", destination="room_ruins10", origin_letter="A"),
    Portal(region="Ruins 11 Past Puzzles", destination="room_ruins12A", origin_letter="B"),

    Portal(region="room_ruins12A", destination="Ruins 11 Past Puzzles", origin_letter="A"),
    Portal(region="room_ruins12A", destination="room_ruins12", origin_letter="B"),

    Portal(region="room_ruins12", destination="room_ruins12A", origin_letter="A"),
    Portal(region="room_ruins12", destination="room_ruins12B", origin_letter="B"),
    Portal(region="room_ruins12", destination="room_ruins13", origin_letter="X"),

    Portal(region="room_ruins12B", destination="room_ruins12", origin_letter="A"),

    Portal(region="room_ruins13", destination="room_ruins12", origin_letter="X"),
    Portal(region="room_ruins13", destination="room_ruins14", origin_letter="B"),

    Portal(region="room_ruins14", destination="room_ruins13", origin_letter="A"),
    Portal(region="Ruins 14 Past Puzzles", destination="room_ruins15A", origin_letter="B"),

    Portal(region="room_ruins15A", destination="Ruins 14 Past Puzzles", origin_letter="A"),
    Portal(region="Ruins 15A Past Puzzles", destination="room_ruins15B", origin_letter="B"),
    Portal(region="room_ruins15A", destination="room_ruins15E", origin_letter="X"),

    Portal(region="room_ruins15B", destination="Ruins 15A Past Puzzles", origin_letter="A"),
    Portal(region="Ruins 15B Past Puzzles", destination="room_ruins15C", origin_letter="B"),
    Portal(region="room_ruins15B", destination="Ruins Pit Circle B", origin_letter="X"),

    Portal(region="room_ruins15C", destination="Ruins 15B Past Puzzles", origin_letter="A"),
    Portal(region="Ruins 15C Past Puzzles", destination="room_ruins15D", origin_letter="B"),
    Portal(region="room_ruins15C", destination="Ruins Pit Circle C", origin_letter="X"),

    Portal(region="room_ruins15D", destination="Ruins 15C Past Puzzles", origin_letter="A"),
    Portal(region="Ruins 15D Past Puzzles", destination="room_ruins16", origin_letter="D"),
    Portal(region="room_ruins15D", destination="Ruins Pit Circle D", origin_letter="X"),

    Portal(region="Ruins Pit Circle B", destination="room_ruins15B", origin_letter="X"),
    Portal(region="Ruins Pit Circle C", destination="room_ruins15C", origin_letter="X"),
    Portal(region="Ruins Pit Circle D", destination="room_ruins15D", origin_letter="X"),

    Portal(region="room_ruins15E", destination="room_ruins15A", origin_letter="X"),

    Portal(region="room_ruins16", destination="Ruins 15D Past Puzzles", origin_letter="C"),
    Portal(region="room_ruins16", destination="room_ruins17", origin_letter="B"),
    Portal(region="room_ruins16", destination="room_ruins19", origin_letter="X"),

    Portal(region="room_ruins17", destination="room_ruins16", origin_letter="A"),
    Portal(region="room_ruins17", destination="room_ruins18OLD", origin_letter="B"),

    Portal(region="room_ruins18OLD", destination="room_ruins17", origin_letter="A"),

    Portal(region="room_ruins19", destination="room_ruins16", origin_letter="X"),
    Portal(region="room_ruins19", destination="room_torhouse1", origin_letter="B"),

    Portal(region="room_torhouse1", destination="room_ruins19", origin_letter="A"),
    Portal(region="room_torhouse1", destination="room_torhouse2", origin_letter="B"),
    Portal(region="room_torhouse1", destination="room_torhouse3", origin_letter="D"),
    Portal(region="room_torhouse1", destination="room_basement1", origin_letter="X"),

    Portal(region="room_torhouse2", destination="room_torhouse1", origin_letter="A"),
    Portal(region="room_torhouse2", destination="room_kitchen", origin_letter="X"),

    Portal(region="room_kitchen", destination="room_torhouse2", origin_letter="X"),

    Portal(region="room_torhouse3", destination="room_torhouse1", origin_letter="C"),
    Portal(region="room_torhouse3", destination="room_asrielroom", origin_letter="D"),
    Portal(region="room_torhouse3", destination="room_torielroom", origin_letter="B"),

    Portal(region="room_asrielroom", destination="room_torhouse3", origin_letter="C"),
    Portal(region="room_torielroom", destination="room_torhouse3", origin_letter="A"),

    Portal(region="room_basement1", destination="room_torhouse1", origin_letter="X"),

    Portal(region="room_basement1", destination="room_basement2", origin_letter="B"),

    Portal(region="room_basement2", destination="room_basement1", origin_letter="A"),
    Portal(region="room_basement2", destination="room_basement3", origin_letter="B"),

    Portal(region="room_basement3", destination="room_basement2", origin_letter="A"),
    Portal(region="room_basement3", destination="room_basement4", origin_letter="B"),

    Portal(region="room_basement4", destination="room_basement3", origin_letter="A"),
    Portal(region="room_basement4", destination="room_basement5", origin_letter="B"),

    Portal(region="room_basement5", destination="room_basement4", origin_letter="A"),
    Portal(region="room_basement5", destination="room_ruinsexit", origin_letter="B"),

    Portal(region="room_ruinsexit", destination="room_basement5", origin_letter="A"),

    Portal(region="room_tundra1", destination="Snowdin Entrance", origin_letter="S"),
    Portal(region="room_tundra1", destination="room_tundra2", origin_letter="B"),

    Portal(region="room_tundra2", destination="room_tundra1", origin_letter="A"),
    Portal(region="room_tundra2", destination="room_tundra3", origin_letter="B"),

    Portal(region="room_tundra3", destination="room_tundra2", origin_letter="A"),
    Portal(region="room_tundra3", destination="room_tundra3A", origin_letter="B"),
    Portal(region="room_tundra3", destination="room_tundra4", origin_letter="D"),

    Portal(region="room_tundra3A", destination="room_tundra3", origin_letter="A"),

    Portal(region="room_tundra4", destination="room_tundra3", origin_letter="C"),
    Portal(region="room_tundra4", destination="room_tundra5", origin_letter="B"),

    Portal(region="room_tundra5", destination="room_tundra4", origin_letter="A"),
    Portal(region="room_tundra5", destination="room_tundra6", origin_letter="B"),

    Portal(region="room_tundra6", destination="room_tundra5", origin_letter="A"),
    Portal(region="room_tundra6", destination="room_tundra6A", origin_letter="B"),
    Portal(region="room_tundra6", destination="room_tundra7", origin_letter="D"),

    Portal(region="room_tundra6A", destination="room_tundra6", origin_letter="A"),

    Portal(region="room_tundra7", destination="room_tundra6", origin_letter="C"),
    Portal(region="room_tundra7", destination="room_tundra8", origin_letter="B"),

    Portal(region="room_tundra8", destination="room_tundra7", origin_letter="A"),
    Portal(region="room_tundra8", destination="room_tundra8A", origin_letter="B"),
    Portal(region="room_tundra8", destination="room_tundra9", origin_letter="D"),

    Portal(region="room_tundra8A", destination="room_tundra8", origin_letter="A"),

    Portal(region="room_tundra9", destination="room_tundra8", origin_letter="C"),
    Portal(region="room_tundra9", destination="room_tundra_spaghetti", origin_letter="B"),

    Portal(region="room_tundra_spaghetti", destination="room_tundra9", origin_letter="A"),
    Portal(region="room_tundra_spaghetti", destination="room_tundra_snowpuzz", origin_letter="B"),

    Portal(region="room_tundra_snowpuzz", destination="room_tundra_spaghetti", origin_letter="A"),
    Portal(region="Snow Puzz After Puzzle", destination="room_tundra_xoxosmall", origin_letter="B"),

    Portal(region="room_tundra_xoxosmall", destination="Snow Puzz After Puzzle", origin_letter="A"),
    Portal(region="small xoxo after puzzle", destination="room_tundra_xoxopuzz", origin_letter="B"),

    Portal(region="room_tundra_xoxopuzz", destination="small xoxo after puzzle", origin_letter="A"),
    Portal(region="xoxo puzz after puzzle", destination="room_tundra_randoblock", origin_letter="B"),

    Portal(region="room_tundra_randoblock", destination="xoxo puzz after puzzle", origin_letter="A"),
    Portal(region="room_tundra_randoblock", destination="room_tundra_lesserdog", origin_letter="B"),

    Portal(region="room_tundra_lesserdog", destination="room_tundra_randoblock", origin_letter="A"),
    Portal(region="room_tundra_lesserdog", destination="room_tundra_iceentrance", origin_letter="D"),

    Portal(region="room_tundra_iceentrance", destination="room_tundra_lesserdog", origin_letter="C"),
    Portal(region="room_tundra_iceentrance", destination="room_tundra_icehole", origin_letter="A"),
    Portal(region="room_tundra_iceentrance", destination="room_tundra_iceexit_new", origin_letter="B"),
    Portal(region="room_tundra_iceentrance", destination="room_tundra_poffzone", origin_letter="X"),

    Portal(region="room_tundra_icehole", destination="room_tundra_iceentrance", origin_letter="B"),

    Portal(region="room_tundra_iceexit_new", destination="room_tundra_iceentrance", origin_letter="A"),
    Portal(region="room_tundra_iceexit_new", destination="room_tundra_iceexit", origin_letter="B"),

    Portal(region="room_tundra_iceexit", destination="room_tundra_iceexit_new", origin_letter="A"),
    Portal(region="room_tundra_iceexit", destination="room_icecave1", origin_letter="X"),

    Portal(region="room_icecave1", destination="room_tundra_iceexit", origin_letter="X"),

    Portal(region="room_tundra_poffzone", destination="room_tundra_iceentrance", origin_letter="X"),
    Portal(region="room_tundra_poffzone", destination="room_tundra_dangerbridge", origin_letter="B"),

    Portal(region="room_tundra_dangerbridge", destination="room_tundra_poffzone", origin_letter="A"),
    Portal(region="room_tundra_dangerbridge", destination="room_tundra_town", origin_letter="B"),

    Portal(region="room_tundra_town", destination="room_tundra_dangerbridge", origin_letter="A"),
    Portal(region="room_tundra_town", destination="room_tundra_town2", origin_letter="B"),
    Portal(region="room_tundra_town", destination="room_shop1", origin_letter="R"),
    Portal(region="room_tundra_town", destination="room_tundra_inn", origin_letter="T"),
    Portal(region="room_tundra_town", destination="room_tundra_grillby", origin_letter="W"),
    Portal(region="room_tundra_town", destination="room_tundra_library", origin_letter="U"),
    Portal(region="room_tundra_town", destination="room_tundra_sanshouse", origin_letter="S"),
    Portal(region="room_tundra_town", destination="room_fogroom", origin_letter="X"),

    Portal(region="room_tundra_town2", destination="room_tundra_town", origin_letter="A"),
    Portal(region="room_tundra_town2", destination="room_tundra_dock", origin_letter="B"),

    Portal(region="room_tundra_dock", destination="room_tundra_town2", origin_letter="A"),

    Portal(region="room_tundra_inn", destination="room_tundra_town", origin_letter="T"),

    Portal(region="room_tundra_grillby", destination="room_tundra_town", origin_letter="W"),

    Portal(region="room_tundra_library", destination="room_tundra_town", origin_letter="U"),

    Portal(region="room_tundra_sanshouse", destination="room_tundra_town", origin_letter="S"),
    Portal(region="Papyrus Rocks", destination="room_tundra_paproom", origin_letter="B"),
    Portal(region="Papyrus Rocks", destination="room_tundra_sansroom", origin_letter="T"),
    Portal(region="room_tundra_sanshouse", destination="room_dogshrine", origin_letter="X"),

    Portal(region="room_tundra_paproom", destination="Papyrus Rocks", origin_letter="A"),

    Portal(region="room_tundra_sansroom", destination="Papyrus Rocks", origin_letter="T"),

    Portal(region="room_dogshrine", destination="room_tundra_sanshouse", origin_letter="X"),

    Portal(region="room_fogroom", destination="room_tundra_town", origin_letter="X"),

    Portal(region="room_shop1", destination="room_tundra_town", origin_letter="R"),

]


for item in portal_mapping:
    if len(item.name) <= 0:
        portal_mapping[portal_mapping.index(item)] = Portal(region=item.region, name=item.region+" "+item.origin_letter, destination=item.destination, origin_letter=item.origin_letter)


class RegionInfo(NamedTuple):
    game_scene: str  # the name of the scene in the actual game
    dead_end: bool = False  # if the region only has one exit
    dead_end_override: bool = False  # if the region only has one exit
    hint: int = 2  # what kind of hint text you should have


class Hint(IntEnum):
    none = 0  # big areas, empty hallways, etc.
    region = 1  # at least one of the portals must not be a dead end
    scene = 2  # multiple regions in the scene, so using region could mean no valid hints


# key is the AP region name. "Fake" in region info just means the mod won't receive that info at all
undertale_er_regions: Dict[str, RegionInfo] = {
    "room_area1": RegionInfo("room_area1"),
    "room_area1_2": RegionInfo("room_area1_2"),
    "room_ruins1": RegionInfo("room_ruins1"),
    "room_ruins2": RegionInfo("room_ruins2"),
    "room_ruins3": RegionInfo("room_ruins3"),
    "room_ruins4": RegionInfo("room_ruins4"),
    "room_ruins5": RegionInfo("room_ruins5"),
    "room_ruins6": RegionInfo("room_ruins6"),
    "room_ruins7": RegionInfo("room_ruins7"),
    "room_ruins7A": RegionInfo("room_ruins7A", dead_end=True),
    "room_ruins8": RegionInfo("room_ruins8"),
    "room_ruins9": RegionInfo("room_ruins9"),
    "room_ruins10": RegionInfo("room_ruins10"),
    "room_ruins11": RegionInfo("room_ruins11"),
    "room_ruins12A": RegionInfo("room_ruins12A"),
    "room_ruins12": RegionInfo("room_ruins12"),
    "room_ruins12B": RegionInfo("room_ruins12B", dead_end=True),
    "room_icecave1": RegionInfo("room_icecave1", dead_end=True),
    "room_ruins13": RegionInfo("room_ruins13"),
    "room_ruins14": RegionInfo("room_ruins14"),
    "room_ruins15A": RegionInfo("room_ruins15A"),
    "room_ruins15B": RegionInfo("room_ruins15B"),
    "room_ruins15C": RegionInfo("room_ruins15C"),
    "room_ruins15D": RegionInfo("room_ruins15D"),
    "room_ruins15E": RegionInfo("room_ruins15E", dead_end=True),
    "room_ruins16": RegionInfo("room_ruins16"),
    "room_ruins17": RegionInfo("room_ruins17"),
    "room_ruins18OLD": RegionInfo("room_ruins18OLD", dead_end=True),
    "room_ruins19": RegionInfo("room_ruins19"),
    "room_torhouse1": RegionInfo("room_torhouse1"),
    "room_torhouse2": RegionInfo("room_torhouse2"),
    "room_torhouse3": RegionInfo("room_torhouse3"),
    "room_torielroom": RegionInfo("room_torielroom", dead_end=True),
    "room_asrielroom": RegionInfo("room_asrielroom", dead_end=True),
    "room_kitchen": RegionInfo("room_kitchen", dead_end=True),
    "room_basement1": RegionInfo("room_basement1"),
    "room_basement2": RegionInfo("room_basement2"),
    "room_basement3": RegionInfo("room_basement3"),
    "room_basement4": RegionInfo("room_basement4"),
    "room_basement5": RegionInfo("room_basement5"),
    "room_ruinsexit": RegionInfo("room_ruinsexit"),
    "room_tundra1": RegionInfo("room_tundra1"),
    "room_tundra2": RegionInfo("room_tundra2"),
    "room_tundra3": RegionInfo("room_tundra3"),
    "room_tundra3A": RegionInfo("room_tundra3A", dead_end=True),
    "room_tundra4": RegionInfo("room_tundra4"),
    "room_tundra5": RegionInfo("room_tundra5"),
    "room_tundra6": RegionInfo("room_tundra6"),
    "room_tundra6A": RegionInfo("room_tundra6A", dead_end=True),
    "room_tundra7": RegionInfo("room_tundra7"),
    "room_tundra8": RegionInfo("room_tundra8"),
    "room_tundra8A": RegionInfo("room_tundra8A", dead_end=True),
    "room_tundra9": RegionInfo("room_tundra9"),
    "room_tundra_spaghetti": RegionInfo("room_tundra_spaghetti"),
    "room_tundra_snowpuzz": RegionInfo("room_tundra_snowpuzz"),
    "Snow Puzz After Puzzle": RegionInfo("room_tundra_snowpuzz", dead_end=True),
    "room_tundra_xoxosmall": RegionInfo("room_tundra_xoxosmall"),
    "small xoxo after puzzle": RegionInfo("room_tundra_xoxosmall", dead_end=True),
    "room_tundra_xoxopuzz": RegionInfo("room_tundra_xoxopuzz"),
    "xoxo puzz after puzzle": RegionInfo("room_tundra_xoxopuzz", dead_end=True),
    "room_tundra_randoblock": RegionInfo("room_tundra_randoblock"),
    "room_tundra_lesserdog": RegionInfo("room_tundra_lesserdog"),
    "room_tundra_icehole": RegionInfo("room_tundra_icehole", dead_end=True),
    "room_tundra_iceentrance": RegionInfo("room_tundra_iceentrance"),
    "room_tundra_iceexit_new": RegionInfo("room_tundra_iceexit_new"),
    "room_tundra_iceexit": RegionInfo("room_tundra_iceexit"),
    "room_tundra_poffzone": RegionInfo("room_tundra_poffzone"),
    "room_tundra_dangerbridge": RegionInfo("room_tundra_dangerbridge"),
    "room_tundra_town": RegionInfo("room_tundra_town"),
    "room_tundra_town2": RegionInfo("room_tundra_town2"),
    "room_tundra_dock": RegionInfo("room_tundra_dock", dead_end=True),
    "room_tundra_inn": RegionInfo("room_tundra_inn", dead_end=True),
    "room_tundra_library": RegionInfo("room_tundra_library", dead_end=True),
    "room_tundra_grillby": RegionInfo("room_tundra_grillby", dead_end=True),
    "room_tundra_sanshouse": RegionInfo("room_tundra_sanshouse"),
    "room_tundra_paproom": RegionInfo("room_tundra_paproom", dead_end=True),
    "room_tundra_sansroom": RegionInfo("room_tundra_sansroom", dead_end=True),
    "room_dogshrine": RegionInfo("room_dogshrine", dead_end=True),
    "room_fogroom": RegionInfo("room_fogroom"),
    "room_shop1": RegionInfo("room_shop1", dead_end=True),
    "room_shop2": RegionInfo("room_shop2", dead_end=True),
    "room_shop5": RegionInfo("room_shop5", dead_end=True),
    "room_water1": RegionInfo("room_water1"),
    "room_water2": RegionInfo("room_water2"),
    "room_water3": RegionInfo("room_water3"),
    "room_water3A": RegionInfo("room_water3A", dead_end=True),
    "room_water4": RegionInfo("room_water4"),
    "room_water_bridgepuzz1": RegionInfo("room_water_bridgepuzz1"),
    "water bridge puzzle after": RegionInfo("room_water_bridgepuzz1", dead_end=True),
    "room_water5": RegionInfo("room_water5"),
    "water bridge puzzle 2 after": RegionInfo("room_water5", dead_end=True),
    "room_water5A": RegionInfo("room_water5A", dead_end=True),
    "room_water6": RegionInfo("room_water6"),
    "room_water7": RegionInfo("room_water7"),
    "room_water8": RegionInfo("room_water8"),
    "room_water9": RegionInfo("room_water9"),
    "room_water_savepoint1": RegionInfo("room_water_savepoint1"),
    "room_water11": RegionInfo("room_water11"),
    "room_water_nicecream": RegionInfo("room_water_nicecream", dead_end=True),
    "room_water12": RegionInfo("room_water12"),
    "room_water_shoe": RegionInfo("room_water_shoe", dead_end=True),
    "room_water_bird": RegionInfo("room_water_bird"),
    "room_water_onionsan": RegionInfo("room_water_onionsan"),
    "room_water14": RegionInfo("room_water14"),
    "room_water_piano": RegionInfo("room_water_piano", dead_end=True),
    "room_water_statue": RegionInfo("room_water_statue"),
    "room_water_prewaterfall": RegionInfo("room_water_prewaterfall"),
    "room_water_waterfall": RegionInfo("room_water_waterfall"),
    "room_water_waterfall2": RegionInfo("room_water_waterfall2"),
    "room_water_waterfall3": RegionInfo("room_water_waterfall3"),
    "Metta Entrance": RegionInfo("room_fire_core_premett"),
    "room_water_waterfall4": RegionInfo("room_water_waterfall4"),
    "room_water_preundyne": RegionInfo("room_water_preundyne"),
    "room_water_undynebridge": RegionInfo("room_water_undynebridge"),
    "room_water_undynebridgeend": RegionInfo("room_water_undynebridgeend"),
    "room_water_trashzone1": RegionInfo("room_water_trashzone1", dead_end=True),
    "room_water_trashsavepoint": RegionInfo("room_water_trashsavepoint"),
    "room_water_trashzone2": RegionInfo("room_water_trashzone2"),
    "room_water_friendlyhub": RegionInfo("room_water_friendlyhub"),
    "room_water_undyneyard": RegionInfo("room_water_undyneyard", dead_end=True),
    "room_water_blookhouse": RegionInfo("room_water_blookhouse", dead_end=True),
    "room_water_hapstablook": RegionInfo("room_water_hapstablook", dead_end=True),
    "hapsta door": RegionInfo("room_water_blookyard"),
    "room_water_blookyard": RegionInfo("room_water_blookyard"),
    "room_water_farm": RegionInfo("room_water_farm"),
    "room_water_shop": RegionInfo("room_water_shop"),
    "room_water_dock": RegionInfo("room_water_dock", dead_end=True),
    "room_water15": RegionInfo("room_water15"),
    "room_water16": RegionInfo("room_water16"),
    "room_water_temvillage": RegionInfo("room_water_temvillage"),
    "room_water17": RegionInfo("room_water17"),
    "room_water18": RegionInfo("room_water18"),
    "room_water19": RegionInfo("room_water19"),
    "room_water20": RegionInfo("room_water20"),
    "room_water21": RegionInfo("room_water21"),
    "room_water_undynefinal": RegionInfo("room_water_undynefinal"),
    "room_fire2": RegionInfo("room_fire2"),
    "Trash Zone Fall": RegionInfo("room_water_trashzone1"),
    "Ruins Pit Circle B": RegionInfo("room_ruins15E"),
    "Ruins Pit Circle C": RegionInfo("room_ruins15E"),
    "Ruins Pit Circle D": RegionInfo("room_ruins15E"),
    "Papyrus Rocks": RegionInfo("room_tundra_sanshouse"),
    "Undyne Rocks": RegionInfo("room_water_friendlyhub"),
    "Ruins Entrance": RegionInfo("room_area1"),
    "Snowdin Entrance": RegionInfo("room_area1"),
    "Waterfall Entrance": RegionInfo("room_area1"),
    "Ruins Exit": RegionInfo("room_area1"),
    "Snowdin Exit": RegionInfo("room_area1"),
    "Waterfall Exit": RegionInfo("room_area1"),
    "Hotland Exit": RegionInfo("room_area1"),
    "Monster Kid Raised Ledge": RegionInfo("room_water_waterfall4", dead_end=True),
    "Menu": RegionInfo("Fake", dead_end=True),
    "room_shop3": RegionInfo("room_shop3", dead_end=True),
    "room_shop4": RegionInfo("room_shop4", dead_end=True),
    "Hotland Entrance": RegionInfo("room_area1"),
    "New Home Entrance": RegionInfo("room_area1"),
    "room_fire_prelab": RegionInfo("room_fire_prelab"),
    "room_fire_dock": RegionInfo("room_fire_dock", dead_end=True),
    "room_fire_lab1": RegionInfo("room_fire_lab1"),
    "room_fire_lab2": RegionInfo("room_fire_lab2", dead_end=True),
    "room_fire3": RegionInfo("room_fire3"),
    "room_fire5": RegionInfo("room_fire5"),
    "room_fire6": RegionInfo("room_fire6"),
    "room_fire6A": RegionInfo("room_fire6A", dead_end=True),
    "room_fire_lasers1": RegionInfo("room_fire_lasers1"),
    "room_fire7": RegionInfo("room_fire7"),
    "room_fire8": RegionInfo("room_fire8"),
    "room_fire_shootguy_2": RegionInfo("room_fire_shootguy_2", dead_end=True),
    "room_fire9": RegionInfo("room_fire9"),
    "room_fire_shootguy_1": RegionInfo("room_fire_shootguy_1", dead_end=True),
    "room_fire_turn": RegionInfo("room_fire_turn"),
    "room_fire_cookingshow": RegionInfo("room_fire_cookingshow"),
    "room_fire_savepoint1": RegionInfo("room_fire_savepoint1"),
    "room_fire_elevator_r1": RegionInfo("room_fire_elevator_r1"),
    "room_fire_elevator_r2": RegionInfo("room_fire_elevator_r2"),
    "room_fire_hotdog": RegionInfo("room_fire_hotdog"),
    "room_fire_walkandbranch": RegionInfo("room_fire_walkandbranch"),
    "room_fire_sorry": RegionInfo("room_fire_sorry", dead_end=True),
    "room_fire_apron": RegionInfo("room_fire_apron", dead_end=True),
    "room_fire10": RegionInfo("room_fire10"),
    "room_fire_rpuzzle": RegionInfo("room_fire_rpuzzle"),
    "room_fire_mewmew2": RegionInfo("room_fire_mewmew2"),
    "room_fire_boysnightout": RegionInfo("room_fire_boysnightout"),
    "room_fire_newsreport": RegionInfo("room_fire_newsreport"),
    "room_fire_coreview2": RegionInfo("room_fire_coreview2"),
    "room_fire_elevator_l2": RegionInfo("room_fire_elevator_l2"),
    "room_fire_elevator_l3": RegionInfo("room_fire_elevator_l3"),
    "room_fire_spidershop": RegionInfo("room_fire_spidershop"),
    "room_fire_walkandbranch2": RegionInfo("room_fire_walkandbranch2"),
    "room_fire_conveyorlaser": RegionInfo("room_fire_conveyorlaser"),
    "room_fire_shootguy_3": RegionInfo("room_fire_shootguy_3", dead_end=True),
    "room_fire_preshootguy4": RegionInfo("room_fire_preshootguy4"),
    "room_fire_shootguy_4": RegionInfo("room_fire_shootguy_4", dead_end=True),
    "room_fire_savepoint2": RegionInfo("room_fire_savepoint2"),
    "room_fire_spider": RegionInfo("room_fire_spider"),
    "room_fire_pacing": RegionInfo("room_fire_pacing"),
    "room_fire_operatest": RegionInfo("room_fire_operatest"),
    "room_fire_multitile": RegionInfo("room_fire_multitile", dead_end=True),
    "room_fire_hotelfront_1": RegionInfo("room_fire_hotelfront_1"),
    "room_fire_hotelfront_2": RegionInfo("room_fire_hotelfront_2"),
    "room_fire_hotellobby": RegionInfo("room_fire_hotellobby"),
    "room_fire_restaurant": RegionInfo("room_fire_restaurant", dead_end=True),
    "room_fire_hoteldoors": RegionInfo("room_fire_hoteldoors", dead_end=True),
    "room_fire_hotelbed": RegionInfo("room_fire_hotelbed", dead_end=True),
    "room_fire_elevator_r3": RegionInfo("room_fire_elevator_r3"),
    "room_fire_precore": RegionInfo("room_fire_precore"),
    "room_fire_core1": RegionInfo("room_fire_core1"),
    "room_fire_core2": RegionInfo("room_fire_core2", dead_end=True),
    "room_fire_core3": RegionInfo("room_fire_core3"),
    "room_fire_core4": RegionInfo("room_fire_core4"),
    "room_fire_core5": RegionInfo("room_fire_core5"),
    "room_fire_core_freebattle": RegionInfo("room_fire_core_freebattle", dead_end=True),
    "room_fire_core_laserfun": RegionInfo("room_fire_core_laserfun"),
    "room_fire_core_branch": RegionInfo("room_fire_core_branch"),
    "room_fire_core_bottomleft": RegionInfo("room_fire_core_bottomleft"),
    "room_fire_core_left": RegionInfo("room_fire_core_left"),
    "room_fire_core_topleft": RegionInfo("room_fire_core_topleft"),
    "room_fire_core_top": RegionInfo("room_fire_core_top"),
    "room_fire_core_topright": RegionInfo("room_fire_core_topright"),
    "room_fire_core_right": RegionInfo("room_fire_core_right"),
    "room_fire_core_bottomright": RegionInfo("room_fire_core_bottomright"),
    "room_fire_core_center": RegionInfo("room_fire_core_center"),
    "room_fire_shootguy_5": RegionInfo("room_fire_shootguy_5", dead_end=True),
    "room_fire_core_treasureleft": RegionInfo("room_fire_core_treasureleft", dead_end=True),
    "room_fire_core_treasureright": RegionInfo("room_fire_core_treasureright", dead_end=True),
    "room_fire_core_warrior": RegionInfo("room_fire_core_warrior", dead_end=True),
    "room_fire_core_bridge": RegionInfo("room_fire_core_bridge"),
    "room_fire_core_premett": RegionInfo("room_fire_core_premett"),
    "room_fire_core_metttest": RegionInfo("room_fire_core_metttest"),
    "room_fire_core_final": RegionInfo("room_fire_core_final"),
    "room_fire_elevator": RegionInfo("room_fire_elevator"),
    "room_fire_elevator_l1": RegionInfo("room_fire_elevator_l1"),
    "room_castle_elevatorout": RegionInfo("room_castle_elevatorout"),
    "room_castle_precastle": RegionInfo("room_castle_precastle"),
    "room_castle_hook": RegionInfo("room_castle_hook"),
    "room_castle_front": RegionInfo("room_castle_front"),
    "room_asghouse1": RegionInfo("room_asghouse1"),
    "room_asghouse2": RegionInfo("room_asghouse2"),
    "room_asghouse3": RegionInfo("room_asghouse3"),
    "room_asgoreroom": RegionInfo("room_asgoreroom", dead_end=True),
    "room_asrielroom_final": RegionInfo("room_asrielroom_final", dead_end=True),
    "room_kitchen_final": RegionInfo("room_kitchen_final", dead_end=True),
    "room_basement1_final": RegionInfo("room_basement1_final"),
    "room_basement2_final": RegionInfo("room_basement2_final"),
    "room_basement3_final": RegionInfo("room_basement3_final"),
    "room_basement4_final": RegionInfo("room_basement4_final"),
    "room_lastruins_corridor": RegionInfo("room_lastruins_corridor"),
    "room_sanscorridor": RegionInfo("room_sanscorridor"),
    "room_castle_finalshoehorn": RegionInfo("room_castle_finalshoehorn"),
    "room_castle_coffins1": RegionInfo("room_castle_coffins1"),
    "room_castle_coffins2": RegionInfo("room_castle_coffins2", dead_end=True),
    "room_castle_throneroom": RegionInfo("room_castle_throneroom", dead_end=True),
    "Hotland Grind Rooms": RegionInfo("Hotland Grind Rooms", dead_end=True, hint=0),
    "Waterfall Grind Rooms": RegionInfo("Waterfall Grind Rooms", dead_end=True, hint=0),
    "Snowdin Grind Rooms": RegionInfo("Snowdin Grind Rooms", dead_end=True, hint=0),
    "Ruins Grind Rooms": RegionInfo("Ruins Grind Rooms", dead_end=True, hint=0),
    "Fire Door 1": RegionInfo("room_fire7"),
    "Fire Door 2": RegionInfo("room_fire_walkandbranch2"),
    "Fire Turn Part 2": RegionInfo("room_fire_turn", dead_end=True),
    "Bed Door One-way": RegionInfo("room_fire_hoteldoors"),
    "Ruins 3 Past Puzzles": RegionInfo("room_ruins3", dead_end=True),
    "Ruins 14 Past Puzzles": RegionInfo("room_ruins14", dead_end=True),
    "Ruins 15A Past Puzzles": RegionInfo("room_ruins15A", dead_end=True),
    "Ruins 15B Past Puzzles": RegionInfo("room_ruins15B", dead_end=True),
    "Ruins 15C Past Puzzles": RegionInfo("room_ruins15C", dead_end=True),
    "Ruins 15D Past Puzzles": RegionInfo("room_ruins15D", dead_end=True),
    "Ruins 11 Past Puzzles": RegionInfo("room_ruins11", dead_end=True),
    "Ruins 9 Past Puzzles": RegionInfo("room_ruins9", dead_end=True),
    "Room Water 7 One Way": RegionInfo("room_water7", dead_end=True),
    "???": RegionInfo("???", dead_end=True, hint=0),
    "room_fire_labelevator": RegionInfo("room_fire_labelevator"),
                }


# so we can just loop over this instead of doing some complicated thing to deal with hallways in the hints
hallways: Dict[str, str] = {
}
hallway_helper: Dict[str, str] = {}
for p1, p2 in hallways.items():
    hallway_helper[p1] = p2
    hallway_helper[p2] = p1


class StaticCxn(NamedTuple):
    origin: str
    destination: str
    reqs: List[List[str]] = []
    region_reqs: List[str] = []
    reverse: bool = False  # if the reverse connection has the same requirements


# the key is the region you have, the value is the regions you get for having that region
# this is mostly so we don't have to do something overly complex to get this information
dependent_regions: Dict[Tuple[str, ...], List[str]] = {
    ("Ruins Pit Circle B",):
         ["room_ruins15E", "Ruins Pit Circle B"],
    ("room_water7",):
         ["room_water7", "Room Water 7 One Way"],
    ("Metta Entrance", "room_fire_core_premett"):
         ["Metta Entrance", "room_fire_core_premett"],
    ("Bed Door One-way",):
         ["room_fire_hoteldoors", "Bed Door One-way"],
    ("room_fire_turn",):
         ["room_fire_turn", "Fire Turn Part 2"],
    ("room_fire7", "Fire Door 1"):
         ["room_fire7", "Fire Door 1"],
    ("room_fire_walkandbranch2", "Fire Door 2"):
         ["room_fire_walkandbranch2", "Fire Door 2"],
    ("Ruins Pit Circle C",):
         ["room_ruins15E", "Ruins Pit Circle C"],
    ("room_tundra_xoxosmall",):
         ["room_tundra_xoxosmall", "small xoxo after puzzle"],
    ("Ruins Pit Circle D",):
         ["room_ruins15E", "Ruins Pit Circle D"],
    ("room_water_waterfall4",):
         ["room_water_waterfall4", "Monster Kid Raised Ledge"],
    ("Papyrus Rocks", "room_tundra_sanshouse"):
         ["Papyrus Rocks", "room_tundra_sanshouse"],
    ("Undyne Rocks", "room_water_friendlyhub"):
         ["Undyne Rocks", "room_water_friendlyhub"],
    ("room_water_undynebridge", "room_water_undynebridgeend", "Trash Zone Fall"):
         ["room_water_undynebridge", "room_water_undynebridgeend", "room_water_trashzone1", "Trash Zone Fall"],
    ("room_water20", "room_water21", "room_water_undynefinal", "room_fire2", "Waterfall Exit"):
         ["room_water20", "room_water21", "room_water_undynefinal", "room_fire2", "Waterfall Exit"],
    ("room_area1",):
         ["room_area1", "Ruins Entrance", "Snowdin Entrance", "Waterfall Entrance"],
    ("room_fire_core_bottomleft",):
         ["room_fire_core_bottomleft","Hotland Grind Rooms"],
    ("room_fire_core_topleft",):
         ["room_fire_core_topleft","Hotland Grind Rooms"],
    ("room_fire_core_topright",):
         ["room_fire_core_topright","Hotland Grind Rooms"],
    ("room_fire_core_bottomright",):
         ["room_fire_core_bottomright","Hotland Grind Rooms"],
    ("room_fire_core_center",):
         ["room_fire_core_center","Hotland Grind Rooms"],
    ("room_fire_core_bridge",):
         ["room_fire_core_bridge","Hotland Grind Rooms"],
    ("room_fire5",):
         ["room_fire5","Hotland Grind Rooms"],
    ("room_fire6",):
         ["room_fire6","Hotland Grind Rooms"],
    ("room_fire_walkandbranch",):
         ["room_fire_walkandbranch","Hotland Grind Rooms"],
    ("room_fire_preshootguy4",):
         ["room_fire_preshootguy4","Hotland Grind Rooms"],
    ("room_water5",):
         ["room_water5","Waterfall Grind Rooms", "water bridge puzzle 2 after"],
    ("room_water6",):
         ["room_water6","Waterfall Grind Rooms"],
    ("room_water12",):
         ["room_water12","Waterfall Grind Rooms"],
    ("room_water15",):
         ["room_water15","Waterfall Grind Rooms"],
    ("room_water16",):
         ["room_water16","Waterfall Grind Rooms"],
    ("room_water17",):
         ["room_water17","Waterfall Grind Rooms"],
    ("room_tundra3",):
         ["room_tundra3","Snowdin Grind Rooms"],
    ("room_tundra4",):
         ["room_tundra4","Snowdin Grind Rooms"],
    ("room_tundra6",):
         ["room_tundra6","Snowdin Grind Rooms"],
    ("room_tundra_snowpuzz",):
         ["room_tundra_snowpuzz","Snowdin Grind Rooms", "Snow Puzz After Puzzle"],
    ("room_tundra_dangerbridge",):
         ["room_tundra_dangerbridge","Snowdin Grind Rooms"],
    ("room_ruins7",):
         ["room_ruins7","Ruins Grind Rooms"],
    ("room_ruins9",):
         ["room_ruins9","Ruins Grind Rooms", "Ruins 9 Past Puzzles"],
    ("room_ruins8",):
         ["room_ruins8","Ruins Grind Rooms"],
    ("room_ruins15A",):
         ["room_ruins15A","Ruins Grind Rooms", "Ruins 15A Past Puzzles"],
    ("room_ruins10",):
         ["room_ruins10","Ruins Grind Rooms"],
    ("room_ruins11",):
         ["room_ruins11","Ruins Grind Rooms", "Ruins 11 Past Puzzles"],
    ("room_ruins15B",):
         ["room_ruins15B","Ruins Grind Rooms", "Ruins 15B Past Puzzles"],
    ("room_ruins15C",):
         ["room_ruins15C","Ruins Grind Rooms", "Ruins 15C Past Puzzles"],
    ("room_ruins15D",):
         ["room_ruins15D","Ruins Grind Rooms", "Ruins 15D Past Puzzles"],
    ("room_ruins14",):
         ["room_ruins14","Ruins Grind Rooms", "Ruins 14 Past Puzzles"],
    ("room_ruins13",):
         ["room_ruins13","Ruins Grind Rooms"],
    ("room_fogroom",):
         ["room_fogroom","Snowdin Exit"],
    ("room_ruinsexit",):
         ["room_ruinsexit","Ruins Exit"],
    ("room_fire_elevator_r1", "room_fire_elevator_r2", "room_fire_elevator_r3", "room_fire_elevator_l1", "room_fire_elevator_l2", "room_fire_elevator_l3", "room_fire_elevator"):
         ["room_fire_elevator_r1", "room_fire_elevator_r2", "room_fire_elevator_r3", "room_fire_elevator_l1", "room_fire_elevator_l2", "room_fire_elevator_l3", "room_fire_elevator"],
    ("room_fire_core_metttest", "room_fire_core_final"):
        ["room_fire_core_metttest", "room_fire_core_final","Hotland Exit"],
    ("room_asghouse1", "room_basement1_final", "room_basement2_final", "room_basement3_final",
         "room_basement4_final", "room_lastruins_corridor", "room_sanscorridor", "room_castle_finalshoehorn",
         "room_castle_coffins1", "room_castle_coffins2", "room_castle_throneroom"):
        ["room_asghouse1", "room_basement1_final", "room_basement2_final", "room_basement3_final",
         "room_basement4_final", "room_lastruins_corridor", "room_sanscorridor", "room_castle_finalshoehorn",
         "room_castle_coffins1", "room_castle_coffins2", "room_castle_throneroom"],
    ("room_fire_lab1",):
         ["room_fire_lab1", "room_fire_labelevator"],
    ("room_ruins3",):
         ["room_ruins3", "Ruins 3 Past Puzzles"],
    ("room_tundra_xoxopuzz",):
         ["room_tundra_xoxopuzz", "xoxo puzz after puzzle"],
    ("room_water_bridgepuzz1",):
         ["room_water_bridgepuzz1", "water bridge puzzle after"],
    ("room_water_blookyard",):
         ["room_water_blookyard", "hapsta door"],
}

names = []
for itm in dependent_regions:
    for ind in itm:
        names.append(ind)
for iteem in names:
    if names.count(iteem) > 1:
        print("DUPLICATE PORTAL NAME " + iteem)
