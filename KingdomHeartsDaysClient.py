# Based (read: copied almost wholesale and edited) off the TLoZ Client.

import asyncio
import copy
import json
import logging
import random
import time
from typing import cast, Dict, Optional
from asyncio import StreamReader, StreamWriter

import Utils
from Utils import async_start
from NetUtils import ClientStatus
from CommonClient import CommonContext, server_loop, gui_enabled, ClientCommandProcessor, logger, \
    get_base_parser

from worlds.khdays.Items import item_table
from worlds.khdays.Locations import location_table

SYSTEM_MESSAGE_ID = 0

CONNECTION_TIMING_OUT_STATUS = "Connection timing out. Please restart your emulator, then restart KHDaysRandomizer.lua"
CONNECTION_REFUSED_STATUS = "Connection Refused. Please start your emulator and make sure KHDaysRandomizer.lua is running"
CONNECTION_RESET_STATUS = "Connection was reset. Please restart your emulator, then restart KHDaysRandomizer.lua"
CONNECTION_TENTATIVE_STATUS = "Initial Connection Made"
CONNECTION_CONNECTED_STATUS = "Connected"
CONNECTION_INITIAL_STATUS = "Connection has not been initiated"

DISPLAY_MSGS = True

item_ids = {item: id.code for item, id in item_table.items()}
location_ids = location_table
items_by_id = {id: item for item, id in item_ids.items()}
locations_by_id = {id: location for location, id in location_ids.items()}


class KHDaysCommandProcessor(ClientCommandProcessor):

    def _cmd_nds(self):
        """Check NDS Connection State"""
        if isinstance(self.ctx, KHDaysContext):
            logger.info(f"NDS Status: {self.ctx.nds_status}")

    def _cmd_toggle_msgs(self):
        """Toggle displaying messages in bizhawk"""
        global DISPLAY_MSGS
        DISPLAY_MSGS = not DISPLAY_MSGS
        logger.info(f"Messages are now {'enabled' if DISPLAY_MSGS else 'disabled'}")

    def _cmd_unlocked_characters(self):
        """Displays a list of characters that you have available."""
        if isinstance(self.ctx, KHDaysContext):
            logger.info(self.ctx.valid_characters)

    def _cmd_set_character_one(self, char_name: str = ""):
        """Sets the first character in the next mission"""
        if isinstance(self.ctx, KHDaysContext):
            if char_name in self.ctx.valid_characters:
                self.ctx.char_1 = char_name
                logger.info("Character one is now "+char_name)
            else:
                logger.info("Invalid character, did you misspell it?")

    def _cmd_set_character_two(self, char_name: str = ""):
        """Sets the second character in the next mission"""
        if isinstance(self.ctx, KHDaysContext):
            if char_name in self.ctx.valid_characters:
                self.ctx.char_2 = char_name
                logger.info("Character two is now "+char_name)
            else:
                logger.info("Invalid character, did you misspell it?")


class KHDaysContext(CommonContext):
    command_processor = KHDaysCommandProcessor
    items_handling = 0b111  # full remote
    char_1 = "Roxas"
    char_2 = ""
    valid_characters = {"Roxas"}
    connected = "false"

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
        self.day_requirement = 358

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(KHDaysContext, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def _set_message(self, msg: str, msg_id: int):
        if DISPLAY_MSGS:
            self.messages[(time.time(), msg_id)] = msg

    def on_package(self, cmd: str, args: dict):
        if cmd == 'Connected':
            slot_data = args["slot_data"]
            self.day_requirement = slot_data["day_requirement"]
            self.connected = "true"
            async_start(self.send_msgs([
                {"cmd": "Get",
                "keys": ["received_items"]}
            ]))
        elif cmd == 'Print':
            msg = args['text']
            if ': !' not in msg:
                self._set_message(msg, SYSTEM_MESSAGE_ID)
        elif cmd == 'Retrieved':
            if "keys" not in args:
                logger.warning(f"invalid Retrieved packet to KingdomHeartsDaysClient: {args}")
                return
            keys = cast(Dict[str, Optional[str]], args["keys"])

    async def connection_closed(self):
        self.connected = "false"
        await super(KHDaysContext, self).connection_closed()

    def on_print_json(self, args: dict):
        if self.ui:
            self.ui.print_json(copy.deepcopy(args["data"]))
        else:
            text = self.jsontotextparser(copy.deepcopy(args["data"]))
            logger.info(text)
        relevant = args.get("type", None) in {"Hint", "ItemSend"}
        if relevant:
            item = args["item"]
            # goes to this world
            if self.slot_concerns_self(args["receiving"]):
                relevant = True
            # found in this world
            elif self.slot_concerns_self(item.player):
                relevant = True
            # not related
            else:
                relevant = False
            if relevant:
                item = args["item"]
                msg = self.raw_text_parser(copy.deepcopy(args["data"]))
                self._set_message(msg, item.item)

    def run_gui(self):
        from kvui import GameManager

        class KHDaysManager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago KH Days Client"

        self.ui = KHDaysManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")


def get_payload(ctx: KHDaysContext):
    current_time = time.time()
    check_locs_count = {}
    check_locs = [''.join([i+" " for i in str(locations_by_id[item]).split(" ")[:-1]])[:-1] for item in ctx.checked_locations if location_table[(''.join([i+" " for i in str(locations_by_id[item]).split(" ")[:-1]])[:-1]+" "+str(max(1, int("".join(locations_by_id[item].split(" ")[len(locations_by_id[item].split(" "))-1]))-1)))] in ctx.checked_locations or int("".join(filter(str.isdigit, str(locations_by_id[item])))) == 1]
    for i in check_locs:
        if not check_locs_count.keys().__contains__(i):
            check_locs_count[i] = 1
        else:
            check_locs_count[i] = check_locs_count[i] + 1
    print(check_locs_count)
    return json.dumps(
        {
            "items": [items_by_id[item.item] for item in ctx.items_received if item.item >= 25000],
            "checked_locs": check_locs_count,
            "messages": {f'{key[0]}:{key[1]}': value for key, value in ctx.messages.items()
                         if key[0] > current_time - 10},
            "char_1": ctx.char_1,
            "char_2": ctx.char_2,
            "connection": ctx.connected
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
                    ctx.valid_characters = {items_by_id[item.item] for item in ctx.items_received if item.item < 25000}
                    if ctx.game is not None and 'checked_locs' in data_decoded:
                        ctx.locations_array = []
                        for i in data_decoded["checked_locs"]:
                            ctx.locations_array.append(data_decoded["checked_locs"][i])
                        await ctx.send_msgs([
                            {"cmd": "LocationChecks",
                            "locations": ctx.locations_array}
                        ])
                    if ctx.game is not None and 'day' in data_decoded:
                        if not ctx.finished_game and int(data_decoded["day"]) >= ctx.day_requirement:
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


if __name__ == '__main__':
    # Text Mode to use !hint and such with games that have no text entry
    Utils.init_logging("KHDaysClient")


    async def main(args):
        if args.diff_file:
            import Patch
            logging.info("Patch file was supplied. Creating nds rom..")
            meta, romfile = Patch.create_rom_file(args.diff_file)
            if "server" in meta:
                args.connect = meta["server"]
            logging.info(f"Wrote rom file to {romfile}")
        ctx = KHDaysContext(args.connect, args.password)
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

    parser = get_base_parser()
    parser.add_argument('diff_file', default="", type=str, nargs="?",
                        help='Path to a Archipelago Binary Patch file')
    args = parser.parse_args()
    colorama.init()

    asyncio.run(main(args))
    colorama.deinit()
