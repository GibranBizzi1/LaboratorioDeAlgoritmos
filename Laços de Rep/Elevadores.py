moradores = 0
elevadorA = 0
elevadorB = 0
elevadorC = 0

while moradores < 10:
    Elevador = input("Digite qual elevador você mais usa, A, B ou C:").upper ()
    moradores += 1

    if Elevador == "A":
        elevadorA += 1

    elif Elevador == "B":
        elevadorB += 1

    elif Elevador == "C":
        elevadorC += 1

print("o total de pessoas que utilizam o A é de:",elevadorA,"o total de pessoas que utilizam o B é de:",elevadorB,"o total de pessoas que utilizam o C é de:",elevadorC)
print ("A porcentagem que utiliza o elevador A é de:", (elevadorA / 10)* 100,"%")     
print ("A porcentagem que utiliza o elevador B é de:", (elevadorB / 10)* 100,"%")   
print ("A porcentagem que utiliza o elevador C é de:", (elevadorC / 10)* 100,"%")   
