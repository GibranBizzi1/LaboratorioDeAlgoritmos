numero1 = int(input("Digite primeiro numero"))
numero2 = int(input("Digite segundo numero"))

while numero1 > numero2:
    numero1 = int(input("Digite primeiro numero"))
    numero2 = int(input("Digite segundo numero"))

for n in range (numero1 + 1, numero2):
    if n % 2 == 0:
        print (n)
    
