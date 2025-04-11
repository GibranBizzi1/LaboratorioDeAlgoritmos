idade = 0
quantidadedeidades = 0
maiordeidade = 0
somaidades = 0
idadeentre10e30anos = 0

while quantidadedeidades < 7:
    idade = int(input("digite sua idade"))
    quantidadedeidades += 1
    somaidades = somaidades + idade

    if idade >= 18:
        maiordeidade += 1

        if idade >= 10 and idade <= 30:
            idadeentre10e30anos += 1

print ("A soma das idades é:", somaidades)
print ("A média das idades é:", somaidades / quantidadedeidades)
print("A porcentagem de idades de 10 a 30 anos é de:", (idadeentre10e30anos / quantidadedeidades) * 100, "%")
