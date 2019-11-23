from chess.chess import Chess
from chess import chess
from point.point import Point
from chess.tempPoint.tempPoint import TempPoint
import math


class Si(Chess):
    def __init__(self, point, white):
        if(white == 1):
            Chess.__init__(self, point, "S", white)
            self.primitiveMove = [Point(3,0), Point(3,2), Point(4,1), Point(5,0), Point(5,2)]
        elif(white == 0):
            Chess.__init__(self, point, "s", white)
            self.primitiveMove = [Point(3,9), Point(3,7), Point(4,8), Point(5,9), Point(5,7)]
        self.value = 120
            
    def positiveMove(self, currentBoard):
        # setUp:
        self.pMove.clear()
        # Your code:
        for m in self.primitiveMove:
            if(abs(m.x - self.point.x) == 1 and abs(m.y-self.point.y) == 1):
                if(not self.isTeammatePoint(m, currentBoard)):
                    self.pMove.append(m)
    def clone(self):
        clone = Si(self.point, self.white)
        clone.active = self.active
        clone.value = self.value

        return clone

    def genarateNewBoards(self, currentBoard):
        boards = []
        self.positiveMove(currentBoard)
        for i in range(len(self.pMove)):
            boards.append(currentBoard.clone())
            boards[i].move(self.point, self.pMove[i])
        return boards

def createSi(board):
    for i in range(2):
        for j in range(2):
            si = Si(Point(3+j*2, i*9), 1-i)
            board.chesses.append(si)
            board.activeChesses.append(si)

            for c in board.chesses:
                if type(c) == TempPoint:
                    if(c.point == si.point):
                        c.deactivate()




