from __future__ import annotations
import os
import logging
import asyncio
import multiprocessing
import subprocess
import urllib.parse
import sys
import typing
import time
import bsdiff4
import CommonClient

import websockets

import Utils

if __name__ == "__main__":
    Utils.init_logging("UndertaleClient", exception_logger="Client")

from NetUtils import Endpoint, decode, NetworkItem, encode, JSONtoTextParser, ClientStatus, Permission, NetworkSlot
from worlds import network_data_package, AutoWorldRegister, undertale
from MultiServer import mark_raw
from CommonClient import gui_enabled, get_base_parser, ClientCommandProcessor, CommonContext, server_loop, \
    gui_enabled, console_loop, ClientCommandProcessor, logger, get_base_parser, keep_alive, server_autoreconnect, \
    process_server_cmd


class UndertaleCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx):
        super().__init__(ctx)

    def _cmd_resync(self):
        """Manually trigger a resync."""
        if isinstance(self.ctx, UndertaleContext):
            self.output(f"Syncing items.")
            self.ctx.syncing = True

    def _cmd_patch(self):
        """Patch the game."""
        if isinstance(self.ctx, UndertaleContext):
            bsdiff4.file_patch_inplace(os.getcwd() + r"/Undertale/data.win", undertale.data_path("patch.bsdiff"))
            self.output(f"Patched.")

    @mark_raw
    def _cmd_auto_patch(self, steaminstall: str):
        """Patch the game automatically."""
        if isinstance(self.ctx, UndertaleContext):
            for file_name in os.listdir(steaminstall+"\\steamapps\\common\\Undertale\\"):
                if file_name != "steam_api.dll":
                    copier(steaminstall+'\\steamapps\\common\\Undertale\\'+file_name, os.getcwd() +"\\Undertale\\"+file_name)
            bsdiff4.file_patch_inplace(os.getcwd() + r"/Undertale/data.win", undertale.data_path("patch.bsdiff"))
            self.output(f"Patched.")

    def _cmd_online(self):
        """Makes you no longer able to see other Undertale players."""
        if isinstance(self.ctx, UndertaleContext):
            self.ctx.update_online_mode(not ("Online" in self.ctx.tags))
            if "Online" in self.ctx.tags:
                self.output(f"Now online.")
            else:
                self.output(f"Now offline.")

    def _cmd_deathlink(self):
        """Toggles deathlink"""
        if isinstance(self.ctx, UndertaleContext):
            self.ctx.deathlink_status = not self.ctx.deathlink_status
            if self.ctx.deathlink_status:
                self.output(f"Deathlink enabled.")
            else:
                self.output(f"Deathlink disabled.")


class UndertaleContext(CommonContext):
    tags = {"AP", "Online"}
    game = "Undertale"
    command_processor = UndertaleCommandProcessor
    items_handling = 0b111
    route = None
    pieces_needed = None
    progkeys = None
    completed_routes = None
    completed_count = 0

    def __init__(self, server_address, password):
        super().__init__(server_address, password)
        self.pieces_needed = 0
        self.game = 'Undertale'
        self.got_deathlink = False
        self.syncing = False
        self.deathlink_status = False
        self.tem_armor = False
        self.progkeys = []
        self.completed_count = 0
        self.completed_routes = {}
        self.completed_routes["pacifist"] = 0
        self.completed_routes["genocide"] = 0
        self.completed_routes["neutral"] = 0

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            self.game = self.slot_info[self.slot].game

    def clear_undertale_files(self):
        path = os.path.expandvars(r"%localappdata%/UNDERTALE")
        self.finished_game = False
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.find("check") > -1:
                    os.remove(root+"/"+file)
                elif file.find(".item") > -1:
                    os.remove(root+"/"+file)
                elif file.find(".victory") > -1:
                    os.remove(root+"/"+file)
                elif file.find(".route") > -1:
                    os.remove(root+"/"+file)
                elif file.find(".playerspot") > -1:
                    os.remove(root+"/"+file)
                elif file.find(".mad") > -1:
                    os.remove(root+"/"+file)
                elif file.find(".youDied") > -1:
                    os.remove(root+"/"+file)
                elif file.find(".LV") > -1:
                    os.remove(root+"/"+file)
                elif file.find("area") > -1:
                    os.remove(root+"/"+file)
                elif file.find(".mine") > -1:
                    os.remove(root+"/"+file)

    async def connection_closed(self):
        await super().connection_closed()
        self.clear_undertale_files()

    async def shutdown(self):
        await super().shutdown()
        self.clear_undertale_files()

    def update_online_mode(self, online):
        old_tags = self.tags.copy()
        if online:
            self.tags.add("Online")
        else:
            self.tags -= {"Online"}
        if old_tags != self.tags and self.server and not self.server.socket.closed:
            asyncio.create_task(self.send_msgs([{"cmd": "ConnectUpdate", "tags": self.tags}]))

    def on_package(self, cmd: str, args: dict):
        asyncio.create_task(process_undertale_cmd(self, cmd, args))

    def run_gui(self):
        from kvui import GameManager

        class UTManager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago Undertale Client"

        self.ui = UTManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")

    def on_deathlink(self, data: dict):
        self.got_deathlink = True
        super().on_deathlink(data)


