import random
from ..selecOrdenamiento.Ruleta import tablaOrdenadaManual, tablaOrdenadaAuto, elitistaRuleta
from ..selecOrdenamiento.Jerarquia import jer, jerAuto, jerElitista
from ..selecOrdenamiento.Torneo import torneo, torneoAuto, torneoElitista
from ..opBasicas.Decodificacion import deco

'''CRUCE 1 PUNTO : Ruleta'''
def cruce(poblacion, longitud, rangoMin, rangoMax, tazaCruce):
    tabla, valoresLongitud = tablaOrdenadaManual(poblacion, longitud, rangoMin, rangoMax)

    # tazaCruce = int(input("\nPor favor ingrese la Taza de cruce: "))

    regl3 = round((tazaCruce * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    print("\nSe procede hacer", regl3, "cruces.\n")
    # pc = int(input("Introduce punto de corte: "))
    pc = random.randint(1, longitud)
    print(f"El punto de corte para esta generacion es: {pc} \n")
    print("-------------------------Empieza Apareamiento-------------------------")
    for i in range(regl3):
        # p1 = int(input("\nIntroduce el indice del padre 1: "))
        # p2 = int(input("Introduce el indice del padre 2: "))
        p1 = random.randint(1, len(valoresLongitud))
        p2 = random.randint(1, len(valoresLongitud))
        while p1 == p2:
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

        hijo1 = padre1[:-pc]
        hijo2 = padre2[:-pc]
        corteP1 = padre1[-pc:]
        corteP2 = padre2[-pc:]
        hijo1 += corteP2
        hijo2 += corteP1

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
        hijo1 = ""
        hijo2 = ""
        corteP1 = ""
        corteP2 = ""
    print()
    print("La tabla con los cruceces es: \n")
    print(tabla)
    return tabla, valoresLongitud

def cruceAuto(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce):
    tabla, valoresLongitud = tablaOrdenadaAuto(listaBin, poblacion, longitud, rangoMin, rangoMax, i)

    # tazaCruce = int(input("\nPor favor ingrese la Taza de cruce: "))

    regl3 = round((tazaCruce * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    print("\nSe procede hacer", regl3, "cruces.\n")
    # pc = int(input("Introduce punto de corte: "))
    pc = random.randint(1, longitud)
    print(f"El punto de corte para esta generacion es: {pc} \n")
    print("-------------------------Empieza Apareamiento-------------------------")
    for i in range(regl3):
        # p1 = int(input("\nIntroduce el indice del padre 1: "))
        # p2 = int(input("Introduce el indice del padre 2: "))
        p1 = random.randint(1, len(valoresLongitud))
        p2 = random.randint(1, len(valoresLongitud))
        while p1 == p2:
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

        hijo1 = padre1[:-pc]
        hijo2 = padre2[:-pc]
        corteP1 = padre1[-pc:]
        corteP2 = padre2[-pc:]
        hijo1 += corteP2
        hijo2 += corteP1

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
        hijo1 = ""
        hijo2 = ""
        corteP1 = ""
        corteP2 = ""
    print()
    print("La tabla con los cruceces es: \n")
    print(tabla)
    return tabla, valoresLongitud

'''CRUCE 1 PUNTO : Jerarquico'''
def cruceJerar(poblacion, longitud, rangoMin, rangoMax, tazaCruce):
    tabla, valoresLongitud = jer(poblacion, longitud, rangoMin, rangoMax)

    # tazaCruce = int(input("\nPor favor ingrese la Taza de cruce: "))

    regl3 = round((tazaCruce * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    print("\nSe procede hacer", regl3, "cruces.\n")
    # pc = int(input("Introduce punto de corte: "))
    pc = random.randint(1, longitud)
    print(f"El punto de corte para esta generacion es: {pc} \n")
    print("-------------------------Empieza Apareamiento-------------------------")
    for i in range(regl3):
        # p1 = int(input("\nIntroduce el indice del padre 1: "))
        # p2 = int(input("Introduce el indice del padre 2: "))
        p1 = random.randint(1, len(valoresLongitud))
        p2 = random.randint(1, len(valoresLongitud))
        while p1 == p2:
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

        hijo1 = padre1[:-pc]
        hijo2 = padre2[:-pc]
        corteP1 = padre1[-pc:]
        corteP2 = padre2[-pc:]
        hijo1 += corteP2
        hijo2 += corteP1

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
        hijo1 = ""
        hijo2 = ""
        corteP1 = ""
        corteP2 = ""
    print()
    print("La tabla con los cruceces es: \n")
    print(tabla)
    return tabla, valoresLongitud

def cruceAutoJerar(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce):
    tabla, valoresLongitud = jerAuto(listaBin, poblacion, longitud, rangoMin, rangoMax, i)

    # tazaCruce = int(input("\nPor favor ingrese la Taza de cruce: "))

    regl3 = round((tazaCruce * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    print("\nSe procede hacer", regl3, "cruces.\n")
    # pc = int(input("Introduce punto de corte: "))
    pc = random.randint(1, longitud)
    print(f"El punto de corte para esta generacion es: {pc} \n")
    print("-------------------------Empieza Apareamiento-------------------------")
    for i in range(regl3):
        # p1 = int(input("\nIntroduce el indice del padre 1: "))
        # p2 = int(input("Introduce el indice del padre 2: "))
        p1 = random.randint(1, len(valoresLongitud))
        p2 = random.randint(1, len(valoresLongitud))
        while p1 == p2:
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

        hijo1 = padre1[:-pc]
        hijo2 = padre2[:-pc]
        corteP1 = padre1[-pc:]
        corteP2 = padre2[-pc:]
        hijo1 += corteP2
        hijo2 += corteP1

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
        hijo1 = ""
        hijo2 = ""
        corteP1 = ""
        corteP2 = ""
    print()
    print("La tabla con los cruceces es: \n")
    print(tabla)
    return tabla, valoresLongitud

'''CRUCE 1 PUNTO : Torneo'''
def cruceTorneo(poblacion, longitud, rangoMin, rangoMax, tazaCruce):
    tabla, valoresLongitud = torneo(poblacion, longitud, rangoMin, rangoMax)

    # tazaCruce = int(input("\nPor favor ingrese la Taza de cruce: "))

    regl3 = round((tazaCruce * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    print("\nSe procede hacer", regl3, "cruces.\n")
    input()
    # pc = int(input("Introduce punto de corte: "))
    pc = random.randint(1, longitud)
    print(f"El punto de corte para esta generacion es: {pc} \n")
    print("-------------------------Empieza Apareamiento-------------------------")
    for i in range(regl3):
        # p1 = int(input("\nIntroduce el indice del padre 1: "))
        # p2 = int(input("Introduce el indice del padre 2: "))
        p1 = random.randint(1, len(valoresLongitud))
        p2 = random.randint(1, len(valoresLongitud))
        while p1 == p2:
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

        hijo1 = padre1[:-pc]
        hijo2 = padre2[:-pc]
        corteP1 = padre1[-pc:]
        corteP2 = padre2[-pc:]
        hijo1 += corteP2
        hijo2 += corteP1

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
        hijo1 = ""
        hijo2 = ""
        corteP1 = ""
        corteP2 = ""
    print()
    print("La tabla con los cruceces es: \n")
    print(tabla)
    return tabla, valoresLongitud

def cruceAutoTorneo(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce):
    tabla, valoresLongitud = torneoAuto(listaBin, poblacion, longitud, rangoMin, rangoMax, i)

    # tazaCruce = int(input("\nPor favor ingrese la Taza de cruce: "))

    regl3 = round((tazaCruce * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    print("\nSe procede hacer", regl3, "cruces.\n")
    # pc = int(input("Introduce punto de corte: "))
    pc = random.randint(1, longitud)
    print(f"El punto de corte para esta generacion es: {pc} \n")
    print("-------------------------Empieza Apareamiento-------------------------")
    for i in range(regl3):
        # p1 = int(input("\nIntroduce el indice del padre 1: "))
        # p2 = int(input("Introduce el indice del padre 2: "))
        p1 = random.randint(1, len(valoresLongitud))
        p2 = random.randint(1, len(valoresLongitud))
        while p1 == p2:
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

        hijo1 = padre1[:-pc]
        hijo2 = padre2[:-pc]
        corteP1 = padre1[-pc:]
        corteP2 = padre2[-pc:]
        hijo1 += corteP2
        hijo2 += corteP1

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
        hijo1 = ""
        hijo2 = ""
        corteP1 = ""
        corteP2 = ""
    print()
    print("La tabla con los cruceces es: \n")
    print(tabla)
    return tabla, valoresLongitud

'''--------------------------ELITISTA--------------------------'''

'''CRUCE 1 PUNTO : Ruleta'''
def cruceElitista(tablaNueva, poblacion, longitud, rangoMin, rangoMax, tazaCruce):
    tabla, valoresLongitud = elitistaRuleta(tablaNueva)

    # tazaCruce = int(input("\nPor favor ingrese la Taza de cruce: "))

    regl3 = round((tazaCruce * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    print("\nSe procede hacer", regl3, "cruces.\n")
    # pc = int(input("Introduce punto de corte: "))
    pc = random.randint(1, longitud)
    print(f"El punto de corte para esta generacion es: {pc} \n")
    print("-------------------------Empieza Apareamiento-------------------------")
    for i in range(regl3):
        # p1 = int(input("\nIntroduce el indice del padre 1: "))
        # p2 = int(input("Introduce el indice del padre 2: "))
        p1 = random.randint(1, len(valoresLongitud))
        p2 = random.randint(1, len(valoresLongitud))
        while p1 == p2:
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

        hijo1 = padre1[:-pc]
        hijo2 = padre2[:-pc]
        corteP1 = padre1[-pc:]
        corteP2 = padre2[-pc:]
        hijo1 += corteP2
        hijo2 += corteP1

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
        hijo1 = ""
        hijo2 = ""
        corteP1 = ""
        corteP2 = ""
    print()
    print("La tabla con los cruceces es: \n")
    print(tabla)
    return tabla, valoresLongitud

'''CRUCE 1 PUNTO : Jerarquico'''
def cruceJerarElitista(tablaNueva, poblacion, longitud, rangoMin, rangoMax, tazaCruce):
    tabla, valoresLongitud = jerElitista(tablaNueva)

    # tazaCruce = int(input("\nPor favor ingrese la Taza de cruce: "))

    regl3 = round((tazaCruce * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    print("\nSe procede hacer", regl3, "cruces.\n")
    # pc = int(input("Introduce punto de corte: "))
    pc = random.randint(1, longitud)
    print(f"El punto de corte para esta generacion es: {pc} \n")
    print("-------------------------Empieza Apareamiento-------------------------")
    for i in range(regl3):
        # p1 = int(input("\nIntroduce el indice del padre 1: "))
        # p2 = int(input("Introduce el indice del padre 2: "))
        p1 = random.randint(1, len(valoresLongitud))
        p2 = random.randint(1, len(valoresLongitud))
        while p1 == p2:
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

        hijo1 = padre1[:-pc]
        hijo2 = padre2[:-pc]
        corteP1 = padre1[-pc:]
        corteP2 = padre2[-pc:]
        hijo1 += corteP2
        hijo2 += corteP1

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
        hijo1 = ""
        hijo2 = ""
        corteP1 = ""
        corteP2 = ""
    print()
    print("La tabla con los cruceces es: \n")
    print(tabla)
    return tabla, valoresLongitud

'''CRUCE 1 PUNTO : Torneo'''
def cruceTorneoElitista(tablaNueva, poblacion, longitud, rangoMin, rangoMax, tazaCruce):
    tabla, valoresLongitud = torneoElitista(tablaNueva)

    # tazaCruce = int(input("\nPor favor ingrese la Taza de cruce: "))

    regl3 = round((tazaCruce * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    print("\nSe procede hacer", regl3, "cruces.\n")
    # pc = int(input("Introduce punto de corte: "))
    pc = random.randint(1, longitud)
    print(f"El punto de corte para esta generacion es: {pc} \n")
    print("-------------------------Empieza Apareamiento-------------------------")
    for i in range(regl3):
        # p1 = int(input("\nIntroduce el indice del padre 1: "))
        # p2 = int(input("Introduce el indice del padre 2: "))
        p1 = random.randint(1, len(valoresLongitud))
        p2 = random.randint(1, len(valoresLongitud))
        while p1 == p2:
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

        hijo1 = padre1[:-pc]
        hijo2 = padre2[:-pc]
        corteP1 = padre1[-pc:]
        corteP2 = padre2[-pc:]
        hijo1 += corteP2
        hijo2 += corteP1

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
        hijo1 = ""
        hijo2 = ""
        corteP1 = ""
        corteP2 = ""
    print()
    print("La tabla con los cruceces es: \n")
    print(tabla)
    return tabla, valoresLongitud
