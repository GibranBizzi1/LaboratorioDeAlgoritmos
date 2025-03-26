nota1 = float(input("Digite a sua primeira nota:"))
nota2 = float(input("Digite a sua segunda nota:"))
media = (nota1 + nota2) /2
if media >=9 and media <=10:
    print ("Parabéns você foi aprovado,sua media final foi de:",media, "você tirou nota A")
elif media >= 7.5:
    print ("Parabéns, você foi aprovado,sua media final foi de:", media, "você tirou nota B")
elif media >= 6:
    print ("Parabéns, você foi aprovado,sua media final foi de:",media, "você tirou nota C")
elif media >= 4:
    print ("Reprovado, sua media final foi de:",media,"você tirou nota D")
else:
    print ("Reprovado, sua media final foi de:",media, "você tirou nota E")