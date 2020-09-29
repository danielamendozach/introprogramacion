horas_trabajadas= int(input("¿Cuantás horas has trabajado? "))
paga_por_hora= float(input("¿Cuantó es la paga por hora? "))
monto_a_pagar = horas_trabajadas * paga_por_hora
resultado= "Monto total a pagar: " + str(monto_a_pagar)
print(resultado)