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
        self.primitiveMove = []
        for i in range(9):
            for j in range(10):
                self.primitiveMove.append(Point(i,j))
    def positiveMove(self):
        # setUp:
        self.pMove.clear()
        # Your code:
        for i in range(self.point.x+1, 9, 1):
            tPoint =  Point(i, self.point.y)
            if(not chess.isChessPoint(tPoint)):
                self.pMove.append(tPoint)
            else:
                if(self.isTeammatePoint(tPoint)):
                    break
                else:
                    self.pMove.append(tPoint)
                    break
        for i in range(self.point.x-1, -1, -1):
            tPoint =  Point(i, self.point.y)
            if(not chess.isChessPoint(tPoint)):
                self.pMove.append(tPoint)
            else:
                if(self.isTeammatePoint(tPoint)):
                    break
                else:
                    self.pMove.append(tPoint)
                    break
        for i in range(self.point.y+1, 10, 1):
            tPoint =  Point(self.point.x, i)
            if(not chess.isChessPoint(tPoint)):
                self.pMove.append(tPoint)
            else:
                if(self.isTeammatePoint(tPoint)):
                    break
                else:
                    self.pMove.append(tPoint)
                    break
        for i in range(self.point.y-1, -1, -1):
            tPoint =  Point(self.point.x, i)
            if(not chess.isChessPoint(tPoint)):
                self.pMove.append(tPoint)
            else:
                if(self.isTeammatePoint(tPoint)):
                    break
                else:
                    self.pMove.append(tPoint)
                    break

def createXe():
    for i in range(2):
        for j in range(2):
            xe = Xe(Point(j*8, i*9), 1-i)
            chess.add(xe)
            for c in chesses:
                if type(c) == TempPoint:
                    if(c.point == xe.point):
                        c.deactivate()