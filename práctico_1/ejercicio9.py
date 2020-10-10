num1= float(input("Ingrese el primer número: "))
operador= input("Ingresar el operador: ")
num2= float(input("Ingresar el segundo número: "))
if operador=="+":
    res= num1+num2
    print(f"{num1}+{num2}={res}")
elif operador=="-":
    res=num1-num2
    print(f"{num1}-{num2}={res}")
elif operador=="*":
    res=num1*num2
    print(f"{num1}*{num2}={res}")
elif operador=="/":
    res=num1/num2
    print(f"{num1}/{num2}={res}")
elif operador=="**":
    res=num1**num2
    print(f"{num1}**{num2}={res}")
else:
    print("Los datos ingresados no son válidos.")