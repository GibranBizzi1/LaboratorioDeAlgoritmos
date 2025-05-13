maiorque100 = []
numeros = []
tamanho = len(numeros)


while len(numeros) != 10:
    try:
        numero = int(input("Digite o número: "))
    except:
         print("Denoovo")


    if numero not in numeros:
        numeros.append(numero)
    else:
         print("Digite um numero não digitado ainda")
         
    if numero >= 100 and numero not in maiorque100:
            maiorque100.append(numero)

print("numeros digitados que são maiores que 100:", maiorque100)