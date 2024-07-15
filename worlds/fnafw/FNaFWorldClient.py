from __future__ import annotations
import bsdiff4
import shutil
import multiprocessing

import platform

from worlds import fnafw
from MultiServer import mark_raw
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
        if platform.system() == "Linux":
            with open(os.path.expanduser("~/Archipelago/FNaFW Game/fnaf-world.exe"), "rb") as f:
                patchedFile = bsdiff4.patch(f.read(), fnafw.data_path("patch.bsdiff"))
            with open(os.path.expanduser("~/Archipelago/FNaFW Game/FNaFW Modded.exe"), "wb") as f:
                f.write(patchedFile)
        else:
            with open(os.path.join(os.getcwd(), "FNaFW Game", "fnaf-world.exe"), "rb") as f:
                patchedFile = bsdiff4.patch(f.read(), fnafw.data_path("patch.bsdiff"))
            with open(os.path.join(os.getcwd(), "FNaFW Game", "FNaFW Modded.exe"), "wb") as f:
                f.write(patchedFile)
        self.output(f"Done!")

    @mark_raw
    def _cmd_savepath(self, directory: str):
        """Redirect to proper save data folder. (Use before connecting!)"""
        self.ctx.save_game_folder = directory
        self.output("Changed to the following directory: " + self.ctx.save_game_folder)

    @mark_raw
    def _cmd_auto_patch(self, steaminstall: typing.Optional[str] = None):
        """Patch the game automatically."""
        if platform.system() == "Linux":
            os.makedirs(name=os.path.expanduser("~/Archipelago/FNaFW Game"), exist_ok=True)
        else:
            os.makedirs(name=os.path.join(os.getcwd(), "FNaFW Game"), exist_ok=True)
        tempInstall = steaminstall
        if tempInstall is not None:
            if not os.path.isfile(os.path.join(tempInstall, "FNaF_World.exe")):
                tempInstall = None
        if tempInstall is None:
            if platform.system() == "Linux":
                tempInstall = os.path.expanduser("~/.steam/steam/steamapps/common/FNaF World/")
            else:
                tempInstall = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\FNaF World"
                if not os.path.exists(tempInstall):
                    tempInstall = "C:\\Program Files\\Steam\\steamapps\\common\\FNaF World"
        elif not os.path.exists(tempInstall):
            tempInstall = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\FNaF World"
            if not os.path.exists(tempInstall):
                tempInstall = "C:\\Program Files\\Steam\\steamapps\\common\\FNaF World"
        if not os.path.exists(tempInstall) or not os.path.isfile(os.path.join(tempInstall, "FNaF_World.exe")):
            self.output("ERROR: Cannot find FNaF World. Please rerun the command with the correct folder."
                        " command. \"/auto_patch (Steam directory)\".")
        else:
            if platform.system() == "Linux":
                shutil.copy(os.path.join(tempInstall, "FNaF_World.exe"),
                            os.path.expanduser("~/Archipelago/FNaFW Game/FNaF_World.exe"))
                with open(os.path.expanduser("~/Archipelago/FNaFW Game/FNaF_World.exe"), "rb") as f:
                    patchedFile = bsdiff4.patch(f.read(), fnafw.data_path("patch.bsdiff"))
                with open(os.path.expanduser("~/Archipelago/FNaFW Game/FNaFW Modded.exe"), "wb") as f:
                    f.write(patchedFile)
                self.output(f"Done!")
            else:
                shutil.copy(os.path.join(tempInstall, "FNaF_World.exe"),
                            os.path.join(os.getcwd(), "FNaFW Game", "FNaF_World.exe"))
                with open(os.path.join(os.getcwd(), "FNaFW Game", "FNaF_World.exe"), "rb") as f:
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
    cheap_endo = True
    ending_goal = ""
    area_warping = ""
    if platform.system() == "Linux":
        save_game_folder = os.path.expanduser(
            "~/.steam/steam/steamapps/compatdata/427920/pfx/drive_c/users/steamuser/AppData/Roaming/MMFApplications/")
    else:
        save_game_folder = os.path.expandvars("%appdata%/MMFApplications")

    def __init__(self, server_address, password):
        super().__init__(server_address, password)
        self.syncing = False
        self.game = 'FNaFW'
        self.got_deathlink = False
        self.deathlink_status = False
        self.cheap_endo = True
        self.ending_goal = ""
        self.area_warping = ""
        # self.save_game_folder: files go in this path to pass data between us and the actual game
        if platform.system() == "Linux":
            self.save_game_folder = os.path.expanduser("~/.steam/steam/steamapps/compatdata/427920/pfx/drive_c/users"
                                                       "/steamuser/AppData/Roaming/MMFApplications/")
        else:
            self.save_game_folder = os.path.expandvars("%appdata%/MMFApplications")

    def on_package(self, cmd: str, arguments: dict):
        asyncio.create_task(process_fnafw_cmd(self, cmd, arguments))

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def clear_fnafw_ap_files(self):
        self.finished_game = False
        path = os.path.join(self.save_game_folder, "fnafwAP5")
        if os.path.exists(path):
            os.remove(path)
        path = os.path.join(self.save_game_folder, "fnafwAPTokens5")
        if os.path.exists(path):
            os.remove(path)
        path = os.path.join(self.save_game_folder, "fnafwAPSCOUT5")
        if os.path.exists(path):
            os.remove(path)

    def clear_all_fnafw_files(self):
        self.finished_game = False
        path = os.path.join(self.save_game_folder, "fnafw5")
        if os.path.exists(path):
            os.remove(path)
        path = os.path.join(self.save_game_folder, "fnafwDEATH5")
        if os.path.exists(path):
            os.remove(path)

    def swap_fnafw_files(self, old_address: str, new_address: str):
        self.finished_game = False
        path = os.path.join(self.save_game_folder, "fnafw5")
        if os.path.exists(path):
            new_file = ""
            to_name = 1
            first_empty = -1
            no_file_count = 0
            while os.path.exists(os.path.join(self.save_game_folder, "fnafw5_"+str(to_name))) or no_file_count < 3:
                if os.path.exists(os.path.join(self.save_game_folder, "fnafw5_"+str(to_name))):
                    no_file_count = 0
                    with open(os.path.join(self.save_game_folder, "fnafw5_"+str(to_name)), "r") as f:
                        lines = f.read()
                        if lines.__contains__("address="+new_address):
                            new_file = os.path.join(self.save_game_folder, "fnafw5_"+str(to_name))
                else:
                    if first_empty == -1:
                        first_empty = to_name
                    no_file_count += 1
                to_name += 1
            while True:
                try:
                    shutil.copy(path, os.path.join(self.save_game_folder, "fnafw5_"+str(first_empty)))
                    break
                except PermissionError:
                    pass
            with open(os.path.join(self.save_game_folder, "fnafw5_"+str(first_empty)), "r+") as f:
                if not f.read().__contains__("address="):
                    f.write("address="+old_address+"\n")
            while True:
                try:
                    os.remove(path)
                    break
                except PermissionError:
                    pass
            while True:
                try:
                    if new_file != "":
                        shutil.copy(new_file, path)
                        os.remove(new_file)
                    break
                except PermissionError:
                    pass

    async def connect(self, address: typing.Optional[str] = None):
        await super().connect(address)

    async def disconnect(self, allow_autoreconnect: bool = False):
        await super().disconnect(allow_autoreconnect)

    async def connection_closed(self):
        await super().connection_closed()

    async def shutdown(self):
        await super().shutdown()

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
    except PermissionError:
        return False


