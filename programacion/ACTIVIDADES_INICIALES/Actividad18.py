#Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores ¡de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por teclado el número de menores y el número de adultos que asisten al cine.
precio=12
adultos=int(input("intoduce el numero de adultos que acudiran al cine:"))
menores=int(input("introduce el numero de menores que acudiran al cine:"))
entradamenor=12*0.5
entradadulto=12*0.9
preciomenores=menores*entradamenor
precioadultos=adultos*entradadulto
print("el precio total de cine de",menores,"menores de 18 años es:",preciomenores)
print("el precio total de cine de",adultos,"mayores de 18 años es:",precioadultos)