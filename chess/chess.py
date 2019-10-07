
from point.point import Point
chesses = []
def add(chess):
    chesses.append(chess)

def update():
    for chess in chesses:
        chess.update()
def infor(point):
    for chess in chesses:
        if chess.active:
            if chess.point == point:
                print("- Chess name:", type(chess))
                print("- Position:", point)
                if(chess.white):
                    print("- White chess")
                elif(chess.white == 0):
                    print("- Dark chess")
                break
    chess.positiveMove()
    print("- Positive move:")
    chess.printpMList()
    return chess
def isChessPoint(point):
    for c in chesses:
        if(c.point == point):
            if(c.active):
                if(c.white != None):
                    return True
    return False

class Chess:
    def __init__(self, point, shape, white):
        self.point = point
        self.shape = shape
        self.white = white
        self.active = True
        self.pMove = []
    def isTeammate(self, other):
        return(self.white == other.white)
    def isTeammatePoint(self, point):
        for c in chesses:
            if c.point == point:
                if(c.active):
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
    def positiveMove(self):
        pass
    def move(self, point):
        for c in chesses:
            if c.point == point:
                c.deactivate()
            if c.shape == ".":
                if c.point == self.point:
                    c.activate()
        print(point)
        self.point = point
        print(self.point)
    def printpMList(self):
        for p in self.pMove:
            print(p, end = " ")
        print()

                
    

