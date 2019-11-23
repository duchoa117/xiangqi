from chess.chess import Chess
from chess import chess
from point.point import Point
import setUp
from board import Board, board
# setup:
setUp.setPlayer()
# end setup

def renderMap(board):
    # print map:
    for i in range(-1, 10, 1):
        for j in range(-1, 9, 1):
            if(i == -1):
                if(j == -1):
                    print(' ', end  = ' ')
                else:
                    print(j, end = ' ')
            elif(j == -1 and i > -1):
                print(i, end = ' ')
            p = Point(j, i)
            for chess in board.chesses:
                chess.update(p)
        print()
    # end print