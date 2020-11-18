
def dici(nome, peso):
    return {"Nome": nome, "Peso": peso}

def maior_menor_peso(nomes_pesos, maior_menor):
    maiores_menores = []
    for M_m in nomes_pesos:
        if(M_m["Peso"] == maior_menor):
            maiores_menores.append(M_m["Nome"])
    return maiores_menores

def main():
    opcao = 's'
    nomes_pesos = []
    while(opcao != 'n'):
        nome = input('Entre com o nome: ').capitalize()
        peso = int(input('Entre com o peso, em Kg: '))
        nomes_pesos.append(dici(nome,peso))
        if(len(nomes_pesos) == 1):
            maior = peso
            menor = peso
        elif(maior < peso):
            maior = peso
        elif(menor > peso):
            menor = peso
        opcao = input('Deseja continuar? [S/N]: ').lower()

    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(f"Você cadastrou {len(nomes_pesos)} pessoa(s) !!!")
    print(f"O maior peso cadastrado foi de: {maior} e a(s) pessoa(s) com esse peso é/são: {maior_menor_peso(nomes_pesos,maior)}")
    print(f"O menor peso cadastrado foi de: {menor} e a(s) pessoa(s) com esse peso é/são: {maior_menor_peso(nomes_pesos, menor)}")

if(__name__ == '__main__'):
    main()