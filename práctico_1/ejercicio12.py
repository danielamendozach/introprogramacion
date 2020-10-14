num= int(input("Ingrese el número de palabras que va a escribir: "))
p_larga=""
p_corta=""
for num in range(1,num+1):
    palabra=input("Ingrese la palabra: ")
    if len(palabra)>=len(p_larga):
        p_larga=palabra
    else:
        p_corta=palabra
print(f"La palabra más larga es: {p_larga}.")
print(f"La palabra más corta es: {p_corta}.")
