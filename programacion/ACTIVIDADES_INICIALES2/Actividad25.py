#Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.
nota=float(input("introduce tu nota: "))
if nota<5:
    print("has sacado un", nota, "has sacado un insuficiente")
if nota>=5 and nota<6.5:
    print("has sacado un",nota,"has sacado un satisfactorio")
if nota>=6.5 and nota<8.5:
    print("has sacado un",nota, "has sacado un notable")
if nota>=8.5 and nota<=10:
    print("has sacado un",nota, "has sacado un excelente")
elif nota>10 or nota<0:
    print("la nota que has introducido no esta entre el 0 y el 10")