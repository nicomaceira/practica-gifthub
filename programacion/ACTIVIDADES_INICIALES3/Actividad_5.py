#Programa que pida n números y que, tras introducir el último número, debe aparecer por pantalla el número total de positivos, negativos y número de 0
numeros = int(input("Introduce la cantidad de numeros: "))
positivos = 0
negativos = 0
ceros = 0
for i in range(numeros):
    numero = float(input(f"Introduce el número {i+1}: "))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros += 1
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")
print(f"Números iguales a cero: {ceros}")
