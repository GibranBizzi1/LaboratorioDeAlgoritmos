listaA = []
listaB = []

while len(listaA) != 10:
    try:
        numero = int(input("Digite seu numero: "))
    except:
        print("denovoo")

    if numero not in listaA:
        listaA.append(numero)
    else:
        print("Digite um valor não digitado anteriormente")

for i in range(9,-1, -1 ):
    listaB.append(listaA[i])
print(listaA)
print(listaB)