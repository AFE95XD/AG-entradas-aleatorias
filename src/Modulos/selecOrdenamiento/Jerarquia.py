import pandas as pd
from ..opBasicas.Decodificacion import DecodificacionManuales, DecodificacionAuto


def sacaJmin(ran):
    jmax = 1.1
    jmin = 2-jmax
    return jmax, jmin


def jer(poblacion, longitud, rangoMin, rangoMax):
    tabla, valoresLongitud = DecodificacionManuales(
        poblacion, longitud, rangoMin, rangoMax)
    print()
    tablaM = tabla.sort_values("Adaptado f(x)")
    tablaM["Jer o Rango"] = valoresLongitud
    tablaM = tablaM.sort_index()
    print("La tabla con los rangos es:\n")
    print(tablaM)
    print()

    listaVJ = []
    for i in range(len(tablaM)):
        rango = tablaM["Jer o Rango"].iloc[i]
        n = len(tablaM)
        jmax, jmin = sacaJmin(rango)
        vj = jmin + ((jmax-jmin)*((rango-1)/(n-1)))
        listaVJ.append(vj)

    tablaM["Val Esp"] = listaVJ
    print("La tabla con los vaoler esperados es:\n")
    print(tablaM)
    print()

    print("\nLa Tabla Ordenada es:\n")
    tabOrd = tablaM.sort_values("Val Esp", ascending=False)
    dic = tabOrd.to_dict("list")
    dicOrdFil = {
        "Binarios": dic["Binarios"],
        "Adaptado f(x)": dic["Adaptado f(x)"]
    }
    tablaOrdenada = pd.DataFrame(dicOrdFil, index=valoresLongitud)
    print(tablaOrdenada)
    return tablaOrdenada, valoresLongitud

def jerAuto(listaBin, poblacion, longitud, rangoMin, rangoMax, i):
    tabla, valoresLongitud = DecodificacionAuto(
        listaBin, poblacion, longitud, rangoMin, rangoMax, i)
    print()
    tablaM = tabla.sort_values("Adaptado f(x)")
    tablaM["Jer o Rango"] = valoresLongitud
    tablaM = tablaM.sort_index()
    print("La tabla con los rangos es:\n")
    print(tablaM)
    print()

    listaVJ = []
    for i in range(len(tablaM)):
        rango = tablaM["Jer o Rango"].iloc[i]
        n = len(tablaM)
        jmax, jmin = sacaJmin(rango)
        vj = jmin + ((jmax-jmin)*((rango-1)/(n-1)))
        listaVJ.append(vj)

    tablaM["Val Esp"] = listaVJ
    print("La tabla con los vaoler esperados es:\n")
    print(tablaM)
    print()

    print("\nLa Tabla Ordenada es:\n")
    tabOrd = tablaM.sort_values("Val Esp", ascending=False)
    dic = tabOrd.to_dict("list")
    dicOrdFil = {
        "Binarios": dic["Binarios"],
        "Adaptado f(x)": dic["Adaptado f(x)"]
    }
    tablaOrdenada = pd.DataFrame(dicOrdFil, index=valoresLongitud)
    print(tablaOrdenada)
    return tablaOrdenada, valoresLongitud