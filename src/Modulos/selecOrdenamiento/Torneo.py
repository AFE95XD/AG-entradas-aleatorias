import random
from Modulos.opBasicas.Decodificacion import DecodificacionManuales

def torneo(poblacion, longitud, rangoMin, rangoMax):
    tablaManual, valoresLongitud = DecodificacionManuales(13, 9, 1, 9)
    # print(valoresLongitud)
    numAl = []
    while len(numAl) < len(valoresLongitud):
        numero = random.randint(1,len(valoresLongitud))
        if numero in numAl:
            pass
        else:
            numAl.append(numero)
    print(numAl)

    # print(tablaManual["Adaptado f(x)"].values[numAl[0]-1])
    # print(tablaManual["Adaptado f(x)"].values[numAl[1]-1])

    nuevaLista = []
    for i, j in zip(range(0,len(numAl)-1,2),range(1,len(numAl),2)):
        # print(i)
        # print(numAl[i])
        # print(j)
        # print(numAl[j])
        indi1 = tablaManual["Adaptado f(x)"].values[numAl[i]-1]
        indi2 = tablaManual["Adaptado f(x)"].values[numAl[1]-1]
        if indi1 > indi2:
            nuevaLista.append(indi1)
        else:
            nuevaLista.append(indi2)
    
    # print(nuevaLista)

# 010111010  186
# 100101001  297
# 001010101  85
# 000111001  57
# 110010101  405
# 110101010  426
# 000110110  54
# 000110101  53
# 011010101  213
# 101100001  353
# 001010101  85
# 001100010  98
# 001111001  121