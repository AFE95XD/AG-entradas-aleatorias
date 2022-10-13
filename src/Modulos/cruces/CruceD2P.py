from ..selecOrdenamiento.Ruleta import tablaOrdenadaManual, tablaOrdenadaAuto
from ..selecOrdenamiento.Jerarquia import jer, jerAuto
from ..opBasicas.Decodificacion import deco


def cruce2P(poblacion, longitud, rangoMin, rangoMax):

    tabla, valoresLongitud = tablaOrdenadaManual(
        poblacion, longitud, rangoMin, rangoMax)

    tazaCruce = int(input("\nPor favor ingrese la Taza de cruce: "))

    regl3 = round((tazaCruce * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    print("\nSe procede hacer", regl3, "cruces.\n")
    pcMin = int(input("Introduce el punto de corte Minimo: "))
    pcMax = int(input("Introduce el punto de corte Maximo: "))

    for i in range(regl3):
        p1 = int(input("\nIntroduce el indice del padre 1: "))
        p2 = int(input("Introduce el indice del padre 2: "))

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

        if pcMin != 0:
            hijo1 = padre1[:-pcMax]
            hijo2 = padre2[:-pcMax]
            corteP1 = padre1[-pcMax:-(pcMin-1)]
            corteP2 = padre2[-pcMax:-(pcMin-1)]
            res1 = padre1[-(pcMin-1):]
            res2 = padre2[-(pcMin-1):]

            hijo1 = hijo1 + corteP2 + res1
            hijo2 = hijo2 + corteP1 + res2
        else:
            hijo1 = padre1[:-pcMax]
            hijo2 = padre2[:-pcMax]
            corteP1 = padre1[-pcMax:]
            corteP2 = padre2[-pcMax:]

            hijo1 = hijo1 + corteP2
            hijo2 = hijo2 + corteP1

        adapHijo1 = deco(hijo1, rangoMin, rangoMax)
        adapHijo2 = deco(hijo2, rangoMin, rangoMax)
        print(f"El hijo1 es = {hijo1} con adaptacion de {adapHijo1}")
        print(f"El hijo2 es = {hijo2} con adaptacion de {adapHijo2}\n")

        if adapHijo1 > adapHijo2:
            if adap1 > adap2:
                tabla.iloc[p2-1, 0] = hijo1
                tabla.iloc[p2-1, 1] = adapHijo1
                print("El hijo 1 sustituye a padre 2")
            else:
                tabla.iloc[p1-1, 0] = hijo1
                tabla.iloc[p1-1, 1] = adapHijo1
                print("El hijo 1 sustituye a padre 1")
        else:
            if adap1 > adap2:
                tabla.iloc[p2-1, 0] = hijo2
                tabla.iloc[p2-1, 1] = adapHijo2
                print("El hijo 2 sustituye a padre 2")
            else:
                tabla.iloc[p1-1, 0] = hijo2
                tabla.iloc[p1-1, 1] = adapHijo2
                print("El hijo 2 sustituye a padre 1")
    print()
    print("La tabla con los cruceces es: \n")
    print(tabla)
    return tabla, valoresLongitud

def cruce2PAuto(listaBin, poblacion, longitud, rangoMin, rangoMax, i):

    tabla, valoresLongitud = tablaOrdenadaAuto(
        listaBin, poblacion, longitud, rangoMin, rangoMax, i)

    tazaCruce = int(input("\nPor favor ingrese la Taza de cruce: "))

    regl3 = round((tazaCruce * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    print("\nSe procede hacer", regl3, "cruces.\n")
    pcMin = int(input("Introduce el punto de corte Minimo: "))
    pcMax = int(input("Introduce el punto de corte Maximo: "))

    for i in range(regl3):
        p1 = int(input("\nIntroduce el indice del padre 1: "))
        p2 = int(input("Introduce el indice del padre 2: "))

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

        if pcMin != 0:
            hijo1 = padre1[:-pcMax]
            hijo2 = padre2[:-pcMax]
            corteP1 = padre1[-pcMax:-(pcMin-1)]
            corteP2 = padre2[-pcMax:-(pcMin-1)]
            res1 = padre1[-(pcMin-1):]
            res2 = padre2[-(pcMin-1):]

            hijo1 = hijo1 + corteP2 + res1
            hijo2 = hijo2 + corteP1 + res2
        else:
            hijo1 = padre1[:-pcMax]
            hijo2 = padre2[:-pcMax]
            corteP1 = padre1[-pcMax:]
            corteP2 = padre2[-pcMax:]

            hijo1 = hijo1 + corteP2
            hijo2 = hijo2 + corteP1

        adapHijo1 = deco(hijo1, rangoMin, rangoMax)
        adapHijo2 = deco(hijo2, rangoMin, rangoMax)
        print(f"El hijo1 es = {hijo1} con adaptacion de {adapHijo1}")
        print(f"El hijo2 es = {hijo2} con adaptacion de {adapHijo2}\n")

        if adapHijo1 > adapHijo2:
            if adap1 > adap2:
                tabla.iloc[p2-1, 0] = hijo1
                tabla.iloc[p2-1, 1] = adapHijo1
                print("El hijo 1 sustituye a padre 2")
            else:
                tabla.iloc[p1-1, 0] = hijo1
                tabla.iloc[p1-1, 1] = adapHijo1
                print("El hijo 1 sustituye a padre 1")
        else:
            if adap1 > adap2:
                tabla.iloc[p2-1, 0] = hijo2
                tabla.iloc[p2-1, 1] = adapHijo2
                print("El hijo 2 sustituye a padre 2")
            else:
                tabla.iloc[p1-1, 0] = hijo2
                tabla.iloc[p1-1, 1] = adapHijo2
                print("El hijo 2 sustituye a padre 1")
    print()
    print("La tabla con los cruceces es: \n")
    print(tabla)
    return tabla, valoresLongitud

def cruce2PJerar(poblacion, longitud, rangoMin, rangoMax):

    tabla, valoresLongitud = jer(
        poblacion, longitud, rangoMin, rangoMax)

    tazaCruce = int(input("\nPor favor ingrese la Taza de cruce: "))

    regl3 = round((tazaCruce * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    print("\nSe procede hacer", regl3, "cruces.\n")
    pcMin = int(input("Introduce el punto de corte Minimo: "))
    pcMax = int(input("Introduce el punto de corte Maximo: "))

    for i in range(regl3):
        p1 = int(input("\nIntroduce el indice del padre 1: "))
        p2 = int(input("Introduce el indice del padre 2: "))

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

        if pcMin != 0:
            hijo1 = padre1[:-pcMax]
            hijo2 = padre2[:-pcMax]
            corteP1 = padre1[-pcMax:-(pcMin-1)]
            corteP2 = padre2[-pcMax:-(pcMin-1)]
            res1 = padre1[-(pcMin-1):]
            res2 = padre2[-(pcMin-1):]

            hijo1 = hijo1 + corteP2 + res1
            hijo2 = hijo2 + corteP1 + res2
        else:
            hijo1 = padre1[:-pcMax]
            hijo2 = padre2[:-pcMax]
            corteP1 = padre1[-pcMax:]
            corteP2 = padre2[-pcMax:]

            hijo1 = hijo1 + corteP2
            hijo2 = hijo2 + corteP1

        adapHijo1 = deco(hijo1, rangoMin, rangoMax)
        adapHijo2 = deco(hijo2, rangoMin, rangoMax)
        print(f"El hijo1 es = {hijo1} con adaptacion de {adapHijo1}")
        print(f"El hijo2 es = {hijo2} con adaptacion de {adapHijo2}\n")

        if adapHijo1 > adapHijo2:
            if adap1 > adap2:
                tabla.iloc[p2-1, 0] = hijo1
                tabla.iloc[p2-1, 1] = adapHijo1
                print("El hijo 1 sustituye a padre 2")
            else:
                tabla.iloc[p1-1, 0] = hijo1
                tabla.iloc[p1-1, 1] = adapHijo1
                print("El hijo 1 sustituye a padre 1")
        else:
            if adap1 > adap2:
                tabla.iloc[p2-1, 0] = hijo2
                tabla.iloc[p2-1, 1] = adapHijo2
                print("El hijo 2 sustituye a padre 2")
            else:
                tabla.iloc[p1-1, 0] = hijo2
                tabla.iloc[p1-1, 1] = adapHijo2
                print("El hijo 2 sustituye a padre 1")
    print()
    print("La tabla con los cruceces es: \n")
    print(tabla)
    return tabla, valoresLongitud

def cruce2PAutoJerar(listaBin, poblacion, longitud, rangoMin, rangoMax, i):

    tabla, valoresLongitud = jerAuto(
        listaBin, poblacion, longitud, rangoMin, rangoMax, i)

    tazaCruce = int(input("\nPor favor ingrese la Taza de cruce: "))

    regl3 = round((tazaCruce * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    print("\nSe procede hacer", regl3, "cruces.\n")
    pcMin = int(input("Introduce el punto de corte Minimo: "))
    pcMax = int(input("Introduce el punto de corte Maximo: "))

    for i in range(regl3):
        p1 = int(input("\nIntroduce el indice del padre 1: "))
        p2 = int(input("Introduce el indice del padre 2: "))

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

        if pcMin != 0:
            hijo1 = padre1[:-pcMax]
            hijo2 = padre2[:-pcMax]
            corteP1 = padre1[-pcMax:-(pcMin-1)]
            corteP2 = padre2[-pcMax:-(pcMin-1)]
            res1 = padre1[-(pcMin-1):]
            res2 = padre2[-(pcMin-1):]

            hijo1 = hijo1 + corteP2 + res1
            hijo2 = hijo2 + corteP1 + res2
        else:
            hijo1 = padre1[:-pcMax]
            hijo2 = padre2[:-pcMax]
            corteP1 = padre1[-pcMax:]
            corteP2 = padre2[-pcMax:]

            hijo1 = hijo1 + corteP2
            hijo2 = hijo2 + corteP1

        adapHijo1 = deco(hijo1, rangoMin, rangoMax)
        adapHijo2 = deco(hijo2, rangoMin, rangoMax)
        print(f"El hijo1 es = {hijo1} con adaptacion de {adapHijo1}")
        print(f"El hijo2 es = {hijo2} con adaptacion de {adapHijo2}\n")

        if adapHijo1 > adapHijo2:
            if adap1 > adap2:
                tabla.iloc[p2-1, 0] = hijo1
                tabla.iloc[p2-1, 1] = adapHijo1
                print("El hijo 1 sustituye a padre 2")
            else:
                tabla.iloc[p1-1, 0] = hijo1
                tabla.iloc[p1-1, 1] = adapHijo1
                print("El hijo 1 sustituye a padre 1")
        else:
            if adap1 > adap2:
                tabla.iloc[p2-1, 0] = hijo2
                tabla.iloc[p2-1, 1] = adapHijo2
                print("El hijo 2 sustituye a padre 2")
            else:
                tabla.iloc[p1-1, 0] = hijo2
                tabla.iloc[p1-1, 1] = adapHijo2
                print("El hijo 2 sustituye a padre 1")
    print()
    print("La tabla con los cruceces es: \n")
    print(tabla)
    return tabla, valoresLongitud