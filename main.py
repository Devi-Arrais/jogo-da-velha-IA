from jogo_da_velha import *
from minimax import movimentoIA

jogador = 0
board = criarboard()
ganhador = verificaganhador(board)
while not ganhador:
    printBoard(board)
    print("#####################")
    if jogador == 0:
        i, j = movimentoIA(board, jogador)
    else:
        i = joogadavalida("digite a linha: ")
        j = joogadavalida("digite a coluna: ")

    if verificarespaco(board, i, j):
        fazerjogada(board, i, j, jogador)
        jogador = (jogador + 1)%2
    else:
        print("A posição ja esta ocupada")

    ganhador = verificaganhador(board)

print("=====================")
printBoard(board)
print("ganhador ", ganhador)
