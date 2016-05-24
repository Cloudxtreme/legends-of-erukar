# pyna-rpg  [![Code Climate](https://codeclimate.com/github/etkirsch/pyna-rpg/badges/gpa.svg)](https://codeclimate.com/github/etkirsch/pyna-rpg) [![Build Status](https://travis-ci.org/etkirsch/pyna-rpg.svg?branch=master)](https://travis-ci.org/etkirsch/pyna-rpg)
A silly mesh-chat/pyna-colada RPG node very loosely based on d20 RPG rulesets

## Mechanics
For the time being, Pyna-RPG uses a simplified Dungeons and Dragons stat system by doing away with mental stats.

### Attributes
The following attributes range from -2 (base) to 10 (maximum). On creation, a player has 6 points to allocate to whichever stats he deems necessary.

* **Strength**: Influences damage dealt
* **Dexterity**: Influences armor, initiative, and attack rolls
* **Vitality**: Influences health gained per level

### Life and Death

The player's health is dependent on his level and vitality using the equation.

```python
player.health = (4 + player.vitality) * player.level
```

This is a roguelike. When the player dies, he is done for good. When the character receives a killing blow he entires the "dying" status and will become incapacitated. After three rounds in this state, the player will die outright. Other players will have the option to use a medical kit on him for revival. A single attack on a "dying" character is called a "coup de grace" and will instantaneously kill that character.

## Commands
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

## Character Progression
A player's level progression is directly tied to his net wealth. That is to say that the more items and money the player has the higher level he is. Item worth, however, is some scalar value less than the absolute value, as shown in the following equation.

```python
# Where SCALAR is a diminishing returns function of player level from 0.9 at level 0 to 0.5 at the maximum player level
# TODO: Add decay with asymptote of 0.5. Half-life should be set to yield slightly longer than 0.5 decay.
SCALAR = 0.9 - player.level*(0.9 / max_player_level)

player.net_worth = player.money + SCALAR*sum(player.inventory.value)
```

This effectively creates a tradeoff between purchasing items and having levels, as you can decrease in levels due to buying items.
