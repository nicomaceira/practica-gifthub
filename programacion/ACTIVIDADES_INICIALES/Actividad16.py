import math
numero = float(input("Introduce un número para calcular su raíz cuadrada: "))
raiz = math.sqrt(numero)
division_entera = int(raiz / 2)
print(f"\nRaíz cuadrada de {numero}: {round(raiz, 2)}")
print(f"Resultado entero de dividir la raíz entre 2: {division_entera}")