
from chess.chess import Chess, chesses

class Tot(Chess):
    def __init__(self, point, white):
        if(white == 1):
            Chess.__init__(self, point, "T", 1)
        elif(white == 0):
            Chess.__init__(self, point, 't', 0)