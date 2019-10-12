
maxDepth = 2
def minFun(board, depth):
    lowestBoardNo = 0
    lowestScore = 100000
    if(depth >= maxDepth):
        board.setScore()
        return board.score 
    boards = board.generateNewBoardWhitesTurn()
    for i in range(len(boards)):
        if(not (boards[i]).isDead(0)):
            score = maxFun(boards[i], depth + 1)
            if(score < lowestScore):
                lowestBoardNo = i
                lowestScore = score

    return lowestScore
def maxFun(board, depth):
    topBoardNo = 0
    topScore = -100000
    if(depth >= maxDepth):
        board.setScore()
        return board.score 
    boards = board.generateNewBoardBlacksTurn()
    for i in range(len(boards)):
        if(not(boards[i]).isDead(1)):
            score = minFun(boards[i], depth + 1)
            if(score > topScore):
                topBoardNo = i
                topScore = score
    return topScore



    
