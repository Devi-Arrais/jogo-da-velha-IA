from jogo_da_velha import *

def movimentoIA(board, jogador):
    possibilidades = posicaovazia(board)
    melhorvalor = None
    melhormovimento = None
    for possibilidade in possibilidades:
        board[possibilidade[0]][possibilidade[1]] = token[jogador]
        valor = minimax(board, jogador)
        board[possibilidade[0]][possibilidade[1]] = branco

        if melhorvalor is None:
            melhorvalor = valor
            melhormovimento = possibilidade
        elif jogador == 0:
            if valor > melhorvalor:
                melhorvalor = valor
                melhormovimento = possibilidade
        elif jogador == 1:
            if valor < melhorvalor:
                melhorvalor = valor
                melhormovimento = possibilidade


    return melhormovimento[0], melhormovimento[1]

def posicaovazia(board):
    posicao = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == branco:
                posicao.append([i, j])

    return posicao

score = {
    "EMPATE": 0,
    "X": 1,
    "O": -1
}
def minimax(board, jogador):
    global score
    ganhador = verificaganhador(board)
    if ganhador:
        return score[ganhador]

    jogador = (jogador + 1)%2

    possibilidades = posicaovazia(board)
    melhorvalor = None
    for possibilidade in possibilidades:
        board[possibilidade[0]][possibilidade[1]] = token[jogador]
        valor = minimax(board, jogador)
        board[possibilidade[0]][possibilidade[1]] = branco

        if melhorvalor is None:
            melhorvalor = valor
        elif jogador == 0:
            if valor > melhorvalor:
                melhorvalor = valor
        elif jogador == 1:
            if valor < melhorvalor:
                melhorvalor = valor

    return melhorvalor
