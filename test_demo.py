import unittest
from demo import *


class TestDemo(unittest.TestCase):

    def test_move(self):
        game = Game()
        player = Player(1, 0)
        game.join(player)

        #TODO
