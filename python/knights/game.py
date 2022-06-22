#!/usr/local/env python3
import random
from collections import UserDict

"""
Six knights start a game.
Each one has 100 health points.
Moves are made in clockwise order.
Every knight hits the next one for a random number of health points
(between 1 and 6).
When a knight loses all his life points, he dies and is excluded from the game.
The winner is the last surviving knight.

K1 hits K2 for 5
K2 hits K3 for 3
…
K1 hits K2 for 6
K2 dies
…
K4 hits K5 for 5
K4 wins
"""


deleted_knights = []


class Knights(UserDict):
    def remove_points(self, knight, points):
        self.data[knight] -= points

    def __delitem__(self, knight: str = None) -> None:
        print(f"{knight} dies")
        deleted_knights.append(knight)
        del self.data[knight]


knights = Knights({})


# Create the six knights (you can create the knights that you need)
for i in range(1, 7):
    knights[f"K{i}"] = 100


def knights_game(knights: UserDict = ({})) -> str:
    lenght = len(knights)

    deleted_knights.clear()

    if not knights:
        return "No knights in the game."
    while len(deleted_knights) < (lenght - 1):
        knights_iterator = iter(knights.copy().keys())
        last_knight = next(knights_iterator)
        for knight in knights.copy().keys():

            if knight not in knights:
                continue

            health_points = random.randint(1, 6)

            if knight == list(knights.copy().keys())[-1]:
                print(f"{knight} hits {last_knight} for {health_points}")
                knights.remove_points(last_knight, health_points)

                if knights[last_knight] <= 0:
                    del knights[last_knight]
            else:
                next_knight = next(knights_iterator)
                knights.remove_points(next_knight, health_points)
                print(f"{knight} hits {next_knight} for {health_points}")

                if knights[next_knight] <= 0:
                    del knights[next_knight]

    return f"The winner is {list(knights.keys())[0]}"


print(knights_game(knights))
