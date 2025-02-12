#Higher or Lower Number Game - www.101computing.net/higher-or-lower-number-game/
from random import randint

number_to_guess = randint(1,100)

#Complete the code here...
while True:
    _input = int(input("Enter a number from 1-100:\n>>>"))
    
    if _input == number_to_guess:
        print("You've guessed right!")
        break
    elif _input < number_to_guess:
        print("Higher!")
    elif _input > number_to_guess:
        print("Lower!")