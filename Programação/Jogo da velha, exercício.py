def exibir_tabuleiro(tabuleiro):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(tabuleiro[i][j], "|", end=" ")
        print("\n-------------")

def verificar_vitoria(tabuleiro, jogador):
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador:
            return True
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogador:
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
    #if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][3] == jogador:  # Erro de indexação, o 3 está fora dos limites do tabuleiro, que vai de 0 á 2 
        return True
    return False

def jogar_jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador = "X"
    jogadas_restantes = 9

    while True:
        exibir_tabuleiro(tabuleiro)
        linha = int(input("Digite o número da linha (0, 1 ou 2): "))
        coluna = int(input("Digite o número da coluna (0, 1 ou 2): "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador
            jogadas_restantes -= 1
            if verificar_vitoria(tabuleiro, jogador):
                exibir_tabuleiro(tabuleiro)
                print("O jogador", jogador, "venceu!")
                break
            elif jogadas_restantes == 0:
                exibir_tabuleiro(tabuleiro)
                print("Empate!")
                break
            jogador = "O" if jogador == "X" else "X"
        else:
            print("Posição inválida. Tente novamente.")

jogar_jogo_da_velha()
