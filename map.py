from chess.chess import Chess, chesses
from chess import chess
from chess.tempPoint import TempPoint
from point.point import Point
# setup:
for i in range(10):
    for j in range(9):
        t = TempPoint(Point(i,j), 1)
        chess.add(t)
# end setup

def renderMap():
    # print map:
    for i in range(-1, 10, 1):
        for j in range(-1, 9, 1):
            if(i == -1):
                if(j == -1):
                    print(' ', end  = ' ')
                else:
                    print(j, end = ' ')
            elif(j == -1 and i > -1):
                print(i, end = ' ')
            p = Point(i, j)
            for chess in chesses:
                chess.update(p)
        print()
    # end print