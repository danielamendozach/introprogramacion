def incisoB():
    vector=[]
    suma=0
    for num in range(num1, num2+1):
        if num%2==0:
            vector.append(num)
            suma=suma+num
    print("Inciso B:")
    print("Valores:", vector)
    print("Suma:", suma)

num1=int(input("Ingrese el número inicial: "))
num2=int(input("Ingrese el número final: "))
incisoB()