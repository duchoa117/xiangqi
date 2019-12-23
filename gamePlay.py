from map import renderMap, board
from chess.chess import Chess
from chess import chess
from point.point import Point
from player.player import players
import pygame
import socket
import re
def youSecond(board):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.1.156', 2222))
        run = True
        turn = 1
        new_msg = True
        while run:
                renderMap(board)
                received = s.recv(1024).decode("utf-8")
                move = re.findall(r'\d+', received)
                while(len(move) != 4 or received[0] != 'B'):
                    received = s.recv(1024).decode("utf-8")
                    move = re.findall(r'\d+', received)
                move = move[0]+" "+move[1]+" "+move[2]+" "+move[3]
                if new_msg:
                        new_msg = False
                print("SERVER: ", move)

                players[0].play(board, move)
                new_msg = True
                turn +=1
                renderMap(board)
                print("Black machine is thinking.....")
                myTurn = players[2].play(board, turn)
                s.send(("RED:"+myTurn+":"+"Chat\n").encode())
                turn += 1
def youFrist(board):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("192.168.1.156", 2222))
        run = True
        turn = 1
        while run:
                renderMap(board)
                print("Red machine is thinking.....")
                myTurn = players[1].play(board, turn)
                turn +=1
                renderMap(board)
                s.send(("RED:"+myTurn+":"+"Chat\n").encode())
                move = s.recv(1024).decode("utf-8")
                while(move[0] == "R"):
                    move = s.recv(1024).decode("utf-8")
                # print(move)
                move = re.findall(r'\d+', move)
                move = move[0]+" "+move[1]+" "+move[2]+" "+move[3]
                # print(move)
                players[0].play(board, move) 
                turn += 1
def matrixLoad(board):
    run = True
    turn = 1
    while run:
        renderMap(board)
        print("White machine is thinking.....")
        players[2].play(board, turn)
        turn +=1
        renderMap(board)
        print("Black machine is thinking.....")
        players[1].play(board, turn) 
        turn += 1

def pygameLoad(board):
    pygame.init()
    run = True
    turn = 1
    canvas = pygame.display.set_mode((640,710))
    pygame.display.set_caption("TEAM_AI")
    clock = pygame.time.Clock()
    bg = pygame.image.load('/Users/apple/Desktop/ai:mlPr/xiangqi/chess/images/board.jpg')
    while run:
        # 1. Event processing
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


