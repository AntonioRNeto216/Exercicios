
frase = input("Digite a expressão: ")

abre = []
fecha = []

for letra in frase:
    if(letra == '('):
        abre.append('(')
    elif(letra == ')'):
        fecha.append(')')

if(len(abre) == len(fecha)):
    print("Sua expressão é válida!!!")
else:
    print("Sua expressão não é válida")