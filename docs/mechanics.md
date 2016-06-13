# Mechanics
For the time being, Pyna-RPG uses a simplified Dungeons and Dragons stat system by doing away with mental stats.

### Attributes
The following attributes range from -2 (base) to 10 (maximum). On creation, a player has 6 points to allocate to whichever stats he deems necessary.

* **Strength**: Influences damage dealt
* **Dexterity**: Influences armor, initiative, and attack rolls
* **Vitality**: Influences health gained per level
* **Acuity**: Influences skill checks involving observation and investigation

### Life and Death

The player's health is dependent on his level and vitality using the equation.

```python
player.health = (4 + player.vitality) * player.level
```

This is a roguelike. When the player dies, he is done for good. When the character receives a killing blow he entires the "dying" status and will become incapacitated. After three rounds in this state, the player will die outright. Other players will have the option to use a medical kit on him for revival. A single attack on a "dying" character is called a "coup de grace" and will instantaneously kill that character.
