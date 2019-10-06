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
                for j in range(tPoint.x+1, 9, 1):
                    tPoint1 = Point(j, tPoint.y)
                    if(self.isTeammatePoint(tPoint1)):
                        break
                    else:
                        if(chess.isChessPoint(tPoint1)):
                            self.pMove.append(tPoint1)
                            break
                break
        for i in range(self.point.x-1, -1, -1):
            tPoint =  Point(i, self.point.y)
            if(not chess.isChessPoint(tPoint)):
                self.pMove.append(tPoint)
            else:
                for j in range(tPoint.x-1, -1, -1):
                    tPoint1 = Point(j, tPoint.y)
                    if(self.isTeammatePoint(tPoint1)):
                        break
                    else:
                        if(chess.isChessPoint(tPoint1)):
                            self.pMove.append(tPoint1)
                            break
                break
        for i in range(self.point.y+1, 10, 1):
            tPoint =  Point(self.point.x, i)
            if(not chess.isChessPoint(tPoint)):
                self.pMove.append(tPoint)
            else:
                for j in range(tPoint.y+1, 10, 1):
                    tPoint1 = Point(tPoint.x, j)
                    if(self.isTeammatePoint(tPoint1)):
                        break
                    else:
                        if(chess.isChessPoint(tPoint1)):
                            self.pMove.append(tPoint1)
                            break
                break
        for i in range(self.point.y-1, -1, -1):
            tPoint =  Point(self.point.x, i)
            if(not chess.isChessPoint(tPoint)):
                self.pMove.append(tPoint)
            else:
                for j in range(tPoint.y-1, -1, -1):
                    tPoint1 = Point(tPoint.x, j)
                    if(self.isTeammatePoint(tPoint1)):
                        break
                    else:
                        if(chess.isChessPoint(tPoint1)):
                            self.pMove.append(tPoint1)
                            break
                break

def createPhao():
    for i in range(2):
        for j in range(2):
            phao = Phao(Point(1+j*6, 2+i*5), 1-i)
            chess.add(phao)
            for c in chesses:
                if type(c) == TempPoint:
                    if(c.point == phao.point):
                        c.deactivate()