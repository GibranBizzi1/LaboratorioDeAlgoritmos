numeros = []

for i in range(5):
    num = int(input("Digite o numero"))
    numeros.append(num)

repetido = 0 

for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        if numeros[i] == numeros[j]:
            repetido = 1

if repetido == 0:
    print("Todos os elementos são distintos.")
else:
    print("Existem elementos repetidos.")
