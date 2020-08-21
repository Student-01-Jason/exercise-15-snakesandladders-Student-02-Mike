Feature: snakes and ladders

  Scenario Outline: move
    Given the game have a player in position <p>
    When the dice rolls out of <i>
    Then the player should move to <np>

    Examples: move
      | p | i | np |
      | 0 | 1 | 1  |
      | 0 | 2 | 16 |
      | 0 | 3 | 3  |
      | 1 | 1 | 16 |
      | 1 | 2 | 3  |
      | 1 | 3 | 4  |
      | 2 | 1 | 3  |
      | 2 | 2 | 4  |
      | 2 | 3 | 20 |
      | 8 | 2 | 10 |
      | 8 | 3 | 11 |
      | 8 | 4 | 25 |
      | 10 | 2 | 25 |
      | 10 | 3 | 13 |
      | 10 | 4 | 11 |

