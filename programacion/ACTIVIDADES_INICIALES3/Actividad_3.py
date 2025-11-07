#Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado o suspendido
# Solicitar al usuario cuántas notas quiere introducir
entrada = input("¿Cuántas notas quieres introducir? ")
if entrada.isdigit():
    cantidad = int(entrada)
    for i in range(1, cantidad + 1):
        nota = float(input(f"Introduce la nota {i}: "))
        if nota >= 5 and nota<=10:
            print("Asignatura aprobada ")
        elif nota<5 and nota>=0:
            print("Asignatura suspendida")
        else:
            print("Error: la nota debe ser un numero entre el 0 y el 10")
else:
    print("Error: Debes introducir un número entero positivo.")
