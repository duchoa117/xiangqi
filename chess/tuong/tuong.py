from chess.chess import Chess, chesses
from chess import chess
from point.point import Point
from chess.tempPoint.tempPoint import TempPoint



class Tuong(Chess):
    def __init__(self, point, white):
        if(white == 1):
            Chess.__init__(self, point, "E", white)
        elif(white == 0):
            Chess.__init__(self, point, "e", white)



def createTuong():
    for i in range(2):
        for j in range(2):
            tuong = Tuong(Point(2+4*j, i*9), 1-i)
            chess.add(tuong)
            for c in chesses:
                if type(c) == TempPoint:
                    if(c.point == tuong.point):
                        c.deactivate()




