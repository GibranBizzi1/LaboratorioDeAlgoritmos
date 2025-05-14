valores = [1,2,3,4,5,6]
resultado= []
multiplicador = int(input("Digite o valor o qual você quer multiplicar"))

for i in range(6):
    resultado1 = valores[i] * multiplicador
    resultado.append(resultado1)
    
print(resultado)