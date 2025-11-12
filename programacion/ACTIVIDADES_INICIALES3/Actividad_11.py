# Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el stringdistinguiendo vocales y las consonantes
palabra = input("Introduce una palabra: ")
vocales = "aeiouAEIOU"
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

