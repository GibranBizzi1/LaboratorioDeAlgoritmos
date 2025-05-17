numerosinteiros = []
maior = 0
menor = 0
posiçãoMAIOR = 0
posiçãoMENOR = 0

for i in range(5):
    try:
        numero = int(input("Digite um numero inteiro"))
        numerosinteiros.append(numero)
    except:
        print("tente denovo")
    
    if i == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
            posiçãoMAIOR = i
    
        if numero < menor:
            menor = numero
            posiçãoMENOR = i

print("O maior numero é: ", maior,"sua posição é: ",posiçãoMAIOR)
print("O menor numero é : ", menor,"sua posição é: ", posiçãoMENOR)