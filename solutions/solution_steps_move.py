from behave import *
from demo import *


@Given('the game have a player in position {p:d}')
def step_impl(context, p):
    game = Game()
    player = Player(1, p)
    game.join(player)
    context.player = player


@When('the dice rolls out of {i:d}')
def step_impl(context, i):
    context.i = i


@Then('the player should move to {np:d}')
def step_impl(context, np):
    new_position = context.player.move(context.i)
    assert new_position == np
