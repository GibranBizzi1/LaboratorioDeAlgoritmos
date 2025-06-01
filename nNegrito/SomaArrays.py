

def somadados(array1,array2,array3):
    soma = 0
    for i in range(len(array1)):
        soma = array1[i] + array2[i]
        array3.append(soma)
    
    return array3



def preencher(array1,array2):
    for i in range(5):
        numero1 = int(input("digite o numero da primeira lista"))   
        numero2 = int(input("digite o numero da segunda lista"))
        array1.append(numero1)
        array2.append(numero2)

    return array1,array2



def main():
    array1 = []
    array2 = []
    array3 = []
    preencher(array1,array2)
    lista3 = somadados(array1,array2,array3)
    print(lista3)




main()