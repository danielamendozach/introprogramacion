consumo= int(input("¿Cuánto fue su consumo? "))
if consumo<100:
    print("Su monto a pagar es 1,00bs.")
elif 100<=consumo<=499:
    print("Su monto a pagar es 1,20bs.")
elif 500<=consumo<=999:
    print("Su monto a pagar es 1,50bs.")
else:
    print("Su monto a pagar son 2,00bs.")