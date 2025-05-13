lista = []
numeros = 0

while len(lista) != 10:
    try:
        numero = int(input("Digite seu numero: "))
    except:
        print("não acontece")

    if numero not in lista:
        lista.append(numero)
    else:
        print("Digite um numero novo")

        
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        numeros += 1
        print("Seu", (numeros),"º número par é", lista[i]," e está na posição", (i))