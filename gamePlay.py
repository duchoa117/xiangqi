from player.player import players
def gamePlay(board):
    for p in players:
        p.play(board)