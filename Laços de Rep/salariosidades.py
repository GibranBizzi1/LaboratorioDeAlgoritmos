habitantes = 0
idade = 0
somasalarios = 0
Fcomsalarioate10000 = 0
maioridade = None
menoridade = None


while habitantes < 10:
    idade = int(input("Digite sua idade"))
    sexo = input("Qual seu sexo? F ou M").upper ()
    salario = float(input("Digite seu salario"))
    somasalarios = somasalarios + salario
    habitantes += 1
    
    if sexo == "F" and salario <=10000:
        Fcomsalarioate10000 += 1

    if maioridade is None or idade > maioridade:
        maioridade = idade

    if menoridade is None or idade < menoridade:
        menoridade = idade
        

print ("A média salarial é de:", somasalarios / 10)
print ("A quantidade de mulheres que recebem até 1000 é de:",Fcomsalarioate10000)
print ("A menor idade é:", menoridade, "e a maior idade é:",maioridade)
