import random
from ..cruces.CruceUniforme import cruceUniforme, cruceUniformeAuto, cruceUniformeJerar, cruceUniformeAutoJerar
from ..opBasicas.Decodificacion import deco

def mutacionUnif(poblacion, longitud, rangoMin, rangoMax):
    tabla, valoresLongitud = cruceUniforme(
        poblacion, longitud, rangoMin, rangoMax)
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

def mutacionUnifAuto(listaBin, poblacion, longitud, rangoMin, rangoMax, i):
    tabla, valoresLongitud = cruceUniformeAuto(
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

def mutacionUnifJerar(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    tabla, valoresLongitud = cruceUniformeJerar(poblacion, longitud, rangoMin, rangoMax, tazaCruce)

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

def mutacionUnifAutoJerar(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce, tazaMutacion):
    tabla, valoresLongitud = cruceUniformeAutoJerar(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce)
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
