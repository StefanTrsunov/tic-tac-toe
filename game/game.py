#just a game
board = [['-','-','-'],['-','-','-'],['-','-','-']]

win = False
winner = None

def logic(board):
    global win
    if board[0][0] == board[0][1] == board[0][2] != '-':
        win = True
    elif board[1][0] == board[1][1] == board[1][2] != '-':
        win = True
    elif board[2][0] == board[2][1] == board[2][2] != '-':
       win = True
    elif board[0][0] == board[1][0] == board[2][0] != '-':
        win = True
    elif board[0][1] == board[1][1] == board[2][1] != '-':
        win = True
    elif board[0][2] == board[1][2] == board[2][2] != '-':
        win = True
    elif board[0][0] == board[1][1] == board[2][2] != '-':
        win = True
    elif board[0][2] == board[1][1] == board[2][0] != '-':
        win = True

def displayBoard(board):
    print(f"{board[0][0]}|{board[0][1]}|{board[0][2]}")
    print('-+-+-')
    print(f"{board[1][0]}|{board[1][1]}|{board[1][2]}")
    print('-+-+-')
    print(f"{board[2][0]}|{board[2][1]}|{board[2][2]}")

def displayPositions(turn,user_choise):
    global board

    if user_choise == 1:
        board[0][0] = turn
    elif user_choise == 2:
        board[0][1] = turn
    elif user_choise == 3:
        board[0][2] = turn
    elif user_choise == 4:
        board[1][0] = turn
    elif user_choise == 5:
        board[1][1] = turn
    elif user_choise == 6:
        board[1][2] = turn
    elif user_choise == 7:
        board[2][0] = turn
    elif user_choise == 8:
        board[2][1] = turn
    elif user_choise == 9:
        board[2][2] = turn

def game():
    positions = [1,2,3,4,5,6,7,8,9]
    turn = 'X'
    count = 0

    while not win:
        displayBoard(board)
        user_choise = int(input('Select a position: '))
        if user_choise in positions:
            displayPositions(turn, user_choise)
            count += 1
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
            
            logic(board)
            if count == 9:
                print('Game draw')

            if win:
                print("There is a winner")
                displayBoard(board)
                break
        else:
            print("Invalid Position")
            continue

game()