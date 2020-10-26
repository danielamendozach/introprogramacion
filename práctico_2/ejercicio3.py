def contador(palabra):
    contador=0
    for i in palabra:
        contador= contador+1
    return contador

plb=input("Ingrese la palabra: ")
print(contador(plb))