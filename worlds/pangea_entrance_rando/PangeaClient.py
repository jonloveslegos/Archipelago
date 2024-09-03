from __future__ import annotations
import os
import asyncio
import typing
import bsdiff4
import shutil
import platformdirs
import platform
import uuid

import Utils

from typing import List, Tuple
from NetUtils import NetworkItem, ClientStatus
try:
    import custom_worlds.undertale.UndertaleClient as ut_world
except ModuleNotFoundError:
    try:
        import worlds.undertale.UndertaleClient as ut_world
    except ModuleNotFoundError:
        import UndertaleClient as ut_world
from MultiServer import mark_raw
from CommonClient import CommonContext, server_loop, \
    gui_enabled, ClientCommandProcessor, logger, get_base_parser
from Utils import async_start
from multiprocessing import Process


def run_undertale():
    print('running Undertale client')
    p = Process(target=ut_world.main)
    p.start()


class PangeaCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx):
        super().__init__(ctx)


class PangeaContext(CommonContext):
    tags = {"AP", "Online"}
    game = "Pangea"
    command_processor = PangeaCommandProcessor
    items_handling = 0b111
    entrances: List[Tuple[str, str]] = None

    def __init__(self, server_address, password):
        super().__init__(server_address, password)
        self.finished_game = False
        self.game = "Pangea"
        self.syncing = False
        self.entrances = []

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            self.game = self.slot_info[self.slot].game
        async_start(process_pangea_cmd(self, cmd, args))

    def run_gui(self):
        from kvui import GameManager

        class UTManager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago Pangea Client"

        self.ui = UTManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")


async def process_pangea_cmd(ctx: PangeaContext, cmd: str, args: dict):
    if cmd == "ReceivedItems":
        start_index = args["index"]

        if start_index == 0:
            ctx.items_received = []
        elif start_index != len(ctx.items_received):
            sync_msg = [{"cmd": "Sync"}]
            if ctx.locations_checked:
                sync_msg.append({"cmd": "LocationChecks",
                                 "locations": list(ctx.locations_checked)})
            await ctx.send_msgs(sync_msg)
        if start_index == len(ctx.items_received):
            for item in args["items"]:
                ctx.items_received.append(NetworkItem(*item))
        ctx.watcher_event.set()


def main():
    Utils.init_logging("PangeaClient", exception_logger="Client")

    async def _main():
        ctx = PangeaContext(None, None)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")

        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()
        run_undertale()

        await ctx.exit_event.wait()
        await ctx.shutdown()

    import colorama

    colorama.init()

    asyncio.run(_main())
    colorama.deinit()


if __name__ == "__main__":
    parser = get_base_parser(description="Pangea Client, for text interfacing.")
    args = parser.parse_args()
    main()
