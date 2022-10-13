import pandas as pd
from ..opBasicas.Decodificacion import DecodificacionManuales, DecodificacionAuto, porcentajeRuleta


def tablaOrdenadaManual(poblacion, longitud, rangoMin, rangoMax):
    tablaManual, valoresLongitud = DecodificacionManuales(
        poblacion, longitud, rangoMin, rangoMax)
    dicCompleto = tablaManual.to_dict("list")
    listaAdaptado = dicCompleto["Adaptado f(x)"]
    tablaManual["Ruleta [%]"] = porcentajeRuleta(listaAdaptado)
    print("\nLa Tabla con el Porsentaje Ruleta es:\n")
    print(tablaManual)
    print("\nLa Tabla Ordenada es:\n")
    tabOrd = tablaManual.sort_values("Ruleta [%]", ascending=False)
    dic = tabOrd.to_dict("list")
    dicOrdFil = {
        "Binarios": dic["Binarios"],
        "Adaptado f(x)": dic["Adaptado f(x)"]
    }
    tablaOrdenada = pd.DataFrame(dicOrdFil, index=valoresLongitud)
    print(tablaOrdenada)

    # print(valoresLongitud)
    return tablaOrdenada, valoresLongitud


def tablaOrdenadaAuto(listaBin, poblacion, longitud, rangoMin, rangoMax, i):
    tablaManual, valoresLongitud = DecodificacionAuto(
        listaBin, poblacion, longitud, rangoMin, rangoMax, i)
    dicCompleto = tablaManual.to_dict("list")
    listaAdaptado = dicCompleto["Adaptado f(x)"]
    tablaManual["Ruleta [%]"] = porcentajeRuleta(listaAdaptado)
    print("\nLa Tabla con el Porsentaje Ruleta es:\n")
    print(tablaManual)
    print(f"\nLa Tabla Ordenada de la generacion {i} es:\n")
    tabOrd = tablaManual.sort_values("Ruleta [%]", ascending=False)
    dic = tabOrd.to_dict("list")
    dicOrdFil = {
        "Binarios": dic["Binarios"],
        "Adaptado f(x)": dic["Adaptado f(x)"]
    }
    tablaOrdenada = pd.DataFrame(dicOrdFil, index=valoresLongitud)
    print(tablaOrdenada)
    # print(valoresLongitud)

    return tablaOrdenada, valoresLongitud
