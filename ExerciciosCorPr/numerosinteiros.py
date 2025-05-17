numerosinteiros = []
soma = 0

for i in range(5):
    try:
        numero = int(input("Digite um numero inteiro"))
        numerosinteiros.append(numero)
        soma += numero
    except:
        print("tente denovo")

print("A soma dos numeros é de:", soma)
print("A media dos numeros é de:",soma / len(numerosinteiros))
    