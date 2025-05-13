maiorq30 = []
soma30 = 0
soma = 0
numeros = []


for i in range(0, 9):
    n = int(input("Digite o número: "))
    numeros.append(n)
    if n > 30:
        maiorq30.append(n)
        soma30 += n
    soma += n


print("Valores: ",numeros)
print("Valores maiores que trinta:", maiorq30)
print("Soma dos valores maiores que 30:", soma30)
print("Soma de todos os numeros: ",soma)