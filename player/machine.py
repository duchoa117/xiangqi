from player.player import Player , players
from chess.chess import chesses
from random import choice
class Machine(Player):
    def __init__(self):
        Player.__init__(self)
    def play(self):
        while True:
            c = choice(chesses)
            if(not c.white):
                if(c.active):
                    if(c.shape != "."):
                        break
        c.positiveMove()
        c.move(choice(c.pMove))
def createMachine():
    m = Machine()
    players.append(m)