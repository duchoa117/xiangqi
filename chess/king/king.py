from chess.chess import Chess, chesses
from chess import chess
from point.point import Point
from chess.tempPoint.tempPoint import TempPoint


class King(Chess):
    def __init__(self, point, white):
        if(white == 1):
            Chess.__init__(self, point, "K", white)
        elif(white == 0):
            Chess.__init__(self, point, "k", white)



def createKing():
    for i in range(2):
        king = King(Point(4, 0 + i*9), 1-i)
        chess.add(king)
        for c in chesses:
                if type(c) == TempPoint:
                    if(c.point == king.point):
                        c.deactivate()


        




