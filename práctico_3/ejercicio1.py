def numfactorial(numf):
    num_fac = 1
    FACT = []
    for num in range(1, numf+1):
        num_fac = num * num_fac
        FACT.append(num_fac)
    print(FACT)

numfinal = 20
numfactorial(numfinal)