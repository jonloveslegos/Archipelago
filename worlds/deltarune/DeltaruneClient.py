from __future__ import annotations
import os
import asyncio
import typing
import bsdiff4
import shutil

import Utils

from NetUtils import NetworkItem, ClientStatus
from worlds import deltarune
from MultiServer import mark_raw
from CommonClient import CommonContext, server_loop, \
    gui_enabled, ClientCommandProcessor, get_base_parser
from Utils import async_start


class DeltaruneCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx):
        super().__init__(ctx)

    def _cmd_patch(self):
        """Patch the game. Only use this command if /auto_patch fails."""
        if isinstance(self.ctx, DeltaruneContext):
            os.makedirs(name=Utils.user_path("Deltarune"), exist_ok=True)
            self.ctx.patch_game()
            self.output("Patched.")

    def _cmd_savepath(self, directory: str):
        """Redirect to proper save data folder. This is necessary for Linux users to use before connecting."""
        if isinstance(self.ctx, DeltaruneContext):
            self.ctx.save_game_folder = directory
            self.output("Changed to the following directory: " + self.ctx.save_game_folder)

    @mark_raw
    def _cmd_auto_patch(self, steaminstall: typing.Optional[str] = None):
        """Patch the game automatically."""
        if isinstance(self.ctx, DeltaruneContext):
            os.makedirs(name=Utils.user_path("Deltarune"), exist_ok=True)
            tempInstall = steaminstall
            if not os.path.isfile(os.path.join(tempInstall, "data.win")):
                tempInstall = None
            if tempInstall is None:
                tempInstall = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\DELTARUNE"
                if not os.path.exists(tempInstall):
                    tempInstall = "C:\\Program Files\\Steam\\steamapps\\common\\DELTARUNE"
            elif not os.path.exists(tempInstall):
                tempInstall = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\DELTARUNE"
                if not os.path.exists(tempInstall):
                    tempInstall = "C:\\Program Files\\Steam\\steamapps\\common\\DELTARUNE"
            if not os.path.exists(tempInstall) or not os.path.exists(tempInstall) or not os.path.isfile(os.path.join(tempInstall, "data.win")):
                self.output("ERROR: Cannot find Deltarune. Please rerun the command with the correct folder."
                            " command. \"/auto_patch (Steam directory)\".")
            else:
                shutil.copytree(tempInstall, Utils.user_path("Deltarune"), dirs_exist_ok=True)
                self.ctx.patch_game()
                self.output("Patching successful!")


class DeltaruneContext(CommonContext):
    tags = {"AP"}
    game = "Deltarune"
    command_processor = DeltaruneCommandProcessor
    items_handling = 0b111
    chapters = None
    goal_macguffin_amount = 1
    save_game_folder = os.path.expandvars(r"%localappdata%/DELTARUNEAP")

    def __init__(self, server_address, password):
        super().__init__(server_address, password)
        self.finished_game = False
        self.game = "Deltarune"
        self.chapters = []
        self.goal_macguffin_amount = 1
        # self.save_game_folder: files go in this path to pass data between us and the actual game
        self.save_game_folder = os.path.expandvars(r"%localappdata%/DELTARUNEAP")

    def patch_game(self):
        with open(Utils.user_path("Deltarune", "chapter1_windows", "data.win"), "rb") as f:
            patchedFile = bsdiff4.patch(f.read(), deltarune.data_path("ch1.bsdiff"))
        with open(Utils.user_path("Deltarune", "chapter1_windows", "data.win"), "wb") as f:
            f.write(patchedFile)

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def clear_deltarune_files(self):
        path = self.save_game_folder
        self.finished_game = False
        for root, dirs, files in os.walk(path):
            for file in files:
                if "check.spot" == file or "scout" == file:
                    os.remove(os.path.join(root, file))
                elif file.endswith((".item", ".victory", ".route", ".mine", ".flag", ".hint")):
                    os.remove(os.path.join(root, file))

    async def connect(self, address: typing.Optional[str] = None):
        self.clear_deltarune_files()
        await super().connect(address)

    async def disconnect(self, allow_autoreconnect: bool = False):
        self.clear_deltarune_files()
        await super().disconnect(allow_autoreconnect)

    async def connection_closed(self):
        self.clear_deltarune_files()
        await super().connection_closed()

    async def shutdown(self):
        self.clear_deltarune_files()
        await super().shutdown()

    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            self.game = self.slot_info[self.slot].game
        async_start(process_deltarune_cmd(self, cmd, args))

    def run_gui(self):
        from kvui import GameManager

        class UTManager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago Deltarune Client"

        self.ui = UTManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")


