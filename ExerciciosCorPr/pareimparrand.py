import random

numeros = []
pares = 0
impares = 0

for i in range(10):
    numeros.append(random.randint(1, 50))

for i in numeros:
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1
        
print(numeros)
print("A quantidade de numeros pares são de: ", pares)
print("A quantidade de numeros impares são de:",impares)
