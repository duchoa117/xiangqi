from chess.chess import Chess
from chess import chess
from point.point import Point
import pygame
from chess.images.imageChess import phaoB, phaoW


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
        self.value = 285
        
        
    def positiveMove(self, currentBoard):
        # setUp:
       
        self.pMove.clear()
        # Your code:
        
        for i in range(self.point.x+1, 9, 1):
            tPoint =  Point(i, self.point.y)
            if(not chess.isChessPoint(tPoint, currentBoard)):
                self.pMove.append(tPoint)
            else:
                for j in range(tPoint.x+1, 9, 1):
                    tPoint1 = Point(j, tPoint.y)
                    if(self.isTeammatePoint(tPoint1, currentBoard)):
                        break
                    else:
                        if(chess.isChessPoint(tPoint1, currentBoard)):
                            self.pMove.append(tPoint1)
                            break
                break
        for i in range(self.point.x-1, -1, -1):
            tPoint =  Point(i, self.point.y)
            if(not chess.isChessPoint(tPoint, currentBoard)):
                self.pMove.append(tPoint)
            else:
                for j in range(tPoint.x-1, -1, -1):
                    tPoint1 = Point(j, tPoint.y)
                    if(self.isTeammatePoint(tPoint1, currentBoard)):
                        break
                    else:
                        if(chess.isChessPoint(tPoint1, currentBoard)):
                            self.pMove.append(tPoint1)
                            break
                break
        for i in range(self.point.y+1, 10, 1):
            tPoint =  Point(self.point.x, i)
            if(not chess.isChessPoint(tPoint, currentBoard)):
                self.pMove.append(tPoint)
            else:
                for j in range(tPoint.y+1, 10, 1):
                    tPoint1 = Point(tPoint.x, j)
                    if(self.isTeammatePoint(tPoint1, currentBoard)):
                        break
                    else:
                        if(chess.isChessPoint(tPoint1, currentBoard)):
                            self.pMove.append(tPoint1)
                            break
                break
        for i in range(self.point.y-1, -1, -1):
            tPoint =  Point(self.point.x, i)
            if(not chess.isChessPoint(tPoint, currentBoard)):
                self.pMove.append(tPoint)
            else:
                for j in range(tPoint.y-1, -1, -1):
                    tPoint1 = Point(tPoint.x, j)
                    if(self.isTeammatePoint(tPoint1, currentBoard)):
                        break
                    else:
                        if(chess.isChessPoint(tPoint1, currentBoard)):
                            self.pMove.append(tPoint1)
                            break
                break
    def clone(self):
        clone = Phao(self.point, self.white)
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
                canvas.blit(phaoW, (35+self.point.x*71-phaoW.get_size()[0]/2, 40+self.point.y*70-phaoW.get_size()[1]/2))
            else:
                canvas.blit(phaoB, (35+self.point.x*71-phaoB.get_size()[0]/2, 40+self.point.y*70-phaoB.get_size()[1]/2))




def createPhao(board):
    for i in range(2):
        for j in range(2):
            phao = Phao(Point(1+j*6, 2+i*5), 1-i)
            board.chesses.append(phao)
            board.activeChesses.append(phao)
            