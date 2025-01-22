import time

game_running = True # Used to keep the game loop running until the player either wins or fails too often
lives = 3
score = 0
game_won = False # Flag used in case the player guessed up to 100
current_number = 1

'''
    Main method used to check the player's inputs
    Very important for determining if the current number requires them to either type in 'fizz', 'buzz', 'fizz-buzz', or just the number itself
    Returns True if all the conditions are met, otherwise return False. That's important for the game loop to determine if the player failed or not

    Parameters
    _number = the current number we have to check for the specific conditions
    _input = the input() of the player, also being provided by the main loop
'''
def check_number(_number, _input):
    _makes_a_fizz = _number % 3 == 0 # Ask for "fizz" if the number is divisible by 3
    _makes_a_buzz = _number % 5 == 0 # Ask for "buzz" if the number is divisible by 3
    _fizzBuzz = _makes_a_fizz and _makes_a_buzz # Ask for "fizzbuzz" if the number is divisible by 3 *and* 5

    # Order of checks is very important
    if _fizzBuzz:
        if _input.upper() == "FIZZ-BUZZ":
            return True
        else:
            return False
    elif _makes_a_buzz:
        if _input.upper() == "BUZZ":
            return True
        else:
            return False
    elif _makes_a_fizz:
        if _input.upper() == "FIZZ":
            return True
    else:
        if _number == int(_input):
            return True
        else:
            return False

'''
    Main game starts here!
'''

time.sleep(0.334)

print('''\n\n Let's begin this round of \"Fizz-Buzz!\"
      
The rules: 
    In this game, we will go through the numbers 1-100. However...
    1. If the number is divisble by 3, type in "Fizz".
    2. If the number is divisible by 5, type in "Buzz".
    3. If the number divisible by 3 *and* 5, type in "Fizz-Buzz".
    4. *Otherwise*, just type in the number itself.
    5. You have three attempts for the whole round. 
      Guessing wrong will make you lose 10 points though.
      
Enter "1" to begin!\n''', end="", flush=True)

while game_running:
    # Fail if the input doesn't meet the requirements
    if not check_number(current_number, input("\r\r\r>>>")):
        lives -= 1
        if lives <= 0:
            game_running = False
        else:
            print("Wrongly guessed!")
            print(lives, "/3 lives left!!!")
            score = max(score-10, 0)
    else:
        current_number += 1
        score += 1
        
        # The game is won once the 100th number has been guessed right
        if current_number == 101:
            game_won = True
            game_running = False

if game_won:
    print("\rCongratulations!, you won!")
else:
    print("You unfortunately failed the game.")

print("Your Score:", score)