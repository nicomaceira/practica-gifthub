#mostramos por pantalla las 4 opciones decombustible
print("1. Sin plomo 95")
print("2. Sin plomo 98")
print("3. Gasoleo A")
print("4. Gasoleo A+")
#introducimos el tipo de combustible y la cantidad
tipo_combustible=int(input("introduce el tipo de combustible:"))
var_litros=int(input("introduce los litros a repostar:"))
#todos los resultados estaran redondeados a 2 decimales
#si es tipo1, haremos la operacion correspondiente y mostraremos su resultado
if tipo_combustible==1:
    precio1=round(1.765*var_litros,2)
    print("el total a pagar es:", precio1)
#si es tipo2, haremos la operacion correspondiente y despues le añadiremos su descuento, por ultimo, mostraremos por pantalla los dos resultados
elif tipo_combustible==2:
    precio2=round(1.913*var_litros,2)
    precio2_descuento=precio2*0.1
    precio2_total=round(precio2-precio2_descuento,2)
    print("el total a pagar es:", precio2,"y con el descuento:", precio2_total)
#si es tipo3, haremos la operacion correspondiente y mostraremos su resultado
elif tipo_combustible==3:
    precio3=round(1.746*var_litros,2)
    print("el total a pagar es:",precio3)
#si es tipo4, haremos la operacion correspondiente y despues le añadiremos su descuento, por ultimo, mostraremos por pantalla los dos resultados
elif tipo_combustible==4:
    precio4=round(1.893*var_litros,2)
    precio4_descuento=precio4*0.12
    precio4_total=round(precio4-precio4_descuento,2)
    print("el total a pagar es:", precio4, "y con el descuento:", precio4_total)
#si el numero introducido no pertenece a ningun combuustible mostraremos por pantalla que ha habido un error
else:
    print("ha habido un error, introduce un numero establecido")