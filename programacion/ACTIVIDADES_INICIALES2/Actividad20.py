#A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados numeros entre 0 y 10
num1=float(input("introduzca un numero entre 0 y 10: "))
num2=float(input("introduzca un numero entre 0 y 10: "))
total=num1-num2
if  total>0:
    print(num1,"es mayor que", num2)
elif  total<0:
    print(num2,"es mayor que", num1)
elif  total==0:
    print("los numeros son iguales")
elif float(num1>10 and num1<0):
    print("no se puede realizar porque un numero es mayor que 10")
elif  float(num2>10 and num2<0):
    print("no se puede realizar porque un numero es mayor que 10")