# word guessing game in python

# helps to pick word randomly
import random

words = ['banana','apple','kumquat','grape','melon','orange','papaya','lychee','blueberry']

# choose random word from list
guessed_word = random.choice(words)

hint = guessed_word[0]+guessed_word[-1]

store_g_l = []
try_p = 6

a = input('enter your name: ')
print('Welcome to the Game world', a)
print('We are going to give you six attempts to guess the word')

# game loop

for guess in range(try_p):
  
    while True:
        letter = input('Guess the letter: ')
        if len(letter) == 1:
            break
        else:
            print('Oops! Please guess another letter!')

    if letter in guessed_word:
        print("yes!")
        store_g_l.append(letter)
    else:
        print("no...")

    if guess == 3:
        print()
        clue_request = input('Would you like a hint?: ')
        if clue_request.lower().startswith('y'):
            print()
            print('CLUE: The first and last letter of the word is: ', hint)
        else:
            print("Ok, no clue!")

print()
print('''Now let's see what you have guessed so far. You have guessed:''',len(store_g_l), 'letters correctly!')
print('These letters are: ', store_g_l)

word_guess = input('Guess the whole word: ')
if word_guess.lower() == guessed_word:
    print('Congrats! You won!')
else:
    print("Sorry! The answer is", guessed_word)

print()
input('Please press Enter to leave the game')
    


