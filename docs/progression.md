# Character Progression
A player's level progression is directly tied to his net wealth. That is to say that the more items and money the player has the higher level he is. Item worth, however, is some scalar value less than the absolute value, as shown in the following equation.

```python
# Where SCALAR is a diminishing returns function of player level from 0.9 at level 0 to 0.5 at the maximum player level
# TODO: Add decay with asymptote of 0.5. Half-life should be set to yield slightly longer than 0.5 decay.
SCALAR = 0.9 - player.level*(0.9 / max_player_level)

player.net_worth = player.money + SCALAR*sum(player.engine.inventory.value)
```

This effectively creates a tradeoff between purchasing items and having levels, as you can decrease in levels due to buying items.