def to_room_name(place_name: str):
    if place_name == "Old Home Exit":
        return "room_ruinsexit"
    elif place_name == "Snowdin Forest":
        return "room_tundra1"
    elif place_name == "Snowdin Town Exit":
        return "room_fogroom"
    elif place_name == "Waterfall":
        return "room_water1"
    elif place_name == "Waterfall Exit":
        return "room_fire2"
    elif place_name == "Hotland":
        return "room_fire_prelab"
    elif place_name == "Hotland Exit":
        return "room_fire_precore"
    elif place_name == "Core":
        return "room_fire_core1"


async def process_undertale_cmd(ctx: UndertaleContext, cmd: str, args: dict):
    if cmd == 'Connected':
        if not os.path.exists(os.path.expandvars(r"%localappdata%/UNDERTALE")):
            os.mkdir(os.path.expandvars(r"%localappdata%/UNDERTALE"))
        ctx.route = args["slot_data"]['route']
        ctx.pieces_needed = args["slot_data"]['key_pieces']
        ctx.tem_armor = args["slot_data"]['temy_armor_include']

        await ctx.send_msgs([{"cmd": "Get", "keys": [str(ctx.slot)+" RoutesDone neutral", str(ctx.slot)+" RoutesDone pacifist", str(ctx.slot)+" RoutesDone genocide"]}])
        await ctx.send_msgs([{"cmd": "SetNotify", "keys": [str(ctx.slot)+" RoutesDone neutral", str(ctx.slot)+" RoutesDone pacifist", str(ctx.slot)+" RoutesDone genocide"]}])
        print(ctx.slot)
        if not args["slot_data"]['key_hunt']:
            ctx.pieces_needed = 0
        if args["slot_data"]['rando_love']:
            filename = f"LOVErando.LV"
            with open(os.path.expandvars(r"%localappdata%/UNDERTALE/"+filename), 'w') as f:
                f.close()
        if args["slot_data"]['rando_stats']:
            filename = f"STATrando.LV"
            with open(os.path.expandvars(r"%localappdata%/UNDERTALE/"+filename), 'w') as f:
                f.close()
        filename = f"{ctx.route}.route"
        with open(os.path.expandvars(r"%localappdata%/UNDERTALE/"+filename), 'w') as f:
            f.close()
        for ss in ctx.checked_locations:
            filename = f"check {ss-12000}.spot"
            with open(os.path.expandvars(r"%localappdata%/UNDERTALE/"+filename), 'w') as f:
                f.close()
        filename = f"area0"
        with open(os.path.expandvars(r"%localappdata%/UNDERTALE/"+filename), 'w') as f:
            f.write(to_room_name(args["slot_data"]["Old Home Exit"]))
            f.close()
        filename = f"area1"
        with open(os.path.expandvars(r"%localappdata%/UNDERTALE/"+filename), 'w') as f:
            f.write(to_room_name(args["slot_data"]["Snowdin Town Exit"]))
            f.close()
        filename = f"area2"
        with open(os.path.expandvars(r"%localappdata%/UNDERTALE/"+filename), 'w') as f:
            f.write(to_room_name(args["slot_data"]["Waterfall Exit"]))
            f.close()
        filename = f"area3"
        with open(os.path.expandvars(r"%localappdata%/UNDERTALE/"+filename), 'w') as f:
            f.write(to_room_name(args["slot_data"]["Hotland Exit"]))
            f.close()
        filename = f"area0.back"
        with open(os.path.expandvars(r"%localappdata%/UNDERTALE/"+filename), 'w') as f:
            f.write(to_room_name(args["slot_data"]["Snowdin Forest"]))
            f.close()
        filename = f"area1.back"
        with open(os.path.expandvars(r"%localappdata%/UNDERTALE/"+filename), 'w') as f:
            f.write(to_room_name(args["slot_data"]["Waterfall"]))
            f.close()
        filename = f"area2.back"
        with open(os.path.expandvars(r"%localappdata%/UNDERTALE/"+filename), 'w') as f:
            f.write(to_room_name(args["slot_data"]["Hotland"]))
            f.close()
        filename = f"area3.back"
        with open(os.path.expandvars(r"%localappdata%/UNDERTALE/"+filename), 'w') as f:
            f.write(to_room_name(args["slot_data"]["Core"]))
            f.close()
        place = "Old Home Exit"
        ctx.progkeys.append(77777)
        while place != "Core Exit":
            if args["slot_data"][place] == "Snowdin Forest":
                if ctx.route == "pacifist" or ctx.route == "all_routes":
                    ctx.progkeys.append(77779)
                ctx.progkeys.append(77778)
                place = "Snowdin Town Exit"
            elif args["slot_data"][place] == "Waterfall":
                if ctx.route == "pacifist" or ctx.route == "all_routes":
                    ctx.progkeys.append(77780)
                ctx.progkeys.append(77781)
                place = "Waterfall Exit"
            elif args["slot_data"][place] == "Hotland":
                if ctx.route != "genocide":
                    ctx.progkeys.append(77783)
                    ctx.progkeys.append(77784)
                ctx.progkeys.append(77785)
                place = "Hotland Exit"
            elif args["slot_data"][place] == "Core":
                ctx.progkeys.append(77786)
                if ctx.route == "pacifist" or ctx.route == "all_routes":
                    ctx.progkeys.append(77782)
                place = "Core Exit"
    elif cmd == 'Retrieved':
        if str(ctx.slot)+" RoutesDone neutral" in args["keys"]:
            if args["keys"][str(ctx.slot)+" RoutesDone neutral"] is not None:
                ctx.completed_routes["neutral"] = args["keys"][str(ctx.slot)+" RoutesDone neutral"]
        if str(ctx.slot)+" RoutesDone genocide" in args["keys"]:
            if args["keys"][str(ctx.slot)+" RoutesDone genocide"] is not None:
                ctx.completed_routes["genocide"] = args["keys"][str(ctx.slot)+" RoutesDone genocide"]
        if str(ctx.slot)+" RoutesDone pacifist" in args["keys"]:
            if args["keys"][str(ctx.slot) + " RoutesDone pacifist"] is not None:
                ctx.completed_routes["pacifist"] = args["keys"][str(ctx.slot)+" RoutesDone pacifist"]
    elif cmd == 'SetReply':
        if args["value"] != None:
            if str(ctx.slot)+" RoutesDone pacifist" == args["key"]:
                ctx.completed_routes["pacifist"] = args["value"]
            elif str(ctx.slot)+" RoutesDone genocide" == args["key"]:
                ctx.completed_routes["genocide"] = args["value"]
            elif str(ctx.slot)+" RoutesDone neutral" == args["key"]:
                ctx.completed_routes["neutral"] = args["value"]
        print(args["key"])
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
            counter = -1
            while counter > -99:
                if os.path.exists(os.path.expandvars(r"%localappdata%/UNDERTALE/"+f"{str(counter)}PLR{str(ctx.slot)}.item")):
                    os.remove(os.path.expandvars(r"%localappdata%/UNDERTALE/"+f"{str(counter)}PLR{str(ctx.slot)}.item"))
                counter -= 1
            placedPlot = 0
            placedWeapon = 0
            placedArmor = 0
            for item in args['items']:
                id = NetworkItem(*item).location
                while NetworkItem(*item).location < 0 and \
                        os.path.isfile(os.path.expandvars(r"%localappdata%/UNDERTALE/"+f"{str(id)}PLR{str(NetworkItem(*item).player)}.item")):
                    id -= 1
                filename = f"{str(id)}PLR{str(NetworkItem(*item).player)}.item"
                with open(os.path.expandvars(r"%localappdata%/UNDERTALE/"+filename), 'w') as f:
                    if NetworkItem(*item).item == 77700:
                        f.write(str(int(ctx.progkeys[placedPlot])-11000))
                        placedPlot += 1
                    elif NetworkItem(*item).item == 77701:
                        if placedWeapon == 0:
                            f.write(str(77013-11000))
                        elif placedWeapon == 1:
                            f.write(str(77014-11000))
                        elif placedWeapon == 2:
                            f.write(str(77025-11000))
                        elif placedWeapon == 3:
                            f.write(str(77045-11000))
                        elif placedWeapon == 4:
                            f.write(str(77049-11000))
                        elif placedWeapon == 5:
                            f.write(str(77047-11000))
                        elif placedWeapon == 6:
                            if str(ctx.route) == "genocide" or str(ctx.route) == "all_routes":
                                f.write(str(77052-11000))
                            else:
                                f.write(str(77051-11000))
                        else:
                            f.write(str(77003-11000))
                        placedWeapon += 1
                    elif NetworkItem(*item).item == 77702:
                        if placedArmor == 0:
                            f.write(str(77012-11000))
                        elif placedArmor == 1:
                            f.write(str(77015-11000))
                        elif placedArmor == 2:
                            f.write(str(77024-11000))
                        elif placedArmor == 3:
                            f.write(str(77044-11000))
                        elif placedArmor == 4:
                            f.write(str(77048-11000))
                        elif placedArmor == 5:
                            if str(ctx.route) == "genocide":
                                f.write(str(77053-11000))
                            else:
                                f.write(str(77046-11000))
                        elif placedArmor == 6 and ((not str(ctx.route) == "genocide") or ctx.tem_armor):
                            if str(ctx.route) == "all_routes":
                                f.write(str(77053-11000))
                            elif str(ctx.route) == "genocide":
                                f.write(str(77064-11000))
                            else:
                                f.write(str(77050-11000))
                        elif placedArmor == 7 and ctx.tem_armor and not str(ctx.route) == "genocide":
                            f.write(str(77064-11000))
                        else:
                            f.write(str(77004-11000))
                        placedArmor += 1
                    else:
                        f.write(str(NetworkItem(*item).item-11000))
                    f.close()
                if id > -1:
                    ctx.items_received.append(NetworkItem(*item))
                if [item.item for item in ctx.items_received].count(77000) >= ctx.pieces_needed > 0:
                    filename = f"{str(-99999)}PLR{str(0)}.item"
                    with open(os.path.expandvars(r"%localappdata%/UNDERTALE/" + filename), 'w') as f:
                        f.write(str(77787 - 11000))
                        f.close()
                    filename = f"{str(-99998)}PLR{str(0)}.item"
                    with open(os.path.expandvars(r"%localappdata%/UNDERTALE/" + filename), 'w') as f:
                        f.write(str(77789 - 11000))
                        f.close()
        ctx.watcher_event.set()

    elif cmd == "RoomUpdate":
        if "checked_locations" in args:
            for ss in ctx.checked_locations:
                filename = f"check {ss-12000}.spot"
                with open(os.path.expandvars(r"%localappdata%/UNDERTALE/"+filename), 'w') as f:
                    f.close()

    elif cmd == "Bounced":
        tags = args.get("tags", [])
        if "DeathLink" in tags and ctx.last_death_link != args["data"]["time"]:
            ctx.on_deathlink(args["data"])
        elif "Online" in tags:
            data = args.get("data", [])
            if data["player"] != ctx.slot and data["player"] != None:
                filename = f"FRISK" + str(data["player"]) + ".playerspot"
                with open(os.path.expandvars(r"%localappdata%/UNDERTALE/" + filename), 'w') as f:
                    f.write(str(data["x"]) + str(data["y"]) + str(data["room"]) + str(
                        data["spr"]) + str(data["frm"]))
                    f.close()


