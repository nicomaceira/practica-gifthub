frase=input("introduce una frase:")
num1=float(input("introduzca un numero:"))
num2=float(input("introduzca el segundo numero:"))
num3=float(input("introduzca el tercer numero:"))
frase_minusculas=frase.lower()
suma=num1+num2+num3
round(suma,2)
media=(num1+num2+num3)/3
round(media,2)
producto=num1*num2*num3
round(producto,3)
print("La suma es:", suma)
print("La media es:", media)
print("El producto es:", producto)
if suma<producto:
    print("¿La suma es mayor que el producto?: False")
elif suma>producto:
    print("¿La suma es mayor que el producto?: True")
