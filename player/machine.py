from player.player import Player , players
from random import choice
from minimaxFunction import maxFunWhite, minFunWhite, minFunBlack, maxFunBlack
from board import board

class Machine(Player):
    def __init__(self):
        Player.__init__(self)
        self.get = 0

    def play(self, board):
        temp = minimaxMoveBlack(board)
        board.chesses = temp.chesses
        board.activeChesses = temp.activeChesses
def minimaxMoveBlack(board):

    alpha = -10000
    beta = +10000
    depth = 0
    topBoardNo = 0
    topScore = -100000
    maxDepth = 2 
    if(len(board.activeChesses) < 16):
        maxDepth = 3
    boards = board.generateNewBoardBlacksTurn()
    for i in range(len(boards)):
        if(not boards[i].kingOverlap()):
            score = minFunBlack(boards[i], depth + 1, alpha, beta, maxDepth)
            if(score > topScore):
                topBoardNo = i
                topScore = score
            if(score > beta):
                return boards[topBoardNo]
            if(score > alpha):
                alpha = score
    return boards[topBoardNo]
def minimaxMoveWhite(board):
    alpha = -10000
    beta = +10000
    depth = 0
    topBoardNo = 0
    lowestScore = 100000
    maxDepth = 2 
    if(len(board.activeChesses) < 16):
        maxDepth = 3
    boards = board.generateNewBoardWhitesTurn()
    for i in range(len(boards)):
        if(not boards[i].kingOverlap()):
            score = maxFunWhite(boards[i], depth + 1, alpha, beta, maxDepth)
            if(score < lowestScore):
                topBoardNo = i
                lowestScore = score
            if(score < alpha):
                return boards[topBoardNo]
            if(score < beta):
                beta = score
    return boards[topBoardNo]



def createMachine():
    m = Machine()
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

    

    


