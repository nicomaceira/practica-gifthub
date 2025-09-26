# Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.
lado = float(input("Introduce el valor del lado (los dos lados iguales): "))
base_menor = float(input("Introduce el valor de la base menor: "))
base_mayor = float(input("Introduce el valor de la base mayor: "))
altura = float(input("Introduce el valor de la altura: "))
area = ((base_mayor + base_menor) * altura) / 2
perimetro = base_mayor + base_menor + 2 * lado
print(f"\nÁrea del trapecio isósceles: {area:.2f}")
print(f"Perímetro del trapecio isósceles: {perimetro:.2f}")
