#Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b la secuencia en descenso. Respeta el formato de salida
intervalo1=int(input("introduce el primer intervalo (ha de ser un numero entero): "))
intervalo2=int(input("introduce el segundo intervalo (ha de ser un numnero entero): "))
if intervalo1<intervalo2:
    for i in range (intervalo1,intervalo2+1):
        print(i,end="-")
elif intervalo2<intervalo1:
    for i in range (intervalo1,intervalo2-1,-1):
        print(i,end="-")


