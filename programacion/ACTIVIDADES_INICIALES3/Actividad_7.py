#Imprime el siguiente patrón utilizando for:
num=(input("introduce el número máximo en el qual empezara la cuenta tras(debe ser positivo y no decimal): "))
if num.isdigit():
    cantidad=int(num)
    for i in range(cantidad, 0, -1):
        for j in range(i, 0, -1):
            print(j, end="")
        print()
else:
    print("el numero que has introducido no cumple con los criterios establecidos")

