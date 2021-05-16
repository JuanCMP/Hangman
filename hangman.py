import os
import time
import random

def load_data():
  '''Load data and return a list of words without normalization. 
  '''
  words = []
  with open('data.txt', 'r', encoding='utf-8') as df:
    for word in df:
      words.append(word)
  return words

def random_name(words):
  '''Pick up just a word randomness from a list of words''' 
  word = random.choice(words)
  return word

def normalization(random_word):
  '''Verify that the word is written in correct form; if not 
  apply normalization (change tilde to without it)'''
  normalizations = {'á':'a','é':'e','í':'i','ó':'o','ú':'u'}
  norm_word = list(random_word)
  for index, letter in enumerate(norm_word):
    if letter in normalizations.keys():
      norm_word[index] = normalizations[letter]
  norm_word = ''.join(norm_word)
  return norm_word

def word2lines(norm_word):
  '''Convert a word to a line of lines'''
  dotted_word = list(norm_word)
  for index, letter in enumerate(dotted_word):
    dotted_word[index] = '_'
  return dotted_word, norm_word

def lines2word(letter, word):
  '''Put letter in the dotted space if letter is in word.
  ex 1: word:'c a m i l a' ---> _ _ _ _ _ _  --> _ a _ _ _ a
  ex 2: word: ---> 'o s o' ---> o __ o 
   '''
  guessed_letter = list(word)
  for index, l in enumerate(guessed_letter):
    if letter == l:
      continue
    else:
      guessed_letter[index] = '_'
  return guessed_letter

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
      # Bug: El problema de la app es que no me guarda los cambios de las letras que ya se adivinaron.
    
    print('The correct word is: {}'. format(word))
    continue_p = int(input(print('Would you like to continue playing?\n 1. Yes\n 2. No')))
    if continue_p == 2:
      start_option = 0
    else:
      start_option = 1






    
 

if __name__ == '__main__':
  run()
