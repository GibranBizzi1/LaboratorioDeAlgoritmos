nome = input("Digite seu nome:")
salario = float(input("Digite qual é o seu salário"))
tempodeservico = float(input("digite por quantos anos você trabalhou"))
if tempodeservico >= 5 and salario <2000:
    print ("Você recebera um aumento de dez porcento,então seu salario com aumento é:", salario * 1.10)
elif tempodeservico >= 5 or salario <2000:
    print ("Você recebera um aumento de cinco porcento,então seu salario com aumento é:", salario * 1.05)
else:
    print ("Você não tem direito de aumento")