async def multi_watcher(ctx: UndertaleContext):
    while not ctx.exit_event.is_set():
        path = os.path.expandvars(r"%localappdata%/UNDERTALE")
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.find("spots.mine") > -1 and "Online" in ctx.tags:
                    with open(root + "/" + file) as mine:
                        this_x = mine.readline()
                        this_y = mine.readline()
                        this_room = mine.readline()
                        this_sprite = mine.readline()
                        this_frame = mine.readline()
                        mine.close()
                    message = [{"cmd": 'Bounce', "tags": ["Online"],
                                "data": {"player": ctx.slot, "x": this_x, "y": this_y, "room": this_room,
                                         "spr": this_sprite, "frm": this_frame}}]
                    await ctx.send_msgs(message)
        await asyncio.sleep(0.02)


async def game_watcher(ctx: UndertaleContext):
    while not ctx.exit_event.is_set():
        await ctx.update_death_link(ctx.deathlink_status)
        path = os.path.expandvars(r"%localappdata%/UNDERTALE")
        if ctx.syncing == True:
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.find(".item") > -1:
                        os.remove(root+"/"+file)
            sync_msg = [{'cmd': 'Sync'}]
            if ctx.locations_checked:
                sync_msg.append({"cmd": "LocationChecks", "locations": list(ctx.locations_checked)})
            await ctx.send_msgs(sync_msg)
            ctx.syncing = False
        if ctx.got_deathlink:
            ctx.got_deathlink = False
            with open(os.path.expandvars(r"%localappdata%/UNDERTALE/WelcomeToTheDead.youDied"), 'w') as f:
                f.close()
        sending = []
        victory = False
        found_routes = 0
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.find("DontBeMad.mad") > -1 and "DeathLink" in ctx.tags:
                    os.remove(root+"/"+file)
                    await ctx.send_death()
                if file.find("check ") > -1:
                    st = file.split("check ", -1)[1]
                    st = st.split(".spot", -1)[0]
                    sending = sending+[(int(st))+12000]
                    message = [{"cmd": 'LocationChecks', "locations": sending}]
                    await ctx.send_msgs(message)
                if file.find("victory") > -1 and file.find(str(ctx.route)) > -1:
                    victory = True
                if file.find("victory") > -1:
                    if str(ctx.route) == "all_routes":
                        if file.find("neutral") > -1 and ctx.completed_routes["neutral"] != 1:
                            await ctx.send_msgs([{"cmd": "Set", "key": str(ctx.slot)+' RoutesDone neutral', "default": 0, "want_reply": True, "operations": [{"operation": "max", "value": 1}]}])
                        elif file.find("pacifist") > -1 and ctx.completed_routes["pacifist"] != 1:
                            await ctx.send_msgs([{"cmd": "Set", "key": str(ctx.slot)+' RoutesDone pacifist', "default": 0, "want_reply": True, "operations": [{"operation": "max", "value": 1}]}])
                        elif file.find("genocide") > -1 and ctx.completed_routes["genocide"] != 1:
                            await ctx.send_msgs([{"cmd": "Set", "key": str(ctx.slot)+' RoutesDone genocide', "default": 0, "want_reply": True, "operations": [{"operation": "max", "value": 1}]}])
        if str(ctx.route) == "all_routes":
            found_routes += ctx.completed_routes["neutral"]
            found_routes += ctx.completed_routes["pacifist"]
            found_routes += ctx.completed_routes["genocide"]
        if str(ctx.route) == "all_routes" and found_routes >= 3:
            victory = True
        ctx.locations_checked = sending
        if (not ctx.finished_game) and victory:
            await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
            ctx.finished_game = True
        await asyncio.sleep(0.1)


