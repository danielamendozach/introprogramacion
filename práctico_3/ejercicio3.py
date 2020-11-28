import random
num=int(input("Ingrese un número: "))
n=input("Ingrese un número: ")
vector=[]
for i in range(1,num+1):
    numA= random.randint(1,300)
    numv= str(numA)
    if len(numv)==1:
        if numv[0]==n:
            vector.append(numv)
    if len(numv)==2:
        if numv[1]==n:
            vector.append(numv)
    if len(numv)==3:
        if numv[2]==n:
            vector.append(numv)
print(vector)