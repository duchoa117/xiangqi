from chess.chess import Chess
from chess import chess
from point.point import Point
import setUp
from board import Board, board
import pygame
# setup:
setUp.setPlayer()
# end setup


def renderMap(board):
    # print map:
    for i in range(-1, 10, 1):
        for j in range(-1, 9, 1):
            cR = False
            if(i == -1):
                if(j == -1):
                    print(' ', end  = ' ')
                    cR = True
                else:
                    print(j, end = ' ')
                    cR = True
            elif(j == -1 and i > -1):
                print(i, end = ' ')
                cR = True
            p = Point(j, i)
            for chess in board.activeChesses:
                if p == chess.point:
                    chess.render()
                    cR = True
            if(not cR):
                print(".", end = ' ')
        print()
    # end print
    