import pygame
from jogo_da_velha import *
from minimax import *

pygame.font.init()

def draw_board(win, board):
    height = 500
    width = 500
    tamanho = 500/3

    for i in range(1, 3):
        pygame.draw.line(win, (0, 0, 0), (0, i * tamanho), (width, i * tamanho), 3)
        pygame.draw.line(win, (0, 0, 0), (i * tamanho, 0), (i * tamanho, height), 3)
    for i in range(3):
        for j in range(3):
            font = pygame.font.SysFont("comicsans", 100)
            x = j * tamanho
            y = i * tamanho

            text = font.render(board[i][j], 1, (128, 0, 0))
            win.blit(text, ((x + 75), (y + 75)))

def redraw_window(win, board):
    win.fill((255, 255, 255))
    draw_board(win, board)

def main():
    win = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Jogo da Velha")

    board = criarboard()
    redraw_window(win, board)
    pygame.display.update()

    jogador = 0

    ganhador = verificaganhador(board)

    while not ganhador:
        print(board)
        if jogador == 0:
            i, j = movimentoIA(board, jogador)
        else:
            jogou = False
            while not jogou:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                    elif event.type == pygame.MOUSEBUTTONUP:
                        pos =pygame.mouse.get_pos()
                        i = int(pos[1]/150)
                        j = int(pos[0]/150)
                        print(i, j)
                        jogou = True

        if verificarespaco(board, i, j):
            fazerjogada(board, i, j, jogador)
            jogador = (jogador + 1)%2

        ganhador = verificaganhador(board)
        redraw_window(win, board)
        pygame.display.update()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


main()
