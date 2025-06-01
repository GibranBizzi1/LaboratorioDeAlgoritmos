def perguntas(A,B,C):
    for i in range(20):
        resposta = input("Digite qual jornal vc mais lê, A, B ou C : ").upper()
        if resposta == "A":
            A.append(1)
        elif resposta == "B":
            B.append(1)
        elif resposta == "C":
            C.append(1)
        else:
            print("Inválido")
    return A,B,C

    




def main():
    A = []
    B = []
    C = []
    perguntaz = perguntas(A,B,C)
    print("Porcentagem Jornal A: ",(len(A)/20) * 100,"%", ", Porcentagem Jornal B: ",(len(B) / 20) * 100,"%",", Porcentagem jornal C: ",(len(C) / 20) * 100,"%")




main()