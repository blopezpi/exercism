"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time: int=0) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time



def preparation_time_in_minutes(how_many_layers: int=1) -> int:
    """Calculate the preparation time in minutes.
    :param how_many_layers: int - number of layers to prepare.
    :return: int - preparation time in minutes.
    """
    return PREPARATION_TIME * how_many_layers


def elapsed_time_in_minutes(how_many_layers: int=1, elapsed_bake_time: int=1) -> int:
    """Calculate the elapsed time in minutes.
    :param how_many_layers: int - number of layers to prepare.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - elapsed time in minutes.
    """
    return elapsed_bake_time + preparation_time_in_minutes(how_many_layers)


print(elapsed_time_in_minutes(1, 3))