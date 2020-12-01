def incisoA():
    vector = []
    for num in range(num1, num2-1, -1):
        vector.append(num)
    print("Inciso A:")
    print("Valores:", vector)

num1=int(input("Ingrese el número inicial: "))
num2=int(input("Ingrese el número final: "))
incisoA()