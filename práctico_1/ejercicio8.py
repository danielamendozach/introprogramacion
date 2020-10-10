num1= int(input("Ingrese el primer número: "))
num2= int(input("Ingrese el segundo número: "))
suma=0
for i in range(num1+1,num2):
    suma=suma+i
print(f"La suma es {suma}.")
