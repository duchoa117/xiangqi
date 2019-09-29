from chess.chess import Chess
class TempPoint(Chess):
    def __init__(self, point, white):
        white = None
        Chess.__init__(self, point, ".", white)


