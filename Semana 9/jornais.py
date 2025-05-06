a = 0 
b = 0
c = 0

for n in range(1, 21):
    jornal = input("Digite qual você mais lê, A, B ou C: ").upper()
    
    if jornal == "A":
        a = a + 1
    elif jornal == "B":
        b = b + 1
    elif jornal == "C":
        c = c + 1
    else:
        print("Invalido")

porc_a = (a * 100) / 20
porc_b = (b * 100) / 20
porc_c = (c * 100) / 20

if porc_a <= porc_b and porc_a <= porc_c:
    print("A:", porc_a)
    if porc_b <= porc_c:
        print("B:", porc_b)
        print("C:", porc_c)
    else:
        print("C:", porc_c)
        print("B:", porc_b)

elif porc_b <= porc_a and porc_b <= porc_c:
    print("B:", porc_b)
    if porc_a <= porc_c:
        print("A:", porc_a)
        print("C:", porc_c)
    else:
        print("C:", porc_c)
        print("A:", porc_a)

else:
    print("C:", porc_c)
    if porc_a <= porc_b:
        print("A:", porc_a)
        print("B:", porc_b)
    else:
        print("B:", porc_b)
        print("A:", porc_a)
