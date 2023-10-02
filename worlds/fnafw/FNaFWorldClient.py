from __future__ import annotations
import multiprocessing

import Utils

from worlds import fnafw
from CommonClient import *
from worlds.fnafw import FNaFWWorld, item_table, location_table
import bsdiff4


class FNaFWCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: CommonContext):
        super().__init__(ctx)

    def _cmd_resync(self):
        """Manually trigger a resync."""
        self.output(f"Syncing items.")
        self.ctx.syncing = True

    def _cmd_patch(self):
        """Patch the vanilla game."""
        bsdiff4.file_patch(os.getcwd() + "/FNaFW Game/fnafworld.exe", os.getcwd() + "/FNaFW Game/FNaFW Modded.exe",
                           fnafw.data_path("patch.bsdiff"))
        self.output(f"Done!")


class FNaFWContext(CommonContext):
    command_processor: int = FNaFWCommandProcessor
    game = "FNaFW"
    items_handling = 0b111  # full remote

    def __init__(self, server_address, password):
        super().__init__(server_address, password)
        self.syncing = False
        self.game = 'FNaFW'

    def on_package(self, cmd: str, args: dict):
        asyncio.create_task(process_fnafw_cmd(self, cmd, args))

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def run_gui(self):
        from kvui import GameManager

        class FNAFWManager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago FNaF World Client"

        self.ui = FNAFWManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")


async def not_in_use(filename):
    try:
        os.rename(filename, filename)
        return True
    except:
        return False


async def process_fnafw_cmd(ctx: FNaFWContext, cmd: str, args: dict):
    if cmd == 'Connected':
        path = os.path.expandvars("%appdata%/MMFApplications/fnafw1")
        if not os.path.exists(path):
            with open(path, "w") as f:
                f.write("[fnafw]\n")
                f.close()

    elif cmd == 'ReceivedItems':
        start_index = args["index"]

        if start_index == 0:
            ctx.items_received = []
        elif start_index != len(ctx.items_received):
            sync_msg = [{'cmd': 'Sync'}]
            if ctx.locations_checked:
                sync_msg.append({"cmd": "LocationChecks",
                                 "locations": list(ctx.locations_checked)})
            await ctx.send_msgs(sync_msg)
        if start_index == len(ctx.items_received):
            if os.path.exists(os.path.expandvars("%appdata%/MMFApplications/fnafwAP1")):
                for item in args['items']:
                    while True:
                        try:
                            with open(os.path.expandvars("%appdata%/MMFApplications/fnafwAP1"), 'r+') as f:
                                lines = f.read()
                                item_got = item_table[FNaFWWorld.item_id_to_name[NetworkItem(*item).item]].setId
                                if not item_got == "armor":
                                    f.write(str(item_got)+"=1\n")
                                if not lines.__contains__("armor="):
                                    f.write("armor=0\n")
                                f.close()
                            break
                        except PermissionError:
                            continue
                    while True:
                        try:
                            with open(os.path.expandvars("%appdata%/MMFApplications/fnafwAP1"), "r") as file:
                                replacement = ""
                                for line in file:
                                    line = line.strip()
                                    if item_table[FNaFWWorld.item_id_to_name[NetworkItem(*item).item]].setId == \
                                            "armor":
                                        if (line.__contains__("armor=10")):
                                            changes = line
                                        elif (line.__contains__("armor=0")):
                                            changes = line.replace("armor=0", "armor=1")
                                        elif (line.__contains__("armor=1")):
                                            changes = line.replace("armor=1", "armor=2")
                                        elif (line.__contains__("armor=2")):
                                            changes = line.replace("armor=2", "armor=10")
                                        else:
                                            changes = line
                                    else:
                                        changes = line
                                    replacement = replacement + changes + "\n"
                                file.close()
                            break
                        except PermissionError:
                            continue
                    lines_to_simplify = replacement.splitlines()
                    temp_lines = []
                    if lines_to_simplify.count("[fnafw]") <= 0:
                        temp_lines.append("[fnafw]\n")
                    for ln in lines_to_simplify:
                        if temp_lines.count(ln+"\n") <= 0:
                            temp_lines.append(ln+"\n")
                    lines_to_simplify = temp_lines
                    while True:
                        try:
                            with open(os.path.expandvars("%appdata%/MMFApplications/fnafwAP1"), "w") as f:
                                f.writelines(lines_to_simplify)
                                f.close()
                            break
                        except PermissionError:
                            continue
                    ctx.items_received.append(NetworkItem(*item))
        ctx.watcher_event.set()


async def game_watcher(ctx: FNaFWContext):
    while not ctx.exit_event.is_set():
        if ctx.syncing:
            sync_msg = [{'cmd': 'Sync'}]
            if ctx.locations_checked:
                sync_msg.append({"cmd": "LocationChecks", "locations": list(ctx.locations_checked)})
            await ctx.send_msgs(sync_msg)
            ctx.syncing = False
        path = os.path.expandvars("%appdata%/MMFApplications/fnafwAP1")
        sending = []
        victory = False
        filesread = ""
        if os.path.exists(os.path.expandvars("%appdata%/MMFApplications/fnafw1")):
            while True:
                try:
                    with open(os.path.expandvars("%appdata%/MMFApplications/fnafw1"), 'r+') as f:
                        filesread = f.read()
                        f.close()
                    break
                except PermissionError:
                    continue
        if os.path.exists(path):
            while True:
                try:
                    with open(path, 'r+') as f:
                        lines = f.read()
                        for name, data in location_table.items():
                            if data.setId in filesread and data.setId != "" and not str(data.id)+"=sent" in lines:
                                sending = sending+[(int(data.id))]
                                f.write(str(data.id)+"=sent\n")
                        f.close()
                    break
                except PermissionError:
                    continue
        path = os.path.expandvars("%appdata%/MMFApplications/fnafwAP1")
        if os.path.exists(path):
            while True:
                try:
                    with open(path, 'r+') as f:
                        filesread = f.readlines()
                        if filesread.__contains__("fin=1\n"):
                            victory = True
                        f.close()
                    break
                except PermissionError:
                    continue
        if victory:
            os.remove(path)
        ctx.locations_checked = sending
        message = [{"cmd": 'LocationChecks', "locations": sending}]
        await ctx.send_msgs(message)
        if not ctx.finished_game and victory:
            await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
            ctx.finished_game = True
        await asyncio.sleep(0.1)


def main():
    Utils.init_logging("FNaFWorldClient", exception_logger="Client")

    async def _main():
        multiprocessing.freeze_support()
        parser = get_base_parser()
        args = parser.parse_args()

        ctx = FNaFWContext(args.connect, args.password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        if not os.path.exists(os.getcwd() + "/FNaFW Game"):
            os.mkdir(os.getcwd() + "/FNaFW Game")

        progression_watcher = asyncio.create_task(
            game_watcher(ctx), name="FNaFWProgressionWatcher")

        await ctx.exit_event.wait()
        ctx.server_address = None

        await ctx.shutdown()

        await progression_watcher

    import colorama

    colorama.init()

    asyncio.run(_main())
    colorama.deinit()


if __name__ == "__main__":

    parser = get_base_parser(description="FNaFW Client, for text interfacing.")

    args, rest = parser.parse_known_args()
    main()

