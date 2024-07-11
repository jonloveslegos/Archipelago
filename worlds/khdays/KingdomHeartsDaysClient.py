# Based (read: copied almost wholesale and edited) off the TLoZ Client.

import asyncio
import copy
import json
import logging
import random
import time
from typing import cast, Dict, Optional, List
from asyncio import StreamReader, StreamWriter

import Utils
from Utils import async_start
from NetUtils import ClientStatus
from CommonClient import CommonContext, server_loop, gui_enabled, ClientCommandProcessor, logger, \
    get_base_parser

from worlds.khdays.Items import item_table, days, true_days, character_list, ItemData
from worlds.khdays.Locations import location_table
from worlds.khdays.Rules import days_day_to_true_day

SYSTEM_MESSAGE_ID = 0

CONNECTION_TIMING_OUT_STATUS = "Connection timing out. Please restart your emulator, then restart KHDaysRandomizer.lua"
CONNECTION_REFUSED_STATUS = "Connection Refused. Please start your emulator and make sure KHDaysRandomizer.lua is running"
CONNECTION_RESET_STATUS = "Connection was reset. Please restart your emulator, then restart KHDaysRandomizer.lua"
CONNECTION_TENTATIVE_STATUS = "Initial Connection Made"
CONNECTION_CONNECTED_STATUS = "Connected"
CONNECTION_INITIAL_STATUS = "Connection has not been initiated"

item_ids = {item: id.code for item, id in item_table.items()}
location_ids = location_table
items_by_id = {id: item for item, id in item_ids.items()}
locations_by_id = {id: location for location, id in location_ids.items()}

days_to_bits = {
    7: "000000111FFFFFFF",
    8: "000001000FFFFFFF",
    9: "000001001FFFFFFF",
    10: "000001010FFFFFFF",
    11: "000001011FFFFFFF",
    12: "000001100FFFFFFF",
    13: "000001101FFFFFFF",
    14: "000001110FFFFFFF",
    15: "000001111FFFFFFF",
    16: "000010000FFFFFFF",
    17: "000010001FFFFFFF",
    22: "000010110FFFFFFF",
    23: "000010111FFFFFFF",
    24: "000011000FFFFFFF",
    25: "000011001FFFFFFF",
    26: "000011010FFFFFFF",
    51: "000110100FFFFFFF",
    52: "000110101FFFFFFF",
    53: "000110110FFFFFFF",
    54: "000110111FFFFFFF",
    71: "001000111FFFFFFF",
    72: "001001000FFFFFFF",
    73: "001001001FFFFFFF",
    74: "001001010FFFFFFF",
    75: "001001011FFFFFFF",
    76: "001001100FFFFFFF",
    77: "001001101FFFFFFF",
    78: "001001110FFFFFFF",
    79: "001001111FFFFFFF",
    94: "001011110FFFFFFF",
    95: "001011111FFFFFFF",
    96: "001100000FFFFFFF",
    97: "001100001FFFFFFF",
    98: "001100010FFFFFFF",
    99: "001100011FFFFFFF",
    100: "001100100FFFFFFF",
    117: "001110101FFFFFFF",
    118: "001110110FFFFFFF",
    119: "001110111FFFFFFF",
    120: "001111000FFFFFFF",
    121: "001111001FFFFFFF",
    122: "001111010FFFFFFF",
    149: "010010101FFFFFFF",
    150: "010010110FFFFFFF",
    151: "010010111FFFFFFF",
    152: "010011000FFFFFFF",
    153: "010011001FFFFFFF",
    154: "010011010FFFFFFF",
    155: "010011011FFFFFFF",
    156: "010011100FFFFFFF",
    171: "010101011FFFFFFF",
    172: "010101100FFFFFFF",
    173: "010101101FFFFFFF",
    174: "010101110FFFFFFF",
    175: "010101111FFFFFFF",
    176: "010110000FFFFFFF",
    193: "011000001FFFFFFF",
    194: "011000010FFFFFFF",
    195: "011000011FFFFFFF",
    196: "011000100FFFFFFF",
    197: "011000101FFFFFFF",
    224: "011100000FFFFFFF",
    225: "011100001FFFFFFF",
    226: "011100010FFFFFFF",
    227: "011100011FFFFFFF",
    255: "011111111FFFFFFF",
    256: "100000000FFFFFFF",
    257: "100000001FFFFFFF",
    258: "100000010FFFFFFF",
    277: "100010101FFFFFFF",
    278: "100010110FFFFFFF",
    279: "100010111FFFFFFF",
    280: "100011000FFFFFFF",
    296: "100101000FFFFFFF",
    297: "100101001FFFFFFF",
    298: "100101010FFFFFFF",
    299: "100101011FFFFFFF",
    300: "100101100FFFFFFF",
    301: "100101101FFFFFFF",
    302: "100101110FFFFFFF",
    303: "100101111FFFFFFF",
    304: "100110000FFFFFFF",
    321: "101000001FFFFFFF",
    322: "101000010FFFFFFF",
    323: "101000011FFFFFFF",
    324: "101000100FFFFFFF",
    325: "101000101FFFFFFF",
    326: "101000110FFFFFFF",
    352: "101100000FFFFFFF",
    353: "101100001FFFFFFF",
    354: "101100010FFFFFFF",
    355: "101100011FFFFFFF",
    357: "101100101FFFFFFF",
    358: "101100110FFFFFFF",
}


