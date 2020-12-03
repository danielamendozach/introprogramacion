x=int(input("Ingrese x: "))
y=int(input("Ingrese y: "))
radio=1
suma=0
while radio!=0:
    radio = int(input("Ingrese el radio de un círculo: "))
    diametro=radio*2
    suma=suma+diametro
if suma<=x or suma<=y:
    print("Entran el rectángulo.")
elif suma>x or suma>y:
    print("No entran en el rectángulo.")

