
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
                print("Chess name:", type(chess))
                print("Chess position:", chess.point.x, chess.point.y)
                if(chess.white):
                    print("White chess")
                elif(chess.white == 0):
                    print("Dark chess")
class Chess:
    def __init__(self, point, shape, white):
        self.point = point
        self.shape = shape
        self.white = white
        self.active = True
    def render(self):
        if(self.active):
            print(self.shape, end = ' ')
    def update(self, point):
        if(self.point == point):
            self.render()
    def deactivate(self):
        self.active = False
    def move(self):
        pass

