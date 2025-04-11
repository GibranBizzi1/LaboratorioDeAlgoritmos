saldo = float(input("digite seu saldo atual"))
opcao = 0
while opcao != 4:
    print ("1 - Sacar")
    print ("2 - Depositar")
    print ("3 - Saldo")
    print ("4 - Sair")
    opcao = int(input("Digite sua opção"))
    
    if opcao == 1:
        valorsaque = float(input("Digite o quanto vc quer sacar"))
        saque = saldo - valorsaque
        print ("Você sacou:", valorsaque,"você ainda tem:", saque, "reais disponiveis")

    elif opcao == 2:
        Deposito = float(input("Digite o quanto você quer depositar"))
        print ("o seu saldo atual é de:",saldo + Deposito)
    
    elif opcao == 3:
        print ("o seu saldo atual é de:",saldo)