def num_mayor(num1,num2):
    if num1>num2:
        print(num1)
    elif num2>num1:
        print(num2)
    else:
        print("Los números son iguales: ",num1)
num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el segundo número: "))
num_mayor(num1,num2)