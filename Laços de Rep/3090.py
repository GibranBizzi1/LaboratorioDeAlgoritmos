numeros = 0
quantidadedenumeros = 0
n30_90 = 0
somanumeros = 0

while quantidadedenumeros < 10:
    numeros = int(input("Digite seu numero"))
    somanumeros = somanumeros + numeros
    quantidadedenumeros += 1
    if numeros >= 30 and numeros <= 90:
        n30_90 += 1

print ("A soma dos numeros é de:", somanumeros)
print ("A quantidade de numeros entre 30 e 90 são:", n30_90)