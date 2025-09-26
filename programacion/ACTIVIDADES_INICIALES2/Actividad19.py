#Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son iguales
num1=float(input("introduce un numero:"))
num2=float(input("introduce un numero:"))
total=num1-num2
if  total>0:
    print(num1,"es mayor que", num2)
if  total<0:
    print(num2,"es mayor que", num1)
if  total==0:
    print("los numeros son iguales")