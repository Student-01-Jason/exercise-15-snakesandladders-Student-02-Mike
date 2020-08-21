import random


class Game:
    def __init__(self):
        self.grid = 36
        self.ladders = {12: 25, 2: 16, 5: 20, 19: 31}
        self.snakes = {35: 23, 28: 21, 22: 15, 14: 11}
        self.players = []

    def join(self, player):
        player.game = self
        self.players.append(player)

    def start(self):
        while (True):
            for player in self.players:
                step = player.dice()
                player.move(step)
                print('{} now is in {}'.format(player.id, player.position))
                if player.win():
                    print('The winner is {}'.format(player.id))
                    return
            print('==================')


class Player:
    def __init__(self, id, position):
        self.id = id
        self.position = position

    def dice(self):
        return random.randint(1, 6)

    def move(self, step):
        self.position += step
        for bottom, top in self.game.ladders.items():
            if self.position == bottom:
                self.position = top
        for head, tail in self.game.snakes.items():
            if self.position == head:
                self.position = tail
        return self.position

    def win(self):
        if self.position >= self.game.grid:
            return True
        else:
            return False


game = Game()
game.join(Player(1, 0))
game.join(Player(2, 0))
game.join(Player(3, 0))
game.start()
