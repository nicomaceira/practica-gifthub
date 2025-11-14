#A partir del programa anterior, soluciona el error que se produce en el test anterior con la palabra Abrigo utilizando únicamente una instrucción.
palabra = input("Introduce una palabra: ")
vocales = "AEIOUaeiouáéíóú"
grupo_vocales = ""
grupo_consonantes = ""
for letra in palabra:
    if letra.isalpha():
        if letra in vocales:
            grupo_vocales += letra
        else:
            grupo_consonantes += letra
print("Vocales:", grupo_vocales)
print("Consonantes:", grupo_consonantes)