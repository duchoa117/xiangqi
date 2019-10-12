from chess import chess
from point.point import Point


def gameIO(board):
    while(True):
        print("Position: ")
        x = int(input("x = "))
        y = int(input("y = "))
        tP = Point(x, y)
        print("Chess information: ")
        c = chess.infor(tP, board)
        move = input("Move?(y/n)")
        if(move == "y"):
                movePositionX = int(input("X: "))
                movePositionY = int(input("Y: "))
                c.move(Point(movePositionX, movePositionY), board)
                break


        


