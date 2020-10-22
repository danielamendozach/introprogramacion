def tablaM(numI):
    for i in range(1,11):
        print(f"{numI}x{i}={numI*i}")

for i in range(1,11):
    print(f"La tabla del {i} es: ")
    tablaM(i)