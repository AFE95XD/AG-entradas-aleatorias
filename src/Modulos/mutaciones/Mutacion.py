import random
from ..cruces.Cruce import cruce, cruceAuto, cruceJerar, cruceAutoJerar, cruceTorneo, cruceAutoTorneo, cruceElitista, cruceJerarElitista, cruceTorneoElitista
from ..opBasicas.Decodificacion import deco

'''MUTACION SIMPLE : Ruleta + Cruce de 1 punto'''
def mutacion(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    tabla, valoresLongitud = cruce(poblacion, longitud, rangoMin, rangoMax, tazaCruce)
    # tazaMutacion = int(input("\nPor favor ingrese la Taza de Mutacion: "))

    regl3 = round((tazaMutacion * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    # i = int(input("\nPor favor ingrese el incide del individuo a mutar: "))
    i = random.randint(1, len(valoresLongitud))
    print(f"\nEl individuo a mutar es el {i}")
    # bit = int(input("\nPor favor ingrese el bit a mutar: "))
    bit = random.randint(1, longitud)
    print(f"El Bit a mutar es el {bit}")

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
    print(f"\nEl individuo a mutar es el {i}")
    # bit = int(input("\nPor favor ingrese el bit a mutar: "))
    bit = random.randint(1, longitud)
    print(f"El Bit a mutar es el {bit}")

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

'''MUTACION SIMPLE: Jerarquica + Cruce de 1 punto'''
def mutacionJerar(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    tabla, valoresLongitud = cruceJerar(poblacion, longitud, rangoMin, rangoMax, tazaCruce)
    # tazaMutacion = int(input("\nPor favor ingrese la Taza de Mutacion: "))

    regl3 = round((tazaMutacion * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    # i = int(input("\nPor favor ingrese el incide del individuo a mutar: "))
    i = random.randint(1, len(valoresLongitud))
    print(f"\nEl individuo a mutar es el {i}")
    # bit = int(input("\nPor favor ingrese el bit a mutar: "))
    bit = random.randint(1, longitud)
    print(f"El Bit a mutar es {bit}")

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

def mutacionAutoJerar(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce, tazaMutacion):
    tabla, valoresLongitud = cruceAutoJerar(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce)
    # tazaMutacion = int(input("\nPor favor ingrese la Taza de Mutacion: "))

    regl3 = round((tazaMutacion * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    # i = int(input("\nPor favor ingrese el incide del individuo a mutar: "))
    i = random.randint(1, len(valoresLongitud))
    print(f"\nEl individuo a mutar es el {i}")
    # bit = int(input("\nPor favor ingrese el bit a mutar: "))
    bit = random.randint(1, longitud)
    print(f"El Bit a mutar es el {bit}")

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

'''MUTACION SIMPLE: Torneo + Cruce de 1 punto'''
def mutacionTorneo(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    tabla, valoresLongitud = cruceTorneo(poblacion, longitud, rangoMin, rangoMax, tazaCruce)
    # tazaMutacion = int(input("\nPor favor ingrese la Taza de Mutacion: "))

    regl3 = round((tazaMutacion * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    # i = int(input("\nPor favor ingrese el incide del individuo a mutar: "))
    i = random.randint(1, len(valoresLongitud))
    print(f"\nEl individuo a mutar es el {i}")
    # bit = int(input("\nPor favor ingrese el bit a mutar: "))
    bit = random.randint(1, longitud)
    print(f"El Bit a mutar es el {bit}")

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

def mutacionAutoTorneo(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce, tazaMutacion):
    tabla, valoresLongitud = cruceAutoTorneo(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce)
    # tazaMutacion = int(input("\nPor favor ingrese la Taza de Mutacion: "))

    regl3 = round((tazaMutacion * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    # i = int(input("\nPor favor ingrese el incide del individuo a mutar: "))
    i = random.randint(1, len(valoresLongitud))
    print(f"\nEl individuo a mutar es el {i}")
    # bit = int(input("\nPor favor ingrese el bit a mutar: "))
    bit = random.randint(1, longitud)
    print(f"El Bit a mutar es el {bit}")

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

'''--------------------------ELITISTA--------------------------'''

'''MUTACION SIMPLE : Ruleta + Cruce de 1 punto'''
def mutacionElitista(tablaNueva, poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    tabla, valoresLongitud = cruceElitista(tablaNueva, poblacion, longitud, rangoMin, rangoMax, tazaCruce)
    # tazaMutacion = int(input("\nPor favor ingrese la Taza de Mutacion: "))

    regl3 = round((tazaMutacion * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    # i = int(input("\nPor favor ingrese el incide del individuo a mutar: "))
    i = random.randint(1, len(valoresLongitud))
    print(f"\nEl individuo a mutar es el {i}")
    # bit = int(input("\nPor favor ingrese el bit a mutar: "))
    bit = random.randint(1, longitud)
    print(f"El Bit a mutar es el {bit}")

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

'''MUTACION SIMPLE: Jerarquica + Cruce de 1 punto'''
def mutacionJerarElitista(tablaNueva, poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    tabla, valoresLongitud = cruceJerarElitista(tablaNueva, poblacion, longitud, rangoMin, rangoMax, tazaCruce)
    # tazaMutacion = int(input("\nPor favor ingrese la Taza de Mutacion: "))

    regl3 = round((tazaMutacion * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    # i = int(input("\nPor favor ingrese el incide del individuo a mutar: "))
    i = random.randint(1, len(valoresLongitud))
    print(f"\nEl individuo a mutar es el {i}")
    # bit = int(input("\nPor favor ingrese el bit a mutar: "))
    bit = random.randint(1, longitud)
    print(f"El Bit a mutar es el {bit}")

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

'''MUTACION SIMPLE: Torneo + Cruce de 1 punto'''
def mutacionTorneoElitista(tablaNueva, poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    tabla, valoresLongitud = cruceTorneoElitista(tablaNueva, poblacion, longitud, rangoMin, rangoMax, tazaCruce)
    # tazaMutacion = int(input("\nPor favor ingrese la Taza de Mutacion: "))

    regl3 = round((tazaMutacion * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    # i = int(input("\nPor favor ingrese el incide del individuo a mutar: "))
    i = random.randint(1, len(valoresLongitud))
    print(f"\nEl individuo a mutar es el {i}")
    # bit = int(input("\nPor favor ingrese el bit a mutar: "))
    bit = random.randint(1, longitud)
    print(f"El Bit a mutar es el {bit}")

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
