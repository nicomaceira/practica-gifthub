#Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales
import math
radio = float(input("Introduce el radio del cilindro: "))
altura = float(input("Introduce la altura del cilindro: "))
area_base = math.pi * (radio ** 2)
area_lateral = 2 * math.pi * radio * altura
area_total = 2 * area_base + area_lateral
volumen = area_base * altura
print(f"\nÁrea total del cilindro: {round(area_total, 2)}")
print(f"Volumen del cilindro: {round(volumen, 2)}")
