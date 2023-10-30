from __future__ import annotations
import os
import asyncio
import bsdiff4
import multiprocessing

import Utils

from NetUtils import NetworkItem, ClientStatus
from worlds import fnafw
from CommonClient import *


class FNaFWCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: CommonContext):
        super().__init__(ctx)

    def _cmd_resync(self):
        """Manually trigger a resync."""
        self.output(f"Syncing items.")
        self.ctx.syncing = True

    def _cmd_patch(self):
        """Patch the vanilla game."""
        with open(os.path.join(os.getcwd(), "FNaFW Game", "fnaf-world.exe"), "rb") as f:
            patchedFile = bsdiff4.patch(f.read(), fnafw.data_path("patch.bsdiff"))
        with open(os.path.join(os.getcwd(), "FNaFW Game", "FNaFW Modded.exe"), "wb") as f:
            f.write(patchedFile)
        self.output(f"Done!")

    def _cmd_deathlink(self):
        """Toggles deathlink"""
        if isinstance(self.ctx, FNaFWContext):
            self.ctx.deathlink_status = not self.ctx.deathlink_status
            if self.ctx.deathlink_status:
                self.output(f"Deathlink enabled.")
            else:
                self.output(f"Deathlink disabled.")


class FNaFWContext(CommonContext):
    command_processor: int = FNaFWCommandProcessor
    game = "FNaFW"
    items_handling = 0b111  # full remote
    progressive_anims_order = []
    progressive_chips_order = []
    progressive_bytes_order = []

    def __init__(self, server_address, password):
        super().__init__(server_address, password)
        self.syncing = False
        self.game = 'FNaFW'
        self.got_deathlink = False
        self.deathlink_status = False

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

    def on_deathlink(self, data: typing.Dict[str, typing.Any]):
        self.got_deathlink = True
        super().on_deathlink(data)


async def not_in_use(filename):
    try:
        os.rename(filename, filename)
        return True
    except:
        return False


async def process_fnafw_cmd(ctx: FNaFWContext, cmd: str, args: dict):
    if cmd == 'Connected':
        ctx.progressive_anims_order = args["slot_data"]["Progressive Animatronics Order"]
        ctx.progressive_chips_order = args["slot_data"]["Progressive Chips Order"]
        ctx.progressive_bytes_order = args["slot_data"]["Progressive Bytes Order"]
        path = os.path.expandvars("%appdata%/MMFApplications/fnafw5")
        if not os.path.exists(path):
            while True:
                try:
                    with open(path, "w") as f:
                        f.write("[fnafw]\n")
                        f.close()
                    break
                except PermissionError:
                    continue
        path = os.path.expandvars("%appdata%/MMFApplications/fnafwAP5")
        while True:
            try:
                with open(path, "w") as f:
                    f.write("[fnafw]\n")
                    f.close()
                break
            except PermissionError:
                continue
        path = os.path.expandvars("%appdata%/MMFApplications/fnafwAPSCOUT5")
        while True:
            try:
                with open(path, "w") as f:
                    f.write("[fnafw]\n")
                    f.close()
                break
            except PermissionError:
                continue
    elif cmd == "LocationInfo":
        for l in args["locations"]:
            while True:
                try:
                    if not os.path.exists(os.path.expandvars("%appdata%/MMFApplications/fnafwAPSCOUT5")):
                        with open(os.path.expandvars("%appdata%/MMFApplications/fnafwAPSCOUT5"), "w") as file:
                            file.write("[fnafw]\n")
                            file.close()
                    with open(os.path.expandvars("%appdata%/MMFApplications/fnafwAPSCOUT5"), 'a') as file:
                        file.write(str(fnafw.location_table[ctx.location_names[l.location]].setId)+"SCOUT="+ctx.player_names[l.player]+"'s "+str(ctx.item_names[l.item])+"\n")
                        file.close()
                    break
                except PermissionError:
                    continue
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
            if os.path.exists(os.path.expandvars("%appdata%/MMFApplications/fnafwAP5")):
                temp_progressive = {}
                temp_progressive["anims"] = ctx.progressive_anims_order.copy()
                temp_progressive["bytes"] = ctx.progressive_bytes_order.copy()
                temp_progressive["chips"] = ctx.progressive_chips_order.copy()
                for item in args['items']:
                    if fnafw.FNaFWWorld.item_id_to_name[NetworkItem(*item).item] == "Progressive Animatronic":
                        if len(temp_progressive["anims"]) > 0:
                            item_got = fnafw.item_table[temp_progressive["anims"].pop(0)].setId
                        else:
                            item_got = "nothing"
                    elif fnafw.FNaFWWorld.item_id_to_name[NetworkItem(*item).item] == "Progressive Byte":
                        if len(temp_progressive["bytes"]) > 0:
                            item_got = fnafw.item_table[temp_progressive["bytes"].pop(0)].setId
                        else:
                            item_got = "nothing"
                    elif fnafw.FNaFWWorld.item_id_to_name[NetworkItem(*item).item] == "Progressive Chip":
                        if len(temp_progressive["chips"]) > 0:
                            item_got = fnafw.item_table[temp_progressive["chips"].pop(0)].setId
                        else:
                            item_got = "nothing"
                    else:
                        item_got = fnafw.item_table[fnafw.FNaFWWorld.item_id_to_name[NetworkItem(*item).item]].setId
                    while True:
                        try:
                            with open(os.path.expandvars("%appdata%/MMFApplications/fnafwAP5"), 'r+') as f:
                                lines = f.read()
                                if not item_got == "armor":
                                    f.write(str(item_got)+"=1\n")
                                if not lines.__contains__("armor="):
                                    f.write("armor=0\n")
                                f.close()
                            with open(os.path.expandvars("%appdata%/MMFApplications/fnafwAP5"), "r") as file:
                                replacement = ""
                                for line in file:
                                    line = line.strip()
                                    if item_got == "armor":
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
                            with open(os.path.expandvars("%appdata%/MMFApplications/fnafwAP5"), "w") as f:
                                f.writelines(lines_to_simplify)
                                f.close()
                            break
                        except PermissionError:
                            continue
                    ctx.items_received.append(NetworkItem(*item))
        ctx.watcher_event.set()


