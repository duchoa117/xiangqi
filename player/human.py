from player.player import Player ,players
from gameIO import gameIO
class Human(Player):
    def __init__(self):
        Player.__init__(self)
    def play(self, board, move):
        gameIO(board, move)

def createHuman():
    h = Human()
    players.append(h)

