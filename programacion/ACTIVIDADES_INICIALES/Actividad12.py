
lado = float(input("Introduce el valor del lado (los dos lados iguales): "))
base_menor = float(input("Introduce el valor de la base menor: "))
base_mayor = float(input("Introduce el valor de la base mayor: "))
altura = float(input("Introduce el valor de la altura: "))
area = ((base_mayor + base_menor) * altura) / 2
perimetro = base_mayor + base_menor + 2 * lado
print(f"\nÁrea del trapecio isósceles: {area:.2f}")
print(f"Perímetro del trapecio isósceles: {perimetro:.2f}")
