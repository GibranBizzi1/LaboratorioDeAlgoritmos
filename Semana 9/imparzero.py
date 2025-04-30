par = 0
impar = 0
zero = 0

for n in range (1,11):
    numero = int(input("Digite nmr"))
    if numero == 0:
        zero += 1
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
    
print ("A quantidade de numeros par:", par)
print ("A quantidade de numeros impar:", impar)
print ("A quantidade de numeros zero:", zero)