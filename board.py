
from chess.chess import Chess
from chess.tempPoint.tempPoint import createTempPoint
from chess.tot.tot import createTot, Tot
from chess.king.king import createKing, King
from chess.si.si import createSi, Si
from chess.xe.xe import createXe, Xe
from chess.phao.phao import createPhao, Phao
from chess.ma.ma import createMa, Ma
from chess.tuong.tuong import createTuong, Tuong
import chessMetrics
def setChess(broad):
        createTempPoint(broad)
        createTot(broad)
        createKing(broad)
        createSi(broad)
        createXe(broad)
        createMa(broad)
        createTuong(broad)
        createPhao(broad)
def positionValue(chess):
    m = chessMetrics.king
    t = type(chess)
    if(t == Ma):
        # print("ma")
        if(chess.white):
            m = chessMetrics.maW
        else:
            m = chessMetrics.maB
    elif(t == Phao):
        # print("phao")
        if(chess.white):
            m = chessMetrics.phaoW
        else:
            m = chessMetrics.phaoB
    elif(t == Si):
        # print("si")
        m = chessMetrics.si
    elif(t == Tot):
        # print("tot")
        if(chess.white):
            m = chessMetrics.totW
        else:
            m = chessMetrics.totB
    elif(t == Tuong):
        # print("tuong")
        m = chessMetrics.tuong
    elif(t == Xe):
        # print("xe")
        if(chess.white):
            m = chessMetrics.xeW
        else:
            m = chessMetrics.xeB
    if(m[chess.point.y*9 + chess.point.x] < -100):
        print("pos value: ",m[chess.point.y*9 + chess.point.x])
    return m[chess.point.y*9 + chess.point.x]

class Board():
    def __init__(self):
        self.chesses = []
        self.activeChesses = []
        self.score = 0
        setChess(self)

    def setScore(self):
        for c in self.activeChesses:
            if(c.white):
                self.score = self.score - c.value - positionValue(c)
                
            else:
                self.score = self.score + c.value + positionValue(c)
            # if(self.score < -1000):
            #         print("score=", self.score)
        # if(self.score < -100):
        # print("score=", self.score)
        
    def isDead(self, white):
        
        if(white == 1):
            for c in self.activeChesses:
                if(c.shape == "K"):
                    return not c.active
        else:
            for c in self.activeChesses:
                if(c.shape == "k"):
                    return not c.active
    def whiteKingDead(self):
        for c in self.activeChesses:
            if(c.shape == "K"):
                return False
        return True
    def blackKingDead(self):
        for c in self.activeChesses:
            if(c.shape == "k"):
                return False
        return True

    def kingOverlap(self):
        k_w = None
        k_b = None
        check = False
        for c in self.activeChesses:
            if(c.shape == "K"):
                k_w = c
            if(c.shape == "k"):
                k_b = c
        if(k_w == None or k_b == None):
            return False
        if(k_w.point.x != k_b.point.x):
            return False
        for c in self.activeChesses:
            if(c.point.x == k_w.point.x):
                if(k_w.point.y < c.point.y < k_b.point.y):
                        return False
                else:
                        check = True
        return check
        
        
    def generateNewBoardWhitesTurn(self, turn):
        boards = []
        if(turn < 4):
            for c in self.activeChesses:
                if(c.white):
                    t = type(c)
                    if t != Tot:
                        if t!= King:
                            if t!= Si:
                                if t!= Tuong:
                                    tempBoards = c.genarateNewBoards(self)
                                    for tB in tempBoards:
                                        boards.append(tB)
            return boards

        else:
            for c in self.activeChesses:
                if(c.white):
                    tempBoards = c.genarateNewBoards(self)
                    for tB in tempBoards:
                        boards.append(tB)

            return boards
    def generateNewBoardBlacksTurn(self, turn):
        boards = []
        if(turn < 4):
            for c in self.activeChesses:
                if(not c.white):
                    t = type(c)
                    if t != Tot:
                        if t!= King:
                            if t!= Si:
                                if t!= Tuong:
                                    tempBoards = c.genarateNewBoards(self)
                                    for tB in tempBoards:
                                        boards.append(tB)
            return boards

        else:
            for c in self.activeChesses:
                if(not c.white):
                    tempBoards = c.genarateNewBoards(self)
                    for tB in tempBoards:
                        boards.append(tB)
            return boards
        
    def move(self, fromPoint, toPoint):
        chess = self.getChess(fromPoint)
        chess.move(toPoint, self)
    def clone(self):
        clone = Board()
        clone.activeChesses.clear()
        for i in range(len(self.chesses)):
            temp = self.chesses[i].clone()
            clone.chesses[i] = temp
            if(temp.active):
                if(temp.shape != '.'):
                    clone.activeChesses.append(temp)
        return clone
    def getChess(self, point):
        for c in self.activeChesses:
            if(c.point == point):
                return c
board = Board()


