import random

def jogar_pedra_papel_tesoura():
    opcoes = ["Pedra", "Papel", "Tesoura"]
    
    while True:
        print("Escolha uma opção:")
        for i, opcao in enumerate(opcoes):
            print(f"{i + 1}. {opcao}")
        
        escolha_jogador = int(input("Sua escolha (Digite o número correspondente): "))
        escolha_jogador -= 1
        
        if escolha_jogador < 0 or escolha_jogador >= len(opcoes):
            print("Opção inválida. Tente novamente.\n")
            continue
        
        escolha_computador = random.randint(0, 2)
        
        print("Jogador escolheu:", opcoes[escolha_jogador])
        print("Computador escolheu:", opcoes[escolha_computador])
        
        resultado = verificar_vencedor(escolha_jogador, escolha_computador)
        
        if resultado == 0:
            print("Empate!\n")
        elif resultado == 1:
            print("Você venceu!\n")
            #print("Você perdeu!\n")  
        else:       #O erro foi que ele inverteu as mensagens, colocando quando a pontuação é positiva, perdeu e negativa
            print("Você perdeu!\n")
            #print("Você venceu!\n")  
        
        jogar_novamente = input("Deseja jogar novamente? (s/n): ")
        if jogar_novamente.lower() != "s":
            break

def verificar_vencedor(escolha_jogador, escolha_computador):
    if (
        (escolha_jogador == 0 and escolha_computador == 2) or
        (escolha_jogador == 1 and escolha_computador == 0) or
        (escolha_jogador == 2 and escolha_computador == 1)
    ):
        return 1
    elif escolha_jogador == escolha_computador:
        return 0
    else:
        return -1

jogar_pedra_papel_tesoura()
