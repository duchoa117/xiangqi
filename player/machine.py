from player.player import Player , players
from random import choice
from minimaxFunction import maxFunWhite, minFunWhite, minFunBlack, maxFunBlack
from board import board, compareBoard
from chessMetrics import firstBlackMove, firstWhiteMove, convertToPoint


class MachineBlack(Player):
    def __init__(self):
        Player.__init__(self)
        self.get = 0

    def play(self, board, turn):
        if turn == 1:
            m = convertToPoint(choice(firstBlackMove))
            board.move(m[0], m[1])
            r = ['y', ' ', 'x', ' ', 'y', ' ', 'x']
            r[0] = str(m[0].y)
            r[2] = str(m[0].x)
            r[4] = str(m[1].y)
            r[6] = str(m[1].x)
            r = ''.join(r)
            return r
        else:
            temp = minimaxMoveBlack(board, turn)
            r = compareBoard(board, temp, 0)
            board.chesses = temp.chesses
            board.activeChesses = temp.activeChesses
            return r
class MachineWhite(Player):
    def __init__(self):
        Player.__init__(self)
        self.get = 0
    def play(self, board, turn):
        if turn == 1:
            m = convertToPoint(choice(firstWhiteMove))
            board.move(m[0], m[1])
            r = ['y', ' ', 'x', ' ', 'y', ' ', 'x']
            r[0] = str(m[0].y)
            r[2] = str(m[0].x)
            r[4] = str(m[1].y)
            r[6] = str(m[1].x)
            r = ''.join(r)
            print(r)
            return r
        else:
            temp = minimaxMoveWhite(board, turn)
            r = compareBoard(board, temp, 1)
            board.chesses = temp.chesses
            board.activeChesses = temp.activeChesses
            return r
def minimaxMoveBlack(board, turn):
    alpha = -10000
    beta = +10000
    depth = 0
    topBoardNo = 0
    topScore = -100000
    maxDepth = 2
    if(turn < 4):
        maxDepth = 3
    if(len(board.activeChesses) < 20):
        maxDepth = 3
    boards = board.generateNewBoardBlacksTurn(turn)
    for i in range(len(boards)):
        if(boards[i].whiteKingDead()):
            return boards[i]
        if(not boards[i].kingOverlap()):
            score = minFunBlack(boards[i], depth + 1, alpha, beta, maxDepth, turn)
            if(score > topScore):
                topBoardNo = i
                topScore = score
            if(score > beta):
                return boards[topBoardNo]
            if(score > alpha):
                alpha = score
    return boards[topBoardNo]
def minimaxMoveWhite(board, turn):
    alpha = -10000
    beta = +10000
    depth = 0
    topBoardNo = 0
    lowestScore = 100000
    maxDepth = 2
    if(turn < 4):
        maxDepth = 3
    if(len(board.activeChesses) < 20):
        maxDepth = 3
    boards = board.generateNewBoardWhitesTurn(turn)
    for i in range(len(boards)):
        if(boards[i].blackKingDead()):
            return boards[i]
        if(not boards[i].kingOverlap()):
            score = maxFunWhite(boards[i], depth + 1, alpha, beta, maxDepth, turn)
            if(score < lowestScore):
                topBoardNo = i
                lowestScore = score
            if(score < alpha):
                return boards[topBoardNo]
            if(score < beta):
                beta = score
    return boards[topBoardNo]



def createMachineBlack():
    m = MachineBlack()
    players.append(m)
def createMachineWhite():
    m = MachineWhite()
    players.append(m)


def randomMove(board):
    while True:
        c = choice(board.chesses)
        if(not c.white):
            if(c.active):
                if(c.shape != "."):
                    break
    c.positiveMove(board)
    c.move(choice(c.pMove), board)

    

    


