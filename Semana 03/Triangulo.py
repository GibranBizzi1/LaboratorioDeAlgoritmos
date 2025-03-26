lado1 = float(input("Digite quantos lados tem o triangulo"))
lado2 = float(input("Digite quantos lados tem o triangulo"))
lado3 = float(input("Digite quantos lados tem o triangulo"))
if lado1 == lado2 == lado3:
    print ("Triangulo Equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print ("Triangulo isosceles")
else:
    print ("triangulo escaleno")