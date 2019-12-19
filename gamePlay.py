from player.player import players
from map import renderMap
turn = 1

def gamePlay(board):
        global turn 
        print("White machine is thinking.....")
        players[2].play(board, turn)
        # players[0].play(board)
        
        turn +=1
        renderMap(board)
        
        
        print("Black machine is thinking.....")
        players[1].play(board, turn) 
        turn += 1


