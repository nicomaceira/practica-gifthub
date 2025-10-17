#introducimos los dos numeros con los que haremos la operacion
var1=float(input("introduce el primer numero:"))
var2=float(input("introduce el segundo numero:"))
#realizamos la suma y la division y rodondeamos el resultado de la division a 3 decimales
var_total=var1+var2
division_total=round(var_total/3, 3)
#mostramos por pantalla los resultados
print("el resultado de sumar", var1, "y", var2,"es:", var_total)
print("el resultado de dividir", var_total,"entre 3 es:", division_total)