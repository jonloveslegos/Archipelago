from __future__ import annotations
import os
import sys
import asyncio
import shutil

import ModuleUpdate
import worlds.dustaet.Items

ModuleUpdate.update()

import Utils

if __name__ == "__main__":
    Utils.init_logging("DustAETClient", exception_logger="Client")

from NetUtils import NetworkItem, ClientStatus
from CommonClient import gui_enabled, logger, get_base_parser, ClientCommandProcessor, \
    CommonContext, server_loop
from worlds.dustaet import Items


class DustAETClientCommandProcessor(ClientCommandProcessor):
    def _cmd_resync(self):
        """Manually trigger a resync."""
        self.output(f"Syncing items.")
        self.ctx.syncing = True


class DustAETContext(CommonContext):
    command_processor: int = DustAETClientCommandProcessor
    game = "DustAET"
    items_handling = 0b111  # full remote

    def __init__(self, server_address, password):
        super(DustAETContext, self).__init__(server_address, password)
        self.send_index: int = 0
        self.syncing = False
        self.awaiting_bridge = False
        # self.game_communication_path: files go in this path to pass data between us and the actual game
        if "localappdata" in os.environ:
            self.game_communication_path = os.path.expandvars(r"%localappdata%/DustAET")
            if not os.path.exists(self.game_communication_path):
                os.mkdir(self.game_communication_path)
        else:
            # not windows. game is an exe so let's see if wine might be around to run it
            if "WINEPREFIX" in os.environ:
                wineprefix = os.environ["WINEPREFIX"]
            elif shutil.which("wine") or shutil.which("wine-stable"):
                wineprefix = os.path.expanduser("~/.wine") # default root of wine system data, deep in which is app data
            else:
                msg = "DustAETClient couldn't detect system type. Unable to infer required game_communication_path"
                logger.error("Error: " + msg)
                Utils.messagebox("Error", msg, error=True)
                sys.exit(1)
            self.game_communication_path = os.path.join(
                wineprefix,
                "drive_c",
                os.path.expandvars("users/$USER/Local Settings/Application Data/DustAET"))

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(DustAETContext, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    async def connection_closed(self):
        await super(DustAETContext, self).connection_closed()
        for root, dirs, files in os.walk(self.game_communication_path):
            for file in files:
                os.remove(root + "/" + file)

    @property
    def endpoints(self):
        if self.server:
            return [self.server]
        else:
            return []

    async def shutdown(self):
        await super(DustAETContext, self).shutdown()
        for root, dirs, files in os.walk(self.game_communication_path):
            for file in files:
                os.remove(root+"/"+file)

    def on_package(self, cmd: str, args: dict):
        if cmd in {"Connected"}:
            if not os.path.exists(self.game_communication_path):
                os.makedirs(self.game_communication_path)
        if cmd in {"ReceivedItems"}:
            start_index = args["index"]
            if start_index != len(self.items_received):
                filename = f"received"
                success = False
                while not success:
                    try:
                        with open(os.path.join(self.game_communication_path, filename), 'a') as f:
                            for item in args['items']:
                                f.write(Items.item_table[Items.lookup_id_to_name[NetworkItem(*item).item]].game_id+"\n")
                            f.close()
                        success = True
                    except Exception as msg:
                        success = False

    def run_gui(self):
        """Import kivy UI system and start running it as self.ui_task."""
        from kvui import GameManager

        class DustAETManager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago DustAET Client"

        self.ui = DustAETManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")


async def game_watcher(ctx: DustAETContext):
    from worlds.dustaet.Locations import advancement_table
    while not ctx.exit_event.is_set():
        if ctx.syncing == True:
            sync_msg = [{'cmd': 'Sync'}]
            if ctx.locations_checked:
                sync_msg.append({"cmd": "LocationChecks", "locations": list(ctx.locations_checked)})
            await ctx.send_msgs(sync_msg)
            ctx.syncing = False
        sending = []
        victory = False
        for root, dirs, files in os.walk(ctx.game_communication_path):
            for file in files:
                if file.find("added") > -1:
                    os.remove(os.path.join(ctx.game_communication_path, file))
                    message = [{"cmd": 'Set', "key": "ItemsAdded", "operations": [{"operation": "replace", "value": ctx.items_received}]}]
                    await ctx.send_msgs(message)
                if file.find("sent") > -1:
                    with open(os.path.join(ctx.game_communication_path, file), 'r') as f:
                        for i in f.readlines():
                            if i.strip() == "General Gaius":
                                victory = True
                            else:
                                for adv in advancement_table:
                                    if advancement_table[adv].game_id == i.strip():
                                        sending = sending+[(int(advancement_table[adv].id))]
        ctx.locations_checked = sending
        message = [{"cmd": 'LocationChecks', "locations": sending}]
        await ctx.send_msgs(message)
        if not ctx.finished_game and victory:
            await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
            ctx.finished_game = True
        await asyncio.sleep(0.1)


if __name__ == '__main__':
    async def main(args):
        ctx = DustAETContext(args.connect, args.password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()
        progression_watcher = asyncio.create_task(
            game_watcher(ctx), name="DustAETProgressionWatcher")

        await ctx.exit_event.wait()
        ctx.server_address = None

        await progression_watcher

        await ctx.shutdown()

    import colorama

    parser = get_base_parser(description="DustAET Client, for text interfacing.")

    args, rest = parser.parse_known_args()
    colorama.init()
    asyncio.run(main(args))
    colorama.deinit()
