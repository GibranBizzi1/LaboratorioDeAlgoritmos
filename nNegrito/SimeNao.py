

def perguntas(sim,nao):
    for i in range(20):
        resposta = input("Digite sua resposta, S ou N").upper()
        if resposta == "S":
            sim.append(1)
        elif resposta == "N":
            nao.append(1)
        else:
            print("Numero inválido")
    return sim,nao




def main():
    sim = []
    nao = []
    perguntaz = perguntas(sim,nao)
    print("Quantidades de sim: ",len(sim), ", Quantidade de nãos: ", len(nao))



main()