from chess.chess import Chess, chesses
from chess import chess
from point.point import Point
from chess.tempPoint.tempPoint import TempPoint


class Ma(Chess):
    def __init__(self, point, white):
        if(white == 1):
            Chess.__init__(self, point, "M", white)
        elif(white == 0):
            Chess.__init__(self, point, "m", white)



def createMa():
    for i in range(2):
        for j in range(2):
            ma = Ma(Point(1+6*j, i*9), 1-i)
            chess.add(ma)
            for c in chesses:
                if type(c) == TempPoint:
                    if(c.point == ma.point):
                        c.deactivate()




