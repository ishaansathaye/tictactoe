board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
row1 = board[0]
row2 = board[1]
row3 = board[2]

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def printBoard():
    for i in range(0,3):
        print(str(row1[i]), end="")
        if i < 2:
            print(" | ", end="")
    print()
    for i in range(0,3):
        print("- ", end="  ")
    print()
    for i in range(0,3):
        print(str(row2[i]), end="")
        if i < 2:
            print(" | ", end="")
    print()
    for i in range(0,3):
        print("- ", end="  ")
    print()
    for i in range(0,3):
        print(str(row3[i]), end="")
        if i < 2:
            print(" | ", end="")
    # print(board[0])
    # print(board[1])
    # print(board[2])

def inBetween(a, b, num):
    if int(a) <= int(num) <= int(b):
        return True
    else:
        return False

def userInput(x):
    if (x == 1):
        return 0, 0
    if (x == 2):
        return 0, 1
    if (x == 3):
        return 0, 2
    if (x == 4):
        return 1, 0
    if (x == 5):
        return 1, 1
    if (x == 6):
        return 1, 2
    if (x == 7):
        return 2, 0
    if (x == 8):
        return 2, 1
    if (x == 9):
        return 2, 2

def checkWin():
    #horizontal win
    if (board[0][0] == board[0][1]) and (board[0][1] == board[0][2]) and (board[0][0] != " "):
        return 1, board[0][0]
    elif (board[1][0] == board[1][1]) and (board[1][1] == board[1][2]) and (board[1][0] != " "):
        return True, board[1][0]
    elif (board[2][0] == board[2][1]) and (board[2][1] == board[2][2]) and (board[2][0] != " "):
        return 1, board[2][0]
    #vertical win
    elif (board[0][0] == board[1][0]) and (board[1][0] == board[2][0]) and (board[0][0] != " "):
        return 1, board[0][0]
    elif (board[0][1] == board[1][1]) and (board[1][1] == board[2][1]) and (board[0][1] != " "):
        return 1, board[0][1]
    elif (board[0][2] == board[1][2]) and (board[1][2] == board[2][2]) and (board[0][2] != " "):
        return 1, board[0][2]
    #diagonal win
    elif (board[0][0] == board[1][1]) and (board[1][1] == board[2][2]) and (board[0][0] != " "):
        return 1, board[0][0]
    elif (board[0][2] == board[1][1]) and (board[1][1] == board[2][0]) and (board[0][2] != " "):
        return 1, board[0][2]
    else:
        return 0, 0


def player1Turn():
    inrange = 1
    while inrange == 1:
        print()
        print()
        position = input(color.BOLD + color.UNDERLINE + "Player 1" + color.END + " enter number of position: ")
        intPosition = int(position)
        if inBetween(1, 9, intPosition):
            firstValue, secondValue = userInput(intPosition)
            if board[firstValue][secondValue] == "O" or board[firstValue][secondValue] == "X":
                print()
                print(color.RED + "Already a piece in that position!" + color.END)
            else:
                board[firstValue][secondValue] = "X"
                inrange = 0
                print()
                printBoard()
        else:
            print()
            print(color.RED + "Position is not in range of board!" + color.END)

def player2Turn():
    inrange = 1
    while inrange == 1:
        print()
        print()
        position = input(color.BOLD + color.UNDERLINE + "Player 2" + color.END + " enter number of position: ")
        intPosition = int(position)
        if inBetween(1, 9, intPosition):
            firstValue, secondValue = userInput(intPosition)
            if board[firstValue][secondValue] == "O" or board[firstValue][secondValue] == "X":
                print()
                print(color.RED + "Already a piece in that position!" + color.END)
            else:
                board[firstValue][secondValue] = "O"
                inrange = 0
                print()
                printBoard()
        else:
            print()
            print(color.RED + "Position is not in range of board!" + color.END)

def boardFilled():
    counter = 0
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] != " ":
                counter = counter + 1
    if counter == 9:
        return True
    else:
        return False


# print("Player 1 is X!")
# print("Player 2 is O!")

changeTurn = 1
ifPlayerWin, playerWon = checkWin()
#tie = boardFilled()
#print(ifPlayerWin, playerWon)

while (ifPlayerWin == 0):
    if ifPlayerWin == 0:
        if changeTurn == 1:
            player1Turn()
            changeTurn = 2
            checkWin()
            ifPlayerWin, playerWon = checkWin()
            boardFilled()
            #tie = boardFilled()
    if boardFilled():
        ifPlayerWin = 1
    if ifPlayerWin == 0:
        if changeTurn == 2:
            player2Turn()
            changeTurn = 1
            checkWin()
            ifPlayerWin, playerWon = checkWin()
            # boardFilled()
            # tie = boardFilled()
    if boardFilled():
        ifPlayerWin = 1


if boardFilled():
    print()
    print()
    print("Tie!")
else:
    print()
    print(playerWon + " wins!")