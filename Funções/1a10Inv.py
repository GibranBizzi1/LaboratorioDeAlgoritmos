

def inverterLista(lista):
    for i in range(len(lista)-1,-1,-1):
        print(lista[i])



def preencherLista(lista):
    for i in range(1,11):
        lista.append(i)
    return lista



def main():
    lista = []
    preencherLista(lista)
    inverterLista(lista)




main()