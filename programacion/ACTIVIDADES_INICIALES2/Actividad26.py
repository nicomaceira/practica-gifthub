# Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.# Solicita una letra al usuario
letra = input("Introduce una letra: ")
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
letra = input("Introduce una letra: ")


