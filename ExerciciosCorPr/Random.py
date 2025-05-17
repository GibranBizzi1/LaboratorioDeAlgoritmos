import random

numeros = []
for i in range(10):
    numeros.append(random.randint(1, 100))

for i in numeros:
    if i % 2 == 0:
        print("Numeros pares : ", i)
