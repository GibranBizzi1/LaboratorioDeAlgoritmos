

def numerosarrays(array):
    for i in range(len(array)):
        for j in range(i + 1,(len(array))):
                try:
                    if array[i] == array[j]:
                         array.pop(j)
                except:
                     print()
    return array
    

def adcNumero(array):
    for i in range(10):
        numero = int(input("Digite um numero"))
        array.append(numero)
    return array


def main():
    array = []
    adcNumero(array)
    numeros = numerosarrays(array)
    print(numeros)



main()