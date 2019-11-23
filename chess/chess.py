
from point.point import Point
def infor(point, board):
    for chess in board.chesses:
        if chess.active:
            if chess.point == point:
                break
    chess.positiveMove(board)
    print("- Positive move:")
    chess.printpMList()
    return chess
def isChessPoint(point, board):
    for c in board.activeChesses:
        if(c.point == point):
            return True

    return False

class Chess:
    def __init__(self, point, shape, white):
        self.point = point
        self.shape = shape
        self.white = white
        self.active = True
        self.pMove = []
        self.value = 0
    def isTeammate(self, other):
        return(self.white == other.white)
    def isTeammatePoint(self, point, board):
        for c in board.activeChesses:
            if c.point == point:
                return self.isTeammate(c)
    def render(self):
        if(self.active):
            print(self.shape, end = ' ')
    def update(self, point):
        if(self.point == point):
            self.render()
    def deactivate(self):
        self.active = False
    def activate(self):
        self.active = True
    def positiveMove(self, board):
        pass

    def move(self, point, board):
        for c in board.chesses:
            if c.point == point:
                if(c.active):
                    c.deactivate()
                    if(c.shape != '.'):
                        self.value += 10
                        board.activeChesses.remove(c)
            elif c.point == self.point:
                if c.shape == ".":
                    c.activate()
        self.point = point
    def printpMList(self):
        for p in self.pMove:
            print(p, end = " ")
        print()
    def generateNewBoards(self, currentBoard):
        boards = []
        self.positiveMove(currentBoard)
        for i in range(self.pMove.len()):
            boards.append(currentBoard.clone())
            boards[i].move(self.point, self.pMove[i])
        return boards
    def clone():
        pass
            
        

                
    

