import os
import time
import random  
 
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
  return random_word, list(random_word) # 'oso', ['o s o']

def word2lines():   
  ''' Convert a word to a line of lines '''
  norm_word, norm_word_s = normalization() 
  for idx in range(len(norm_word)):
    norm_word_s[idx] = '_'
  return norm_word, norm_word_s # 'oso' --> ['_','_','_'] 

def line2letter(letter, word):
  ''' Add letter to a list if is in word '''
  
  tidx = [] # add letter if is in word 
  if letter in word:
    tidx.append(letter)
  return tidx
  
def run():   
  try:
    start_option = int(input(print('Are you ready to playing hangman?\n 1. Yes, I\'m ready\n 2. I\'m later\n')))
  except:
    print('You can\'t enter letter, insert a integer option.') 
  assert (start_option == 1) or (start_option == 2), '{} does not exist!'. format(start_option)
  
  while start_option == 1:
    norm_word, hidden_word = word2lines() #'oso', ['_','_','_']
    n_lives = 5
    print('Number of lives {}'. format(n_lives))  
    os.system('clear')
    print('The word to guess is: {}'. format(hidden_word))
    fidx = []
    while n_lives > 0:
      letter = input(print('Insert a letter: '))
      tidx = line2letter(letter, norm_word)
      if letter in tidx:
        for i in range(len(tidx)):
          for j in range(len(norm_word)):
            if tidx[i] == list(norm_word)[j]:
              hidden_word[j] = tidx[i]
          print('Processing...')
          print('Congrat!, {} is in word'. format(letter))
          time.sleep(2)
          os.system('clear')
          print('Lives = {}'. format(n_lives))
          print('Remember wrong letter inserted =', fidx)
          print(hidden_word)
      else:
        fidx.append(letter)
        print('{} is wrong'. format(letter))
        n_lives -= 1
        time.sleep(2)
        os.system('clear')
        print('Lives = {}'. format(n_lives))
        print('Remember wrong letter inserted = ',fidx)
        print(hidden_word) 
        
      if n_lives == 0:
        print('You have lost, the correct word is: {}'. format(norm_word))
        continue_play = int(input(print('Do you play continue to playing?\n 1. Yes\n 2. No')))
        if continue_play == 1:
          start_option = 1
        else:
          start_option = 0   

if __name__ == '__main__':
  print('**----- W E L C O M E    T O    H A N G M A N -----**')
  run()

#Lastly, we need to define winner function, that is when player guessed all letter
