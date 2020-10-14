num= int(input("Ingrese el número de términos a utilizar: "))
suma=0
for i in range(1,num+1):
    if i % 2==0:
        signo= -1
    else:
        signo= 1
    valor= signo/( 1 + 2 * ( i - 1 ) )
    suma= suma + valor
pi= 4 * suma
print(pi)