resposta1 = input("Telefonou para a vítima? (sim/não): ").lower()
resposta2 = input("Esteve no local do crime? (sim/não): ").lower()
resposta3 = input("Mora perto da vítima? (sim/não): ").lower()
resposta4 = input("Devia para a vítima? (sim/não): ").lower()
resposta5 = input("Já trabalhou com a vítima? (sim/não): ").lower()

if (resposta1 == "sim") + (resposta2 == "sim") + (resposta3 == "sim") + (resposta4 == "sim") + (resposta5 == "sim") == 2:
    print ("Suspeita")
elif (resposta1 == "sim") + (resposta2 == "sim") + (resposta3 == "sim") + (resposta4 == "sim") + (resposta5 == "sim") in [3, 4]:
    print ("cumplice")
elif (resposta1 == "sim") + (resposta2 == "sim") + (resposta3 == "sim") + (resposta4 == "sim") + (resposta5 == "sim") == 5:
    print ("Assasino")
else:
    print ("inocente")