async def process_deltarune_cmd(ctx: DeltaruneContext, cmd: str, args: dict):
    if cmd == "Connected":
        if not os.path.exists(ctx.save_game_folder):
            os.mkdir(os.path.join(ctx.save_game_folder))
        ctx.chapters = args["slot_data"]["chapters"]
        # for itm in ctx.chapters:
        #     filename = f"{itm}.route"
        #     with open(os.path.join(ctx.save_game_folder, filename), "w") as f:
        #         f.close()
        ctx.goal_macguffin_amount = args["slot_data"]["goal_macguffin_amount"]
        filename = f"macguffin_amount.flag"
        with open(os.path.join(ctx.save_game_folder, filename), "w") as f:
            f.write(str(ctx.goal_macguffin_amount)+"\n")
            f.close()
        filename = f"check.spot"
        with open(os.path.join(ctx.save_game_folder, filename), "a") as f:
            for ss in set(args["checked_locations"]):
                f.write(str(ss)+"\n")
            f.close()
    elif cmd == "LocationInfo":
        for l in args["locations"]:
            locationid = l.location
            filename = f"{str(locationid)}.hint"
            with open(os.path.join(ctx.save_game_folder, filename), "w") as f:
                toDraw = ""
                for i in range(20):
                    if i < len(str(ctx.item_names.lookup_in_game(l.item))):
                        toDraw += str(ctx.item_names.lookup_in_game(l.item))[i]
                    else:
                        break
                f.write(toDraw)
                f.close()
    elif cmd == "ReceivedItems":
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
            counter = -1
            for item in args["items"]:
                id = NetworkItem(*item).location
                while NetworkItem(*item).location < 0 and \
                        counter <= id:
                    id -= 1
                if NetworkItem(*item).location < 0:
                    counter -= 1
                filename = f"{str(id)}PLR{str(NetworkItem(*item).player)}.item"
                with open(os.path.join(ctx.save_game_folder, filename), "w") as f:
                    f.write(str(NetworkItem(*item).item))
                    f.close()
                ctx.items_received.append(NetworkItem(*item))
        ctx.watcher_event.set()

    elif cmd == "RoomUpdate":
        if "checked_locations" in args:
            filename = f"check.spot"
            with open(os.path.join(ctx.save_game_folder, filename), "a") as f:
                for ss in set(args["checked_locations"]):
                    f.write(str(ss)+"\n")
                f.close()


async def game_watcher(ctx: DeltaruneContext):
    while not ctx.exit_event.is_set():
        path = ctx.save_game_folder
        sending = []
        victory = False
        found_routes = 0
        for root, dirs, files in os.walk(path):
            for file in files:
                if "scout" == file:
                    sending = []
                    try:
                        with open(os.path.join(root, file), "r") as f:
                            lines = f.readlines()
                        for l in lines:
                            if ctx.server_locations.__contains__(int(l)):
                                sending = sending + [int(l.rstrip('\n'))]
                    finally:
                        await ctx.send_msgs([{"cmd": "LocationScouts", "locations": sending,
                                                          "create_as_hint": int(2)}])
                        os.remove(os.path.join(root, file))
                if "check.spot" in file:
                    sending = []
                    try:
                        with open(os.path.join(root, file), "r") as f:
                            lines = f.readlines()
                        for l in lines:
                            sending = sending+[(int(l.rstrip('\n')))]
                    finally:
                        await ctx.send_msgs([{"cmd": "LocationChecks", "locations": sending}])
                if "victory" in file:
                    victory = True
        ctx.locations_checked = sending
        if (not ctx.finished_game) and victory:
            await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
            ctx.finished_game = True
        await asyncio.sleep(0.1)


def main():
    Utils.init_logging("DeltaruneClient", exception_logger="Client")

    async def _main():
        ctx = DeltaruneContext(None, None)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
        asyncio.create_task(
            game_watcher(ctx), name="DeltaruneProgressionWatcher")

        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        await ctx.exit_event.wait()
        await ctx.shutdown()

    import colorama

    colorama.init()

    asyncio.run(_main())
    colorama.deinit()


if __name__ == "__main__":
    parser = get_base_parser(description="Deltarune Client, for text interfacing.")
    args = parser.parse_args()
    main()
