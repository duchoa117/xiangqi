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
    def positiveMove(self):
        # setUp:
        self.pMove.clear()
        # Your code:
        mL = []
        m1 = self.point + Point(0, 1)
        mL.append(m1)
        if(self.point.y > 4):
            for i in range(-1, 2, 2):
                mL.append(self.point + Point(i, 0))
        for m in mL:
            if ((not self.isTeammatePoint(m)) and m.checkOnBoard()):
                # add tP in Positive Move:
                self.pMove.append(m)
            # _____________________________________
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




