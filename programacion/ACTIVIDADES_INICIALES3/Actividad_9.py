#Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima por pantalla cada letra
palabra = input("Introduce una palabra: ")
for z in range(len(palabra)):
    print("En la posicion", z, "esta la", palabra[z])

