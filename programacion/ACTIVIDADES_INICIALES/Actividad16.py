# Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso(raíz y división)
import math
numero = float(input("Introduce un número para calcular su raíz cuadrada: "))
raiz = math.sqrt(numero)
division_entera = int(raiz // 2)
print(f"\nRaíz cuadrada de {numero}: {round(raiz, 2)}")
print(f"Resultado entero de dividir la raíz entre 2: {division_entera}")