valores = []

for i in range(5):
    try:
        numero = int(input("Digite um numero"))
        valores.append(numero)
    except:
        print("Numero inteiroo")

for i in range(5):
    verificador = int(input("Digite o valor que quer verificar: "))
    if verificador in valores:
        print("Esse valor está na lista")
    else:
        print ("Esse valor não está na lista")