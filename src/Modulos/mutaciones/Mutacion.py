import random
from ..cruces.Cruce import cruce, cruceAuto, cruceJerar, cruceAutoJerar
from ..opBasicas.Decodificacion import deco


def mutacion(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    tabla, valoresLongitud = cruce(poblacion, longitud, rangoMin, rangoMax, tazaCruce)
    # tazaMutacion = int(input("\nPor favor ingrese la Taza de Mutacion: "))

    regl3 = round((tazaMutacion * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    # i = int(input("\nPor favor ingrese el incide del individuo a mutar: "))
    i = random.randint(1, len(valoresLongitud))
    # bit = int(input("\nPor favor ingrese el bit a mutar: "))
    bit = random.randint(1, longitud)

    indi = tabla.iloc[i-1].values[0]

    transforma = list(indi)

    if transforma[-bit] == "1":
        transforma[-bit] = "0"
    elif transforma[-bit] == "0":
        transforma[-bit] = "1"

    indi = "".join(transforma)

    adap = deco(indi, rangoMin, rangoMax)

    tabla.iloc[i-1, 0] = indi
    tabla.iloc[i-1, 1] = adap

    print()
    print("La tabla con el/los individuos mutados es:\n")
    print(tabla)
    print()
    dic = tabla.to_dict("list")
    lista = dic["Binarios"]
    # print(dic)
    # print(lista)
    return lista, tabla

def mutacionAuto(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce, tazaMutacion):
    tabla, valoresLongitud = cruceAuto(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce)
    # tazaMutacion = int(input("\nPor favor ingrese la Taza de Mutacion: "))

    regl3 = round((tazaMutacion * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    # i = int(input("\nPor favor ingrese el incide del individuo a mutar: "))
    i = random.randint(1, len(valoresLongitud))
    # bit = int(input("\nPor favor ingrese el bit a mutar: "))
    bit = random.randint(1, longitud)

    indi = tabla.iloc[i-1].values[0]

    transforma = list(indi)

    if transforma[-bit] == "1":
        transforma[-bit] = "0"
    elif transforma[-bit] == "0":
        transforma[-bit] = "1"

    indi = "".join(transforma)

    adap = deco(indi, rangoMin, rangoMax)

    tabla.iloc[i-1, 0] = indi
    tabla.iloc[i-1, 1] = adap

    print()
    print("La tabla con el/los individuos mutados es:\n")
    print(tabla)
    print()
    dic = tabla.to_dict("list")
    lista = dic["Binarios"]
    # print(dic)
    # print(lista)

    return lista, tabla

def mutacionJerar(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    tabla, valoresLongitud = cruceJerar(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
    tazaMutacion = int(input("\nPor favor ingrese la Taza de Mutacion: "))

    regl3 = round((tazaMutacion * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    i = int(input("\nPor favor ingrese el incide del individuo a mutar: "))
    bit = int(input("\nPor favor ingrese el bit a mutar: "))

    indi = tabla.iloc[i-1].values[0]

    transforma = list(indi)

    if transforma[-bit] == "1":
        transforma[-bit] = "0"
    elif transforma[-bit] == "0":
        transforma[-bit] = "1"

    indi = "".join(transforma)

    adap = deco(indi, rangoMin, rangoMax)

    tabla.iloc[i-1, 0] = indi
    tabla.iloc[i-1, 1] = adap

    print()
    print("La tabla con el/los individuos mutados es:\n")
    print(tabla)
    print()
    dic = tabla.to_dict("list")
    lista = dic["Binarios"]
    # print(dic)
    # print(lista)
    return lista

def mutacionAutoJerar(listaBin, poblacion, longitud, rangoMin, rangoMax, i):
    tabla, valoresLongitud = cruceAutoJerar(
        listaBin, poblacion, longitud, rangoMin, rangoMax, i)
    tazaMutacion = int(input("\nPor favor ingrese la Taza de Mutacion: "))

    regl3 = round((tazaMutacion * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    i = int(input("\nPor favor ingrese el incide del individuo a mutar: "))
    bit = int(input("\nPor favor ingrese el bit a mutar: "))

    indi = tabla.iloc[i-1].values[0]

    transforma = list(indi)

    if transforma[-bit] == "1":
        transforma[-bit] = "0"
    elif transforma[-bit] == "0":
        transforma[-bit] = "1"

    indi = "".join(transforma)

    adap = deco(indi, rangoMin, rangoMax)

    tabla.iloc[i-1, 0] = indi
    tabla.iloc[i-1, 1] = adap

    print()
    print("La tabla con el/los individuos mutados es:\n")
    print(tabla)
    print()
    dic = tabla.to_dict("list")
    lista = dic["Binarios"]
    # print(dic)
    # print(lista)

    return lista
