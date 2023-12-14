# A Robot Named Fight Setup Guide

## Install manually

### Install BepInEx to the game client's folder

### Install the Archipelago Mod
Drop the Archipelago.ARobotNamedFight.dll and Archipelago.MultiClient.Net.dll files into the BepInEx\plugins folder within the A Robot Named Fight game client's folder.

### Configure the mod to connect to your server using an apconfig.xml file in the client folder
In a file named apconfig.xml, fill out the following fields:
 - url: The address and port where the server is hosted (default: archipelago.gg:38281)
 - slot: Your name in the multiworld. This is the name you entered in the YAML.

With this xml file in place, you will become connected to the Archipelago server once you start the game and select a file.  You should be able to use an existing or new file without issue.

## Running the Modded Game
Run the game from your Steam Library.

## Configuring your YAML File
### What is a YAML and why do I need one?
You can see the [basic multiworld setup guide](/tutorial/Archipelago/setup/en) here on the Archipelago website to learn 
about why Archipelago uses YAML files and what they're for.

### Where do I get a YAML?
You can use the [game settings page](/games/A%20Robot%20Named%20Fight/player-settings) here on the Archipelago 
website to generate a YAML using a graphical interface.

## Joining an Archipelago Session
### Connecting to server
The game client will automatically attempt to connect using the settings in the apconfig.xml file when you select one of the three save slots from the main screen.

Start the game whenever you are ready.

### Gameplay
Simply start any game mode that you configured in your YAML originally.  For example, if "Normal Included" was enabled, you can simply select "Normal" and "New Game"
from the menu.  If "Classic Boss Rush Included" was enabled, that can be found by going to "Seed" and then selecting "Classic Boss Rush" in the left column.

While playing A Robot Named Fight, any item that you pick up around the map that is not necessary for your own traversal will send a check out.  At that time, the timer
at the top center of the screen will pulse red with an "S:" followed by the name of the location that was checked (such as "Normal1") for about 2 seconds.

When your player receives an item from the server, the timer will instead pulse green with an "R:" followed by the item that was received (such as "HealthTank") for about 2 seconds.

In addition, any achievements that you earn will show a white message starting with "A:", instead of stopping your game to inform you of the unlock occurring.

If you die and must start over, don't worry!  Starting a new game will result in all of your previous locations checked already being marked off on the map, and you will receive
equivalent items for your current run for every item that was previously sent to you!

### Chat/Commands
There currently is no integration with the server from the game client.