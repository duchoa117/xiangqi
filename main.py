
from map import renderMap, board
from chess.chess import Chess, chesses
from chess import chess
from point.point import Point
from gamePlay import gamePlay

while(True):
    renderMap(board)
    gamePlay(board)
