"""Roll dice"""

import random


def roll_dice(num_dice=1, sides=6):
    """Roll dice and return the sum and individual rolls."""
    rolls = [random.randint(1, sides) for _ in range(num_dice)]
    return sum(rolls), rolls
