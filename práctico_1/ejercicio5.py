palabra1= input("Ingrese la palabra1: ")
palabra2= input("Ingrese la palabra2: ")
long_p1= len(palabra1)
long_p2= len(palabra2)
if len(palabra1)>len(palabra2):
    print(f"{palabra1} es más larga que {palabra2} por {long_p1-long_p2} letras.")
elif len(palabra1)==len(palabra2):
    print(f"{palabra1} es de la misma longitud que {palabra2}.")
else:
    print(f"{palabra2} es más larga que {palabra1} por {long_p2-long_p1} letras.")