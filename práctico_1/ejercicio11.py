from time import localtime
fecha_actual= localtime()
print(fecha_actual)
año=int(input("Ingrese el año de nacimiento: "))
mes=int(input("Ingrese el mes de nacimiento: "))
día= int(input("Ingrese el día de nacimiento: "))
años= fecha_actual.tm_year - año
meses= fecha_actual.tm_mon - mes
días=  fecha_actual.tm_mday - día
if meses<0 or días<0:
    años=años-1
print(f"Usted tiene {años} años.")
if meses<0:
    print(f"Faltan {meses*-1} meses para tu cumpleaños.")
if días<0:
    print(f"Faltan {días*-1} días para tu cumpleaños.")