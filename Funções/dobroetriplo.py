def retornarDobro(valor):
    dobro = valor * 2
    return dobro

def retornarTriplo(valor):
    triplo = valor * 3
    return triplo


def main():
    valor = int(input("Digite o seu valor"))
    dobro = retornarDobro(valor)
    triplo = retornarTriplo(valor)
    print(dobro)
    print(triplo)

main()