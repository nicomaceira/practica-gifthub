#Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo
import math

def resolver_ecuacion_segundo_grado(a, b, c):
    discriminante = b**2 - 4*a*c

    if discriminante < 0:
        print("La ecuación no tiene soluciones reales.")
        return None
    elif discriminante == 0:
        x = -b / (2*a)
        print(f"La ecuación tiene una única solución real: x = {x}")
        return x
    else:
        raiz = math.sqrt(discriminante)
        x1 = (-b + raiz) / (2*a)
        x2 = (-b - raiz) / (2*a)
        print(f"La ecuación tiene dos soluciones reales: x1 = {x1}, x2 = {x2}")
        return x1, x2
a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))
resolver_ecuacion_segundo_grado(a, b, c)
