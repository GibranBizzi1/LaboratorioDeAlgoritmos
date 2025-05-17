vetor = []
opcao = 0
maiorqX = 0

while opcao <= 8:
    print("1 - Inserir item")
    print("2 - Listar itens")
    print("3 - Retirar item")
    print("4 - Retirar todos os itens")
    print("5 - Contar quantos itens são maiores que um valor X (onde X é informado pelo usuário)")
    print("6 - Verificar se um determinado número (informado pelo usuário) está presente no array")
    print("7 - Encontrar o maior e o menor item do array")
    print("8 - Sair")
    opcao = int(input("Digite a opção desejada, de 1 a 8: "))
    
    if opcao == 1:
        try:
            numero = int(input("Digite o seu numero, apenas numeros pares: "))
            if numero % 2 == 0:
                vetor.append(numero)
            else:
                print("Erro, numero impar")
        except:
            print("Erro")
    
    elif opcao == 2:
        print(vetor)
    
    elif opcao == 3:
        print(vetor)
        remover = int(input("Deseje o numero que queira remover: "))
        try:
            if remover in vetor:
                vetor.remove(remover)
                print(vetor)
            else:
                print("Esse numero não existe na lista")
        except:
            print("Erro")
    
    elif opcao == 4:
        vetor.clear()
        print("Você removeu todos os elementos da lista")
        maiorqx = 0

    elif opcao == 5:
        x = int(input("Digite o valor q quer ver a quantia de numeros maiores"))
        for i in range(len(vetor)):
            if vetor[i] > x:
                maiorqX += 1
        print("A quantidade de numeros maiores que x é de: ", maiorqX)
    
    elif opcao == 6:
        numeropresent = int(input("Digite o numero q vc quer ver se está no vetor"))
        if numeropresent in vetor:
            print("Esse numero está presente no vetor")
        else:
            print("Esse numero não está presente no vetor")
    
    elif opcao == 7:
        if not vetor:
            print("O vetor está vazio.")
        else:
            maior = vetor[0]
            menor = vetor[0]
            for i in vetor:
                if i > maior:
                    maior = i
                if i < menor:
                    menor = i
            print("O maior número presente no vetor é:", maior)
            print("O menor número presente no vetor é:", menor)

    elif opcao == 8:
        print("Saindoo")
    
    else:
        print("Opção Inválida")

    

    

        

