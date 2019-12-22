from chess.chess import Chess
from chess import chess
from point.point import Point
import pygame
from chess.images.imageChess import totB, totW

class Tot(Chess):
    def __init__(self, point, white):
        if(white == 1):
            Chess.__init__(self, point, "T", white)

        elif(white == 0):
            Chess.__init__(self, point, "t", white)

        self.value = 30
    def positiveMove(self, currentBoard):
        # setUp:
        self.pMove.clear()
        # Your code:
        mL = []
        if(self.white):
            m1 = self.point + Point(0, 1)
            mL.append(m1)

            if(self.point.y > 4):
                for i in range(-1, 2, 2):
                    mL.append(self.point + Point(i, 0))
            for m in mL:
                if ((not self.isTeammatePoint(m, currentBoard)) and m.checkOnBoard()):
                    # add tP in Positive Move:
                    self.pMove.append(m)
                # _____________________________________
        elif(not self.white):
            m1 = self.point + Point(0, -1)
            mL.append(m1)

            if(self.point.y < 5):
                for i in range(-1, 2, 2):
                    mL.append(self.point + Point(i, 0))
            for m in mL:
                if ((not self.isTeammatePoint(m, currentBoard)) and m.checkOnBoard()):
                    # add tP in Positive Move:
                    self.pMove.append(m)
                # _____________________________________
    def clone(self):
        clone = Tot(self.point, self.white)
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
                canvas.blit(totW, (35+self.point.x*71-totW.get_size()[0]/2, 40+self.point.y*70-totW.get_size()[1]/2))
            else:
                canvas.blit(totB, (35+self.point.x*71-totB.get_size()[0]/2, 40+self.point.y*70-totB.get_size()[1]/2))


        

def createTot(board):
    for i in range(2):
        for j in range(5):
            if(i == 0):
                tot = Tot(Point(j*2, 3), 1)
            elif(i == 1):
                tot = Tot(Point(j*2, 6), 0)
            board.chesses.append(tot)
            board.activeChesses.append(tot)




