# Introduce por teclado dos números y muestre por pantalla la siguiente información: cociente, resto y si el dividendo es par o impar.
dividendo = int(input("Introduce el dividendo: "))
divisor = int(input("Introduce el divisor: "))
cociente = dividendo // divisor
resto = dividendo % divisor
if dividendo % 2 == 0:
    paridad = "par"
else:
    paridad = "impar"
print(f"Cociente: {cociente}")
print(f"Resto: {resto}")
print(f"El dividendo es {paridad}.")
