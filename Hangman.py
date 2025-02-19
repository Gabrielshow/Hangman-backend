import random

stages = ['''
  +---+
  |   |
  0   |
 /|\  |
 / \  |
      |
=======     
''', '''
  +---+
  |   |
  0   |
 /|\  |
 /    |
      |
=======     
''', '''
  +---+
  |   |
  0   |
 /|\  |
      |
      |
=======     
''','''
  +---+
  |   |
  0   |
 /|   |
      |
      |
=======     
''','''
  +---+
  |   |
  0   |
  |   |
      |
      |
=======     
''','''
  +---+
  |   |
  0   |
      |
      |
      |
=======     
''', '''
  +---+
  |   |
      |
      |
      |
      |
=======     
''']


class Hangman:
    def __init__(self):
        self.word_list = ['aardvark', 'camel', 'beans', 'rice', 'father', 'mother']
        self.start_new_game()
    
    def start_new_game(self):
        """Starts a new game by resetting the game state."""
        self.chosen_word = random.choice(self.word_list)
        self.word_length = len(self.chosen_word)
        self.display = ['_'] * self.word_length
        self.lives = 6
        self.end_of_game = False
        self.message = ''
    
    def get_display(self):
        """Returns the current word display and lives."""
        return {'display': ''.join(self.display), 'lives': self.lives, 'end_of_game': self.end_of_game, 'message': self.message}

    def guess(self, letter):
        """Handles guessing a letter."""
        if self.end_of_game:
            self.message = 'Game over. Start a new game.'
            return {'error': self.message}
        
        if len(letter) != 1 or not letter.isalpha():
            return {'error': 'Please provide a valid single letter.'}

        letter = letter.lower()

        if letter in self.chosen_word:
            # Update the display with correctly guessed letters
            for i in range(self.word_length):
                if self.chosen_word[i] == letter:
                    self.display[i] = letter

        else:
            self.lives -= 1

        # Check for game over or win condition
        if self.lives == 0:
            self.end_of_game = True
            return {'message': 'You lost! The word was ' + self.chosen_word, 'display': ''.join(self.display), 'lives': self.lives}
        
        if "_" not in self.display:
            self.end_of_game = True
            self.message = 'You win!'
            return self.get_display()
        
        return self.get_display()
