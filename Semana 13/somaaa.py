
def somas(numero):
    soma = 0
    for i in range(numero,0,-1):
        soma += i
    return soma





def main():
    numero = int(input("Digite um numero"))
    if numero > 0:
        sominha = somas(numero)
        print(sominha)



main()