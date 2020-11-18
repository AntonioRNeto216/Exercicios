import random

def main():
    print("=======================")
    print("       Bem Vindo       ")
    print("=======================")

    print(" [0] - Pedra ")
    print(" [1] - Papel ")
    print(" [2] - Tesoura ")

    escolha = int(input(" Faça sua escolha: "))
    jogo = {0: "Pedra", 1: "Papel", 2: "Tesoura"}

    if (escolha > 2 or escolha < 0):
        print(" Desculpe, essa opção é inválida !! ")
    else:
        escolha_pc = random.randrange(0, 3)
        if (escolha == escolha_pc):
            print(" EMPATE ")
        elif ((escolha == 0 and escolha_pc == 2) or (escolha == 1 and escolha_pc == 0) or (
                escolha == 2 and escolha_pc == 1)):
            print(f" Você jogou: {jogo[escolha]} e o Computador jogou {jogo[escolha_pc]}")
            print(" Parabéns Usuário !! Você ganhou !!")
        else:
            print(f" Você jogou: {jogo[escolha]} e o Computador jogou {jogo[escolha_pc]}")
            print(" Que pena Usuário. Você perdeu ;C")


if(__name__ == "__main__"):
    main()
