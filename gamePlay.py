from player.player import players
from map import renderMap
def gamePlay(board):
        print("White Machine is thinking.....")
        players[1].play(board, 1)
        renderMap(board)
        print("Balck Machine is thinking.....")
        players[1].play(board, 0)