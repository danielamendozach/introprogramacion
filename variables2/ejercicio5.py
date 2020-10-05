num1= float(input("Ingrese número: "))
igual= num1 == 5
print(f"El número es igual a 5: {igual}")
igual_float= num1 == 5.0
print(f"El número es igual a 5.0: {igual_float}")
mayor0_menor10= 0 < num1 < 10
print(f"El número es mayor que 0 y menor que 10: {mayor0_menor10}")
if num1<0:
    print("El número es menor que 0: True")
elif num1>10:
    print("El número es mayor que 10: True")
if num1 ==5:
    print("El número es igual a 5: True")
elif 10<num1<20:
    print("El número es mayor a 10 y menor a 20: True")