async def game_watcher(ctx: FNaFWContext):
    while not ctx.exit_event.is_set():
        await ctx.update_death_link(ctx.deathlink_status)
        if ctx.syncing:
            sync_msg = [{'cmd': 'Sync'}]
            if ctx.locations_checked:
                sync_msg.append({"cmd": "LocationChecks", "locations": list(ctx.locations_checked)})
            await ctx.send_msgs(sync_msg)
            ctx.syncing = False
        path = os.path.expandvars("%appdata%/MMFApplications/fnafwAP5")
        if ctx.got_deathlink:
            ctx.got_deathlink = False
            while True:
                try:
                    with open(os.path.expandvars("%appdata%/MMFApplications/fnafwAP5"), 'r+') as f:
                        lines = f.read()
                        if not lines.__contains__("deathlink="):
                            f.write("deathlink=0\n")
                        f.close()
                    with open(os.path.expandvars("%appdata%/MMFApplications/fnafwAP5"), "r") as file:
                        replacement = ""
                        for line in file:
                            line = line.strip()
                            if (line.__contains__("deathlink=0")):
                                changes = line.replace("deathlink=0", "deathlink=1")
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
                    with open(os.path.expandvars("%appdata%/MMFApplications/fnafwAP5"), "w") as f:
                        f.writelines(lines_to_simplify)
                        f.close()
                    break
                except PermissionError:
                    continue
        sending = []
        hinting = []
        victory = False
        filesread = []
        if os.path.exists(os.path.expandvars("%appdata%/MMFApplications/fnafw5")):
            while True:
                try:
                    with open(os.path.expandvars("%appdata%/MMFApplications/fnafw5"), 'r') as f:
                        filesread = f.readlines()
                        f.close()
                    break
                except PermissionError:
                    continue
        if os.path.exists(os.path.expandvars("%appdata%/MMFApplications/fnafwDEATH5")):
            while True:
                try:
                    with open(os.path.expandvars("%appdata%/MMFApplications/fnafwDEATH5"), 'r') as f:
                        if "deathlink=1\n" in f.readlines():
                            if "DeathLink" in ctx.tags:
                                await ctx.send_death()
                        f.close()
                    break
                except PermissionError:
                    continue
        if os.path.exists(path):
            while True:
                try:
                    with open(path, 'r+') as f:
                        lines = f.readlines()
                        for name, data in fnafw.location_table.items():
                            if data.setId+"=1\n" in filesread and data.setId != "" and not str(data.id)+"=sent\n" in lines:
                                sending = sending+[(int(data.id))]
                                f.write(str(data.id)+"=sent\n")
                            if data.hintId+"=1\n" in filesread and data.hintId != "" and not str(data.id)+"HINT=sent\n" in lines:
                                hinting = hinting+[(int(data.id))]
                                f.write(str(data.id)+"HINT=sent\n")
                        f.close()
                    break
                except PermissionError:
                    continue
        path = os.path.expandvars("%appdata%/MMFApplications/fnafwAP5")
        if os.path.exists(path):
            while True:
                try:
                    with open(path, 'r') as f:
                        filesread = f.readlines()
                        if "fin=1\n" in filesread:
                            victory = True
                        f.close()
                    break
                except PermissionError:
                    continue
        if os.path.exists(os.path.expandvars("%appdata%/MMFApplications/fnafwDEATH5")):
            while True:
                try:
                    with open(os.path.expandvars("%appdata%/MMFApplications/fnafwDEATH5"), "w") as f:
                        f.writelines(["[fnafw]", "deathlink=0"])
                        f.close()
                    break
                except PermissionError:
                    continue
        if victory:
            os.remove(path)
        ctx.locations_checked = sending
        message = [{"cmd": 'LocationChecks', "locations": sending}]
        await ctx.send_msgs(message)
        if len(hinting) > 0:
            hint_message = [{"cmd": 'LocationScouts', "locations": hinting, "create_as_hint": 2}]
            await ctx.send_msgs(hint_message)
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

