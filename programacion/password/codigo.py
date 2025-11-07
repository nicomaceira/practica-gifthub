#visualitzar per pantalla els criteris per introduir la paraula clau:
print("INSTRUCCIONS")
print("1. La longitud del password te que tenir entre 6 y 8 carácters")
print("2. Forçar els seguents valors segon la posició indicada:")
print("Posició 1: un numero major o igual que 1 i menor o igual que 5.")
print("Posició 2: una lletra minúscula.")
print("Posició 3: una lletra majúscula.")
print("Posició 4: un dels següents símbols: * ,  _  ,  @.")
print("Posició 5: una lletra minúscula.")
print("Posició 6: un numero major que igual que 6 i menor o igual que 9.")
print("Posició 7: un dels següents símbols: & , / , #.")
print("Posició 8: un numero menor o igual que 5.")
#introduir el password
password=input("introduieix el teu password: ")
#validar la longitud del password
if len(password)<6 or len(password)>8:
    print("la longitud del password no compleix els requisits")