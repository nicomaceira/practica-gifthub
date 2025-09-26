#Realiza un programa que, a partir introducir el lado de un cubo, presente por pantalla el área y para calcular el volumen utiliza el operador de exponente.
lado = float(input("Introduce el valor del lado del cubo: "))
area = 6 * (lado ** 2)
volumen = lado ** 3
print(f"\nÁrea total del cubo: {area:.2f}")
print(f"Volumen del cubo: {volumen:.2f}")
