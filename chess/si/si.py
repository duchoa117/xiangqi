from chess.chess import Chess, chesses
from chess import chess
from point.point import Point
from chess.tempPoint.tempPoint import TempPoint


class Si(Chess):
    def __init__(self, point, white):
        if(white == 1):
            Chess.__init__(self, point, "S", white)
        elif(white == 0):
            Chess.__init__(self, point, "s", white)



def createSi():
    for i in range(2):
        for j in range(2):
            si = Si(Point(3+j*2, i*9), 1-i)
            chess.add(si)
            for c in chesses:
                if type(c) == TempPoint:
                    if(c.point == si.point):
                        c.deactivate()




