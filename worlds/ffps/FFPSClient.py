from __future__ import annotations

import Utils

if __name__ == "__main__":
    Utils.init_logging("ffpsClient", exception_logger="Client")

from CommonClient import *
from worlds import ffps
import bsdiff4


class FFPSCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: CommonContext):
        super().__init__(ctx)

    def _cmd_resync(self):
        """Manually trigger a resync."""
        self.output(f"Syncing items.")
        self.ctx.syncing = True

    def _cmd_patch(self):
        """Patch the vanilla game."""
        os.makedirs(name=Utils.user_path("FFPS Game"), exist_ok=True)
        with open(Utils.user_path("FFPS Game", "Pizzeria Simulator.exe"), "rb") as f:
            patchedFile = bsdiff4.patch(f.read(), ffps.data_path("patch.bsdiff"))
        with open(Utils.user_path("FFPS Game", "FFPS Mod.exe"), "wb") as f:
            f.write(patchedFile)
        self.output(f"Done!")

    def _cmd_toggle_jumpscares(self):
        """Disable or enable all jumpscares."""
        path = os.path.expandvars("%appdata%/MMFApplications/FNAF6")
        scare_set_to = "0"
        if os.path.exists(path):
            with open(path, "r") as f:
                lines = f.read()
                f.close()
            with open(path, "w") as f:
                if lines.__contains__("skipScare=1"):
                    lines = lines.replace("skipScare=1",
                                          "skipScare=0")
                    self.output(f"Jumpscares enabled")
                    scare_set_to = "0"
                elif lines.__contains__("skipScare=0"):
                    lines = lines.replace("skipScare=0",
                                          "skipScare=1")
                    self.output(f"Jumpscares disabled")
                    scare_set_to = "1"
                f.writelines(lines)
                f.close()
        path = os.path.expandvars("%appdata%/MMFApplications/FNAF6BOUGHT")
        if os.path.exists(path):
            with open(path, "r") as f:
                lines = f.read()
                f.close()
            with open(path, "w") as f:
                lines = lines.replace("skipScare=1",
                                      "skipScare=" + scare_set_to)
                lines = lines.replace("skipScare=0",
                                      "skipScare=" + scare_set_to)
                f.writelines(lines)
                f.close()
        else:
            with open(path, "w") as f:
                f.write("skipScare=" + scare_set_to)
                f.close()


class FFPSContext(CommonContext):
    command_processor: int = FFPSCommandProcessor
    game = "FFPS"
    items_handling = 0b111  # full remote

    def __init__(self, server_address, password):
        super().__init__(server_address, password)
        self.syncing = False
        self.max_anim = 4
        self.difficulty = 0
        self.easier_money_grinding = 0
        self.recieved_stages = 0
        self.recieved_cups = 0
        self.recieved_speakers = 0
        self.recieved_maxmoney = 0
        self.wallet_money = False
        self.night_select = 0
        self.maxm = 999999
        self.game = 'FFPS'

    def on_package(self, cmd: str, args: dict):
        asyncio.create_task(process_ffps_cmd(self, cmd, args))

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def run_gui(self):
        from kvui import GameManager

        class UTManager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago FFPS Client"

        self.ui = UTManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")


async def not_in_use(filename):
    try:
        os.rename(filename, filename)
        return True
    except:
        return False


