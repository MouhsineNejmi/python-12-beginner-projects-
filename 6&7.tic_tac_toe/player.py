import random

class Player:
  def __init__(self, letter):
    # letter is either x or o
    self.letter = letter

  # All the players should get their next move
  def get_move(self, game):
    pass

class RandomComputerPlayer(Player):
  def __init__(self, letter):
    super().__init__(letter)
  
  def get_move(self, game):
    # get a random valid spot
    square = random.choice(game.available_moves())
    return square

class HumanPlayer(Player):
  def __init__(self, letter):
    super().__init__(letter)
  
  def get_move(self, game):
    valid_square = False
    val = None
    while not valid_square:
      square = input(self.letter + '\'s turn. Input move (0-8):')
      try:
        val = int(square)
        if val not in game.available_moves():
          raise ValueError
        valid_square = True # if these are successful, then yay!
      except ValueError:
        print('Invalid square. Try again.')

    return val