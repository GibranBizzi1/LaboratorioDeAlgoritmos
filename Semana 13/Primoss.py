

def primoo(numero):
    if numero == 1:
        return False
    for i in (2,numero):
        if numero == 2:
            return True
        if numero % i == 0:
            return False
    return True
    


def main():
    numero = int(input("Digite seu numero"))
    bababoy = primoo(numero)
    print(bababoy)



main()