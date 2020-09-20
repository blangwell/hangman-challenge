from random import seed
from random import randint

word_bank = ['booger', 'ostrich', 'dinosaur', 'tweaker', 'hamburger', 'orange', 'television', 'fungus', 'tarantula', 'bulging']

# seed random number each time the script is run based on system time
seed()
# DONE display secret word as underscores
# 

class Game:
  def __init__(self):
    # get a word from a random index of word_bank
    self.word = list(word_bank[randint(0, len(word_bank) - 1)])
    self.game_over = True
    self.hangman = '-o-|-<'
    self.guesses = [] # display letters chosen by the player
    self.display = ['_'] * len(self.word) # generate a string/array the same len of self.word consisting only of underscores
    self.wrong_guesses = 0

  def __str__(self):
    # print current Game's word
    return f'''The secret word is {self.word} 
    its length is {len(self.word)}, 
    the game is displaying {self.display}, 
    its len is {len(self.display)}'''

  def take_turn(self):
    self.game_over = False

    if self.game_over == False:
      guess = input('enter a letter\n')
      print(f'HERES THE TURN {guess}')
      # DONE replace underscore with correct guess at indeces found
      chars_found = [i for i in range(len(self.word)) if self.word[i] == guess]

      if chars_found:
        for i in range(len(chars_found)):
          index = chars_found[i]
          print('CHARS FOUND ', index)
          self.display[index] = guess
        print('UPDATED DISPLAY : ', self.display)
        self.guesses.append(guess)
        print('GUESSES : ', self.guesses)
        if '_' not in self.display:
          self.game_over = False
          print('YOU WIN!')
        else:
          self.take_turn() # recursive call
      else:
        self.guesses.append(guess)
        self.wrong_guesses += 1
        print('wrong_guesses : {}'.format(self.wrong_guesses))
        if self.wrong_guesses >= 5:
          self.game_over = True
          print('Game Over!')
        else:
          self.take_turn()


new_game = Game()
print(new_game)
new_game.take_turn()