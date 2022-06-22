import unittest

from game import knights_game, Knights


class GameTest(unittest.TestCase):
    def test_empty_game(self):
        response = knights_game()
        self.assertEqual(response, "No knights in the game.",
                         "Message on empty test not expected")

    def test_game_1_knight(self):
        knights = Knights({"K1": 20})
        response = knights_game(knights)
        self.assertEqual(response, "The winner is K1",
                         "Message on 1 knight not expected")

    def test_game_6_knights(self):
        knights = Knights({})

        for i in range(1, 7):
            if i == 5:
                knights[f"K{i}"] = 1000
            else:
                knights[f"K{i}"] = 10
        response = knights_game(knights)
        self.assertEqual(response, "The winner is K5",
                         "Message on 6 knights not expected")

    def test_game_20_knights(self):
        knights = Knights({})

        for i in range(1, 21):
            if i == 10:
                knights[f"K{i}"] = 1000
            else:
                knights[f"K{i}"] = 10
        response = knights_game(knights)
        self.assertEqual(response, "The winner is K10",
                         "Message on 20 knights not expected")


if __name__ == "__main__":
    unittest.main()
