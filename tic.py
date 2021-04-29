# --------- Global Variables -----------
import random,os,time,tabulate

# Will hold our game board data
board = ['-','-','-','-','-','-','-','-','-']
row1 = [0,1,2]
row2 = [3,4,5]
row3 = [6,7,8]
column1 = [0,3,6]
column2 = [1,4,7]
column3 = [2,5,8]
diagonal1 =[0,4,8]
diagonal2 = [2,4,6]
rows = [row1,row2,row3,column1,column2,column3,diagonal1,diagonal2]
# Lets us know if the game is over yet
game_still_going = True
replay = True
# Tells us who the winner is
winner = None

# Tells us who the current player is (X goes first)
current_player = "X"


# ------------- Functions ---------------

# Play a game of tic tac toe
def play_game():
    global replay,board,game_still_going,current_player
    o = x = 0
    p=0
    while(p<1000):
        board = ['-','-','-','-','-','-','-','-','-']
        display_board()
        game_still_going = True
        player = current_player
        while game_still_going:
            

            # Handle a turn
            handle_turn(player)

            # Check if the game is over
            check_if_game_over()

            # Flip to the other player
            
            player = flip_player(player)

        # Since the game is over, print the winner or tie
        if winner == "X":
            print(winner + " won.")
            x+=1
        elif winner == "O":
            print(winner + " won.")
            o+=1
        elif winner == None:
            print("Tie.")
        print("\n\n\tSCOREBOARD\n")
        print(tabulate.tabulate([['AI', x], ['COMPUTER', o]], headers=['Player', 'Wins']))
        '''if input("Play again? (y/n)") == 'n':
          replay = False'''
        p+=1
        current_player = flip_player(current_player)
          

# Display the game board to the screen
def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")


# Handle a turn for an arbitrary player
def handle_turn(player):
    # Get position from player
    if(player == 'O'):
        #time.sleep(2)
        print('\n\n\n\nCOMPUTER :')
        position = fight()


    else:
        print('AI :')
        position = fightc()
        '''position = input("\n\n\n\nHUMAN : \n\nChoose a position from 1-9: ")

        # Whatever the user inputs, make sure it is a valid input, and the spot is open
        valid = False
        while not valid:

            # Make sure the input is valid
            while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                position = input("Choose a position from 1-9: ")

            # Get correct index in our board list
            position = int(position) - 1

            # Then also make sure the spot is available on the board
            if board[position] == "-":
                valid = True
            else:
                print("You can't go there. Go again.")'''


    # Put the game piece on the board
    board[position] = player


    # Show the game board
    display_board()


# Check if the game is over
def check_if_game_over():
    check_for_winner()
    check_for_tie()


# Check to see if somebody has won
def check_for_winner():
    # Set global variables
    global winner
    # Check if there was a winner anywhere
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    # Get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


# Check the rows for a win
def check_rows():
    # Set global variables
    global game_still_going
    # Check if any of the rows have all the same value (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    # Or return None if there was no winner
    else:
        return None


# Check the columns for a win
def check_columns():
    # Set global variables
    global game_still_going
    # Check if any of the columns have all the same value (and is not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # If any row does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # Return the winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    # Or return None if there was no winner
    else:
        return None


# Check the diagonals for a win
def check_diagonals():
    # Set global variables
    global game_still_going
    # Check if any of the columns have all the same value (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    # If any row does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # Return the winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    # Or return None if there was no winner
    else:
        return None


# Check if there is a tie
def check_for_tie():
    # Set global variables
    global game_still_going
    # If board is full
    if "-" not in board:
        game_still_going = False
        return True
    # Else there is no tie
    else:
        return False


# Flip the current player from X to O, or O to X
def flip_player(player):
    # Global variables we need
    
    # If the current player was X, make it O
    if player == "X":
        player = "O"
    # Or if the current player was O, make it X
    elif player == "O":
        player = "X"
    return player
      

def fight():
    global rows
    #For the first turn of 0...picking a random empty slot
    z = [i for i in range(0,9) if board[i]=='-']
    pos = random.choice(z)

    #Priority 1 : checking if there are 2 Os in a row for an imminent win
    for row in rows:
        b = [board[ro] for ro in row]
        if 'X' not in b:
            c = b.count('O')
            if c == 2:
                for i in range(0,3):
                    if(b[i] == '-'):
                        pos = row[i]
                        return pos
    #Priority 2 : checking if there are 2 Xs in a row to prevent X from winning
    for row in rows:
        b = [board[q] for q in row]
        if 'X' in b:
            f = b.count('X')
            if f == 2:
                for j in range(0,3):
                    if(b[j] == '-'):
                        pos = row[j]
                        return pos
    #Last Priority : Assigning position to an empty slot in a row with an existing O
    for row in rows:
        b = [board[ro] for ro in row]
        if 'X' not in b:
            c = b.count('O')
            if c == 1:
                for i in range(0,3):
                    if(b[i] == '-'):
                        pos = row[i]
                        return pos
    # For the random slot in 1st turn
    return pos

def fightc():
    global rows
    #For the first turn of 0...picking a random empty slot
    z = [i for i in range(0,9) if board[i]=='-']
    pos = random.choice(z)

    #Priority 1 : checking if there are 2 Os in a row for an imminent win
    for row in rows:
        b = [board[ro] for ro in row]
        if 'O' not in b:
            c = b.count('X')
            if c == 2:
                for i in range(0,3):
                    if(b[i] == '-'):
                        pos = row[i]
                        return pos
    #Priority 2 : checking if there are 2 Xs in a row to prevent X from winning
    for row in rows:
        b = [board[q] for q in row]
        if 'O' in b:
            f = b.count('O')
            if f == 2:
                for j in range(0,3):
                    if(b[j] == '-'):
                        pos = row[j]
                        return pos
    #Last Priority : Assigning position to an empty slot in a row with an existing O
    for row in rows:
        b = [board[ro] for ro in row]
        if 'O' not in b:
            c = b.count('X')
            if c == 1:
                for i in range(0,3):
                    if(b[i] == '-'):
                        pos = row[i]
                        return pos
    # For the random slot in 1st turn
    return pos



