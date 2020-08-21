import unittest
from demo import *


class TestDemo(unittest.TestCase):

    def test_move(self):
        game = Game()
        player = Player(1, 0)
        game.join(player)

        player.position = 0
        self.assertEqual(player.move(1), 1)
        player.position = 0
        self.assertEqual(player.move(2), 16)
        player.position = 0
        self.assertEqual(player.move(3), 3)
        player.position = 1
        self.assertEqual(player.move(1), 16)
        player.position = 1
        self.assertEqual(player.move(2), 3)
        player.position = 1
        self.assertEqual(player.move(3), 4)
        player.position = 2
        self.assertEqual(player.move(1), 3)
        player.position = 2
        self.assertEqual(player.move(2), 4)
        player.position = 2
        self.assertEqual(player.move(3), 20)
