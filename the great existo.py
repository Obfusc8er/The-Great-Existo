# The Great Existo game
import random

print('Hello. I am The Great Existo! What is your name?')
name = input()

print('Yes, ' + name + ', I already knew that! I have conjured a number between 1 and 20. Guess which number it is!')
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('Enter your guess!')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low! Try again.')
    elif guess > secretNumber:
        print('Your guess is too high! Try again.')
    else:
        break # Guess is correct.

if guess == secretNumber:
    print('You guessed the correct number in ' + str(guessesTaken) + ' guesses! I bow to ' + name + '\'s superior powers!')
else:
    print('You are defeated! My number was ' + str(secretNumber) + '!')
    
    



