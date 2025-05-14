VetorA = []

for i in range(15):
    try:
        valor = int(input("Digite um valor inteiro"))

    except:
        print("valor inteirooo")
    
    if valor in VetorA:
        print ("Esse numero já esta na lista, digite um valor que não está na lista")
        valor = int(input("Digite um valor inteiro"))
    else:
        VetorA.append(valor)

print(VetorA)














        
