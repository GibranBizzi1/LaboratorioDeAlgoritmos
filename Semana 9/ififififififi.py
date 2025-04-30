mulherescond = 0
azul = 0
verde = 0
olhcastanho = 0
cabcastanho = 0
loiro = 0
cabpreto = 0
maioridade = 0
F = 0
M = 0

for n in range (1,16):
    if n == 1:
        maioridade = maioridade
    else:
        if idade > maioridade:
            maioridade = idade
        
    sexo = input("Digite qual seu sexo M ou F").upper()
    cordoseyes = input("Digite a cor do seus olhos:A (azuis), V (verdes) e C (castanhos)").upper()
    cordohair = input("Digite a cor do seu cabelo:L (loiros), C (castanhos) e P (pretos)").upper()
    idade = int(input("Digite sua idade"))

    if sexo == "F" and idade >= 18 and idade <= 35 and cordoseyes == "V" and cordohair == "L":
        mulherescond += 1
    
    if cordohair == "L":
        loiro += 1
    elif cordohair == "C":
        olhcastanho += 1
    elif cordohair == "P":
        cabpreto += 1
    
    if cordoseyes == "A":
        azul += 1
    elif cordoseyes == "V":
        verde += 1
    elif cordoseyes == "C":
        olhcastanho += 1
    
    if sexo == "F":
        F += 1
    elif sexo == "M":
        M += 1


print ("A maioridade do grupo é:", maioridade)
print ("A quantidade de mulheres com aquelas especificações é de:", mulherescond)
print ("A porcentagem de pessoas com olhos azuis é de:", (azul / 15) *100)
print ("A porcentagem de pessoas com olhos verdes é de:", (verde / 15) *100)
print ("A porcentagem de pessoas com olhos azuis é de:", (olhcastanho / 15) *100)
print ("A porcentagem de loiros é de:", (loiro / 15) * 100)
print ("A porcentagem de castanhos é de:", (cabcastanho / 15) * 100)
print ("A porcentagem de cabelos pretos é de:", (cabpreto / 15) * 100)
print ("A porcentagem de mulheres é de:", (F / 15) *100)
print ("A porcentagem de homens é de:", (M / 15) *100)

