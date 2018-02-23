# This is a guess the number game.

import random # Call random module

print('Hello. What is your name')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1,20) # Use random module

# Ask the player to guess 6 times.
for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input()) # Change str input into int
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is the correct guess!

if guess == secretNumber:           # guessesTaken it is int to concatenation we have to convert to str
    print('Good job, ' + name + ' ! You guessed my number in ' + str(guessesTaken) + ' guesses.')
else:
    print('Nope. The number I was thinking was ' + str(secretNumber))
