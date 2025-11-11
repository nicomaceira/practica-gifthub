#Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado o suspendido
entrada = input("Introduce el número de notas que quieres introducir: ")
if entrada.isdigit():
    cantidad = int(entrada)
    for i in range(1, cantidad + 1):
        nota = float(input(f"Introduce la nota {i}: "))
        if nota >= 5:
            print("Asignatura aprobada ")
        else:
            print("Asignatura suspendida")
else:
    print("Error: Debes introducir un número entero positivo.")
