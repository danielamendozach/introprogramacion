def ahorcado(intentos):
    if intentos==1:
        print("================")
        print("=")
        print("=")
        print("=")
        print("=")
        print("=")
        print("=")
        print("=")
        print("=")
        print("===")
    if (intentos == 2):
        print("================")
        print("=              |")
        print("=              O")
        print("=")
        print("=")
        print("=")
        print("=")
        print("=")
        print("=")
        print("===")
    if (intentos == 3):
        print("================")
        print("=              |")
        print("=              O")
        print("=              |")
        print("=              |")
        print("=")
        print("=")
        print("=")
        print("=")
        print("===")
    if (intentos == 4):
        print("================")
        print("=              |")
        print("=              O")
        print("=              |\ ")
        print("=              | \ ")
        print("=")
        print("=")
        print("=")
        print("=")
        print("===")
    if (intentos == 5):
        print("================")
        print("=              |")
        print("=              O")
        print("=             /|\ ")
        print("=            / | \ ")
        print("=              |")
        print("=")
        print("=")
        print("=")
        print("===")

def juego(archivo):
    for palabra in lista:
        palabra = palabra.replace("\n", "")
        tam = len(palabra)
        vectorplb = []
        vectorguion = []
        intentos = 6
        for pos in range(0, tam):
            vectorplb.append(str(palabra[pos]))
            vectorguion.append("-")
        print(vectorguion)
        while intentos > 0:
            print("Cantidad de intentos: ", intentos)
            coincidencias = 0
            cantguiones = 0
            letra = input("Ingrese una letra: ")
            letra = letra.upper()
            for pos in range(0, tam):
                if letra == vectorplb[pos]:
                    vectorguion[pos] = letra
                    coincidencias = coincidencias + 1
            print(vectorguion)
            for pos in range(0, tam):
                if vectorguion[pos] == "-":
                    cantguiones = cantguiones + 1
            if coincidencias == 0:
                intentos = intentos - 1
                ahorcado(intentos)

            if (intentos == 6):
                print("================")
                print("=              |")
                print("=              O")
                print("=             /|\ ")
                print("=            / | \ ")
                print("=              |")
                print("=             / \ ")
                print("=            /   \ ")
                print("=")
                print("===")

            if cantguiones == 0:
                print("Ganaste, adivinaste la palabra!")
                intentos = -1
        if intentos == 0:
            print("Te quedaste sin intentos, perdiste!")

archivo= open("palabraoculta.txt","r")
lista = archivo.readlines()
archivo.close()
juego(archivo)

archivo = open("palabraoculta2", "r")
lista = archivo.readlines()
archivo.close()
juego(archivo)

archivo = open("palabraoculta3", "r")
lista = archivo.readlines()
archivo.close()
juego(archivo)








