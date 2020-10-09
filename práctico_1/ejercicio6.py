num1= int(input("Ingrese el primer número: "))
num2= int(input("Ingrese el segundo número: "))
min= num1, num2
max= num2, num1
if num1<num2:
    print(min)
elif num1>num2:
    print(max)
else:
    print("Los números son iguales.")