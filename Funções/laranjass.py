def precoMe12(laranjas):
    valorfme12 = laranjas * 0.40
    return valorfme12

def precoMA12(laranjas):
    valorfma12 = laranjas * 0.25
    return valorfma12


def main():
    laranjas = int(input("Quantas laranjas quer"))
    if laranjas <= 12:
        valorfinal = precoMe12(laranjas)
        print(laranjas)
        print(valorfinal)
    else:
        valorfinal2 = precoMA12(laranjas)
        print(laranjas)
        print(valorfinal2)



main()