num = int(input("Ingrese la duración del tramo: "))
suma=0
while num>0:
    suma=suma+num
    num = int(input("Ingrese la duración del tramo: "))
tiempo= suma/60
print(f"El tiempo total de viaje es: {round(tiempo,2)} horas.")

