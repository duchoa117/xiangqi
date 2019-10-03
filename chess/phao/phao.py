from chess.chess import Chess, chesses
from chess import chess
from point.point import Point
from chess.tempPoint.tempPoint import TempPoint


class Phao(Chess):
    def __init__(self, point, white):
        if(white == 1):
            Chess.__init__(self, point, "P", white)
        elif(white == 0):
            Chess.__init__(self, point, "p", white)



def createPhao():
    for i in range(2):
        for j in range(2):
            phao = Phao(Point(1+j*6, 2+i*5), 1-i)
            chess.add(phao)
            for c in chesses:
                if type(c) == TempPoint:
                    if(c.point == phao.point):
                        c.deactivate()