#Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el peso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso.
peso=input("introduce tu peso:")
altura=input("introduce tu altura:")
IMC=peso/altura*altura
print("tu IMC es", IMC)
IMC>25
print("estas en sobrepeso")