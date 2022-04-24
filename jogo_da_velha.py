branco = " "
token = ["X", "O"]
def criarboard():
    board = [
        [branco, branco, branco],
        [branco, branco, branco],
        [branco, branco, branco]

    ]
    return board

def printBoard(board):
    for i in range(3):
        print("|".join(board[i]))
        if i < 2:
            print("-----")

def joogadavalida(mensagem):
    try:
        n = int(input(mensagem))
        if n >= 1 and n <= 3:
            return n - 1
        else:
            print("Numero invalido digite entre 3 e 1")
            return joogadavalida(mensagem)
    except:
        print("Numero invalido")
        jogadavalida(mensagem)

def verificarespaco(board, i, j):
    if board[i][j] == branco:
        return True
    else:
        return False

def fazerjogada(board, i, j, jogador):
    board[i][j] = token[jogador]

def verificaganhador(board):
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != branco:
            return board[i][0]

    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != branco:
            return board[0][i]

    if board[0][0] != branco and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] != branco and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]

    for i in range(3):
        for j in range(3):
            if board[i][j] == branco:
                return False
    return "EMPATE"