async def process_ffps_cmd(ctx: FFPSContext, cmd: str, args: dict):
    if cmd == 'Connected':
        ctx.max_anim = args["slot_data"]["max_anim_appears"]
        ctx.difficulty = args["slot_data"]["night_difficulty"]
        ctx.wallet_money = False
        ctx.night_select = args["slot_data"]["day_sanity"]
        ctx.easier_money_grinding = args["slot_data"]["easier_money_grinding"]
        if args["slot_data"]["wallet_sanity"]:
            ctx.maxm = 25
        if args["slot_data"]["full_wallet"]:
            ctx.wallet_money = True
        path = os.path.expandvars("%appdata%/MMFApplications/FNAF6")
        if not os.path.exists(path):
            with open(path, "w") as f:
                f.write("[FNAF6]\n")
                f.write("stage=0\n")
                f.write("cups=0\n")
                f.write("speakers=0\n")
                f.write("money=100\n")
                f.write("moneytoget=0\n")
                f.write("maxmoney=" + str(ctx.maxm) + "\n")
                f.write("skipScare=0\n")
                f.write("diffap=" + str(ctx.difficulty) + "\n")
                f.write("nightselect=" + str(ctx.night_select) + "\n")
                f.close()
        else:
            with open(path, "r") as f:
                lines = f.read()
                f.close()
            with open(path, "r") as f:
                linesorganized = f.readlines()
                f.close()
            while True:
                try:
                    with open(path, "w") as f:
                        maxm_file = "999999"
                        for itm in linesorganized:
                            if itm.startswith("maxmoney="):
                                maxm_file = itm.removeprefix("maxmoney=").strip()
                        lines = lines.replace("maxmoney=" + maxm_file,
                                              "maxmoney=" + str(ctx.maxm))
                        lines = lines.replace("diffap=0",
                                              "diffap=" + str(ctx.difficulty))
                        lines = lines.replace("diffap=1",
                                              "diffap=" + str(ctx.difficulty))
                        lines = lines.replace("skipScare=1",
                                              "skipScare=0")
                        lines = lines.replace("nightselect=1",
                                              "nightselect=" + str(ctx.night_select))
                        lines = lines.replace("nightselect=0",
                                              "nightselect=" + str(ctx.night_select))
                        f.writelines(lines)
                        f.close()
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
            if os.path.exists(os.path.expandvars("%appdata%/MMFApplications/FNAF6")):
                while True:
                    try:
                        ctx.recieved_stages = 0
                        ctx.recieved_speakers = 0
                        ctx.recieved_cups = 0
                        received_money = 0
                        ctx.recieved_maxmoney = 0
                        with open(os.path.expandvars("%appdata%/MMFApplications/FNAF6"), 'r+') as f:
                            lines = f.read()
                            for item in args['items']:
                                item_got = ffps.item_table[
                                    ffps.FFPSWorld.item_id_to_name[NetworkItem(*item).item]].setId
                                if (lines.count("m2") + lines.count("m3") + lines.count("m4") + lines.count("m5")) < \
                                        ctx.max_anim and \
                                        (item_got == "m2" or item_got == "m3" or item_got == "m4" or item_got == "m5"):
                                    f.write(str(item_got) + "=1\n")
                                if not item_got == "m2" and not item_got == "m3" and not item_got == "m4" \
                                        and not item_got == "m5" and not item_got == "speakers" \
                                        and not item_got == "cups" and not item_got == "stage" \
                                        and not item_got == "money" and not item_got == "maxmoney":
                                    f.write(str(item_got) + "=1\n")
                            if not lines.__contains__("stage="):
                                f.write("stage=0\n")
                            if not lines.__contains__("cups="):
                                f.write("cups=0\n")
                            if not lines.__contains__("speakers="):
                                f.write("speakers=0\n")
                            if not lines.__contains__("money="):
                                f.write("money=100\n")
                            if not lines.__contains__("moneytoget="):
                                f.write("moneytoget=0\n")
                            if not lines.__contains__("maxmoney="):
                                f.write("maxmoney=" + str(ctx.maxm) + "\n")
                            f.close()
                        with open(os.path.expandvars("%appdata%/MMFApplications/FNAF6"), "r") as file:
                            replacement = ""
                            for item in args['items']:
                                if ffps.item_table[ffps.FFPSWorld.item_id_to_name[NetworkItem(*item).item]].setId == \
                                        "stage":
                                    ctx.recieved_stages += 1
                                elif ffps.item_table[ffps.FFPSWorld.item_id_to_name[NetworkItem(*item).item]].setId == \
                                        "cups":
                                    ctx.recieved_cups += 1
                                elif ffps.item_table[ffps.FFPSWorld.item_id_to_name[NetworkItem(*item).item]].setId == \
                                        "speakers":
                                    ctx.recieved_speakers += 1
                                elif ffps.item_table[ffps.FFPSWorld.item_id_to_name[NetworkItem(*item).item]].setId == \
                                        "maxmoney":
                                    ctx.recieved_maxmoney += 1
                                    ctx.maxm = 25
                                    for i in range(ctx.recieved_maxmoney):
                                        ctx.maxm = ctx.maxm * 2
                                    if ctx.wallet_money:
                                        received_money += ctx.maxm
                                elif ffps.item_table[ffps.FFPSWorld.item_id_to_name[NetworkItem(*item).item]].setId == \
                                        "money":
                                    received_money += 250
                            for line in file:
                                line = line.strip()
                                if line.startswith("stage="):
                                    changes = "stage=" + str(ctx.recieved_stages)
                                elif line.startswith("cups="):
                                    changes = "cups=" + str(ctx.recieved_cups)
                                elif line.startswith("speakers="):
                                    changes = "speakers=" + str(ctx.recieved_speakers)
                                elif line.startswith("maxmoney="):
                                    changes = "maxmoney=" + str(ctx.maxm)
                                elif line.startswith("moneytoget="):
                                    changes = "moneytoget=" + str(received_money)
                                else:
                                    changes = line
                                replacement = replacement + changes + "\n"
                            file.close()
                        lines_to_simplify = replacement.splitlines()
                        temp_lines = []
                        if lines_to_simplify.count("[FNAF6]") <= 0:
                            temp_lines.append("[FNAF6]\n")
                        for ln in lines_to_simplify:
                            if ln != "canWin=1":
                                if temp_lines.count(ln + "\n") <= 0:
                                    temp_lines.append(ln + "\n")
                        anim_count = 0
                        anim_gotten = []
                        for itm in ctx.items_received:
                            if ffps.item_table[ffps.FFPSWorld.item_id_to_name[itm.item]].setId not in anim_gotten and \
                                    (ffps.item_table[ffps.FFPSWorld.item_id_to_name[itm.item]].setId == "m2" or
                                     ffps.item_table[ffps.FFPSWorld.item_id_to_name[itm.item]].setId == "m3" or
                                     ffps.item_table[ffps.FFPSWorld.item_id_to_name[itm.item]].setId == "m4" or
                                     ffps.item_table[ffps.FFPSWorld.item_id_to_name[itm.item]].setId == "m5"):
                                anim_count += 1
                                anim_gotten.append(ffps.item_table[ffps.FFPSWorld.item_id_to_name[itm.item]].setId)
                        if anim_count >= 4 and lines_to_simplify.count("canWin=1") <= 0:
                            temp_lines.append("canWin=1\n")
                        lines_to_simplify = temp_lines
                        while True:
                            try:
                                with open(os.path.expandvars("%appdata%/MMFApplications/FNAF6"), "w") as f:
                                    f.writelines(lines_to_simplify)
                                    f.close()
                                break
                            except PermissionError:
                                continue
                        for item in args['items']:
                            ctx.items_received.append(NetworkItem(*item))
                        break
                    except PermissionError:
                        continue
        ctx.watcher_event.set()


