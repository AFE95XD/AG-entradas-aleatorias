import random
from ..cruces.CruceUniforme import cruceUniforme, cruceUniformeAuto, cruceUniformeJerar, cruceUniformeAutoJerar, cruceUniformeTorneo, cruceUniformeAutoTorneo, cruceUniformeElitista, cruceUniformeJerarElitista, cruceUniformeTorneoElitista
from ..opBasicas.Decodificacion import deco

'''MUTACION SIMPLE: Ruleta + Cruce Uniforme'''
def mutacionUnif(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    tabla, valoresLongitud = cruceUniforme(poblacion, longitud, rangoMin, rangoMax, tazaCruce)
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

def mutacionUnifAuto(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce, tazaMutacion):
    tabla, valoresLongitud = cruceUniformeAuto(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce)
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

'''MUTACION SIMPLE: Jerarquica + Cruce Uniforme'''
def mutacionUnifJerar(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    tabla, valoresLongitud = cruceUniformeJerar(poblacion, longitud, rangoMin, rangoMax, tazaCruce)

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

def mutacionUnifAutoJerar(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce, tazaMutacion):
    tabla, valoresLongitud = cruceUniformeAutoJerar(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce)
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

'''MUTACION SIMPLE: Jerarquica + Cruce Uniforme'''
def mutacionUnifTorneo(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    tabla, valoresLongitud = cruceUniformeTorneo(poblacion, longitud, rangoMin, rangoMax, tazaCruce)

    regl3 = round((tazaMutacion * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    # i = int(input("\nPor favor ingrese el incide del individuo a mutar: "))
    i = random.randint(1, len(valoresLongitud))
    print(f"\nEl individuo a mutar es el{i}")
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

def mutacionUnifAutoTorneo(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce, tazaMutacion):
    tabla, valoresLongitud = cruceUniformeAutoTorneo(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce)
    # tazaMutacion = int(input("\nPor favor ingrese la Taza de Mutacion: "))

    regl3 = round((tazaMutacion * len(valoresLongitud)) / 100)

    if regl3 == 0:
        regl3 = 1

    # i = int(input("\nPor favor ingrese el incide del individuo a mutar: "))
    i = random.randint(1, len(valoresLongitud))
    print(f"\nEl individuo a mutar es el {i}")
    # bit = int(input("\nPor favor ingrese el bit a mutar: "))
    bit = random.randint(1, longitud)
    print(f"El Bit a mutar es el{bit}")

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

'''MUTACION SIMPLE: Ruleta + Cruce Uniforme'''
def mutacionUnifElitista(tablaNueva, poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    tabla, valoresLongitud = cruceUniformeElitista(tablaNueva, poblacion, longitud, rangoMin, rangoMax, tazaCruce)
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

'''MUTACION SIMPLE: Jerarquica + Cruce Uniforme'''
def mutacionUnifJerarElitista(tablaNueva, poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    tabla, valoresLongitud = cruceUniformeJerarElitista(tablaNueva, poblacion, longitud, rangoMin, rangoMax, tazaCruce)
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

'''MUTACION SIMPLE: Torneo + Cruce Uniforme'''
def mutacionUnifTorneoElitista(tablaNueva, poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    tabla, valoresLongitud = cruceUniformeTorneoElitista(tablaNueva, poblacion, longitud, rangoMin, rangoMax, tazaCruce)
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
