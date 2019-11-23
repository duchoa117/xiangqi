from chess.chess import Chess
from chess import chess
from point.point import Point
from chess.tempPoint.tempPoint import TempPoint
import math


class King(Chess):
    def __init__(self, point, white):
        if(white == 1):
            Chess.__init__(self, point, "K", white)
            self.primitiveMove = []
            for i in range(3,6,1):
                for j in range(0,3,1):
                    self.primitiveMove.append(Point(i,j)) 
        elif(white == 0):
            Chess.__init__(self, point, "k", white)
            self.primitiveMove = []
            for i in range(3,6,1):
                for j in range(7,10,1):
                    self.primitiveMove.append(Point(i,j)) 
        self.value = 10000
        
    def positiveMove(self, currentBoard):
        # setUp:
        self.pMove.clear()
        # Your code:
        for m in self.primitiveMove:
            if (abs(m.x-self.point.x) + abs(m.y-self.point.y) == 1):
                if (not self.isTeammatePoint(m, currentBoard)):
                    self.pMove.append(m)
    def clone(self):
        clone = King(self.point, self.white)
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




def createKing(board):
    for i in range(2):
        king = King(Point(4, 0 + i*9), 1-i)
        board.chesses.append(king)
        board.activeChesses.append(king)
        for c in board.chesses:
                if type(c) == TempPoint:
                    if(c.point == king.point):
                        c.deactivate()


        