async def game_watcher(ctx: FFPSContext):
    while not ctx.exit_event.is_set():
        if ctx.syncing:
            sync_msg = [{'cmd': 'Sync'}]
            if ctx.locations_checked:
                sync_msg.append({"cmd": "LocationChecks", "locations": list(ctx.locations_checked)})
            await ctx.send_msgs(sync_msg)
            ctx.syncing = False

        if os.path.exists(os.path.expandvars("%appdata%/MMFApplications/FNAF6")):
            while True:
                try:
                    with open(os.path.expandvars("%appdata%/MMFApplications/FNAF6"), 'r+') as f:
                        lines = f.read()
                        if not lines.__contains__("[FNAF6]"):
                            f.write("[FNAF6]\n")
                        if not lines.__contains__("stage="):
                            f.write("stage=0\n")
                        if not lines.__contains__("cups="):
                            f.write("cups=0\n")
                        if not lines.__contains__("speakers="):
                            f.write("speakers=0\n")
                        if not lines.__contains__("money="):
                            f.write("money=100\n")
                        if not lines.__contains__("moneytoget="):
                            f.write("moneytoget=0\n")
                        if not lines.__contains__("maxmoney="):
                            f.write("maxmoney=" + str(ctx.maxm) + "\n")
                        if not lines.__contains__("first="):
                            f.write("first=1\n")
                        if not lines.__contains__("night="):
                            f.write("night=1\n")
                        if not lines.__contains__("phase="):
                            f.write("phase=1\n")
                        if not lines.__contains__("skipScare="):
                            f.write("skipScare=0\n")
                        if not lines.__contains__("1play="):
                            f.write("1play=0\n")
                        if not lines.__contains__("2play="):
                            f.write("2play=0\n")
                        if not lines.__contains__("3play="):
                            f.write("3play=0\n")
                        if not lines.__contains__("4play="):
                            f.write("4play=0\n")
                        if not lines.__contains__("5play="):
                            f.write("5play=0\n")
                        if not lines.__contains__("6play="):
                            f.write("6play=0\n")
                        if not lines.__contains__("diffap="):
                            f.write("diffap=" + str(ctx.difficulty) + "\n")
                        if not lines.__contains__("nightselect="):
                            f.write("nightselect=" + str(ctx.night_select) + "\n")
                        if not lines.__contains__("n="):
                            f.write("n=2\n")
                        for itm in ffps.shop_table:
                            for var_type in ["atmosphere", "entertainment", "revenue", "liability", "health"]:
                                if not lines.__contains__(itm.setId + var_type + "="):
                                    f.write(itm.setId + var_type + "=" + str(getattr(itm, var_type)) + "\n")
                        f.close()
                    break
                except PermissionError:
                    continue
            must_write = False
            while True:
                wrte = []
                try:
                    with open(os.path.expandvars("%appdata%/MMFApplications/FNAF6"), 'r') as f:
                        filesread = f.readlines()
                        for itm in filesread:
                            if "1play=" in itm and itm[6] != "0" and ctx.easier_money_grinding:
                                wrte.append("1play=0\n")
                                must_write = True
                            elif "2play=" in itm and itm[6] != "0" and ctx.easier_money_grinding:
                                wrte.append("2play=0\n")
                                must_write = True
                            elif "3play=" in itm and itm[6] != "0" and ctx.easier_money_grinding:
                                wrte.append("3play=0\n")
                                must_write = True
                            elif "4play=" in itm and itm[6] != "0" and ctx.easier_money_grinding:
                                wrte.append("4play=0\n")
                                must_write = True
                            elif "5play=" in itm and itm[6] != "0" and ctx.easier_money_grinding:
                                wrte.append("5play=0\n")
                                must_write = True
                            elif "6play=" in itm and itm[6] != "0" and ctx.easier_money_grinding:
                                wrte.append("6play=0\n")
                                must_write = True
                            elif itm.startswith("money="):
                                if int(itm.removeprefix("money=").strip()) > ctx.maxm:
                                    wrte.append("money=" + str(ctx.maxm) + "\n")
                                    must_write = True
                                else:
                                    wrte.append(itm.strip() + "\n")
                            else:
                                wrte.append(itm.strip() + "\n")
                        f.close()
                    break
                except PermissionError:
                    continue
            if must_write:
                while True:
                    try:
                        with open(os.path.expandvars("%appdata%/MMFApplications/FNAF6"), 'w') as f:
                            for itm in wrte:
                                f.write(str(itm))
                            f.close()
                        break
                    except PermissionError:
                        continue
        path = os.path.expandvars("%appdata%/MMFApplications/FNAF6BOUGHT")
        sending = []
        victory = False
        if os.path.exists(path):
            while True:
                try:
                    with open(os.path.expandvars("%appdata%/MMFApplications/FNAF6"), 'r+') as f:
                        lines = f.read()
                        if not lines.__contains__("stage="):
                            f.write("stage=0\n")
                        if not lines.__contains__("cups="):
                            f.write("cups=0\n")
                        if not lines.__contains__("speakers="):
                            f.write("speakers=0\n")
                        if not lines.__contains__("money="):
                            f.write("money=100\n")
                        if not lines.__contains__("moneytoget="):
                            f.write("moneytoget=0\n")
                        if not lines.__contains__("maxmoney="):
                            f.write("maxmoney=" + str(ctx.maxm) + "\n")
                        if not lines.__contains__("first="):
                            f.write("first=1\n")
                        if not lines.__contains__("night="):
                            f.write("night=1\n")
                        if not lines.__contains__("phase="):
                            f.write("phase=1\n")
                        if not lines.__contains__("skipScare="):
                            f.write("skipScare=0\n")
                        f.close()
                    break
                except PermissionError:
                    continue
            while True:
                try:
                    with open(path, 'r') as f:
                        filesread = f.read()
                        for name, data in ffps.location_table.items():
                            if data.setId == "stage" or data.setId == "cups" or data.setId == "speakers":
                                for i in range(int([int(s) for s in name.split() if s.isdigit()][0]), 10):
                                    if data.setId + "=" + str(i) in filesread and not str(
                                            data.id) + "=sent" in filesread:
                                        sending = sending + [(int(data.id))]
                                        break
                            elif data.setId in filesread and data.setId != "" and not str(
                                    data.id) + "=sent" in filesread:
                                sending = sending + [(int(data.id))]
                        f.close()
                    break
                except PermissionError:
                    continue
            while True:
                try:
                    with open(path, 'r') as f:
                        sentread = f.read()
                        f.close()
                    with open(os.path.expandvars("%appdata%/MMFApplications/FNAF6"), 'r') as f:
                        filesread = f.readlines()
                        for data in ffps.money_table:
                            if not str(data.id) + "=sent" in sentread:
                                for itm in filesread:
                                    if "CS=" in itm:
                                        if itm.index("CS=") == 0:
                                            if data.amount <= int(itm.replace("CS=", "").strip()):
                                                sending = sending + [(int(data.id))]
                        f.close()
                    break
                except PermissionError:
                    continue
            while True:
                try:
                    with open(path, 'r+') as f:
                        f.read()
                        if not (not ctx.server or not ctx.server.socket.open or ctx.server.socket.closed):
                            for itm in sending:
                                f.write(str(itm) + "=sent\n")
                        f.close()
                    break
                except PermissionError:
                    continue
        path = os.path.expandvars("%appdata%/MMFApplications/VICTORYFFPS")
        if os.path.exists(path):
            while True:
                try:
                    with open(path, 'r+') as f:
                        filesread = f.readlines()
                        if filesread.__contains__("[FIN]\n") and filesread.__contains__("fin=1\n"):
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
    Utils.init_logging("FFPSClient", exception_logger="Client")

    async def _main():
        ctx = FFPSContext(None, None)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
        if not os.path.exists(os.getcwd() + "/FFPS Game"):
            os.mkdir(os.getcwd() + "/FFPS Game")

        asyncio.create_task(
            game_watcher(ctx), name="FFPSProgressionWatcher")

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
    parser = get_base_parser(description="FFPS Client, for text interfacing.")
    args = parser.parse_args()
    main()
