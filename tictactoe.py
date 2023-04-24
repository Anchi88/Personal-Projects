import random
# Tic Tac Toe game


# how does board look like?
# how to position the O and X?
# winn?
# try again or quit?


# print board
def printBoard(board):
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("_   _   _")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("_   _   _")
    print(f"{board[0]} | {board[1]} | {board[2]}")

# choose your letter
def playerLetters():
    userLetter = ""

    while not (userLetter == "X" or userLetter == "O"):  # if the letter is not o or x, ask again
        userLetter = input("Do you want to be X or O? ").upper()

    if userLetter == "X":
        computerLetter = "O"
    else:
        computerLetter = "X"

    return userLetter, computerLetter

# random decision who goes firs
def whoGoesFirst():
     head = random.randint(0, 1)
     if head == 1:
         return "user"
     else:
         return "computer"

# user move
def userMove(userLetter):  # we use letter user has defined

    while True:  # ask so long until place on board is free
        move = int(input("What is your move? (1 - 9): "))
        move -= 1  # because index is always one number smaller
        isMoveFree = checkIfFree(move) # go into the def isMoveFree and return true or false
        if isMoveFree:  # if the move is not free, while loop will repeat
            board[move] = userLetter  # remove index(move) and replace with user letter
            win = checkWin(userLetter, board)  # check if user has won and save the value
            return win
            break



def computerMove(computerLetter):

    while True:
        move = random.randint(0,8)  # choose random number between 0 and 8
        isMoveFree = checkIfFree(move)
        if isMoveFree:
            board[move] = computerLetter
            printBoard(board)
            win = checkWin(computerLetter,board)
            return win
            break




def checkIfFree(move):
    if board[move] == "X" or board[move] == "O":  # if there is a X or O on the field, give False - no freeMove
        freeMove = False
    else:
        freeMove = True

    return freeMove  # return if True or False



def checkWin(letter,board):  # check for win or tie
    win = 0
    if ((board[0] == letter and board[1] == letter and board[2] == letter) or
        (board[3] == letter and board[4] == letter and board[5] == letter) or
        (board[6] == letter and board[7] == letter and board[8] == letter) or
        (board[0] == letter and board[3] == letter and board[6] == letter) or
        (board[1] == letter and board[4] == letter and board[7] == letter) or
        (board[2] == letter and board[5] == letter and board[8] == letter) or
        (board[0] == letter and board[4] == letter and board[8] == letter) or
        (board[2] == letter and board[4] == letter and board[6] == letter)):
        win = 2
        return win
    elif win !=2 and board.count(letter) >= 5:
        win = 1
        return win
    else:
        return win




# main proccess

while True:
    gameOver = False
    board = ["1","2","3","4","5","6","7","8","9"]

    print("Welcome to Tic Tac Toe!")
    print("------BOARD------")
    printBoard(board)
    print("-----------------")
    userLetter, computerLetter = playerLetters()
    player = whoGoesFirst()
    print(f"First will go: {player}")

    while gameOver == False:
        if player == "computer":
            win = computerMove(computerLetter)
            if win == 1:
                print("It is a tie!")
                gameOver = True

            elif win == 2:
                print("Computer won!")
                gameOver = True

            else:
                player = "user"

        else:
            win = userMove(userLetter)
            if win == 1:
                print("It is a tie!")
                gameOver = True

            elif win == 2:
                print("You won!")
                gameOver = True

            else:
                player = "computer"

    if gameOver == True:
        print("------------------------------------")
        playAgain = input("Do you want to play again? yes or no").lower()
        if not playAgain == "y":
          print("Thank you for playing Tic Tac Toe")
          break




# print out actual Board
