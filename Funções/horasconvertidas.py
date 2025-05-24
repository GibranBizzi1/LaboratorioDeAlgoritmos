
def mostrarHora(horasConvertidas, minutos):
    if horasConvertidas <= 0 and horasConvertidas <12:
        print(horasConvertidas,":",minutos,"A.M")
    else:
        print(horasConvertidas,":",minutos,"P.M")




def converter(horas,minutos):
    if horas >= 12:
        horasConvertidas = (horas - 12)
    else:
        horasConvertidas = (horas + 12)
    return horasConvertidas



def main():
    try:
        horas = int(input("Digite as horas 0-23: "))
        minutos = int(input("Digite os minutos 0-59: "))
        if horas >= 0 and horas <23 and minutos >= 0 and minutos < 59:
            HorasConvertidas = converter(horas,minutos)
    except:
        print("Tente denovo")
    amostrarhora = mostrarHora(HorasConvertidas, minutos)
  



main()