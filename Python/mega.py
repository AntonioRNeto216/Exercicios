import random
import time

print("=" * 20)
print("    Mega Sena    ")
print("=" * 20)

quantidade = int(input("Quatos jogos quer que eu sorteie? "))

print("Começando...")
print("-"*20)
time.sleep(2)

if(quantidade > 0):
    for i in range(0,quantidade):
        jogo = []
        for j in range(0,6):
            if(len(jogo) > 0):
                num = random.randrange(1,61)
                if(jogo.count(num) != 0):
                    while (jogo.count(num) != 0):
                        num = random.randrange(1, 61)
                jogo.append(num)
            else:
                nume = random.randrange(1,61)
                jogo.append(nume)

        print(f"Jogo {i+1}: {jogo}")
        time.sleep(0.5)

