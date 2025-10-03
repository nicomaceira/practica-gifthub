#Mejora el programa anterior para controlar que el valor introducido es una letra y en caso de introducir un número, aparezca un aviso por pantalla
letra =(input("Introduce una letra: "))
if letra.isupper():
    mayuscula = True
else:
    mayuscula = False
if letra.islower():
    minuscula = True
else:
    minuscula = False
print("¿Está en mayúscula?", mayuscula)
print("¿Está en minúscula?", minuscula)
