
def convertido(graus):
     Fahrenheit = (graus * 9/5) + 32
     return Fahrenheit




def main():
    graus = float(input("digite quantos graus esta"))
    grausconvertido = convertido(graus)
    print(grausconvertido)



main()