from chess.chess import Chess, chesses
from chess import chess
from point.point import Point
from chess.tempPoint.tempPoint import TempPoint


class Xe(Chess):
    def __init__(self, point, white):
        if(white == 1):
            Chess.__init__(self, point, "X", white)
        elif(white == 0):
            Chess.__init__(self, point, "x", white)



def createXe():
    for i in range(2):
        for j in range(2):
            xe = Xe(Point(j*8, i*9), 1-i)
            chess.add(xe)
            for c in chesses:
                if type(c) == TempPoint:
                    if(c.point == xe.point):
                        c.deactivate()