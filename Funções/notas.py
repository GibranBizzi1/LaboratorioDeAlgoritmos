def somanotas(notas):
    soma = 0
    for i in notas:
        soma = soma + i
    return soma


def dividirasnotas(soma):
    divisao = soma / 5
    return divisao


def adicionarNotas(notasLista):
    for i in range(5):
        notas = float(input("Digite sua nota"))
        notasLista.append(notas)
    return notasLista


def main():
    notasLista = []
    notas = adicionarNotas(notasLista)
    soma = somanotas(notas)
    divisao = dividirasnotas(soma)
    if divisao >= 7:
        print("Aprovado")
    elif divisao >= 4 and divisao < 7:
        print("Em exame")
    else:
        print("Reprovado")

main()
