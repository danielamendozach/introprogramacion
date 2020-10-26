def palindromo(palabra):
    tam=len(palabra)
    tam=tam-1
    palabrainv=""
    for i in range(tam,-1,-1):
        palabrainv=palabrainv + palabra[i]
    if palabrainv==palabra:
        print(palabrainv, "True")
    else:
        print(palabrainv, "False")

plb=input("Ingrese una palabra: ")
palindromo(plb)