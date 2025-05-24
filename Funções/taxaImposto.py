
def somaimposto(taxa,custo):
    valorfinal = custo + custo * (taxa / 100)
    return valorfinal



def main():
    try:
        taxa = float(input("Porcentagem da taxa" ))
        custo = float(input("Digite o custo do produto"))
    except:
        print("tente denovo")
        
    valorfinal = somaimposto(taxa,custo)
    print(valorfinal)





main()