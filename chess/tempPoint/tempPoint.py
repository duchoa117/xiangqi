from chess.chess import Chess
from chess import chess
from point.point import Point


class TempPoint(Chess):
    def __init__(self, point, white):
        white = None
        Chess.__init__(self, point, ".", white)


def createTempPoint():
    for i in range(10):
        for j in range(9):
            temp = TempPoint(Point(i,j), 1)
            chess.add(temp)




