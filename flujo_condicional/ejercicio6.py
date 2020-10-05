año= int(input("Ingrese el año: "))
if año % 4 == 0 and not año % 100==0:
    print("El año es bisiesto.")
elif año % 100 == 0 and año % 400==0:
    print("El año es bisiesto.")
else:
    print("El año no es bisiesto.")