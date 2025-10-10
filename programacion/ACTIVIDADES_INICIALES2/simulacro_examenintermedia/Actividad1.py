nombre=input("introduce tu nombre:")
edad=int(input("Introduce tu edad:"))
nombre_mayusculas=nombre.upper()
if edad<0 or edad>100:
    print("Edad no valida")
if edad>0 or edad<100:
    año_actual=2025
    futuro=año_actual+(100-edad)
    print("Hola", nombre_mayusculas,"cumpliras 100 años en el", futuro)