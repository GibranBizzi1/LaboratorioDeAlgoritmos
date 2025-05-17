lista1 = []
lista2 = []
lista3 = []

for i in range(5):
    try:
        numero = int(input("Digite o seu numero"))
        lista1.append(numero)
    except:
        print("Tente denovoo")

for i in range(5):
    try:
        numero = int(input("Digite o seu numero da lista 2: "))
        lista2.append(numero)
    except:
        print("Tente denovoo")
    
for i in range(5):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print(lista3)
