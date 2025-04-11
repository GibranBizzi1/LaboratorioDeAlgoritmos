pessoas = 0
idade = 0
idademaiorouigual18 = 0
somaidades = 0

while pessoas < 10:
    idade = int(input("Digite sua idade"))
    somaidades = somaidades + idade
    pessoas += 1
    if idade >= 18:
        idademaiorouigual18 += 1

print ("a soma das idades é de:",somaidades)
print ("A quantidade de pessoa maior de idade é de:", idademaiorouigual18)
        