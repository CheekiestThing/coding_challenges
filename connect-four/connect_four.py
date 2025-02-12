from colorama import Fore
import re

'''
    Game-related variables
'''

horizontal_pattern = r"(\[●\]\s){4,6}"
diagonal_left_pattern = r"(\[[●]\]([\s\S]{4}){4}[\s\S]){4,6}"
diagonal_right_pattern = r"(\[[●]\]([\s\S]{4}){6}[\s\S]){4,6}"
win_pattern = horizontal_pattern + "|" + diagonal_left_pattern + "|" + diagonal_right_pattern

game_running = True         # as long as it's True, the round is still on-going
winner = 0                  # used after the round is over, to remember who won            
current_player = 0

# Board settings
board_rows = 6
board_collumns = 6

# String definitions for the slots and filled slots
empty_slot = "[ ]"
p1_key = "1" # r -> RED
p2_key = "2" # b -> BLUE

# Functions
'''
place_token 
    Tries to place a token to the board; If it can't, return False
    _row = the row to try placing the token in
    _key = the key to use (p1_key or p2_key)
'''
def place_token(_row: int, _key : str):
    if (_row < board_collumns):
        for row in reversed(board):
            if row[_input] == empty_slot:
                row[_input] = row[_input].replace(" ", _key)
                return True
    print(f"Token couldn't be placed at row {_row + 1}")
    return False

'''
full_board
    Returns the full board as a simple string representation
'''
def full_board():
    _output = ""
    for row in board:
        _output += (" ".join(row))
        _output += "\n"
    return _output

'''
print_board
    Print the board to the command line WITH the keys/tokens replaced with their actual colored symbols
'''
def print_board():
    print(full_board().replace(p1_key, Fore.RED + "●" + Fore.WHITE).replace(p2_key, Fore.BLUE + "●" + Fore.WHITE), end="")

'''
print_message
    Print a message to the command line WITH the player names being colored in
    _message = the message to print out
'''
def print_message(_message):
    print(_message.replace("Player 1", Fore.RED + "Player 1" + Fore.WHITE).replace("Player 2", Fore.BLUE + "Player 2" + Fore.WHITE))

'''
check_win
    Utilizes RegEx (using the combined win_pattern) to see if a player has four tiles connect;
    _key = the key to use (p1_key or p2_key)
'''
def check_win(_key : str):
     return len(re.findall(win_pattern, full_board().replace(_key, "●"))) > 0

board = []
for row in range(0, board_rows):
    board.append([])
    for collumn in range(0, board_collumns): 
        board[row].append(empty_slot)

while game_running:

    # Diplay the game board
    print_board()
    
    '''
        Play the actual rounds, switch between the players during each loop
    '''
    # Ask for the player's input
    valid_input = False
    _input = None

    # Let the player not go on until they have made a valid move
    while not valid_input:
        # Exit the program if anything other than an integer has been passed
        try:
            print_message(f"\rPlayer {current_player + 1}; Where do you want to place the next token?")
            _input = int(input(">>>")) - 1
        except:
            exit()

        # Try placing a token, then switch players. If it didn't work, ask for a new collum to place a token in 
        if current_player == 0:
            if (place_token(_input, p1_key)):
                valid_input = True
                current_player = 1
        else:
            if (place_token(_input, p2_key)):
                valid_input = True
                current_player = 0

    '''
        Check winning conditions
    '''
    if check_win(p1_key):
        winner = 1
        game_running = False
    elif check_win(p2_key):
        winner = 2
        game_running = False

'''
    Game End
'''
print_board()

if winner != 0:
    print_message(f"\rCongratulations, Player {winner}!, you won!")
else:
    print_message("Tied!")