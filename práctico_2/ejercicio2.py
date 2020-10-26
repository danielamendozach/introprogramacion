def num_mayor_3(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        print(num1)
    elif num2>=num1 and num2>=num3:
        print(num2)
    elif num3>=num1 and num3>=num2:
        print(num3)
num1=int(input("Ingrese el primero número: "))
num2=int(input("Ingrese el segundo número: "))
num3=int(input("Ingrese el tercer número: "))
num_mayor_3(num1,num2,num3)