dentro = 0
fora = 0

for n in range (1,11):
    numero = int(input("Digite nmr"))
    if numero >= 10 and numero <= 20:
        dentro += 1
    else:
        fora += 1

print ("A quantidade de nmrs no intwervalo é de:",dentro)
print ("A quantidade de nmrs fora do intwervalo é de:",fora)