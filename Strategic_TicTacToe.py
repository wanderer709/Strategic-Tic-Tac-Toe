import random

# Nine local boards each with ten empty strings; the first nine for the spots
# on the local board, the tenth indicating which player has "taken" the board
board1 = [0,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
board2 = [1,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
board3 = [2,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
board4 = [3,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
board5 = [4,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
board6 = [5,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
board7 = [6,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
board8 = [7,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
board9 = [8,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

## FOR TESTING
#board1 = [1,'x','x','o','x','x','o','x','x','o','x']
#board2 = [2,'x','x','o','x','x','o','x','x','o','x']
#board3 = [3,'x','x','o','x','x','o','x','x','o','o']
#board4 = [4,'x','x','o','x','x','o','x','x','o','o']
#board5 = [5,'x','x','o','x','x','o','x','x','o','o']
#board6 = [6,'x','x','o','x','x','o','x','x','o','x']
#board7 = [7,'x','o','x','o','o','x','x','x','o','n']
#board8 = [8,'x','x','o','x','x','o','x','x','o','o']
#board9 = [9,'x','x','o','x','x','o','x','x','o','x']

# global_board is for all local boards "taken" by a player.
global_board = [board1[10], board2[10], board3[10], board4[10], board5[10], board6[10], board7[10], board8[10], board9[10]]
board_dict = {1:board1, 2:board2, 3:board3, 4:board4, 5:board5, 6:board6, 7:board7, 8:board8, 9:board9}

# Function for printing the board
def show_global():
    print(f"___{board7[10]}|___{board8[10]}|___{board9[10]}")
    print(f"{board7[7]}{board7[8]}{board7[9]}||{board8[7]}{board8[8]}{board8[9]}||{board9[7]}{board9[8]}{board9[9]}|")
    print(f"{board7[4]}{board7[5]}{board7[6]}||{board8[4]}{board8[5]}{board8[6]}||{board9[4]}{board9[5]}{board9[6]}|")
    print(f"{board7[1]}{board7[2]}{board7[3]}||{board8[1]}{board8[2]}{board8[3]}||{board9[1]}{board9[2]}{board9[3]}|")
    print("==============")
    print(f"___{board4[10]}|___{board5[10]}|___{board6[10]}")
    print(f"{board4[7]}{board4[8]}{board4[9]}||{board5[7]}{board5[8]}{board5[9]}||{board6[7]}{board6[8]}{board6[9]}|")
    print(f"{board4[4]}{board4[5]}{board4[6]}||{board5[4]}{board5[5]}{board5[6]}||{board6[4]}{board6[5]}{board6[6]}|")
    print(f"{board4[1]}{board4[2]}{board4[3]}||{board5[1]}{board5[2]}{board5[3]}||{board6[1]}{board6[2]}{board6[3]}|")
    print("==============")
    print(f"___{board1[10]}|___{board2[10]}|___{board3[10]}")
    print(f"{board1[7]}{board1[8]}{board1[9]}||{board2[7]}{board2[8]}{board2[9]}||{board3[7]}{board3[8]}{board3[9]}|")
    print(f"{board1[4]}{board1[5]}{board1[6]}||{board2[4]}{board2[5]}{board2[6]}||{board3[4]}{board3[5]}{board3[6]}|")
    print(f"{board1[1]}{board1[2]}{board1[3]}||{board2[1]}{board2[2]}{board2[3]}||{board3[1]}{board3[2]}{board3[3]}|")
    
# Function for placing a single mark on the board    
def marking(board,mark):
    select = None
    board_select = None
    while select == None:
        if board[10] == ' ' and board[1:10].count(' ') != 0:
            print(f"Player {mark}, you are on local board ")
            try:
                select = int(input(f"Player {mark}: Enter the number for the square to place your mark."))
            except:
                select = None
            if select in range(1,10):
                if board[select] == ' ':
                    board[select] = mark
                    global board_to_check
                    board_to_check = board
                    global next_board
                    next_board = board_dict[select]
                else:
                    print("Spot is occupied. Choose a differnt spot.\n")
                    select = None
            else:
                select = None
        else:
            while board_select == None:
                try:
                    board_select = int(input(f"Player {mark}: Which local board do you want to place your mark? " ))
                except:
                    board_select = None
                if board_select in range(1,10):
                    board = board_dict[board_select]
                    if board_dict[board_select][10] != ' ':
                        print("Local board is taken. Choose a different board.")
                        board_select = None
                else:
                    board_select = None
            while select == None:                    
                try:
                    select = int(input(f"Player {mark}: Enter the number for the square to place your mark. "))
                except:
                    select = None
                if select in range(1,10):
                    if board[select] == ' ':
                        board[select] = mark
                        board_to_check = board
                        next_board = board_dict[select]
                    else:
                        print("Spot is taken. Choose a differnt spot.\n")
                        select = None
                else:
                    select = None

# If a local board becomes full (with no winner), it's last index for its list becomes
# the 'tied' mark, allowing accomidation of the check_global_win function.
tied = 'n'

# Function checking whether a local board has a victor or is tied   
def check_local_win(board,mark):
    win = False
    if (board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[6] == mark) or (board[7] == board[8] == board[9] == mark):
        print(f"{mark} takes local board {board[0]}!")
        board[10] = mark
        win = True
    elif (board[1] == board[4] == board[7] == mark) or (board[2] == board[5] == board[8] == mark) or (board[3] == board[6] == board[9] == mark):
        print(f"{mark} takes local board {board[0]}!")
        board[10] = mark
        win = True
    elif (board[1] == board[5] == board[9] == mark) or (board[7] == board[5] == board[3] == mark):
        print(f"{mark} takes local board {board[0]}!")
        board[10] = mark
        win = True
    elif win == False and board[1:10].count(' ') == 0:
        print("This local board is tied!")
        board[10] = tied
        global_board[board[0]] = tied

# Function checking whether the global board has a victor or is tied
def check_global_win(mark):
    if (board1[10] == board2[10] == board3[10] == mark) or (board4[10] == board5[10] == board6[10] == mark) or (board7[10] == board8[10] == board9[10] == mark):
        print(f"{mark} wins the game!")
        global roundon
        roundon = False
        if mark == mark1: # if mark == 'x' for testing
            global wins1_count
            wins1_count += 1
        else:
            global wins2_count
            wins2_count += 1
    elif (board1[10] == board4[10] == board7[10] == mark) or (board2[10] == board5[10] == board8[10] == mark) or (board3[10] == board6[10] == board9[10] == mark):
        print(f"{mark} wins the game!")
        roundon = False
        if mark == mark1:
            wins1_count += 1
        else:
            wins2_count += 1
    elif (board1[10] == board5[10] == board9[10] == mark) or (board3[10] == board5[10] == board7[10] == mark):
        print(f"{mark} wins the game!")
        roundon = False
        if mark == mark1:
            wins1_count += 1
        else:
            wins2_count += 1            
    elif global_board.count(' ') == 0:
        print("Tie game!")
        roundon = False
        global tie_count
        tie_count += 1

# Function for a single round        
def single_round(a,b):
    marking(board5,a)
    show_global()
    global roundon
    while roundon == True:
        marking(next_board,b)
        check_local_win(board_to_check,b)
        show_global()
        check_global_win(b)
        if roundon == False:
            break
        marking(next_board,a)
        check_local_win(board_to_check,a)
        show_global()
        check_global_win(a)

## UNCOMMENT FOR TESTING
#wins1_count = 0
#wins2_count = 0
#tie_count = 0       
#roundon = True
#check_local_win(board7, 'x')
#show_global()
#check_global_win('x')
#check_global_win('o')
#print("\nSCOREBOARD:")
#print(f"Player x: {wins1_count}")
#print(f"Player o: {wins2_count}")
#print(f"Ties {tie_count}")

# COMMENT OUT ALL BELOW FOR TESTING
print("Welcome to Strategic Tic-Tac-Toe! Each player takes turns placing their mark on the small (or local) boards.\n")
show_global()
print("Whichever spot on the local board you mark determines the local board where your opponent places his/her mark.\n")
print("Get three in a row on a local board and that board is marked for you on the GLOBAL (or big) board.\n")       
print("Get three in a row on the global board and you win the game!\n")
print("To place a mark, just press a button on the NUM-PAD, then press ENTER.\n")
pad = None
while pad == None:
    pad = input('Is the NUM-PAD activated? y/n ')
    if pad == 'y':
        print('Good!\n')
    else:
        pad == None
        
ready = None
while ready == None:
    ready = input('Are both players ready? y/n ')
    if ready == 'y':
        print('Good fortunes!')
    else:
        ready = None
        
# The two players then decide and input their marks. Game allows only a single
# key for a mark, but otherwise it can be any mark; not just the traditional X or O.

mark1 = None
while mark1 == None:
    mark1 = input('Player 1, choose your mark (single key please!): ')
    if len(mark1) != 1:
        mark1 = None
        print('Single key please!')
    elif mark1 == ' ':
        mark1 = None
        print('Err...space-bar is not a key.')
    # The 'tied' mark changes should either player choose the mark it starts as.
    if mark1 == tied:
        tied = 'N'
    print(f"Player 1's mark will be {mark1}.")
        
mark2 = None
while mark2 == None:
    mark2 = input('Player 2, choose your mark (single key please!): ')
    if len(mark2) != 1:
        mark2 = None
        print('Single key please!')
    elif mark2 == ' ':
        mark2 = None
        print('Err...space-bar is not a key.')
    elif mark2 == mark1:
        mark2 = None
        print("That's Player 1's mark silly.")
    if tied == 'N' and mark2 == tied:
        tied= '#'
    print(f"Player 2's mark will be {mark2}.")

# These variables appear in the commands and functions.
roundon = True
wins1_count = 0
wins2_count = 0
tie_count = 0
next_board = None

gameon = True
while gameon:
    # Game asks who will go first (may be chosen at random). A different 
    # single_round function is executed depending on who goes first.
    first = None
    while first == None:
        first = input('Who will go first ({} or {})? Or should the game decide for you (press the space-bar)? '.format(mark1, mark2))
        if first == '{}'.format(mark1):
            single_round(mark1,mark2)
        elif first == '{}'.format(mark2):
            single_round(mark2,mark1)
        elif first == ' ':
            first = random.randint(1,2)
            if first == 1:
                print('Player 1 ({}) was chosen at random to go first.'.format(mark1))
                single_round(mark1,mark2)
            elif first == 2:
                print('Player 2 ({}) was chosen at random to go first.'.format(mark2))
                single_round(mark2,mark1)
        else:
            first = None
            
    # After each round, game prints the number of wins for each player plus the number of tie games.        
    print("\nSCOREBOARD:")
    print(f"Player {mark1}: {wins1_count}")
    print(f"Player {mark2}: {wins2_count}")
    print(f"Ties: {tie_count}")
    
    # Game then asks whether the players wish to play again.        
    again = None
    while again == None:
        again = input('Play again? y/n ')
        if again == 'y':
            board1 = [1,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
            board2 = [2,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
            board3 = [3,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
            board4 = [4,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
            board5 = [5,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
            board6 = [6,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
            board7 = [7,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
            board8 = [8,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
            board9 = [9,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
            show_global()
            print("\nBoard reset.")
            roundon = True
        elif again == 'n':
            gameon = False
            print("Okay, bye.")
        else:
            again = None