import math
radio = float(input("Introduce el radio del cilindro: "))
altura = float(input("Introduce la altura del cilindro: "))
area_base = math.pi * (radio ** 2)
area_lateral = 2 * math.pi * radio * altura
area_total = 2 * area_base + area_lateral
volumen = area_base * altura
print(f"\nÁrea total del cilindro: {round(area_total, 2)}")
print(f"Volumen del cilindro: {round(volumen, 2)}")
