
def maioremenor(numeros):
    for i in range(len(numeros)):
        if i == 0:
            maior = numeros[i]
            menor = numeros[i]
        else:
            if numeros[i] > maior:
                maior = numeros[i]
            if numeros[i] < menor:
                menor = numeros[i]
    print("O maior numero é o: ", maior)
    print("O menor numero é o: ", menor)
    return


def main():
    numeros = [1,2,3,4,5,6,7,8,9,10]
    maioremenor(numeros)




main()