class KHDaysCommandProcessor(ClientCommandProcessor):

    def _cmd_nds(self):
        """Check NDS Connection State"""
        if isinstance(self.ctx, KHDaysContext):
            logger.info(f"NDS Status: {self.ctx.nds_status}")

    def _cmd_unlocked_characters(self):
        """Displays a list of characters that you have available."""
        if isinstance(self.ctx, KHDaysContext):
            logger.info(self.ctx.valid_characters)

    def _cmd_unlocked_days(self):
        """Displays a list of days that you have available."""
        if isinstance(self.ctx, KHDaysContext):
            logger.info(self.ctx.valid_days)

    def _cmd_set_character_one(self, char_name: str = ""):
        """Sets the first character in the next mission"""
        if isinstance(self.ctx, KHDaysContext):
            self.ctx.set_character_one(char_name)

    def _cmd_set_character_two(self, char_name: str = ""):
        """Sets the second character in the next mission"""
        if isinstance(self.ctx, KHDaysContext):
            self.ctx.set_character_two(char_name)

    def _cmd_set_day(self, day_number: str = ""):
        """Sets the day after the next mission"""
        if isinstance(self.ctx, KHDaysContext):
            self.ctx.set_day(day_number)


class KHDaysContext(CommonContext):
    command_processor = KHDaysCommandProcessor
    items_handling = 0b111  # full remote
    char_1 = "Roxas"
    char_2 = "Xion"
    chosen_day_number = days_to_bits[8]
    chosen_day = 8
    valid_days = ["8"]
    valid_characters = ["Roxas"]
    connected = "false"
    locations_array = []
    options = {}

    def __init__(self, server_address, password):
        super().__init__(server_address, password)
        self.bonus_items = []
        self.nds_streams: (StreamReader, StreamWriter) = None
        self.nds_sync_task = None
        self.messages = {}
        self.locations_array = []
        self.nds_status = CONNECTION_INITIAL_STATUS
        self.game = 'Kingdom Hearts Days'
        self.awaiting_rom = False
        self.shard_requirement = 5
        self.check_locs_count = {}
        self.chosen_day_number = days_to_bits[8]
        self.chosen_day = 8
        self.valid_days = ["8"]
        self.valid_characters = ["Roxas"]
        self.options = {}
        self.options["synthesis"] = True
        self.options["levels"] = True
        self.options["gifts"] = True

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(KHDaysContext, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def set_character_one(self, char_name: str = ""):
        """Sets the first character in the next mission"""
        if isinstance(self, KHDaysContext):
            if char_name in self.valid_characters:
                if char_name == self.char_2:
                    logger.info("Both characters cannot be the same!")
                else:
                    self.char_1 = char_name
                    logger.info("Character one is now "+char_name)
            else:
                logger.info("Invalid character, did you misspell it?")

    def set_character_two(self, char_name: str = ""):
        """Sets the second character in the next mission"""
        if isinstance(self, KHDaysContext):
            if char_name in self.valid_characters:
                if char_name == self.char_1:
                    logger.info("Both characters cannot be the same!")
                else:
                    self.char_2 = char_name
                    logger.info("Character two is now "+char_name)
            else:
                logger.info("Invalid character, did you misspell it?")

    def set_day(self, day_number: str = ""):
        """Sets the day after the next mission"""
        if isinstance(self, KHDaysContext):
            if day_number in self.valid_days:
                self.chosen_day_number = days_to_bits[int(day_number)]
                self.chosen_day = int(day_number)
                logger.info("Next day will now be day "+day_number)
            else:
                logger.info("Invalid day, do you have it unlocked?")

    def on_package(self, cmd: str, args: dict):
        if cmd == 'Connected':
            slot_data = args["slot_data"]
            self.shard_requirement = slot_data["shard_requirement"]
            self.connected = "true"
            self.chosen_day_number = days_to_bits[8]
            self.chosen_day = 8
            self.valid_characters = []
            self.options["synthesis"] = slot_data["randomize_synthesis"]
            self.options["levels"] = slot_data["randomize_level_rewards"]
            self.options["gifts"] = slot_data["randomize_hub_gifts"]
            self.ui.update_tracker()

        if cmd in {"ReceivedItems"}:
            self.valid_characters = [items_by_id[item.item] for item in self.items_received if item.item < 25000 and item.item > 24000]
            self.valid_days = ["8"]
            for item in {items_by_id[item.item] for item in self.items_received if item.item <= 24000 and item.item > 23000}:
                day_numb = item.removeprefix("Day Unlock: ")
                self.valid_days.append(day_numb)
                if true_days.count(int(day_numb)) > 1:
                    for i in days:
                        if days_day_to_true_day(i) == int(day_numb) and i != day_numb:
                            self.valid_days.append(str(i))
            shard_count = 0
            for item in self.items_received:
                if item.item == 23000:
                    shard_count += 1
            print(shard_count)
            if shard_count >= self.shard_requirement:
                self.valid_days.append("358")
            self.ui.update_tracker()

    async def connection_closed(self):
        self.connected = "false"
        await super(KHDaysContext, self).connection_closed()

    def run_gui(self):
        from kvui import GameManager
        from kivy.uix.tabbedpanel import TabbedPanelItem
        from kivy.uix.button import Button
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.label import Label
        from kivy.uix.gridlayout import GridLayout

        class TrackerLayout(BoxLayout):
            pass

        class CommanderSelect(BoxLayout):
            pass

        class CommanderButton(Button):
            pass

        class FactionBox(BoxLayout):
            pass

        class CommanderGroup(GridLayout):
            pass

        class KHDaysManager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago KH Days Client"
            ctx: KHDaysContext
            commander_buttons: Dict[int, List[CommanderButton]]
            day_buttons: List[CommanderButton]
            tracker_items: Dict[str, ItemData] = {
                **item_table
            }

            def build(self):
                container = super().build()
                panel = TabbedPanelItem(text="Character Selector")
                panel.content = self.build_tracker()
                self.tabs.add_widget(panel)
                panel = TabbedPanelItem(text="Day Selector")
                panel.content = self.build_day_tracker()
                self.tabs.add_widget(panel)
                self.update_tracker()
                return container

            def build_day_tracker(self) -> TrackerLayout:
                try:
                    tracker = TrackerLayout(orientation="horizontal")
                    self.day_buttons = []

                    commander_group = CommanderGroup(cols=10)
                    commander_buttons = []
                    for commander in days+[358]:
                        commander_button = CommanderButton(text="Day "+str(commander))
                        commander_button.bind(on_press=lambda instance: self.ctx.set_day(instance.text.removeprefix("Day ")))
                        commander_buttons.append(commander_button)
                        commander_group.add_widget(commander_button)
                    self.day_buttons = commander_buttons
                    tracker.add_widget(commander_group)
                    return tracker
                except Exception as e:
                    print(e)

            def build_tracker(self) -> TrackerLayout:
                try:
                    tracker = TrackerLayout(orientation="horizontal")
                    commander_select = CommanderSelect(orientation="vertical", spacing=20)
                    self.commander_buttons = {}

                    for i in range(2):
                        faction_box = FactionBox()
                        commander_group = CommanderGroup(cols=5)
                        commander_buttons = []
                        for commander in character_list:
                            commander_button = CommanderButton(text=commander)
                            if i == 0:
                                commander_button.bind(on_press=lambda instance: self.ctx.set_character_one(instance.text))
                            else:
                                commander_button.bind(on_press=lambda instance: self.ctx.set_character_two(instance.text))
                            commander_buttons.append(commander_button)
                            commander_group.add_widget(commander_button)
                        self.commander_buttons[i] = commander_buttons
                        faction_box.add_widget(Label(text="Character "+str(i+1), size_hint_x=None, valign='middle', height=10))
                        faction_box.add_widget(commander_group)
                        commander_select.add_widget(faction_box)
                    tracker.add_widget(commander_select)
                    return tracker
                except Exception as e:
                    print(e)

            def update_tracker(self):
                for i in range(2):
                    for commander_button in self.commander_buttons[i]:
                        commander_button.disabled = not (commander_button.text in self.ctx.valid_characters)
                for day_button in self.day_buttons:
                    day_button.disabled = not (day_button.text.removeprefix("Day ") in self.ctx.valid_days)

        self.ui = KHDaysManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")


def get_payload(ctx: KHDaysContext):
    current_time = time.time()
    ctx.check_locs_count = {}
    for item in item_table:
        ctx.check_locs_count[item] = 0
    total_rank = 0
    for item in ctx.items_received:
        if items_by_id[item.item] == "Progressive Rank":
            total_rank += 1
    for item in ctx.checked_locations:
        if locations_by_id[item].startswith("Synthesis: "):
            temp_view = locations_by_id[item].removeprefix("Synthesis: ").split(" ")
            ctx.check_locs_count["".join([i+" " for i in temp_view[:-1]]).removesuffix(" ")] += 1
        if locations_by_id[item].startswith("Hub: "):
            temp_view = locations_by_id[item].removeprefix("Hub: ").split(" ")
            ctx.check_locs_count["".join([i+" " for i in temp_view[:-1]]).removesuffix(" ")] += 1
    return json.dumps(
        {
            "items": [items_by_id[item.item] for item in ctx.items_received if item.item >= 25000],
            "checked_locs": ctx.check_locs_count,
            "rank": total_rank,
            "day_numb": ctx.chosen_day_number,
            "locs_sent": {key: value for key, value in ctx.locations_checked},
            "messages": {f'{key[0]}:{key[1]}': value for key, value in ctx.messages.items()
                         if key[0] > current_time - 10},
            "char_1": ctx.char_1,
            "char_2": ctx.char_2,
            "connection": ctx.connected,
            "options": ctx.options,
            "day_chosen": ctx.chosen_day,
            "days_unlocked": ctx.valid_days,
        }
    )


async def nds_sync_task(ctx: KHDaysContext):
    logger.info("Starting nds connector. Use /nds for status information")
    while not ctx.exit_event.is_set():
        error_status = None
        if ctx.nds_streams:
            (reader, writer) = ctx.nds_streams
            if len(ctx.valid_characters) > 0:
                if ctx.char_1 not in ctx.valid_characters:
                    ctx.char_1 = random.choice(tuple(ctx.valid_characters))
                if ctx.char_2 not in ctx.valid_characters:
                    ctx.char_2 = random.choice(tuple(ctx.valid_characters))
            if len(ctx.valid_days) > 0:
                if ctx.chosen_day_number not in days_to_bits.values():
                    ctx.chosen_day_number = days_to_bits[8]
            if ctx.char_2 == ctx.char_1:
                if ctx.char_1 == "Xion":
                    ctx.char_2 = "Roxas"
                else:
                    ctx.char_2 = "Xion"
            msg = get_payload(ctx).encode()
            writer.write(msg)
            writer.write(b'\n')
            try:
                await asyncio.wait_for(writer.drain(), timeout=1.5)
                try:
                    # Data will return a dict with up to two fields:
                    # 1. A keepalive response of the Players Name (always)
                    # 2. An array representing the memory values of the locations area (if in game)
                    data = await asyncio.wait_for(reader.readline(), timeout=5)
                    data_decoded = json.loads(data.decode())
                    if ctx.game is not None and 'checked_locs' in data_decoded:
                        for i in data_decoded["checked_locs"]:
                            if data_decoded["checked_locs"][i] not in ctx.locations_array:
                                ctx.locations_array.append(data_decoded["checked_locs"][i])
                                if data_decoded["checked_locs"][i] not in ctx.server_locations:
                                    print("Unknown location: "+str(data_decoded["checked_locs"][i]))
                        await ctx.send_msgs([
                            {"cmd": "LocationChecks",
                            "locations": ctx.locations_array}
                        ])
                    if ctx.game is not None and 'day' in data_decoded:
                        if not ctx.finished_game and int(data_decoded["day"]) >= 358:
                            await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                            ctx.finished_game = True
                except asyncio.TimeoutError:
                    logger.debug("Read Timed Out, Reconnecting")
                    error_status = CONNECTION_TIMING_OUT_STATUS
                    writer.close()
                    ctx.nds_streams = None
                except ConnectionResetError as e:
                    logger.debug("Read failed due to Connection Lost, Reconnecting")
                    error_status = CONNECTION_RESET_STATUS
                    writer.close()
                    ctx.nds_streams = None
            except TimeoutError:
                logger.debug("Connection Timed Out, Reconnecting")
                error_status = CONNECTION_TIMING_OUT_STATUS
                writer.close()
                ctx.nds_streams = None
            except ConnectionResetError:
                logger.debug("Connection Lost, Reconnecting")
                error_status = CONNECTION_RESET_STATUS
                writer.close()
                ctx.nds_streams = None
            if ctx.nds_status == CONNECTION_TENTATIVE_STATUS:
                if not error_status:
                    ctx.locations_array = []
                    logger.info("Successfully Connected to NDS")
                    ctx.nds_status = CONNECTION_CONNECTED_STATUS
                else:
                    ctx.nds_status = f"Was tentatively connected but error occured: {error_status}"
            elif error_status:
                ctx.nds_status = error_status
                logger.info("Lost connection to nds and attempting to reconnect. Use /nds for status updates")
        else:
            try:
                logger.debug("Attempting to connect to NDS")
                ctx.nds_streams = await asyncio.wait_for(asyncio.open_connection("localhost", 52987), timeout=10)
                ctx.nds_status = CONNECTION_TENTATIVE_STATUS
            except TimeoutError:
                logger.debug("Connection Timed Out, Trying Again")
                ctx.nds_status = CONNECTION_TIMING_OUT_STATUS
                continue
            except ConnectionRefusedError:
                logger.debug("Connection Refused, Trying Again")
                ctx.nds_status = CONNECTION_REFUSED_STATUS
                continue


def main():
    # Text Mode to use !hint and such with games that have no text entry
    Utils.init_logging("KHDaysClient", exception_logger="Client")

    async def _main():
        ctx = KHDaysContext(None, None)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="ServerLoop")
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()
        ctx.nds_sync_task = asyncio.create_task(nds_sync_task(ctx), name="NDS Sync")

        await ctx.exit_event.wait()
        ctx.server_address = None

        await ctx.shutdown()

        if ctx.nds_sync_task:
            await ctx.nds_sync_task

    import colorama

    colorama.init()

    asyncio.run(_main())
    colorama.deinit()


if __name__ == "__main__":
    parser = get_base_parser(description="KHDays Client, for text interfacing.")
    args = parser.parse_args()
    main()
