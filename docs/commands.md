# Commands
To execute a command, the user must send a whisper to the Autonomous Node hosting the RPG server.

| Command | Implemented? | Description |
| ------- | --------- |  ----------- |
| Inspect *object* | **Yes** | Inspect a specified person or object. |
| Attack *object* | **Yes** | Attack a specified person or object. Cannot select self. |
| Equip *item* | **Yes** | Equip a weapon or armor, if it's currently in your inventory |
| Unequip *item* | **Yes** | Unequip a weapon or armor if it's currently equipped |
| Move [NESW] | **Yes** | Move North, East, South, or West in the current room if there's another room in that direction |
| Inventory | **Yes** | View your inventory |
| Stats | **Yes** | View your stats |
| Take *item* | **Yes** |Take an item from the environment, if it exists |
| Open *object*/[NESW] | **Yes** | Open NESW door or an object, if it exists and is openable |
| Close *object*/[NESW] | **Yes** | Close NESW door or an object, if it exists and is openable |
| Join | No | Join the system; if the player has a character already, that character is resumed, otherwise the New Character wizard starts |
| Quit | No | Leave the system. The character will remain in place for five rounds before it is removed. |
| Use *item* on *object* | No | Use an item on an object |
| Give *item* to *object* | No | Give an item to an object, such as a chest or another player |
