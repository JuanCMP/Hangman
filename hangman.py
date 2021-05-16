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
  norm_word = ''.join(split_word)
  return norm_word

def word2lines(norm_word):
  '''Convert a word to a line of lines'''
  dotted_word = list(norm_word)
  for index, letter in enumerate(dotted_word):
    dotted_word[index] = '_'
  return dotted_word, word

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

def number_lives(live):
  if live != 0:
    return print('The letter is wrong, try again \n You have {} lives'.format(live))
  else:
    return print('You have lost!')

def run():
  
  start_option = int(input(print('Are you ready to playing hangman?\n\t1. Yes, I\'m ready\n\t2. I\'m later\n')))
  assert (start_option == 1) or (start_option == 2), str(start_option) +' does not exist!'
  
  if start_option == 2:
    print('Bye!')
    time.sleep(1)
    os.system('clear')
  else:
    print('Let\'s get start!')
    for live in range(5, 0, -1):
      print('You have ' + str(live) + ' lives. Keep safe always!')
      dotted_word, word = word2lines(normalization(random_name(load_data())))
      print('The word is:\n', dotted_word)
      guess_word = input(print('Insert a letter: '))
      
      if guess_word in word:
        lines2word(guess_word, word)
        
      else:
        number_lives(live)
        if live == 0:
          break

if __name__ == '__main__':
  run()
