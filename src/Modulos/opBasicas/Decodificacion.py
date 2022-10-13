import matplotlib.pyplot as plt
import pandas as pd

import math
from ..opBasicas.BinarioDecimal import binarioDecimal, binarioDecimalAuto

# Este es el rango que proporciona para evaluar la funcion
# rangoMin = 1
# rangoMax = 8  # 9


def funcionMatematica(valor):
    # fx = (5 * math.sin(valor)) + (2 * math.pow(valor, 2))
    fx = ((8 * math.cos(valor)) + valor + (5 * math.pow(valor, 2)))
    # fx = (5*math.sin(valor) + 3*valor + 4 * (valor**2))
    return fx


def sacarReal(decimal, lng, rangoMin, rangoMax):
    # x = (rangoMin + decimal * ((rangoMax - rangoMin)/(math.pow(2, lng)-1)))
    x = (rangoMin + decimal * ((rangoMax - rangoMin)/(math.pow(2, lng)-1)))
    return x


def sacarAdaptado(real):
    # fun = (5 * math.sin(real)) + (2 * math.pow(real, 2))
    fun = ((8 * math.cos(real)) + real + (5 * math.pow(real, 2)))
    # fun = (5*math.sin(real) + 3*real + 4 * (real**2))
    return fun


def sumaValoresAdap(lista):
    totalAdap = 0
    for i in lista:
        totalAdap += i
    return totalAdap


def porcentajeRuleta(lista):
    total = sumaValoresAdap(lista)
    porcentajes = []
    for vad in lista:
        porcentajes.append((vad * 100) / total)
    return porcentajes


def DecodificacionManuales(poblacion, longitud, rangoMin, rangoMax):
    listaDecimales, longitud, listaBinarios = binarioDecimal(
        poblacion, longitud)

    funMin = funcionMatematica(rangoMin)
    funMax = funcionMatematica(rangoMax)

    listaReales = []

    listaAdaptado = []

    for x in listaDecimales:
        listaReales.append(sacarReal(x, longitud, rangoMin, rangoMax))

    for y in listaReales:
        listaAdaptado.append(sacarAdaptado(y))

    valoresLongitud = []
    for x in range(len(listaAdaptado)):
        valoresLongitud.append(x + 1)

    print("\nLa funcion evaluada en el rango maximo es: ", funMax)
    # print("\nLos decimales son: ", listaDecimales)
    # print("\nLos valores reales son: ", listaReales)

    # print("\nLos valores adaptados son: ", listaAdaptado)
    print("\nLos individuos son: ", valoresLongitud)
    print("\nLa suma de todos los valores Adaptados es: ",
          sumaValoresAdap(listaAdaptado))
    # print("\nLos porcentajes son: ",
    #       porcentajeRuleta(listaAdaptado))

    print("\nLa suma de todos los porsentajes es: ",
          sumaValoresAdap(porcentajeRuleta(listaAdaptado)), "\n")

    data = {
        "Binarios": listaBinarios,
        "Decimal": listaDecimales,
        "Reales": listaReales,
        "Adaptado f(x)": listaAdaptado,
        # "Ruleta [%]": porcentajeRuleta(listaAdaptado)
    }

    tablaManual = pd.DataFrame(data, index=valoresLongitud)

    print("\nLa tabla inicial sin ordenar es:\n")
    print(tablaManual)

    # dic = {}
    # for clave, valor in zip(listaBinarios, listaAdaptado):
    #     # print("el binario es",clave,": y su decimal es.",valor)
    #     dic[clave] = valor

    # print(dic)
    '''PARA GRAFICAR'''
    # xpoints = valoresLongitud
    # ypoints = listaAdaptado

    # plt.plot(xpoints, ypoints)

    # plt.title("Valor Adaptado VS Valor Maximo")
    # plt.xlabel("Individuos")
    # plt.ylabel("Valor Adaptado")

    # plt.show()
    return tablaManual, valoresLongitud
# DecodificacionManuales(10,9,1,9)


def deco(binario, rangoMin, rangoMax):
    numeroDecimal = int(binario, 2)
    numReal = sacarReal(numeroDecimal, len(binario), rangoMin, rangoMax)
    numAdaptado = sacarAdaptado(numReal)
    return numAdaptado


def DecodificacionAuto(listaBin, poblacion, longitud, rangoMin, rangoMax, i):
    listaDecimales, longitud, listaBinarios = binarioDecimalAuto(
        listaBin, poblacion, longitud)
    funMin = funcionMatematica(rangoMin)
    funMax = funcionMatematica(rangoMax)

    listaReales = []

    listaAdaptado = []

    for x in listaDecimales:
        listaReales.append(sacarReal(x, longitud, rangoMin, rangoMax))

    for y in listaReales:
        listaAdaptado.append(sacarAdaptado(y))

    valoresLongitud = []
    for x in range(len(listaAdaptado)):
        valoresLongitud.append(x + 1)

    print("\nLa funcion evaluada en el rango maximo es: ", funMax)
    # print("\nLos decimales son: ", listaDecimales)
    # print("\nLos valores reales son: ", listaReales)

    # print("\nLos valores adaptados son: ", listaAdaptado)
    print("\nLos individuos son: ", valoresLongitud)
    print("\nLa suma de todos los valores Adaptados es: ",
          sumaValoresAdap(listaAdaptado))
    # print("\nLos porcentajes son: ",
    #       porcentajeRuleta(listaAdaptado))

    print("\nLa suma de todos los porsentajes es: ",
          sumaValoresAdap(porcentajeRuleta(listaAdaptado)), "\n")

    data = {
        "Binarios": listaBinarios,
        "Decimal": listaDecimales,
        "Reales": listaReales,
        "Adaptado f(x)": listaAdaptado,
        # "Ruleta [%]": porcentajeRuleta(listaAdaptado)
    }

    tablaManual = pd.DataFrame(data, index=valoresLongitud)

    print(f"\nLa tabla Generacional {i} sin ordenar es:\n")
    print(tablaManual)

    # dic = {}
    # for clave, valor in zip(listaBinarios, listaAdaptado):
    #     # print("el binario es",clave,": y su decimal es.",valor)
    #     dic[clave] = valor

    # print(dic)
    '''PARA GRAFICAR'''
    # xpoints = valoresLongitud
    # ypoints = listaAdaptado

    # plt.plot(xpoints, ypoints)

    # plt.title("Valor Adaptado VS Valor Maximo")
    # plt.xlabel("Individuos")
    # plt.ylabel("Valor Adaptado")

    # plt.show()
    return tablaManual, valoresLongitud
