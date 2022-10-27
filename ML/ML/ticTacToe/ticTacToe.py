'''
    To Do:
        !!!Check if someone has won
        !Instructions

    Later:
        AI stuff
'''

board = [["#","#","#"],
        ["#","#","#"],
        ["#","#","#"]]

#takes player input, checks if it is valid and updates the board
def takeTurn(player):
    coordinates = ""
    userInput = input("Enter coordinates of " + player + "\'s move: ")
    for i in userInput:
        if i.isdigit():
            coordinates += i
    point = board[int(coordinates[0])-1][int(coordinates[1])-1]
    if point == "#":
        board[int(coordinates[0])-1][int(coordinates[1])-1] = player
    else:
        while point != "#":
            coordinates1 = ""
            print()
            print("Invalid move!")
            print()
            userInput = input("Enter coordinates of " + player + "\'s move: ")
            for i in userInput:
                if i.isdigit():
                    coordinates1 += i
            point = board[int(coordinates1[0])-1][int(coordinates1[1])-1]
        board[int(coordinates1[0])-1][int(coordinates1[1])-1] = player

#updates the screen
def update():
    print()
    for i in board:
        print(i)
    print()

#checks if someone has won
def check(player):
    print(player)
    if board[0][0] == player:
        if board[0][1] == player:
            if board[0][2] == player:
                return False
        if board[1][0] == player:
            if board[2][0] == player:
                return False
        if board[1][1] == player:
            if board[2][2] == player:
                return False
    if board[0][1] == player:
        if board[1][1] == player:
            if board[2][1] == player:
                return False
    if board[0][2] == player:
        if board[1][1] == player:
            if board[2][0] == player:
                return False
        if board[1][2] == player:
            if board[2][2] == player:
                return False
    if board[1][0] == player:
        if board[1][1] == player:
            if board[1][2] == player:
                return False
    if board[2][0] == player:
        if board[2][1] == player:
            if board[2][2] == player:
                return False
    return True

def main():
    update()
    counter = 0
    gameRunning = True
    while gameRunning:
        counter += 1
        if counter % 2 == 1:
            player = 'X'
        else:
            player = 'O'
        takeTurn(player)
        update()
        gameRunning = check(player)
    print()
    print(player, "won the game!")

main()
