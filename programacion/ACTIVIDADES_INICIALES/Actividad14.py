
import math
diametro = float(input("Introduce el diámetro del círculo: "))
radio = diametro / 2
area = math.pi * (radio ** 2)
perimetro = math.pi * diametro
print(f"\nÁrea del círculo: {round(area, 1)}")
print(f"Perímetro del círculo: {round(perimetro, 1)}")
