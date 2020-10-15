num= int(input("Ingrese un número entero: "))
while num>1:
    if num%2==0:
        secuencia=num//2
        num=secuencia
        print(secuencia,"*" * secuencia)
    elif num%2!=0:
        secuencia=(num*3)+1
        num=secuencia
        print(secuencia,"*" * secuencia)

