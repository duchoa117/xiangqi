from chess.chess import Chess, chesses
from chess import chess
from point.point import Point
from chess.tempPoint.tempPoint import TempPoint
import math



class Tuong(Chess):
    def __init__(self, point, white):
        if(white == 1):
            Chess.__init__(self, point, "E", white)
            self.primitiveMove= []
            for i in range (0,9,1):
                for j in range (0,5,1):
                    self.primitiveMove.append(Point(i,j))
        elif(white == 0):
            Chess.__init__(self, point, "e", white)
            self.primitiveMove= []
            for i in range (0,9,1):
                for j in range (5,10,1):
                    self.primitiveMove.append(Point(i,j))
            
    def positiveMove(self):
        #setUp:
        self.pMove.clear()
        # Your code:
        for m in self.primitiveMove:
            if(abs(m.x - self.point.x) == 2 and abs(m.y-self.point.y) == 2):
                if(not self.isTeammatePoint(m)):
                    if(not (chess.isChessPoint(self.point+(m-self.point)*(1/2)))):
                        self.pMove.append(m)




def createTuong():
    for i in range(2):
        for j in range(2):
            tuong = Tuong(Point(2+4*j, i*9), 1-i)
            chess.add(tuong)
            for c in chesses:
                if type(c) == TempPoint:
                    if(c.point == tuong.point):
                        c.deactivate()




