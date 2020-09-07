import numpy
import math

def board():
    new_board = numpy.array([[" "," "," "],[" "," "," "],[" "," "," "]])
    return new_board

def move(board, spot, spot2, char):
    if board[spot,spot2] != " ":
        row = int(input("This move is taken, please input new spot(row):"))
        col = int(input("This move is taken, please input new spot(col):"))
        move(board, row, col, char)
    else:
        board[spot, spot2] = char
        return board

def check(board):
    if ((board[0,0] == board[0,1] == board[0,2] == "X") or (board[0,0] == board[1,0] == board[2,0] == "X")
    or (board[0,0] == board[1,1] == board[2,2] == "X") or (board[1,0] == board[1,1] == board[1,2] == "X")
    or (board[2,0] == board[2,1] == board[2,2] == "X") or (board[0,1] == board[1,1] == board[2,2] == "X")
    or (board[0,2] == board[1,2] == board[2,2] == "X") or (board[0,2] == board[1,1] == board[2,0] == "X")):
        print("X wins")
        return True
    elif ((board[0,0] == board[0,1] == board[0,2] == "O") or (board[0,0] == board[1,0] == board[2,0] == "O")
    or (board[0,0] == board[1,1] == board[2,2] == "O") or (board[1,0] == board[1,1] == board[1,2] == "O")
    or (board[2,0] == board[2,1] == board[2,2] == "O") or (board[0,1] == board[1,1] == board[2,2] == "O")
    or (board[0,2] == board[1,2] == board[2,2] == "O") or (board[0,2] == board[1,1] == board[2,0] == "O")):
        print("O wins")
        return True
    else:
        return False




if __name__ == '__main__':
    playfield = board()
    print(numpy.array2string(playfield, separator = ',', formatter = {'str_kind': lambda playfield: playfield}))
    while numpy.count_nonzero(playfield == ' ') != 0:
        row = int(input("Make a move X(row):"))
        col = int(input("Make a move X(col):"))
        playfield = move(playfield, row, col, "X")
        print(numpy.array2string(playfield, separator = ',', formatter = {'str_kind': lambda playfield: playfield}))
        checkwinner = check(playfield)
        if checkwinner:
            break
        row = int(input("Make a move O(row):"))
        col = int(input("Make a move O(col):"))
        playfield = move(playfield, row, col, "O")
        print(numpy.array2string(playfield, separator = ',', formatter = {'str_kind': lambda playfield: playfield}))
        checkwinner = check(playfield)
        if checkwinner:
            break


