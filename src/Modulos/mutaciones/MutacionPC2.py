import random
from ..cruces.CruceD2P import cruce2P, cruce2PAuto, cruce2PJerar, cruce2PAutoJerar, cruce2PTorneo, cruce2PAutoTorneo
from ..opBasicas.Decodificacion import deco

'''MUTACION SIMPLE: Ruleta + Cruce de 2 puntos'''
def mutacionPC2(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    tabla, valoresLongitud = cruce2P(poblacion, longitud, rangoMin, rangoMax, tazaCruce)
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

def mutacionPC2Auto(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce, tazaMutacion):
    tabla, valoresLongitud = cruce2PAuto(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce)
    tazaMutacion = int(input("\nPor favor ingrese la Taza de Mutacion: "))

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

'''MUTACION SIMPLE: Jerarquica + Cruce de 2 puntos'''
def mutacionPC2Jerar(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    tabla, valoresLongitud = cruce2PJerar(poblacion, longitud, rangoMin, rangoMax, tazaCruce)
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

def mutacionPC2AutoJerar(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce, tazaMutacion):
    tabla, valoresLongitud = cruce2PAutoJerar(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce)
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

'''MUTACION SIMPLE: Torneo + Cruce de 2 puntos'''
def mutacionPC2Torneo(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    tabla, valoresLongitud = cruce2PTorneo(poblacion, longitud, rangoMin, rangoMax, tazaCruce)
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

def mutacionPC2AutoTorneo(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce, tazaMutacion):
    tabla, valoresLongitud = cruce2PAutoTorneo(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce)
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
