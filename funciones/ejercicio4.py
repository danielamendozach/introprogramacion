import math
vectorx=[]
vectory=[]
for i in range(3):
    x=int(input("Ingrese las coordenadas x: "))
    y=int(input("Ingrese las coordenadas y: "))
    vectorx.append(x)
    vectory.append(y)
base=vectorx[2]-vectorx[0]
altura=vectory[1]-vectory[0]
hip= math.sqrt(base**2+altura**2)
perimetro=base+altura+hip
area=base*altura/2
print("El perímetro del triángulo es: ",perimetro)
print("El área del triángulo es: ",area)