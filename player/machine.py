from player.player import Player , players
from random import choice
from minimaxFunction import maxFun, minFun, maxDepth
from board import board

class Machine(Player):
    def __init__(self):
        Player.__init__(self)
        self.get = 0

    def play(self, board, white):
        # random move:
        # randomMove(board)
        # end 
        if(white):
            board.chesses = minimaxMoveWhite(board).chesses
        else:
            board.chesses = minimaxMoveBlack(board).chesses
def minimaxMoveBlack(board):
    alpha = -10000
    beta = +10000
    depth = 0
    topBoardNo = 0
    topScore = -100000
    boards = board.generateNewBoardBlacksTurn()
    for i in range(len(boards)):
        if(not boards[i].isDead(0)):
            score = minFun(boards[i], depth + 1, alpha, beta)
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
    lowestBoardNo = 0
    lowestScore = 100000
    boards = board.generateNewBoardWhitesTurn()
    for i in range(len(boards)):
        if(not boards[i].isDead(1)):
            score = maxFun(boards[i], depth + 1, alpha, beta)
            if(score < lowestScore):
                lowestBoardNo = i
                lowestScore = score
            if(score < alpha):
                return boards[lowestBoardNo]
            if(score < beta):
                beta = score
    return boards[lowestBoardNo]




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

    

    


