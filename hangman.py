class hangman:
  import os
  import time
  import random
  # object = player
  
  def __init__(self, lives = 5):
    self.lives = lives
  
  def load_data(self):
    with open(data.txt, 'r', encoding='utf-8') as df:
      words = [word for word in df]

  def random_name(self):
    '''Pick up just a word randomness from a list of words''' 
    word = random.choice(self.load_data())
    sep_word = list(word)
    return word, sep_word

  def normalization(self):
    '''Quit acents to the random word'''

    normalizations = {'á':'a','é':'e','í':'i','ó':'o','ú':'u'}
    word, sep_word_norm = self.random_name()
    for index, letter in enumerate(sep_word_norm):
      if letter in normalizations.keys():
        sep_word_norm[index] = normalizations[letter]
    return sep_word_norm, word

  def word2lines(self):
    '''Convert a word to a line of lines'''
    sep_word_norm, word = self.normalizations()
    for index, letter in enumerate(sep_word_norm):
      sep_word_norm[index] = '_'
    return sep_word_norm, word # [_ _ _], 'oso'

  def lines2word(self, letter):
    '''Put letter in the dotted space if letter is in word.
    ex 1: word:'c a m i l a' ---> _ _ _ _ _ _  --> _ a _ _ _ a
    ex 2: word: ---> 'o s o' ---> o __ o 
    '''
    word_line, word = self.word2lines()
    sep_word, _ = self.normalization()
    for index, l in enumerate(sep_word):
      if letter == l:
        word_line[index] = l
    return word_line

  def run():   
    try:
      start_option = int(input(print('Are you ready to playing hangman?\n\t1. Yes, I\'m ready\n\t2. I\'m later\n')))
    except TypeError:
      print('You can\'t enter letter, insert a integer option.') 
    assert (start_option == 1) or (start_option == 2), '{} does not exist!'. format(start_option)
    
    
    while start_option == 1:
      n_lives = 5
      print('Number of lives {}'. format(n_lives))
      dotted_word, word = word2lines(normalization(random_name(load_data())))
      print('The word to guess is: {}'. format(dotted_word))
      
      while n_lives > 0:  
        letter = input(print('Insert a letter: '))
        guessed_letter = lines2word(letter, word)
        print(guessed_letter) # retorne un nuevo tablero colocando la(s) letra(s) en tablero si fue verdadero
        if letter in list(word):
          print('Congrat, you have guessed a new letter')  
        else:
          n_lives -= 1
          print('The letter {} does not exist, you now have {} lives'. format(letter, n_lives))
        # Bug 1: El problema de la app es que no me guarda los cambios de las letras que ya se adivinaron.
        # Bug 2. Genera un '_' adicional a la palabra a adivinar
        # Bug 3. Al inicio me genera un 'None' que precede al input
      
      print('The correct word is: {}'. format(word))
      continue_p = int(input(print('Would you like to continue playing?\n 1. Yes\n 2. No')))
      if continue_p == 2:
        start_option = 0
      else:
        start_option = 1






    
 

if __name__ == '__main__':
  run()
