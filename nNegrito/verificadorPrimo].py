def verifica_primos():
    numeros = []
    primos = []

    for i in range(10):
        numeros.append(int(input("Digite um número: ")))

    for numero in numeros:
        eh_primo = True
        if numero <= 1:
            eh_primo = False
        else:
            for i in range(2, numero):
                if numero % i == 0:
                    eh_primo = False
        if eh_primo:
            primos.append(numero)

    print("Números primos:", primos)

def main():
    verifica_primos()
    
main()
