from chess.chess import Chess
from chess import chess
from point.point import Point


class TempPoint(Chess):
    def __init__(self, point, white):
        white = None
        Chess.__init__(self, point, ".", white)
    def clone(self):
        clone = TempPoint(self.point, self.white)
        clone.active = self.active
        return clone

def createTempPoint(board):
    for i in range(9):
        for j in range(10):
            temp = TempPoint(Point(i,j), 1)
            board.chesses.append(temp)




