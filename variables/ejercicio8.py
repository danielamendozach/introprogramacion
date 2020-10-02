monto_a_invertir= float(input("Ingrese el monto a invertir: "))
interés_anual= float(input("Ingrese el intéres anual: "))
años_a_invertir= float(input("Ingrese el número de años a invertir: "))
ganancia=  monto_a_invertir*(1+interés_anual/100)**años_a_invertir
print(f"La ganancia neta generada de la inversión son {round(ganancia,2)}")
