import os
import time
import random
import copy
  
 
def load_data():
  with open('data.txt', 'r', encoding='utf-8') as df:
    words = [word for word in df]
  return words

def random_name():
  '''Pick up just a single word randomness from a list of words''' 
  random_word = random.choice(load_data())
  return random_word  # osó

def normalization():
  '''Remove accents to the random word'''
  normalizations = {'á':'a','é':'e','í':'i','ó':'o','ú':'u'}
  random_word = random_name()
  for index, letter in enumerate(list(random_word)):
    if letter in normalizations.keys():
      list(random_word)[index] = normalizations[letter]  
  return random_word, list(random_word) # 'osó', 'o s o'

def word2lines():   
  ''' Convert a word to a line of lines '''
  norm_word, norm_word_s = normalization() 
  for idx in range(len(norm_word)):
    norm_word_s[idx] = '_'
  return norm_word, norm_word_s # 'oso' --> _ _ _ 

def line2letter(letter, word): # a --> ['o','s','o']
  ''' Verifica si la letra esta en la palabra y la coloca, si no; deja el cambio anterior '''
  
  tidx = [] # letter is in word 
  fidx = []  # letter is not in word
  if letter in word:
    tidx.append(letter)
  else:
    fidx.append(letter)
  return tidx, fidx
  
def run():   
  try:
    start_option = int(input(print('Are you ready to playing hangman?\n 1. Yes, I\'m ready\n 2. I\'m later\n')))
  except TypeError:
    print('You can\'t enter letter, insert a integer option.') 
  assert (start_option == 1) or (start_option == 2), '{} does not exist!'. format(start_option)
  
  while start_option == 1:
    norm_word, hidden_word = word2lines() #oso, ['_','_','_']
    print('The word to guess is: {}'. format(hidden_word))
    n_lives = 5
    print('Number of lives {}'. format(n_lives))  
    while n_lives > 0:  
      letter = input(print('Insert a letter: '))
      tidx, fidx = line2letter(letter, norm_word)
      if letter in tidx:
        print('Good guessed')
        for i in range(len(tidx)):
          for j in range(len(norm_word)):
            if tidx[i] == list(norm_word)[j]:
              hidden_word[j] = tidx[i]
          print(hidden_word)
      else:
        print('{} is wrong'. format(letter))
        print('Remember wrong letters {}'.format(fidx))
        n_lives -= 1
        print('Lives = {}'.format(n_lives))
        
      if n_lives == 0:
        print('You have lost, the correct word is {}'. format(norm_word))
        continue_play = int(input(print('Do you play continue to playing?\n 1. Yes\n 2. No')))
        if continue_play == 1:
          start_option = 1
        else:
          start_option = 0   

if __name__ == '__main__':
  run()
