#Programa que sume los n primeros números naturales. n Lo introduce el usuario.
n_veces = int(input("Introduce un número entero positivo: "))
if n_veces > 0:
    suma = n_veces * (n_veces + 1) // 2
    print(f"La suma de los primeros {n_veces} números naturales es: {suma}")
else:
    print("Por favor, introduce un número entero positivo mayor que cero.")

