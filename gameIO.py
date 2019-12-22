from board import Board
from point.point import Point
def gameIO(board, move):
    fromPoint = Point(int(move[2]), int(move[0]))
    toPoint = Point(int(move[6]), int(move[4]))
    board.move(fromPoint, toPoint)
    



        


