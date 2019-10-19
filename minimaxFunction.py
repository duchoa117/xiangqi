
maxDepth = 2
def minFun(board, depth, alpha, beta):
    lowestScore = 100000
    if(depth >= maxDepth):
        board.setScore()
        return board.score 
    boards = board.generateNewBoardWhitesTurn()
    for i in range(len(boards)):
        if(not (boards[i]).isDead(1)):
            score = maxFun(boards[i], depth + 1, alpha, beta)
            if(score < lowestScore):
                lowestScore = score
            if(score < alpha):
                return lowestScore
            if(score < beta):
                beta = score

            


    return lowestScore
def maxFun(board, depth, alpha, beta):
    topScore = -100000
    if(depth >= maxDepth):
        board.setScore()
        return board.score 
    boards = board.generateNewBoardBlacksTurn()
    for i in range(len(boards)):
        if(not(boards[i]).isDead(0)):
            score = minFun(boards[i], depth + 1, alpha, beta)
            if(score > topScore):
                topScore = score
            if(score > beta):
                return topScore
            if(score > alpha):
                alpha = score
    return topScore



    
