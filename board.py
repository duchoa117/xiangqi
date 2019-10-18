
from chess.chess import chesses, Chess
from chess.tempPoint.tempPoint import createTempPoint
from chess.tot.tot import createTot
from chess.king.king import createKing
from chess.si.si import createSi
from chess.xe.xe import createXe
from chess.phao.phao import createPhao
from chess.ma.ma import createMa
from chess.tuong.tuong import createTuong
def setChess(broad):
        createTempPoint(broad)
        createMa(broad)
        createTot(broad)
        createXe(broad)
        createSi(broad)
        createPhao(broad)
        createTuong(broad)
        createKing(broad)
        
        
class Board():
    def __init__(self):
        self.chesses = []
        self.score = 0
        setChess(self)

    def setScore(self):
        self.score = 0
        for c in self.chesses:
            if(c.active):
                if(c.white):
                    self.score = self.score - c.value
                else:
                    self.score = self.score + c.value
        
    def isDead(self, white):
        if(white == 1):
            for c in self.chesses:
                if(c.shape == "K"):
                    return not c.active
        else:
            for c in self.chesses:
                if(c.shape == "k"):
                    return not c.active
    def generateNewBoardWhitesTurn(self):
        boards = []
        for c in self.chesses:
            if(c.white):
                if(c.active):
                    tempBoards = c.genarateNewBoards(self)
                    for tB in tempBoards:
                        boards.append(tB)
        return boards
    def generateNewBoardBlacksTurn(self):
        boards = []
        for c in self.chesses:
            if(c.white == 0):
                if(c.active):
                    tempBoards = c.genarateNewBoards(self)
                    for tB in tempBoards:
                        boards.append(tB)
        return boards
    
    def move(self, fromPoint, toPoint):
        chess = self.getChess(fromPoint)
        chess.move(toPoint, self)
    def clone(self):
        clone = Board()
        for i in range(len(self.chesses)):
            clone.chesses[i] = self.chesses[i].clone()
        return clone
    def getChess(self, point):
        for c in self.chesses:
            if(c.active):
                if(c.shape != "."):
                    if(c.point == point):
                        return c
board = Board()


