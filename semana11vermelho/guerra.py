import random
guardioes = []
invasores = []
resultados = []
vitoria = 0
vitoriainv = 0
while len(guardioes) != 5:
    try:
        ataque = int(input("Digite o ataque dos guardioes"))
        guardioes.append(ataque)
    except:
        print("Denovoooo, numeros inteiros")

while len(invasores) != 5:
    valor = random.randint(0,100)
    if valor not in invasores:
        invasores.append(valor)
        print("valor adicionada a invasores: ", valor)

for i in range(len(guardioes)):
    if guardioes[i] > invasores[i]:
        resultados.append(1)
        print("Os guardiões venceram")
        vitoria+= 1

    elif guardioes[i] <= invasores[i]:
        resultados.append(0)
        vitoriainv += 1
        print("Os invasores venceram")
        
print("A força dos guardiões é: ", guardioes)
print("A força dos invasores é: ", invasores)
print("A quantidade de vitórias dos guardões é:", vitoria)
print("A quantidade de vitórias dos invasores é de: ", vitoriainv)
    



    
  
