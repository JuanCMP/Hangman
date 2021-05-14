def load_data():
  '''Load data and return a list of words without normalization. 
  '''
  words = []
  with open('../data.txt', 'r', encoding='utf-8') as df:
    for word in df:
      words.append(word)
  return words


def normalization(word):
  '''Verify that the word is write correct; if not apply normalization'''
  
  normalizations = {'á':'a','é':'e','í':'i','ó':'o','ú':'u'}
  split_word = list(word)
  for index, letter in enumerate(split_word):
    if letter in normalizations.keys():
      split_word[index] = normalizations[letter]
  word = ''.join(split_word)
  return word

def random_name(words):
  '''Pick up just a word randomness from a list of words''' 
  word = random.choice(words)
  return word


def word2lines(word):
  '''Convert a word to a line of lines'''
  split_word = list(word)
  for index, letter in enumerate(split_word):
    split_word[index] = '_'
  return split_word_dotted, word

def lines2word(letter, word):
  '''Return letters in the lines spaces. If 'a' is in 'camila' the return as:
  ex 1: _ _ _ _ _ _ --> _ a _ _ _ a
  ex 2: 'o s o' and 'o' is entered:
      _ _ _ --> o __ o 
   '''
  guessed_letter = list(word)
  for index, l in enumerate(guessed_letter):
    if letter == l:
      continue
    else:
      guessed_letter[index] = '_'
  return guessed_letter

def run():
  import os
  import time
  import random
  
  start_option = int(input(print('Are you ready to playing hangman?\n 1. Yes, I\'m ready\n 2. I\'m later\n')))
  assert (start_option == 1) or (start_option == 2), 'This options does not exist!'
  while start_option == 1:
    os.system('cls')
    print('Let\'s get start!')
    time.sleep(1)
    os.system('cls')
    print('
               HANGMAN
        *___________________*
        |                   |
        |                   |                 
        |                   |
        |                   |                                               
        |                   | 
        |                   |
        |                   |                
        _____________________
        ||                 ||   
        =====================      
        *** PRO PLAYER 64 ***
        =====================
     ')
    
    for live in range(6, -1, -1):
      
      print('You have ' + str(live) + ' lives. Keep safe always!')
      dotted_word, word = word2lines(normalization(random_name(load_data())))
      print('The word is:\n', dotted_word)
      guess_word = input(print('Insert a letter: '))
      
      if guess_word in word:
        lines2word(guess_word, word)
        live += 1
        
      else:
        os.system('cls')
        if live == 6:
          print('
                   HANGMAN
            *___________________*
            |        |         |
            |        |         |                 
            |                  |
            |                  |                                               
            |                  | 
            |                  |
            |                  |                
            _____________________
            ||                 ||   
            =====================      
            ***PRO PLAYER 64***
            =====================
           ')
        elif live == 5:
          print('
                   HANGMAN
            *___________________*
            |         |         |
            |         |         |                 
            |         0         |
            |                   |                                               
            |                   | 
            |                   |
            |                   |                
            _____________________
            ||                 ||   
            =====================      
             ***PRO PLAYER 64***
            =====================
           ')
        elif live == 4:
          print('
                   HANGMAN            
            *___________________*
            |         |         |
            |         |         |                 
            |         0         |
            |         |\        |                                               
            |                   | 
            |                   |
            |                   |                
            _____________________
            ||                 ||   
            =====================      
             ***PRO PLAYER 64***
            =====================
          ')
        
        elif live == 3:
          print('
                   HANGMAN
            *___________________*
            |         |         |
            |         |         |                 
            |         0         |
            |        /|\        |                                               
            |                   | 
            |                   |
            |                   |                
            _____________________
            ||                 ||   
            =====================      
             ***PRO PLAYER 64***
            =====================
           ')
        elif live == 2:
          print('
                   HANGMAN
            *___________________*
            |         |         |
            |         |         |                 
            |         0         |
            |        /|\        |                                               
            |         |         | 
            |          \        |
            |                   |                
            _____________________
            ||                 ||   
            =====================      
             ***PRO PLAYER 64***
            =====================
           ')
        
        elif live == 1:
          print('
                   HANGMAN
            *___________________*
            |         |         |
            |         |         |                 
            |         0         |
            |        /|\        |                                               
            |         |         | 
            |          \_       |
            |                   |                
            _____________________
            ||                 ||   
            =====================      
             ***PRO PLAYER 64***
            =====================
           ')
        elif live == 0:
          print('
                   HANGMAN
            *___________________*
            |         |         |
            |         |         |                 
            |         0         |
            |        /|\        |                                               
            |         |         | 
            |        / \        |
            |       LOST!       |                
            _____________________
            ||                 ||   
            =====================      
             ***PRO PLAYER 64***
            =====================
        ')
          break









        
     
    if __name__ == '__main__':
    run()
