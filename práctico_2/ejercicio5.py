def inversa(palabra):
    tam= len(palabra)
    tam= tam-1
    for i in range(tam,-1,-1):
        palabrainv= palabrainv + palabra[i]
    print(palabrainv)

plb=input("Ingrese una frase: ")
inversa(plb)