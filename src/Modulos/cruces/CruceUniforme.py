import random
from ..selecOrdenamiento.Ruleta import tablaOrdenadaManual, tablaOrdenadaAuto, elitistaRuleta
from ..selecOrdenamiento.Jerarquia import jer, jerAuto, jerElitista
from ..selecOrdenamiento.Torneo import torneo, torneoAuto, torneoElitista
from ..opBasicas.Decodificacion import deco
# padre1 = "011101010110"
# padre2 = "010110101101"

# mascara = "101010110110"

# # cero padre1 y uno padre2
# hijo1 = ""
# hijo2 = ""
# for x, i in zip(mascara, range(len(mascara))):
#     if x == "0":
#         hijo1 += padre1[i]
#         hijo2 += padre2[i]
#     else:
#         hijo1 += padre2[i]
#         hijo2 += padre1[i]

# print(hijo1)
# print(hijo2)
'''CRUCE UNIFORME : Ruleta'''
def cruceUniforme(poblacion, longitud, rangoMin, rangoMax, tazaCruce):

    tabla, valoresLongitud = tablaOrdenadaManual(poblacion, longitud, rangoMin, rangoMax)

    # tazaCruce = int(input("\nPor favor ingrese la Taza de cruce: "))

    regl3 = round((tazaCruce * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    print("\nSe procede hacer", regl3, "cruces.\n")
    # mascara = input("Introduce la mascara: ")
    mascara = ""
    for y in range(int(longitud)):
        numero = str(random.randint(0, 1))
        mascara += numero
    print("La mascara es:", mascara, "\n")
    print("-------------------------Empieza Apareamiento-------------------------")
    for i in range(regl3):
        # p1 = int(input("\nIntroduce el indice del padre 1: "))
        # p2 = int(input("Introduce el indice del padre 2: "))
        p1 = random.randint(1, len(valoresLongitud))
        p2 = random.randint(1, len(valoresLongitud))

        # aqui se obtine el binario
        padre1 = tabla.iloc[p1-1].values[0]
        padre2 = tabla.iloc[p2-1].values[0]
        # indice1 = tabla.values[p1-1][0]
        # aqui se saca el valor adaptado de los padres
        adap1 = tabla.iloc[p1-1].values[1]
        adap2 = tabla.iloc[p2-1].values[1]

        print()
        print(
            f"El padre 1 es el individuo {p1} = {padre1} con adaptacion de {adap1}")
        print(
            f"El padre 2 es el individuo {p2} = {padre2} con adaptacion de {adap2}\n")

        # cero padre1 y uno padre2
        hijo1 = ""
        hijo2 = ""
        for x, i in zip(mascara, range(len(mascara))):
            if x == "0":
                hijo1 += padre1[i]
                hijo2 += padre2[i]
            else:
                hijo1 += padre2[i]
                hijo2 += padre1[i]

        adapHijo1 = deco(hijo1, rangoMin, rangoMax)
        adapHijo2 = deco(hijo2, rangoMin, rangoMax)
        print(f"El hijo1 es = {hijo1} con adaptacion de {adapHijo1}")
        print(f"El hijo2 es = {hijo2} con adaptacion de {adapHijo2}\n")

        if adapHijo1 > adapHijo2:
            if adap1 > adap2:
                tabla.iloc[p2-1, 0] = hijo1
                tabla.iloc[p2-1, 1] = adapHijo1
                print("El hijo 1 sustituye a padre 2")
                print("-----------------------------")
            else:
                tabla.iloc[p1-1, 0] = hijo1
                tabla.iloc[p1-1, 1] = adapHijo1
                print("El hijo 1 sustituye a padre 1")
                print("-----------------------------")
        else:
            if adap1 > adap2:
                tabla.iloc[p2-1, 0] = hijo2
                tabla.iloc[p2-1, 1] = adapHijo2
                print("El hijo 2 sustituye a padre 2")
                print("-----------------------------")
            else:
                tabla.iloc[p1-1, 0] = hijo2
                tabla.iloc[p1-1, 1] = adapHijo2
                print("El hijo 2 sustituye a padre 1")
                print("-----------------------------")
    print()
    print("La tabla con los cruceces es: \n")
    print(tabla)
    return tabla, valoresLongitud

def cruceUniformeAuto(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce):

    tabla, valoresLongitud = tablaOrdenadaAuto(listaBin, poblacion, longitud, rangoMin, rangoMax, i)

    # tazaCruce = int(input("\nPor favor ingrese la Taza de cruce: "))

    regl3 = round((tazaCruce * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    print("\nSe procede hacer", regl3, "cruces.\n")
    # mascara = input("Introduce la mascara: ")
    mascara = ""
    for y in range(int(longitud)):
        numero = str(random.randint(0, 1))
        mascara += numero
    print("La mascara es:", mascara, "\n")
    print("-------------------------Empieza Apareamiento-------------------------")
    for i in range(regl3):
        # p1 = int(input("\nIntroduce el indice del padre 1: "))
        # p2 = int(input("Introduce el indice del padre 2: "))
        p1 = random.randint(1, len(valoresLongitud))
        p2 = random.randint(1, len(valoresLongitud))

        # aqui se obtine el binario
        padre1 = tabla.iloc[p1-1].values[0]
        padre2 = tabla.iloc[p2-1].values[0]
        # indice1 = tabla.values[p1-1][0]
        # aqui se saca el valor adaptado de los padres
        adap1 = tabla.iloc[p1-1].values[1]
        adap2 = tabla.iloc[p2-1].values[1]

        print()
        print(
            f"El padre 1 es el individuo {p1} = {padre1} con adaptacion de {adap1}")
        print(
            f"El padre 2 es el individuo {p2} = {padre2} con adaptacion de {adap2}\n")

        # cero padre1 y uno padre2
        hijo1 = ""
        hijo2 = ""
        for x, i in zip(mascara, range(len(mascara))):
            if x == "0":
                hijo1 += padre1[i]
                hijo2 += padre2[i]
            else:
                hijo1 += padre2[i]
                hijo2 += padre1[i]

        adapHijo1 = deco(hijo1, rangoMin, rangoMax)
        adapHijo2 = deco(hijo2, rangoMin, rangoMax)
        print(f"El hijo1 es = {hijo1} con adaptacion de {adapHijo1}")
        print(f"El hijo2 es = {hijo2} con adaptacion de {adapHijo2}\n")

        if adapHijo1 > adapHijo2:
            if adap1 > adap2:
                tabla.iloc[p2-1, 0] = hijo1
                tabla.iloc[p2-1, 1] = adapHijo1
                print("El hijo 1 sustituye a padre 2")
                print("-----------------------------")
            else:
                tabla.iloc[p1-1, 0] = hijo1
                tabla.iloc[p1-1, 1] = adapHijo1
                print("El hijo 1 sustituye a padre 1")
                print("-----------------------------")
        else:
            if adap1 > adap2:
                tabla.iloc[p2-1, 0] = hijo2
                tabla.iloc[p2-1, 1] = adapHijo2
                print("El hijo 2 sustituye a padre 2")
                print("-----------------------------")
            else:
                tabla.iloc[p1-1, 0] = hijo2
                tabla.iloc[p1-1, 1] = adapHijo2
                print("El hijo 2 sustituye a padre 1")
                print("-----------------------------")
    print()
    print("La tabla con los cruceces es: \n")
    print(tabla)
    return tabla, valoresLongitud

'''CRUCE UNIFORME : Jerarquico'''
def cruceUniformeJerar(poblacion, longitud, rangoMin, rangoMax, tazaCruce):

    tabla, valoresLongitud = jer(poblacion, longitud, rangoMin, rangoMax)

    # tazaCruce = int(input("\nPor favor ingrese la Taza de cruce: "))

    regl3 = round((tazaCruce * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    print("\nSe procede hacer", regl3, "cruces.\n")
    
    mascara = ""
    for y in range(int(longitud)):
        numero = str(random.randint(0, 1))
        mascara += numero
    print("La mascara es:", mascara, "\n")
    print("-------------------------Empieza Apareamiento-------------------------")
    for i in range(regl3):
        # p1 = int(input("\nIntroduce el indice del padre 1: "))
        # p2 = int(input("Introduce el indice del padre 2: "))
        p1 = random.randint(1, len(valoresLongitud))
        p2 = random.randint(1, len(valoresLongitud))

        # aqui se obtine el binario
        padre1 = tabla.iloc[p1-1].values[0]
        padre2 = tabla.iloc[p2-1].values[0]
        # indice1 = tabla.values[p1-1][0]
        # aqui se saca el valor adaptado de los padres
        adap1 = tabla.iloc[p1-1].values[1]
        adap2 = tabla.iloc[p2-1].values[1]

        print()
        print(
            f"El padre 1 es el individuo {p1} = {padre1} con adaptacion de {adap1}")
        print(
            f"El padre 2 es el individuo {p2} = {padre2} con adaptacion de {adap2}\n")

        # cero padre1 y uno padre2
        hijo1 = ""
        hijo2 = ""
        for x, i in zip(mascara, range(len(mascara))):
            if x == "0":
                hijo1 += padre1[i]
                hijo2 += padre2[i]
            else:
                hijo1 += padre2[i]
                hijo2 += padre1[i]

        adapHijo1 = deco(hijo1, rangoMin, rangoMax)
        adapHijo2 = deco(hijo2, rangoMin, rangoMax)
        print(f"El hijo1 es = {hijo1} con adaptacion de {adapHijo1}")
        print(f"El hijo2 es = {hijo2} con adaptacion de {adapHijo2}\n")

        if adapHijo1 > adapHijo2:
            if adap1 > adap2:
                tabla.iloc[p2-1, 0] = hijo1
                tabla.iloc[p2-1, 1] = adapHijo1
                print("El hijo 1 sustituye a padre 2")
                print("-----------------------------")
            else:
                tabla.iloc[p1-1, 0] = hijo1
                tabla.iloc[p1-1, 1] = adapHijo1
                print("El hijo 1 sustituye a padre 1")
                print("-----------------------------")
        else:
            if adap1 > adap2:
                tabla.iloc[p2-1, 0] = hijo2
                tabla.iloc[p2-1, 1] = adapHijo2
                print("El hijo 2 sustituye a padre 2")
                print("-----------------------------")
            else:
                tabla.iloc[p1-1, 0] = hijo2
                tabla.iloc[p1-1, 1] = adapHijo2
                print("El hijo 2 sustituye a padre 1")
                print("-----------------------------")
    print()
    print("La tabla con los cruceces es: \n")
    print(tabla)
    return tabla, valoresLongitud

def cruceUniformeAutoJerar(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce):
    tabla, valoresLongitud = jerAuto(listaBin, poblacion, longitud, rangoMin, rangoMax, i)

    # tazaCruce = int(input("\nPor favor ingrese la Taza de cruce: "))

    regl3 = round((tazaCruce * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    print("\nSe procede hacer", regl3, "cruces.\n")
    
    mascara = ""
    for y in range(int(longitud)):
        numero = str(random.randint(0, 1))
        mascara += numero
    print("La mascara es:", mascara, "\n")
    print("-------------------------Empieza Apareamiento-------------------------")
    for i in range(regl3):
        # p1 = int(input("\nIntroduce el indice del padre 1: "))
        # p2 = int(input("Introduce el indice del padre 2: "))
        p1 = random.randint(1, len(valoresLongitud))
        p2 = random.randint(1, len(valoresLongitud))

        # aqui se obtine el binario
        padre1 = tabla.iloc[p1-1].values[0]
        padre2 = tabla.iloc[p2-1].values[0]
        # indice1 = tabla.values[p1-1][0]
        # aqui se saca el valor adaptado de los padres
        adap1 = tabla.iloc[p1-1].values[1]
        adap2 = tabla.iloc[p2-1].values[1]

        print()
        print(
            f"El padre 1 es el individuo {p1} = {padre1} con adaptacion de {adap1}")
        print(
            f"El padre 2 es el individuo {p2} = {padre2} con adaptacion de {adap2}\n")

        # cero padre1 y uno padre2
        hijo1 = ""
        hijo2 = ""
        for x, i in zip(mascara, range(len(mascara))):
            if x == "0":
                hijo1 += padre1[i]
                hijo2 += padre2[i]
            else:
                hijo1 += padre2[i]
                hijo2 += padre1[i]

        adapHijo1 = deco(hijo1, rangoMin, rangoMax)
        adapHijo2 = deco(hijo2, rangoMin, rangoMax)
        print(f"El hijo1 es = {hijo1} con adaptacion de {adapHijo1}")
        print(f"El hijo2 es = {hijo2} con adaptacion de {adapHijo2}\n")

        if adapHijo1 > adapHijo2:
            if adap1 > adap2:
                tabla.iloc[p2-1, 0] = hijo1
                tabla.iloc[p2-1, 1] = adapHijo1
                print("El hijo 1 sustituye a padre 2")
                print("-----------------------------")
            else:
                tabla.iloc[p1-1, 0] = hijo1
                tabla.iloc[p1-1, 1] = adapHijo1
                print("El hijo 1 sustituye a padre 1")
                print("-----------------------------")
        else:
            if adap1 > adap2:
                tabla.iloc[p2-1, 0] = hijo2
                tabla.iloc[p2-1, 1] = adapHijo2
                print("El hijo 2 sustituye a padre 2")
                print("-----------------------------")
            else:
                tabla.iloc[p1-1, 0] = hijo2
                tabla.iloc[p1-1, 1] = adapHijo2
                print("El hijo 2 sustituye a padre 1")
                print("-----------------------------")
    print()
    print("La tabla con los cruceces es: \n")
    print(tabla)
    return tabla, valoresLongitud

'''CRUCE UNIFORME : Torneo'''
def cruceUniformeTorneo(poblacion, longitud, rangoMin, rangoMax, tazaCruce):

    tabla, valoresLongitud = torneo(poblacion, longitud, rangoMin, rangoMax)

    # tazaCruce = int(input("\nPor favor ingrese la Taza de cruce: "))

    regl3 = round((tazaCruce * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    print("\nSe procede hacer", regl3, "cruces.\n")
    mascara = ""
    for y in range(int(longitud)):
        numero = str(random.randint(0, 1))
        mascara += numero
    print("La mascara es:", mascara, "\n")
    print("-------------------------Empieza Apareamiento-------------------------")
    for i in range(regl3):
        # p1 = int(input("\nIntroduce el indice del padre 1: "))
        # p2 = int(input("Introduce el indice del padre 2: "))
        p1 = random.randint(1, len(valoresLongitud))
        p2 = random.randint(1, len(valoresLongitud))

        # aqui se obtine el binario
        padre1 = tabla.iloc[p1-1].values[0]
        padre2 = tabla.iloc[p2-1].values[0]
        # indice1 = tabla.values[p1-1][0]
        # aqui se saca el valor adaptado de los padres
        adap1 = tabla.iloc[p1-1].values[1]
        adap2 = tabla.iloc[p2-1].values[1]

        print()
        print(
            f"El padre 1 es el individuo {p1} = {padre1} con adaptacion de {adap1}")
        print(
            f"El padre 2 es el individuo {p2} = {padre2} con adaptacion de {adap2}\n")

        # cero padre1 y uno padre2
        hijo1 = ""
        hijo2 = ""
        for x, i in zip(mascara, range(len(mascara))):
            if x == "0":
                hijo1 += padre1[i]
                hijo2 += padre2[i]
            else:
                hijo1 += padre2[i]
                hijo2 += padre1[i]

        adapHijo1 = deco(hijo1, rangoMin, rangoMax)
        adapHijo2 = deco(hijo2, rangoMin, rangoMax)
        print(f"El hijo1 es = {hijo1} con adaptacion de {adapHijo1}")
        print(f"El hijo2 es = {hijo2} con adaptacion de {adapHijo2}\n")

        if adapHijo1 > adapHijo2:
            if adap1 > adap2:
                tabla.iloc[p2-1, 0] = hijo1
                tabla.iloc[p2-1, 1] = adapHijo1
                print("El hijo 1 sustituye a padre 2")
                print("-----------------------------")
            else:
                tabla.iloc[p1-1, 0] = hijo1
                tabla.iloc[p1-1, 1] = adapHijo1
                print("El hijo 1 sustituye a padre 1")
                print("-----------------------------")
        else:
            if adap1 > adap2:
                tabla.iloc[p2-1, 0] = hijo2
                tabla.iloc[p2-1, 1] = adapHijo2
                print("El hijo 2 sustituye a padre 2")
                print("-----------------------------")
            else:
                tabla.iloc[p1-1, 0] = hijo2
                tabla.iloc[p1-1, 1] = adapHijo2
                print("El hijo 2 sustituye a padre 1")
                print("-----------------------------")
    print()
    print("La tabla con los cruceces es: \n")
    print(tabla)
    return tabla, valoresLongitud

def cruceUniformeAutoTorneo(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce):
    tabla, valoresLongitud = torneoAuto(listaBin, poblacion, longitud, rangoMin, rangoMax, i)

    # tazaCruce = int(input("\nPor favor ingrese la Taza de cruce: "))

    regl3 = round((tazaCruce * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    print("\nSe procede hacer", regl3, "cruces.\n")
    
    mascara = ""
    for y in range(int(longitud)):
        numero = str(random.randint(0, 1))
        mascara += numero
    print("La mascara es:", mascara, "\n")
    print("-------------------------Empieza Apareamiento-------------------------")
    for i in range(regl3):
        # p1 = int(input("\nIntroduce el indice del padre 1: "))
        # p2 = int(input("Introduce el indice del padre 2: "))
        p1 = random.randint(1, len(valoresLongitud))
        p2 = random.randint(1, len(valoresLongitud))

        # aqui se obtine el binario
        padre1 = tabla.iloc[p1-1].values[0]
        padre2 = tabla.iloc[p2-1].values[0]
        # indice1 = tabla.values[p1-1][0]
        # aqui se saca el valor adaptado de los padres
        adap1 = tabla.iloc[p1-1].values[1]
        adap2 = tabla.iloc[p2-1].values[1]

        print()
        print(
            f"El padre 1 es el individuo {p1} = {padre1} con adaptacion de {adap1}")
        print(
            f"El padre 2 es el individuo {p2} = {padre2} con adaptacion de {adap2}\n")

        # cero padre1 y uno padre2
        hijo1 = ""
        hijo2 = ""
        for x, i in zip(mascara, range(len(mascara))):
            if x == "0":
                hijo1 += padre1[i]
                hijo2 += padre2[i]
            else:
                hijo1 += padre2[i]
                hijo2 += padre1[i]

        adapHijo1 = deco(hijo1, rangoMin, rangoMax)
        adapHijo2 = deco(hijo2, rangoMin, rangoMax)
        print(f"El hijo1 es = {hijo1} con adaptacion de {adapHijo1}")
        print(f"El hijo2 es = {hijo2} con adaptacion de {adapHijo2}\n")

        if adapHijo1 > adapHijo2:
            if adap1 > adap2:
                tabla.iloc[p2-1, 0] = hijo1
                tabla.iloc[p2-1, 1] = adapHijo1
                print("El hijo 1 sustituye a padre 2")
                print("-----------------------------")
            else:
                tabla.iloc[p1-1, 0] = hijo1
                tabla.iloc[p1-1, 1] = adapHijo1
                print("El hijo 1 sustituye a padre 1")
                print("-----------------------------")
        else:
            if adap1 > adap2:
                tabla.iloc[p2-1, 0] = hijo2
                tabla.iloc[p2-1, 1] = adapHijo2
                print("El hijo 2 sustituye a padre 2")
                print("-----------------------------")
            else:
                tabla.iloc[p1-1, 0] = hijo2
                tabla.iloc[p1-1, 1] = adapHijo2
                print("El hijo 2 sustituye a padre 1")
                print("-----------------------------")
    print()
    print("La tabla con los cruceces es: \n")
    print(tabla)
    return tabla, valoresLongitud

'''--------------------------ELITISTA--------------------------'''

'''CRUCE UNIFORME : Ruleta'''
def cruceUniformeElitista(tablaNueva, poblacion, longitud, rangoMin, rangoMax, tazaCruce):
    tabla, valoresLongitud = elitistaRuleta(tablaNueva)

    # tazaCruce = int(input("\nPor favor ingrese la Taza de cruce: "))

    regl3 = round((tazaCruce * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    print("\nSe procede hacer", regl3, "cruces.\n")
    # mascara = input("Introduce la mascara: ")
    mascara = ""
    for y in range(int(longitud)):
        numero = str(random.randint(0, 1))
        mascara += numero
    print("La mascara es:", mascara, "\n")
    print("-------------------------Empieza Apareamiento-------------------------")
    for i in range(regl3):
        # p1 = int(input("\nIntroduce el indice del padre 1: "))
        # p2 = int(input("Introduce el indice del padre 2: "))
        p1 = random.randint(1, len(valoresLongitud))
        p2 = random.randint(1, len(valoresLongitud))

        # aqui se obtine el binario
        padre1 = tabla.iloc[p1-1].values[0]
        padre2 = tabla.iloc[p2-1].values[0]
        # indice1 = tabla.values[p1-1][0]
        # aqui se saca el valor adaptado de los padres
        adap1 = tabla.iloc[p1-1].values[1]
        adap2 = tabla.iloc[p2-1].values[1]

        print()
        print(
            f"El padre 1 es el individuo {p1} = {padre1} con adaptacion de {adap1}")
        print(
            f"El padre 2 es el individuo {p2} = {padre2} con adaptacion de {adap2}\n")

        # cero padre1 y uno padre2
        hijo1 = ""
        hijo2 = ""
        for x, i in zip(mascara, range(len(mascara))):
            if x == "0":
                hijo1 += padre1[i]
                hijo2 += padre2[i]
            else:
                hijo1 += padre2[i]
                hijo2 += padre1[i]

        adapHijo1 = deco(hijo1, rangoMin, rangoMax)
        adapHijo2 = deco(hijo2, rangoMin, rangoMax)
        print(f"El hijo1 es = {hijo1} con adaptacion de {adapHijo1}")
        print(f"El hijo2 es = {hijo2} con adaptacion de {adapHijo2}\n")

        if adapHijo1 > adapHijo2:
            if adap1 > adap2:
                tabla.iloc[p2-1, 0] = hijo1
                tabla.iloc[p2-1, 1] = adapHijo1
                print("El hijo 1 sustituye a padre 2")
                print("-----------------------------")
            else:
                tabla.iloc[p1-1, 0] = hijo1
                tabla.iloc[p1-1, 1] = adapHijo1
                print("El hijo 1 sustituye a padre 1")
                print("-----------------------------")
        else:
            if adap1 > adap2:
                tabla.iloc[p2-1, 0] = hijo2
                tabla.iloc[p2-1, 1] = adapHijo2
                print("El hijo 2 sustituye a padre 2")
                print("-----------------------------")
            else:
                tabla.iloc[p1-1, 0] = hijo2
                tabla.iloc[p1-1, 1] = adapHijo2
                print("El hijo 2 sustituye a padre 1")
                print("-----------------------------")
    print()
    print("La tabla con los cruceces es: \n")
    print(tabla)
    return tabla, valoresLongitud

'''CRUCE UNIFORME : Jerarquico'''
def cruceUniformeJerarElitista(tablaNueva, poblacion, longitud, rangoMin, rangoMax, tazaCruce):
    tabla, valoresLongitud = jerElitista(tablaNueva)

    # tazaCruce = int(input("\nPor favor ingrese la Taza de cruce: "))

    regl3 = round((tazaCruce * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    print("\nSe procede hacer", regl3, "cruces.\n")
    # mascara = input("Introduce la mascara: ")
    mascara = ""
    for y in range(int(longitud)):
        numero = str(random.randint(0, 1))
        mascara += numero
    print("La mascara es:", mascara, "\n")
    print("-------------------------Empieza Apareamiento-------------------------")
    for i in range(regl3):
        # p1 = int(input("\nIntroduce el indice del padre 1: "))
        # p2 = int(input("Introduce el indice del padre 2: "))
        p1 = random.randint(1, len(valoresLongitud))
        p2 = random.randint(1, len(valoresLongitud))

        # aqui se obtine el binario
        padre1 = tabla.iloc[p1-1].values[0]
        padre2 = tabla.iloc[p2-1].values[0]
        # indice1 = tabla.values[p1-1][0]
        # aqui se saca el valor adaptado de los padres
        adap1 = tabla.iloc[p1-1].values[1]
        adap2 = tabla.iloc[p2-1].values[1]

        print()
        print(
            f"El padre 1 es el individuo {p1} = {padre1} con adaptacion de {adap1}")
        print(
            f"El padre 2 es el individuo {p2} = {padre2} con adaptacion de {adap2}\n")

        # cero padre1 y uno padre2
        hijo1 = ""
        hijo2 = ""
        for x, i in zip(mascara, range(len(mascara))):
            if x == "0":
                hijo1 += padre1[i]
                hijo2 += padre2[i]
            else:
                hijo1 += padre2[i]
                hijo2 += padre1[i]

        adapHijo1 = deco(hijo1, rangoMin, rangoMax)
        adapHijo2 = deco(hijo2, rangoMin, rangoMax)
        print(f"El hijo1 es = {hijo1} con adaptacion de {adapHijo1}")
        print(f"El hijo2 es = {hijo2} con adaptacion de {adapHijo2}\n")

        if adapHijo1 > adapHijo2:
            if adap1 > adap2:
                tabla.iloc[p2-1, 0] = hijo1
                tabla.iloc[p2-1, 1] = adapHijo1
                print("El hijo 1 sustituye a padre 2")
                print("-----------------------------")
            else:
                tabla.iloc[p1-1, 0] = hijo1
                tabla.iloc[p1-1, 1] = adapHijo1
                print("El hijo 1 sustituye a padre 1")
                print("-----------------------------")
        else:
            if adap1 > adap2:
                tabla.iloc[p2-1, 0] = hijo2
                tabla.iloc[p2-1, 1] = adapHijo2
                print("El hijo 2 sustituye a padre 2")
                print("-----------------------------")
            else:
                tabla.iloc[p1-1, 0] = hijo2
                tabla.iloc[p1-1, 1] = adapHijo2
                print("El hijo 2 sustituye a padre 1")
                print("-----------------------------")
    print()
    print("La tabla con los cruceces es: \n")
    print(tabla)
    return tabla, valoresLongitud

'''CRUCE UNIFORME : Torneo'''
def cruceUniformeTorneoElitista(tablaNueva, poblacion, longitud, rangoMin, rangoMax, tazaCruce):
    tabla, valoresLongitud = torneoElitista(tablaNueva, poblacion, longitud, rangoMin, rangoMax)

    # tazaCruce = int(input("\nPor favor ingrese la Taza de cruce: "))

    regl3 = round((tazaCruce * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    print("\nSe procede hacer", regl3, "cruces.\n")
    # mascara = input("Introduce la mascara: ")
    mascara = ""
    for y in range(int(longitud)):
        numero = str(random.randint(0, 1))
        mascara += numero
    print("La mascara es:", mascara, "\n")
    print("-------------------------Empieza Apareamiento-------------------------")
    for i in range(regl3):
        # p1 = int(input("\nIntroduce el indice del padre 1: "))
        # p2 = int(input("Introduce el indice del padre 2: "))
        p1 = random.randint(1, len(valoresLongitud))
        p2 = random.randint(1, len(valoresLongitud))

        # aqui se obtine el binario
        padre1 = tabla.iloc[p1-1].values[0]
        padre2 = tabla.iloc[p2-1].values[0]
        # indice1 = tabla.values[p1-1][0]
        # aqui se saca el valor adaptado de los padres
        adap1 = tabla.iloc[p1-1].values[1]
        adap2 = tabla.iloc[p2-1].values[1]

        print()
        print(
            f"El padre 1 es el individuo {p1} = {padre1} con adaptacion de {adap1}")
        print(
            f"El padre 2 es el individuo {p2} = {padre2} con adaptacion de {adap2}\n")

        # cero padre1 y uno padre2
        hijo1 = ""
        hijo2 = ""
        for x, i in zip(mascara, range(len(mascara))):
            if x == "0":
                hijo1 += padre1[i]
                hijo2 += padre2[i]
            else:
                hijo1 += padre2[i]
                hijo2 += padre1[i]

        adapHijo1 = deco(hijo1, rangoMin, rangoMax)
        adapHijo2 = deco(hijo2, rangoMin, rangoMax)
        print(f"El hijo1 es = {hijo1} con adaptacion de {adapHijo1}")
        print(f"El hijo2 es = {hijo2} con adaptacion de {adapHijo2}\n")

        if adapHijo1 > adapHijo2:
            if adap1 > adap2:
                tabla.iloc[p2-1, 0] = hijo1
                tabla.iloc[p2-1, 1] = adapHijo1
                print("El hijo 1 sustituye a padre 2")
                print("-----------------------------")
            else:
                tabla.iloc[p1-1, 0] = hijo1
                tabla.iloc[p1-1, 1] = adapHijo1
                print("El hijo 1 sustituye a padre 1")
                print("-----------------------------")
        else:
            if adap1 > adap2:
                tabla.iloc[p2-1, 0] = hijo2
                tabla.iloc[p2-1, 1] = adapHijo2
                print("El hijo 2 sustituye a padre 2")
                print("-----------------------------")
            else:
                tabla.iloc[p1-1, 0] = hijo2
                tabla.iloc[p1-1, 1] = adapHijo2
                print("El hijo 2 sustituye a padre 1")
                print("-----------------------------")
    print()
    print("La tabla con los cruceces es: \n")
    print(tabla)
    return tabla, valoresLongitud
