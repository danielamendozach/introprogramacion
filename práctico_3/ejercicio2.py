vector1=[]
for i in range(1,6):
    num=int(input("Ingrese el primer número: "))
    vector1.append(num)
print(vector1)
vector2=[]
for i in range(1,6):
    num=int(input("Ingrese el primer número: "))
    vector2.append(num)
print(vector2)
suma=0
vectorsuma=[]
for num in range(0,5):
    suma=vector1[num]+vector2[num]
    vectorsuma.append(suma)
print(vectorsuma)
