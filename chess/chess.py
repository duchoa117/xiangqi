import pygame

from point.point import Point
def infor(point, board):
    for chess in board.chesses:
        if chess.active:
            if chess.point == point:
                break
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
        self.image = None
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
                    self.value += 10
                    board.activeChesses.remove(c)
        self.point = point
    def printpMList(self):
        for p in self.pMove:
            print(p, end = " ")
        print()
    def generateNewBoards(self, currentBoard, turn):
        boards = []
        if turn < 4:
            if self.shape == 'p':
                if self.point == Point(7, 7) or self.point == Point(1, 7):
                    self.pMove.clear()
                    self.pMove.append(Point(4, 7))
            elif self.shape == 'P':
                if self.point == Point(7, 2) or self.point == Point(1, 2):
                    self.pMove.clear()
                    self.pMove.append(Point(4, 2))
        else:
            self.positiveMove(currentBoard)
        for i in range(len(self.pMove)):
            boards.append(currentBoard.clone())
            boards[i].move(self.point, self.pMove[i])
        return boards
    def clone():
        pass
    def imageRender(self, canvas):
       pass

