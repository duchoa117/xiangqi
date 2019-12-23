import socket
import time
from map import board
import pygame
pygame.init()
canvas = pygame.display.set_mode((640,710))
pygame.display.set_caption("TEAM_AI")
clock = pygame.time.Clock()
bg = pygame.image.load('chess/images/board.jpg')
canvas.blit(bg, (0, 0))
# for c in board.activeChesses:
#     c.imageRender(canvas)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 9999))
s.listen(5)
while True:
    canvas.blit(bg, (0, 0))
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    while True:
        canvas.blit(bg, (0, 0))
        msg = input("input: ")
        clientsocket.send(bytes(msg,"utf-8"))
        receive = clientsocket.recv(1024).decode("utf-8")
        print("CLIENT: ", receive)
        canvas.fill((0, 0, 0))
        canvas.blit(bg, (0, 0))
        for c in board.activeChesses:
            c.imageRender(canvas)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
        for c in board.activeChesses:
            c.imageRender(canvas)
        print("White machine is thinking.....")
        players[2].play(board, turn)
        turn +=1

        canvas.fill((0, 0, 0))
        canvas.blit(bg, (0, 0))
        for c in board.activeChesses:
            c.imageRender(canvas)
        print("Black machine is thinking.....")
        players[1].play(board, turn) 
        turn += 1
        pygame.display.flip()
        clock.tick(60)

    
    
