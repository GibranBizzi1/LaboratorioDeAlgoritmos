a = 0
b = 0
c = 0

for n in range (1,21):
    jornal = input("Digite qual vc mais lê, A, B ou C").upper()
    if jornal == "A":
        a += 1
    elif jornal == "B":
        b += 1
    elif jornal == "C":
        c += 1
    else:
        print ("inválido")

print ("A porcentagem que lê o jornal a é de:", (a / 20)* 100)
print ("A porcentagem que lê o jornal b é de:", (b / 20)* 100)
print ("A porcentagem que lê o jornal c é de:", (c / 20)* 100)