from chess.chess import Chess
from chess import chess
from point.point import Point
import math
import pygame
from chess.images.imageChess import siB, siW



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

    def genarateNewBoards(self, currentBoard, tP):
        boards = []
        self.positiveMove(currentBoard)
        for i in range(len(self.pMove)):
            boards.append(currentBoard.clone(tP))
            boards[i].move(self.point, self.pMove[i])
        return boards
    def imageRender(self, canvas):
        if self.active:
            if self.white:
                canvas.blit(siW, (35+self.point.x*71-siW.get_size()[0]/2, 40+self.point.y*70-siW.get_size()[1]/2))
            else:
                canvas.blit(siB, (35+self.point.x*71-siB.get_size()[0]/2, 40+self.point.y*70-siB.get_size()[1]/2))


def createSi(board):
    for i in range(2):
        for j in range(2):
            si = Si(Point(3+j*2, i*9), 1-i)
            board.chesses.append(si)
            board.activeChesses.append(si)