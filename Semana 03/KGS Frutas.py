kg_morango = float(input("Digite a quantidade de morangos (em Kg): "))
kg_maça = float(input("Digite a quantidade de maçãs (em Kg): "))

if kg_morango <= 5:
    preco_morango = 2.50 * kg_morango
else:
    preco_morango = 2.20 * kg_morango

if kg_maça <= 5:
    preco_maca = 1.80 * kg_maca
else:
    preco_maça = 1.50 * kg_maça

total = preco_morango + preco_maça

if (kg_morango + kg_maça) > 8 or total > 25:
    total *= 0.90 

print("O valor total a ser pago é: R$", total)
