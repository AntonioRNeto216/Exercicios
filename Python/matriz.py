
matriz = []

N = int(input("Qual o valor de N para sua matriz NxN: "))

for i in range(0,N):
    linha = []
    for j in range(0,N):
        num = int(input(f"Digite um valor para [{i},{j}]: "))
        linha.append(num)
    matriz.append(linha)

print('-='*30)

for i in range(0,N):
    for j in range(0,N):
        print(f"[{matriz[i][j]}]", end=' ')
    print(end='\n')