def copier(_src, _dst):
    if not os.path.exists(_src):
        return False

    _src_fp = open(_src, "rb")
    _dst_fp = open(_dst, "wb")

    line = _src_fp.readline()
    while line:
        _dst_fp.write(line)
        line = _src_fp.readline()
    _src_fp.close()
    _dst_fp.close()

    return True


if __name__ == '__main__':

    async def main(args):
        ctx = UndertaleContext(args.connect, args.password)
        ctx.auth = args.name
        ctx.server_address = args.connect
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")

        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        progression_watcher = asyncio.create_task(
            game_watcher(ctx), name="UndertaleProgressionWatcher")

        multiplayer_watcher = asyncio.create_task(
            multi_watcher(ctx), name="UndertaleMultiplayerWatcher")
        await ctx.exit_event.wait()
        await ctx.shutdown()
        await progression_watcher
        await multiplayer_watcher

    import colorama

    parser = get_base_parser(description="Undertale Client, for text interfacing.")
    parser.add_argument('--name', default=None, help="Slot Name to connect as.")
    parser.add_argument("url", nargs="?", help="Archipelago connection url")
    parser.add_argument('--install', '-i', dest='install', nargs='?', default="",
        help="Patch the vanilla game for randomization. Does not launch the client afterwards.")

    args = parser.parse_args()
    if args.install != "":
        logging.info("Patching Undertale")
        if os.path.exists(os.getcwd() + r"/Undertale"):
            path = os.getcwd() + r"/Undertale"
            for root, dirs, files in os.walk(path):
                for file in files:
                    os.remove(root+"/"+file)
            os.removedirs(os.getcwd() + r"/Undertale")
        if not os.path.exists(os.getcwd() + r"/Undertale"):
            os.mkdir(os.getcwd() + r"/Undertale")
        logging.info(args.install)
        copier(args.install+"/data.win", os.getcwd() + r"/Undertale/data.win")
        bsdiff4.file_patch_inplace(os.getcwd() + r"/Undertale/data.win", undertale.data_path("patch.bsdiff"))
        sys.exit(0)
    if not os.path.exists(os.getcwd() + r"/Undertale"):
        os.mkdir(os.getcwd() + r"/Undertale")

    if args.url:
        url = urllib.parse.urlparse(args.url)
        args.connect = url.netloc
        if url.username:
            args.name = urllib.parse.unquote(url.username)
        if url.password:
            args.password = urllib.parse.unquote(url.password)

    colorama.init()

    asyncio.run(main(args))
    colorama.deinit()
