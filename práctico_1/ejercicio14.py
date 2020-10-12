edad= int(input("Ingrese su edad: "))
peso= float(input("Ingrese su peso en kilogramos: "))
estatura= float(input("Ingrese su estatura en metros: "))
IMC= peso/estatura**2
if edad<45:
    if IMC<22.0:
        print("Su condición de riesgo es: baja.")
    elif IMC>=22.0:
        print("Su condición de riesgo es: media.")
if edad>=45:
    if IMC<22.0:
        print("Su condición de riesgo es: media.")
    elif IMC>=22.0:
        print("Su condición de riesgo es: alta.")