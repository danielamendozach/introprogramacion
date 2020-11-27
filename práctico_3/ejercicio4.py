num=int(input("Ingrese un número: "))
num=str(num)
tam=len(num)
numvol=""
for pos in range(tam-1,-1,-1):
    numvol=numvol+num[pos]
if numvol==num :
    print("El número es capicua.")
else:
    print("El número no es capicua.")
