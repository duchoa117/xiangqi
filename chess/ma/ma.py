from chess.chess import Chess, chesses
from chess import chess
from point.point import Point
from chess.tempPoint.tempPoint import TempPoint


class Ma(Chess):
    def __init__(self, point, white):
        if(white == 1):
            Chess.__init__(self, point, "M", white)
            self.primitiveMove= []
            for i in range (0,9,1):
                for j in range (0,10,1):
                    self.primitiveMove.append(Point(i,j))
        elif(white == 0):
            Chess.__init__(self, point, "m", white)
            self.primitiveMove= []
            for i in range (0,9,1):
                for j in range (0,10,1):
                    self.primitiveMove.append(Point(i,j))

    def positiveMove(self):
        #setUp:
        self.pMove.clear()
        # Your code:
        for m in self.primitiveMove:
            if((abs(m.x - self.point.x) == 1 and abs(m.y-self.point.y) == 2) or 
                (abs(m.x - self.point.x) == 2 and abs(m.y-self.point.y) == 1) ):
                if(not self.isTeammatePoint(m)):
                    if(abs(m.x - self.point.x) == 1):
                        if(not (chess.isChessPoint(Point(self.point.x,self.point.y + (m.y-self.point.y)/abs(m.y-self.point.y)  )))):
                            self.pMove.append(m)
                    elif (abs(m.x - self.point.x) == 2): 
                        if(not (chess.isChessPoint(Point(self.point.x + (m.x-self.point.x)/abs(m.x-self.point.x), self.point.y )))):
                            self.pMove.append(m)



def createMa():
    for i in range(2):
        for j in range(2):
            ma = Ma(Point(1+6*j, i*9), 1-i)
            chess.add(ma)
            for c in chesses:
                if type(c) == TempPoint:
                    if(c.point == ma.point):
                        c.deactivate()




