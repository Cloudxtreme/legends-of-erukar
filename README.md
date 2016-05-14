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
