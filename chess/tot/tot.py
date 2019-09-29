from chess.chess import Chess, chesses
from chess import chess
from point.point import Point
from chess.tempPoint.tempPoint import TempPoint


class Tot(Chess):
    def __init__(self, point, white):
        if(white == 1):
            Chess.__init__(self, point, "T", white)
        elif(white == 0):
            Chess.__init__(self, point, "t", white)



def createTot():
    for i in range(2):
        for j in range(5):
            if(i == 0):
                tot = Tot(Point(j*2, 3), 1)
            elif(i == 1):
                tot = Tot(Point(j*2, 6), 0)
            chess.add(tot)
            for c in chesses:
                if type(c) == TempPoint:
                    if(c.point == tot.point):
                        c.deactivate()




