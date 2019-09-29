
import map
from chess.chess import Chess, chesses
from chess import chess
from chess.tempPoint import TempPoint
from point.point import Point

while(True):
    map.renderMap()
    print("Position: ")
    x = int(input("x = "))
    y = int(input("y = "))
    tP = Point(x, y)
    print("Chess information: ")
    chess.infor(tP)
    input()