async def process_fnafw_cmd(ctx: FNaFWContext, cmd: str, arguments: dict):
    if cmd == 'Connected':
        ctx.progressive_anims_order = arguments["slot_data"]["Progressive Animatronics Order"]
        ctx.progressive_chips_order = arguments["slot_data"]["Progressive Chips Order"]
        ctx.progressive_bytes_order = arguments["slot_data"]["Progressive Bytes Order"]
        ctx.ending_goal = arguments["slot_data"]["ending_goal"]
        ctx.area_warping = arguments["slot_data"]["area_warping"]

        ctx.cheap_endo = arguments["slot_data"]["cheap_endo"]
        path = os.path.join(ctx.save_game_folder, "fnafwAP5")
        while True:
            try:
                saved_address = ""
                for i in range(10):
                    saved_address += str(arguments["slot_data"]["fnafw_world_identifier"][i])
                found = False
                if os.path.exists(path):
                    with open(path, "r") as f:
                        lines = f.readlines()
                        for line in lines:
                            if line.strip() == "address="+saved_address:
                                found = True
                    if not found:
                        for line in lines:
                            if line.strip().__contains__("address="):
                                ctx.swap_fnafw_files(line.strip().split("=")[1], saved_address)
                                ctx.clear_fnafw_ap_files()
                with open(path, "w") as f:
                    f.write("[fnafw]\n")
                    f.write("address="+saved_address+"\n")
                    f.write("endinggoal="+ctx.ending_goal+"\n")
                    f.write("areawarping="+ctx.area_warping+"\n")
                    if ctx.cheap_endo:
                        f.write("cheapendo=1\n")
                    else:
                        f.write("cheapendo=0\n")
                    f.close()
                break
            except PermissionError:
                pass
        path = os.path.join(ctx.save_game_folder, "fnafw5")
        if not os.path.exists(path):
            while True:
                try:
                    with open(path, "w") as f:
                        f.write("[fnafw]\n")
                        f.close()
                    break
                except PermissionError:
                    pass
        path = os.path.join(ctx.save_game_folder, "fnafwAPSCOUT5")
        while True:
            try:
                with open(path, "w") as f:
                    f.write("[fnafw]\n")
                    f.close()
                break
            except PermissionError:
                pass
    elif cmd == "LocationInfo":
        for loc in arguments["locations"]:
            while True:
                try:
                    if not os.path.exists(os.path.join(ctx.save_game_folder, "fnafwAPSCOUT5")):
                        with open(os.path.join(ctx.save_game_folder, "fnafwAPSCOUT5"), "w") as file:
                            file.write("[fnafw]\n")
                            file.close()
                    with open(os.path.join(ctx.save_game_folder, "fnafwAPSCOUT5"), 'a') as file:
                        file.write(str(fnafw.location_table[ctx.location_names[loc.location]].setId) + "SCOUT=" +
                                   ctx.player_names[loc.player] + "'s " + str(ctx.item_names[loc.item]) + "\n")
                        file.close()
                    break
                except PermissionError:
                    pass
    elif cmd == 'ReceivedItems':
        start_index = arguments["index"]

        if start_index == 0:
            ctx.items_received = []
        elif start_index != len(ctx.items_received):
            sync_msg = [{'cmd': 'Sync'}]
            if ctx.locations_checked:
                sync_msg.append({"cmd": "LocationChecks",
                                 "locations": list(ctx.locations_checked)})
            await ctx.send_msgs(sync_msg)
        if start_index == len(ctx.items_received):
            if os.path.exists(os.path.join(ctx.save_game_folder, "fnafwAP5")):
                temp_progressive = {"anims": ctx.progressive_anims_order.copy(),
                                    "bytes": ctx.progressive_bytes_order.copy(),
                                    "chips": ctx.progressive_chips_order.copy()}
                with open(os.path.join(ctx.save_game_folder, "fnafwAPTokens5"), 'w') as f:
                    f.write("tokens=0\n")
                    f.close()
                for item in arguments['items']:
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
                            with open(os.path.join(ctx.save_game_folder, "fnafwAP5"), 'r+') as f:
                                lines = f.read()
                                if not item_got == "armor" and not item_got.__contains__("tokens"):
                                    f.write(str(item_got) + "=1\n")
                                if not lines.__contains__("armor="):
                                    f.write("armor=0\n")
                                f.close()
                            with open(os.path.join(ctx.save_game_folder, "fnafwAP5"), "r") as file:
                                replacement = ""
                                for line in file:
                                    line = line.strip()
                                    if item_got == "armor":
                                        if line.__contains__("armor=10"):
                                            changes = line
                                        elif line.__contains__("armor=0"):
                                            changes = line.replace("armor=0", "armor=1")
                                        elif line.__contains__("armor=1"):
                                            changes = line.replace("armor=1", "armor=2")
                                        elif line.__contains__("armor=2"):
                                            changes = line.replace("armor=2", "armor=10")
                                        else:
                                            changes = line
                                    else:
                                        changes = line
                                    replacement = replacement + changes + "\n"
                                file.close()
                            break
                        except PermissionError:
                            pass
                    lines_to_simplify = replacement.splitlines()
                    temp_lines = []
                    if lines_to_simplify.count("[fnafw]") <= 0:
                        temp_lines.append("[fnafw]\n")
                    for ln in lines_to_simplify:
                        if temp_lines.count(ln + "\n") <= 0:
                            temp_lines.append(ln + "\n")
                    lines_to_simplify = temp_lines
                    while True:
                        try:
                            with open(os.path.join(ctx.save_game_folder, "fnafwAP5"), "w") as f:
                                f.writelines(lines_to_simplify)
                                f.close()
                            break
                        except PermissionError:
                            pass
                    while True:
                        try:
                            with open(os.path.join(ctx.save_game_folder, "fnafwAPTokens5"), 'r+') as f:
                                lines = f.read()
                                if not lines.__contains__("tokens="):
                                    f.write("tokens=0\n")
                                f.close()
                            with open(os.path.join(ctx.save_game_folder, "fnafwAPTokens5"), "r") as file:
                                replacement = ""
                                for line in file:
                                    line = line.strip()
                                    if item_got.__contains__("tokens"):
                                        if line.__contains__("tokens="):
                                            changes = "tokens=" + str(
                                                int(line.split("=")[1]) + int(item_got.split("=")[1]))
                                        else:
                                            changes = line
                                    else:
                                        changes = line
                                    replacement = replacement + changes + "\n"
                                file.close()
                            break
                        except PermissionError:
                            pass
                    lines_to_simplify = replacement.splitlines()
                    temp_lines = []
                    if lines_to_simplify.count("[fnafw]") <= 0:
                        temp_lines.append("[fnafw]\n")
                    for ln in lines_to_simplify:
                        if temp_lines.count(ln + "\n") <= 0:
                            temp_lines.append(ln + "\n")
                    lines_to_simplify = temp_lines
                    while True:
                        try:
                            with open(os.path.join(ctx.save_game_folder, "fnafwAPTokens5"), "w") as f:
                                f.writelines(lines_to_simplify)
                                f.close()
                            break
                        except PermissionError:
                            pass
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
        path = os.path.join(ctx.save_game_folder, "fnafwAP5")
        if ctx.got_deathlink:
            ctx.got_deathlink = False
            while True:
                try:
                    with open(os.path.join(ctx.save_game_folder, "fnafwAPDEATHREC5"), 'r+') as f:
                        lines = f.read()
                        if not lines.__contains__("deathlink="):
                            f.write("deathlink=0\n")
                        f.close()
                    with open(os.path.join(ctx.save_game_folder, "fnafwAPDEATHREC5"), "r") as file:
                        replacement = ""
                        for line in file:
                            line = line.strip()
                            if line.__contains__("deathlink=0"):
                                changes = line.replace("deathlink=0", "deathlink=1")
                            else:
                                changes = line
                            replacement = replacement + changes + "\n"
                        file.close()
                    break
                except PermissionError:
                    pass
            lines_to_simplify = replacement.splitlines()
            temp_lines = []
            if lines_to_simplify.count("[fnafw]") <= 0:
                temp_lines.append("[fnafw]\n")
            for ln in lines_to_simplify:
                if temp_lines.count(ln + "\n") <= 0:
                    temp_lines.append(ln + "\n")
            lines_to_simplify = temp_lines
            while True:
                try:
                    with open(os.path.join(ctx.save_game_folder, "fnafwAP5"), "w") as f:
                        f.writelines(lines_to_simplify)
                        f.close()
                    break
                except PermissionError:
                    pass
        sending = []
        hinting = []
        victory = False
        filesread = []
        if os.path.exists(os.path.join(ctx.save_game_folder, "fnafw5")):
            while True:
                try:
                    with open(os.path.join(ctx.save_game_folder, "fnafw5"), 'r') as f:
                        filesread = f.readlines()
                        f.close()
                    break
                except PermissionError:
                    pass
        if os.path.exists(os.path.join(ctx.save_game_folder, "fnafwDEATH5")):
            while True:
                try:
                    with open(os.path.join(ctx.save_game_folder, "fnafwDEATH5"), 'r') as f:
                        if "deathlink=1\n" in f.readlines():
                            if "DeathLink" in ctx.tags:
                                await ctx.send_death()
                        f.close()
                    break
                except PermissionError:
                    pass
        if os.path.exists(path):
            while True:
                try:
                    with open(path, 'r') as f:
                        lines = f.readlines()
                    with open(path, 'a') as f:
                        for name, data in fnafw.location_table.items():
                            if data.setId + "=1\n" in filesread and data.setId != "" and not str(
                                    data.id) + "=sent\n" in lines:
                                sending = sending + [(int(data.id))]
                                f.write(str(data.id) + "=sent\n")
                            if data.hintId + "=1\n" in filesread and data.hintId != "" and not str(
                                    data.id) + "HINT=sent\n" in lines:
                                hinting = hinting + [(int(data.id))]
                                f.write(str(data.id) + "HINT=sent\n")
                        f.close()
                    break
                except PermissionError:
                    pass
        path = os.path.join(ctx.save_game_folder, "fnafw5")
        if os.path.exists(path):
            while True:
                try:
                    with open(path, 'r') as f:
                        filesread = f.readlines()
                        if "fin"+ctx.ending_goal+"=1\n" in filesread:
                            victory = True
                        f.close()
                    break
                except PermissionError:
                    pass
        if os.path.exists(os.path.join(ctx.save_game_folder, "fnafwDEATH5")):
            while True:
                try:
                    with open(os.path.join(ctx.save_game_folder, "fnafwDEATH5"), "w") as f:
                        f.writelines(["[fnafw]\n", "deathlink=0\n"])
                        f.close()
                    break
                except PermissionError:
                    pass
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
        parser = get_base_parser(description="FNaFW Client, for text interfacing.")
        args = parser.parse_args()

        ctx = FNaFWContext(args.connect, args.password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        if platform.system() == "Linux":
            if not os.path.exists(os.path.expanduser("~/Archipelago/FNaFW Game")):
                os.makedirs(name=os.path.expanduser("~/Archipelago/FNaFW Game"))
        else:
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
    main()
