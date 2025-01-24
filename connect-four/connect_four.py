from colorama import Fore

'''
    Game-related variables
'''

game_running = True         # as long as it's True, the round is still on-going
game_won = False            
current_player = 0          # 0 = player, 1 = computer

# Board settings
board_rows = 6
board_collumns = 6

# String definitions for the slots and filled slots
empty_slot = "[ ]"
p1_token = "[" + Fore.RED + "●" + Fore.WHITE + "]"
p2_token = "[" + Fore.BLUE + "●" + Fore.WHITE + "]"

'''
    Game-related variables
'''

def place_token(_row, _token):
    if (_row < board_collumns):
        for row in reversed(board):
            if row[_input] == empty_slot:
                row[_input] = _token
                return True
    print(f"Token couldn't be placed at row {_row + 1}")
    return False

def draw_board():
    for row in board:
        print(" ".join(row))

def check_win(_check):
    _result = "".join(_check)
    if p1_token + p1_token + p1_token + p1_token in _result:
        return 1
    elif p2_token + p2_token + p2_token + p2_token in _result:
        return 2
    else:
        return 0

'''
    Create the board
'''

board = []

for row in range(0, board_rows):
    board.append([])
    for collumn in range(0, board_collumns): 
        board[row].append(empty_slot)

while game_running:

    # Draw the game's board if the player's up
    if not current_player == 1:
        draw_board()
    
    '''
        Play the actual rounds, switch between the players during each loop
    '''
    if current_player == 0:
        # Ask for the player's input
        valid_input = False
        while not valid_input:
            _input = int(input(f"Where do you want to place the next token? (1-{board_collumns})\n>>>")) - 1
            
            if (place_token(_input, p1_token)):
                valid_input = True
        current_player = 1

    elif current_player == 1:
        # Ask for the computer's input
        valid_input = False
        while not valid_input:
            _input = int(input(f"Player 2 (1-{board_collumns})\n>>>")) - 1
            #_input = 0 #random.randrange(1, 8, 1)
            
            if (place_token(_input, p2_token)):
                valid_input = True
        current_player = 0

    '''
        Check winning conditions
    '''
    _check = []
    # Horziontal matches
    for row in board:
        for collumn in row:
            _check.append(collumn)

    _check.append(".")
    # Vertical matches
    for collumn in range(0, board_rows):
        for row in range(0, board_collumns):
            _check.append(board[row][collumn])

    _check.append(".")
    # Diagonal matches
    hori_offset = 0
    while hori_offset < board_collumns-3:
        vert_offset = 0
        while vert_offset < board_rows-3:
            _check.append(board[hori_offset+vert_offset][vert_offset])
            vert_offset += 1
        hori_offset += 1

    if check_win(_check) == 1:
        game_won = True
        game_running = False
        print(_check)
    elif check_win(_check) == 2:
        game_running = False
        print(_check)


'''
    Game End
'''
draw_board()

if game_won:
    print("\rCongratulations!, you won!")
else:
    print("You unfortunately failed the game.")