# pyna-rpg
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

This is a roguelike. When the player dies, he is done for good.

## Commands
To execute a command, the user must send a whisper to the Autonomous Node hosting the RPG server.

| Command | Description |
| ------- | ----------- |
| Inspect *object* | Inspect a specified person or object. |
| Attack *object* | Attack a specified person or object. Cannot select self. |
| Equip *item* | Equip a weapon or armor, if it's currently in your inventory |
| Unequip *item* | Unequip a weapon or armor if it's currently equipped |
| Move [NESW] | Move North, East, South, or West in the current room if there's another room in that direction |
| Inventory | View your inventory |
| Stats | View your stats |
| Take *item* | Take an item from the environment, if it exists |
| Open *object*/[NESW] | Open NESW door or an object, if it exists and is openable |
| Close *object*/[NESW] | Close NESW door or an object, if it exists and is openable |
| Use *item* on *object* | Use an item on an object |
| Give *item* to *object* | Give an item to an object, such as a chest or another player |
