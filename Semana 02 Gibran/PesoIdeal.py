altura = float(input("digite qual é sua altura"))
sexo = input("seu sexo é (homem ou mulher)")
if sexo == "homem":
    pesoideal= (72.7 * altura) - 58
    print ("seu peso ideal é", pesoideal)
else:
    pesoideal= (62.1 * altura) - 44.7
    print ("seu peso ideal é", pesoideal)