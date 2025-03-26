nota1 = float(input("digite sua primeira nota"))
nota2 = float(input("digite sua segunda nota"))
frequencia = float(input("digite sua frequencia em"))
medianota = (nota1 + nota2) / 2
if medianota >= 7 and frequencia >= 75:
    print ("Aprovado")
elif medianota >= 4 and medianota < 7 and frequencia>=75:
    print ("exame")
else:
    print ("reprovado")