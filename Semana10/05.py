opcao = 0
valores = []

while opcao != 5:
    print("1- Inserir valor")
    print("2- Remover valor")
    print("3- Listar valor")
    print("4- Listar todos os vlores")
    print("5- Sair")
    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        valor = int(input("Valor para inserir: "))
        valores.append(valor)
    elif opcao == 2:
        try:
            valor = int(input("Valor para retirar: "))
            valores.remove(valor)
        except:
            print("Não encontrado")

    elif opcao == 3:
        print(valores)

    elif opcao == 4:
        for i in range(0, len(valores)):
            print(valores[i])
    else:
        print("Saindo, thanks")