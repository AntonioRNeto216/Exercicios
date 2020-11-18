
def opcoes():
    print("Usuário, deseja saber: ")
    print("(1) - A soma dos valores pares da matriz ?")
    print("(2) - A soma dos valores de uma coluna específica ?")
    print("(3) - O maior valor de uma linha ?")
    print("(0) - Sair")
    escolha = int(input("Faça sua escolha: "))
    return escolha

def main():
    matriz = []
    num_par = 0

    N = int(input("Qual o valor de N para sua matriz NxN: "))

    for i in range(0, N):
        linha = []
        for j in range(0, N):
            num = int(input(f"Digite um valor para [{i},{j}]: "))
            if(num%2 == 0):
                num_par = num_par + num
            linha.append(num)
        matriz.append(linha)

    print('-=' * 30)

    for i in range(0, N):
        for j in range(0, N):
            print(f"[{matriz[i][j]}]", end=' ')
        print(end='\n')

    escolha = opcoes()
    while(escolha != 0):
        if(escolha < 0 and escolha > 3):
            print("Desculpe, essa opcao não exite!! Tente novamente.")
        else:
            if(escolha == 1):
                print(f"A soma de números pares é: {num_par}")
            elif(escolha == 2):
                col = int(input("Qual a coluna deseja obter a soma? "))
                soma = 0
                for i in range(0,N):
                    soma = soma + matriz[i][col]
                print(f"A soma da coluna {col} é: {soma}")
            elif(escolha == 3):
                linha = int(input("Qual a linha deseja? "))
                maior = matriz[linha][0]
                for i in range(0,N):
                    if(maior < matriz[linha][i]):
                        maior = matriz[linha][i]
                print(f"O maior valor na linha {linha} é: {maior}")
        escolha = opcoes()

if(__name__ == "__main__"):
    main()