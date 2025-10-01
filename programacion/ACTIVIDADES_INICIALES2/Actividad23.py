#Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos
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