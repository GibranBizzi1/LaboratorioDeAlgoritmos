
def mostrarSaldo(saldo):
    print(saldo)



def depositar(saldo):
    try:
        deposito = float(input("Digite o quanto quer depositar: "))
        if deposito >= 0:
            saldo = saldo + deposito
            print("Deposito Realizado com Sucesso")
            print("Seu saldo atual é de: ", saldo)
        else:
            print("Deposito não realizado")
        return saldo

    except:
        print("Erro")
        return saldo




def sacar(saldo):
    try:
        sacar = float(input("Digite o quanto quer sacar: "))
        if sacar <= saldo:
            saldo = saldo - sacar
            print("Saque realizado com sucesso")
            print("Seu saldo atual é de: ", saldo)
        else:
             print("Inválido")
        return saldo
    except:
        print("Erro")
        return saldo



def menu():
    print("○ 1 - Sacar dinheiro")
    print("○ 2 - Depositar dinheiro")
    print("○ 3 - Mostrar saldo")
    print("○ 4 - Sair")
    try:
        opcao = int(input("Digite a opção: "))
        return opcao

    except:
         print("Inválido , tente uma opção de 1 - 4")
         return 0






def main():
    saldo = 0
    while True:
        opcao = menu()
        if opcao == 1:
                saldo = sacar(saldo)
        elif opcao == 2:
                saldo = depositar(saldo)
        elif opcao == 3:
                mostrarSaldo(saldo)
        elif opcao == 4:
                print("Saindoo")
                break
        else:
            print("Opção Inválida")
            

            






main()