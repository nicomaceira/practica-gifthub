#Realiza un programa que controle si la longitud de una frase introducida por teclado esigual, menor o mayor de 11 caracteres. Utiliza elif
frase=input("introduce una frase:")
longitud=len(frase)
if longitud<11:
    print("la frase tiene menos de 11 caracteres")
elif longitud==11:
    print("la frase tiene 11 caracteres")
elif longitud>11:
    print("la frase tiene mas de 11 caracteres")