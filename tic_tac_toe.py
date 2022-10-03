def print_board(board):
    print(board["1"],"|",board["2"],"|",board["3"])
    print(board["4"],"|",board["5"],"|",board["6"])
    print(board["7"],"|",board["8"],"|",board["9"])


def winner_winner_chicken_dinner(board):
    
    if board["1"]==board["2"]==board["3"]:
        return 1
    elif board["4"]==board["5"]==board["6"]:
        return 1
    elif board["7"]==board["8"]==board["9"]:
        return 1
    elif board["1"]==board["4"]==board["7"]:
        return 1
    elif board["2"]==board["5"]==board["8"]:
        return 1
    elif board["3"]==board["6"]==board["9"]:
        return 1
    elif board["1"]==board["5"]==board["9"]:
        return 1
    elif board["3"]==board["5"]==board["7"]:
        return 1
    else:
        return 0
    

board = {"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"}
print_board(board)
player_1 = input("Enter name of player 1:")
player_2 = input("Enter name of player 2:")
turn = 1
while True:
    if turn % 2 != 0:
        print(player_1,"turn-")
        pos = input("Enter position to mark:")
        board[pos] = "X"
        print_board(board)
    else:
        print(player_2,"turn-")
        pos = input("Enter position to mark:")
        board[pos] = "O"
        print_board(board)
    Z = winner_winner_chicken_dinner(board)
    if Z == 1:
        if turn%2 != 0:
            print(player_1," Won!..")
            print_board(board)
        else:
            print(player_2,"Won!..")
            print_board(board)
        break
    turn = turn + 1

    if turn == 10:
        print("Draw ..")
        break

    

