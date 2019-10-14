from player.player import players
from map import renderMap
def gamePlay(board):
        players[0].play(board)
        renderMap(board)
        print("Machine is thinking.....")
        players[1].play(board)