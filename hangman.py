import os
import time
import random  
 
def load_data():
  with open('data.txt', 'r+', encoding='utf-8') as df:
    words = [word for word in df]
  return words

def random_name():
  '''Pick up just a single word randomness from a list of words''' 
  random_word = random.choice(load_data())
  return random_word

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
  return norm_word, norm_word_s

'''def line2letter(letter, word):
  Add letter to a list if is in word
  
  tidx = [] # add letter if is in word 
  if letter in word:
    tidx.append(letter)
  return tidx'''
  
def main():   
  try:
    start_option = int(input('Are you ready to playing hangman?\n 1. Yes, I\'m ready\n 2. I\'m later\n Enter you option: '))
    assert (start_option == 1) or (start_option == 2), f'{start_option} does not exist!'
  except ValueError:
    print('You can\'t enter letter, insert a integer option.') 
  
  while start_option == 1:
    norm_word, hidden_word = word2lines()
    n_lives = 5
    print(f'Number of lives {n_lives}')  
    os.system('clear')
    print(f'The word to guess is: {hidden_word}') 
    fidx = []
  
    while n_lives > 0:
      letter = input('Insert a letter: ')
      tidx = []
      if letter in norm_word:
        tidx.append(letter)
        for i in range(len(tidx)):
          for j in range(len(norm_word)):
            if tidx[i] == list(norm_word)[j]:
              hidden_word[j] = tidx[i]
          print(f'Great!, {letter} is in word')
          time.sleep(2)
          os.system('clear')
          print(f'Lives = {n_lives}')
          print('Remember wrong letter inserted =', fidx)
          print(hidden_word[:-1])
          if not '_' in hidden_word[:-1]:
            print('You have won!')
            try: 
              continue_play = int(input('Do you play continue to playing?\n 1. Yes\n 2. No\n Enter your option: ' ))
            except ValueError:
              print('You can\'t enter letters')
            if continue_play == 1:
              continue
            else:
              break #bug              
          
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
        print(f'You have lost, the correct word is: {norm_word}')
        try: 
          continue_play = int(input('Do you play continue to playing?\n 1. Yes\n 2. No\n Enter your option: ' ))
        except ValueError:
          print('You can\'t enter letters')
        if continue_play == 1:
          start_option = 1
        else:
          break   
   

if __name__ == '__main__':
  main()
  print('**----- W E L C O M E    T O    H A N G M A N -----**')

