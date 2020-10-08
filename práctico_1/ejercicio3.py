divisor= int(input("Ingrese el divisor: "))
dividendo= int(input("Ingrese el dividendo: "))
cociente= divisor//dividendo
resto= divisor%dividendo
if divisor%dividendo==0:
    print("La división es exacta.")
else:
    print("La división no es exacta.")
print(f"Cociente: {cociente}")
print(f"Resto: {resto}")