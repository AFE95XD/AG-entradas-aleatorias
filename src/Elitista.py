import pandas as pd
from Modulos.opBasicas.Decodificacion import DecodificacionManuales, decoElitista
from Modulos.mutaciones.Mutacion import mutacionElitista, mutacionAuto, mutacionJerarElitista, mutacionAutoJerar, mutacionTorneoElitista, mutacionAutoTorneo
from Modulos.mutaciones.MutacionPC2 import mutacionPC2Elitista, mutacionPC2Auto, mutacionPC2JerarElitista, mutacionPC2AutoJerar, mutacionPC2TorneoElitista, mutacionPC2AutoTorneo
from Modulos.mutaciones.MutacionUniforme import mutacionUnifElitista, mutacionUnifAuto, mutacionUnifJerarElitista, mutacionUnifAutoJerar, mutacionUnifTorneoElitista, mutacionUnifAutoTorneo

'''------------------------------------Opciones con 1: Elitista------------------------------------'''

'''COMBINACION 1 A = Ruleta + Cruce de 1 punto'''
def elitista1A(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    tablaManual, _, = DecodificacionManuales(poblacion, longitud, rangoMin, rangoMax)
    tablaOrd = tablaManual.sort_values("Adaptado f(x)", ascending=False, ignore_index=True)
    # print("\n",tablaOrd)
    mejor = pd.DataFrame()
    fila = pd.Series(tablaOrd.iloc[0].to_dict())
    mejor = pd.concat([mejor, fila.to_frame().T], ignore_index=True)
    mejor.index = [1]
    print("\nEl individuo con mayor adaptacion es:\n")
    print(mejor)
    tablaNueva = tablaOrd.drop(index=0)
    print("\nLos individuos restantes son:\n")
    print(tablaNueva)
    _, tabla = mutacionElitista(tablaNueva, poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
    valoresIndi = []
    for x in range(len(tabla)):
        valoresIndi.append(x + 1)
    print("La tabla ordenada para evaluar es:\n")
    tabla = tabla.sort_values("Adaptado f(x)", ascending=False)
    tabla.index = valoresIndi
    print(tabla)
    if mejor.iloc[0].values[3] > tabla.iloc[0].values[1]:
        aux = tabla.iloc[0].values[0]
        tabla["Binarios"].values[0] = mejor["Binarios"].values[0]
        tabla["Adaptado f(x)"].values[0] = mejor["Adaptado f(x)"].values[0]
        numeroDecimal, numReal, numAdaptado = decoElitista(aux, rangoMin, rangoMax)
        mejor["Binarios"].values[0] = aux
        mejor["Decimal"].values[0] = numeroDecimal
        mejor["Reales"].values[0] = numReal
        mejor["Adaptado f(x)"].values[0] = numAdaptado
        # mejor.index = 
    
    print("\nEl nuevo mejor es:\n")
    print(mejor)
    # valoresLongitud = []
    # for x in range(len(tabla)):
    #     valoresLongitud.append(x + 1)
    dic = tabla.to_dict("list")
    print("\nLa tabla con los individuos es:\n")
    # tabla.index = valoresLongitud
    print(tabla)
    lista = dic["Binarios"]
    return lista, tabla, mejor

def elitista1Aauto(mejor1, listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce, tazaMutacion):
    _, tabla, = mutacionAuto(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce, tazaMutacion)

    print("La tabla ordenada para evaluar es:\n")
    tabla = tabla.sort_values("Adaptado f(x)", ascending=False)
    valoresIndi = []
    for x in range(len(tabla)):
        valoresIndi.append(x + 1)
    tabla.index = valoresIndi
    print(tabla)
    # input("en este punto ya se hizo S/C/M")
    if mejor1.iloc[0].values[3] > tabla.iloc[0].values[1]:
        aux = tabla.iloc[0].values[0]
        tabla["Binarios"].values[0] = mejor1["Binarios"].values[0]
        tabla["Adaptado f(x)"].values[0] = mejor1["Adaptado f(x)"].values[0]
        numeroDecimal, numReal, numAdaptado = decoElitista(aux, rangoMin, rangoMax)
        mejor1["Binarios"].values[0] = aux
        mejor1["Decimal"].values[0] = numeroDecimal
        mejor1["Reales"].values[0] = numReal
        mejor1["Adaptado f(x)"].values[0] = numAdaptado
        # mejor.index = 
    # input("en este punto ya EVALUO CUAL ES EL MAYOR CHECAR")
    
    print("\nEl nuevo mejor es:\n")
    print(mejor1)
    dic = tabla.to_dict("list")
    print("\nLa tabla con los individuos es:\n")
    # tabla.index = valoresLongitud
    print(tabla)
    print()
    lista = dic["Binarios"]
    return lista, tabla, mejor1

'''COMBINACION 1 B = Ruleta + Cruce de 2 puntos'''
def elitista1B(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    tablaManual, _, = DecodificacionManuales(poblacion, longitud, rangoMin, rangoMax)
    tablaOrd = tablaManual.sort_values("Adaptado f(x)", ascending=False, ignore_index=True)
    # print("\n",tablaOrd)
    mejor = pd.DataFrame()
    fila = pd.Series(tablaOrd.iloc[0].to_dict())
    mejor = pd.concat([mejor, fila.to_frame().T], ignore_index=True)
    mejor.index = [1]
    print("\nEl individuo con mayor adaptacion es:\n")
    print(mejor)
    tablaNueva = tablaOrd.drop(index=0)
    print("\nLos individuos restantes son:\n")
    print(tablaNueva)
    _, tabla = mutacionPC2Elitista(tablaNueva, poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
    valoresIndi = []
    for x in range(len(tabla)):
        valoresIndi.append(x + 1)
    print("La tabla ordenada para evaluar es:\n")
    tabla = tabla.sort_values("Adaptado f(x)", ascending=False)
    tabla.index = valoresIndi
    print(tabla)
    if mejor.iloc[0].values[3] > tabla.iloc[0].values[1]:
        aux = tabla.iloc[0].values[0]
        tabla["Binarios"].values[0] = mejor["Binarios"].values[0]
        tabla["Adaptado f(x)"].values[0] = mejor["Adaptado f(x)"].values[0]
        numeroDecimal, numReal, numAdaptado = decoElitista(aux, rangoMin, rangoMax)
        mejor["Binarios"].values[0] = aux
        mejor["Decimal"].values[0] = numeroDecimal
        mejor["Reales"].values[0] = numReal
        mejor["Adaptado f(x)"].values[0] = numAdaptado
        # mejor.index = 
    
    print("\nEl nuevo mejor es:\n")
    print(mejor)
    # valoresLongitud = []
    # for x in range(len(tabla)):
    #     valoresLongitud.append(x + 1)
    dic = tabla.to_dict("list")
    print("\nLa tabla con los individuos es:\n")
    # tabla.index = valoresLongitud
    print(tabla)
    lista = dic["Binarios"]
    return lista, tabla, mejor

def elitista1Bauto(mejor1, listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce, tazaMutacion):
    _, tabla, = mutacionPC2Auto(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce, tazaMutacion)

    print("La tabla ordenada para evaluar es:\n")
    tabla = tabla.sort_values("Adaptado f(x)", ascending=False)
    valoresIndi = []
    for x in range(len(tabla)):
        valoresIndi.append(x + 1)
    tabla.index = valoresIndi
    print(tabla)
    # input("en este punto ya se hizo S/C/M")
    if mejor1.iloc[0].values[3] > tabla.iloc[0].values[1]:
        aux = tabla.iloc[0].values[0]
        tabla["Binarios"].values[0] = mejor1["Binarios"].values[0]
        tabla["Adaptado f(x)"].values[0] = mejor1["Adaptado f(x)"].values[0]
        numeroDecimal, numReal, numAdaptado = decoElitista(aux, rangoMin, rangoMax)
        mejor1["Binarios"].values[0] = aux
        mejor1["Decimal"].values[0] = numeroDecimal
        mejor1["Reales"].values[0] = numReal
        mejor1["Adaptado f(x)"].values[0] = numAdaptado
        # mejor.index = 
    # input("en este punto ya EVALUO CUAL ES EL MAYOR CHECAR")
    
    print("\nEl nuevo mejor es:\n")
    print(mejor1)
    dic = tabla.to_dict("list")
    print("\nLa tabla con los individuos es:\n")
    # tabla.index = valoresLongitud
    print(tabla)
    print()
    lista = dic["Binarios"]
    return lista, tabla, mejor1

'''COMBINACION 1 C = Ruleta + Cruce Uniforme'''
def elitista1C(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    tablaManual, _, = DecodificacionManuales(poblacion, longitud, rangoMin, rangoMax)
    tablaOrd = tablaManual.sort_values("Adaptado f(x)", ascending=False, ignore_index=True)
    # print("\n",tablaOrd)
    mejor = pd.DataFrame()
    fila = pd.Series(tablaOrd.iloc[0].to_dict())
    mejor = pd.concat([mejor, fila.to_frame().T], ignore_index=True)
    mejor.index = [1]
    print("\nEl individuo con mayor adaptacion es:\n")
    print(mejor)
    tablaNueva = tablaOrd.drop(index=0)
    print("\nLos individuos restantes son:\n")
    print(tablaNueva)
    _, tabla = mutacionUnifElitista(tablaNueva, poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
    valoresIndi = []
    for x in range(len(tabla)):
        valoresIndi.append(x + 1)
    print("La tabla ordenada para evaluar es:\n")
    tabla = tabla.sort_values("Adaptado f(x)", ascending=False)
    tabla.index = valoresIndi
    print(tabla)
    if mejor.iloc[0].values[3] > tabla.iloc[0].values[1]:
        aux = tabla.iloc[0].values[0]
        tabla["Binarios"].values[0] = mejor["Binarios"].values[0]
        tabla["Adaptado f(x)"].values[0] = mejor["Adaptado f(x)"].values[0]
        numeroDecimal, numReal, numAdaptado = decoElitista(aux, rangoMin, rangoMax)
        mejor["Binarios"].values[0] = aux
        mejor["Decimal"].values[0] = numeroDecimal
        mejor["Reales"].values[0] = numReal
        mejor["Adaptado f(x)"].values[0] = numAdaptado
        # mejor.index = 
    
    print("\nEl nuevo mejor es:\n")
    print(mejor)
    # valoresLongitud = []
    # for x in range(len(tabla)):
    #     valoresLongitud.append(x + 1)
    dic = tabla.to_dict("list")
    print("\nLa tabla con los individuos es:\n")
    # tabla.index = valoresLongitud
    print(tabla)
    lista = dic["Binarios"]
    return lista, tabla, mejor

def elitista1Cauto(mejor1, listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce, tazaMutacion):
    _, tabla, = mutacionUnifAuto(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce, tazaMutacion)

    print("La tabla ordenada para evaluar es:\n")
    tabla = tabla.sort_values("Adaptado f(x)", ascending=False)
    valoresIndi = []
    for x in range(len(tabla)):
        valoresIndi.append(x + 1)
    tabla.index = valoresIndi
    print(tabla)
    # input("en este punto ya se hizo S/C/M")
    if mejor1.iloc[0].values[3] > tabla.iloc[0].values[1]:
        aux = tabla.iloc[0].values[0]
        tabla["Binarios"].values[0] = mejor1["Binarios"].values[0]
        tabla["Adaptado f(x)"].values[0] = mejor1["Adaptado f(x)"].values[0]
        numeroDecimal, numReal, numAdaptado = decoElitista(aux, rangoMin, rangoMax)
        mejor1["Binarios"].values[0] = aux
        mejor1["Decimal"].values[0] = numeroDecimal
        mejor1["Reales"].values[0] = numReal
        mejor1["Adaptado f(x)"].values[0] = numAdaptado
        # mejor.index = 
    # input("en este punto ya EVALUO CUAL ES EL MAYOR CHECAR")
    
    print("\nEl nuevo mejor es:\n")
    print(mejor1)
    dic = tabla.to_dict("list")
    print("\nLa tabla con los individuos es:\n")
    # tabla.index = valoresLongitud
    print(tabla)
    print()
    lista = dic["Binarios"]
    return lista, tabla, mejor1

'''------------------------------------Opciones con 2: Elitista------------------------------------'''

'''COMBINACION 2 A = Jerarquica + Cruce de 1 punto'''
def elitista2A(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    tablaManual, _, = DecodificacionManuales(poblacion, longitud, rangoMin, rangoMax)
    tablaOrd = tablaManual.sort_values("Adaptado f(x)", ascending=False, ignore_index=True)
    # print("\n",tablaOrd)
    mejor = pd.DataFrame()
    fila = pd.Series(tablaOrd.iloc[0].to_dict())
    mejor = pd.concat([mejor, fila.to_frame().T], ignore_index=True)
    mejor.index = [1]
    print("\nEl individuo con mayor adaptacion es:\n")
    print(mejor)
    tablaNueva = tablaOrd.drop(index=0)
    print("\nLos individuos restantes son:\n")
    print(tablaNueva)
    _, tabla = mutacionJerarElitista(tablaNueva, poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
    valoresIndi = []
    for x in range(len(tabla)):
        valoresIndi.append(x + 1)
    print("La tabla ordenada para evaluar es:\n")
    tabla = tabla.sort_values("Adaptado f(x)", ascending=False)
    tabla.index = valoresIndi
    print(tabla)
    if mejor.iloc[0].values[3] > tabla.iloc[0].values[1]:
        aux = tabla.iloc[0].values[0]
        tabla["Binarios"].values[0] = mejor["Binarios"].values[0]
        tabla["Adaptado f(x)"].values[0] = mejor["Adaptado f(x)"].values[0]
        numeroDecimal, numReal, numAdaptado = decoElitista(aux, rangoMin, rangoMax)
        mejor["Binarios"].values[0] = aux
        mejor["Decimal"].values[0] = numeroDecimal
        mejor["Reales"].values[0] = numReal
        mejor["Adaptado f(x)"].values[0] = numAdaptado
        # mejor.index = 
    
    print("\nEl nuevo mejor es:\n")
    print(mejor)
    # valoresLongitud = []
    # for x in range(len(tabla)):
    #     valoresLongitud.append(x + 1)
    dic = tabla.to_dict("list")
    print("\nLa tabla con los individuos es:\n")
    # tabla.index = valoresLongitud
    print(tabla)
    lista = dic["Binarios"]
    return lista, tabla, mejor

def elitista2Aauto(mejor1, listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce, tazaMutacion):
    _, tabla, = mutacionAutoJerar(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce, tazaMutacion)

    print("La tabla ordenada para evaluar es:\n")
    tabla = tabla.sort_values("Adaptado f(x)", ascending=False)
    valoresIndi = []
    for x in range(len(tabla)):
        valoresIndi.append(x + 1)
    tabla.index = valoresIndi
    print(tabla)
    # input("en este punto ya se hizo S/C/M")
    if mejor1.iloc[0].values[3] > tabla.iloc[0].values[1]:
        aux = tabla.iloc[0].values[0]
        tabla["Binarios"].values[0] = mejor1["Binarios"].values[0]
        tabla["Adaptado f(x)"].values[0] = mejor1["Adaptado f(x)"].values[0]
        numeroDecimal, numReal, numAdaptado = decoElitista(aux, rangoMin, rangoMax)
        mejor1["Binarios"].values[0] = aux
        mejor1["Decimal"].values[0] = numeroDecimal
        mejor1["Reales"].values[0] = numReal
        mejor1["Adaptado f(x)"].values[0] = numAdaptado
        # mejor.index = 
    # input("en este punto ya EVALUO CUAL ES EL MAYOR CHECAR")
    
    print("\nEl nuevo mejor es:\n")
    print(mejor1)
    dic = tabla.to_dict("list")
    print("\nLa tabla con los individuos es:\n")
    # tabla.index = valoresLongitud
    print(tabla)
    print()
    lista = dic["Binarios"]
    return lista, tabla, mejor1

'''COMBINACION 2 B = Jerarquica + Cruce de 2 puntos'''
def elitista2B(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    tablaManual, _, = DecodificacionManuales(poblacion, longitud, rangoMin, rangoMax)
    tablaOrd = tablaManual.sort_values("Adaptado f(x)", ascending=False, ignore_index=True)
    # print("\n",tablaOrd)
    mejor = pd.DataFrame()
    fila = pd.Series(tablaOrd.iloc[0].to_dict())
    mejor = pd.concat([mejor, fila.to_frame().T], ignore_index=True)
    mejor.index = [1]
    print("\nEl individuo con mayor adaptacion es:\n")
    print(mejor)
    tablaNueva = tablaOrd.drop(index=0)
    print("\nLos individuos restantes son:\n")
    print(tablaNueva)
    _, tabla = mutacionPC2JerarElitista(tablaNueva, poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
    valoresIndi = []
    for x in range(len(tabla)):
        valoresIndi.append(x + 1)
    print("La tabla ordenada para evaluar es:\n")
    tabla = tabla.sort_values("Adaptado f(x)", ascending=False)
    tabla.index = valoresIndi
    print(tabla)
    if mejor.iloc[0].values[3] > tabla.iloc[0].values[1]:
        aux = tabla.iloc[0].values[0]
        tabla["Binarios"].values[0] = mejor["Binarios"].values[0]
        tabla["Adaptado f(x)"].values[0] = mejor["Adaptado f(x)"].values[0]
        numeroDecimal, numReal, numAdaptado = decoElitista(aux, rangoMin, rangoMax)
        mejor["Binarios"].values[0] = aux
        mejor["Decimal"].values[0] = numeroDecimal
        mejor["Reales"].values[0] = numReal
        mejor["Adaptado f(x)"].values[0] = numAdaptado
        # mejor.index = 
    
    print("\nEl nuevo mejor es:\n")
    print(mejor)
    # valoresLongitud = []
    # for x in range(len(tabla)):
    #     valoresLongitud.append(x + 1)
    dic = tabla.to_dict("list")
    print("\nLa tabla con los individuos es:\n")
    # tabla.index = valoresLongitud
    print(tabla)
    lista = dic["Binarios"]
    return lista, tabla, mejor

def elitista2Bauto(mejor1, listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce, tazaMutacion):
    _, tabla, = mutacionPC2AutoJerar(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce, tazaMutacion)

    print("La tabla ordenada para evaluar es:\n")
    tabla = tabla.sort_values("Adaptado f(x)", ascending=False)
    valoresIndi = []
    for x in range(len(tabla)):
        valoresIndi.append(x + 1)
    tabla.index = valoresIndi
    print(tabla)
    # input("en este punto ya se hizo S/C/M")
    if mejor1.iloc[0].values[3] > tabla.iloc[0].values[1]:
        aux = tabla.iloc[0].values[0]
        tabla["Binarios"].values[0] = mejor1["Binarios"].values[0]
        tabla["Adaptado f(x)"].values[0] = mejor1["Adaptado f(x)"].values[0]
        numeroDecimal, numReal, numAdaptado = decoElitista(aux, rangoMin, rangoMax)
        mejor1["Binarios"].values[0] = aux
        mejor1["Decimal"].values[0] = numeroDecimal
        mejor1["Reales"].values[0] = numReal
        mejor1["Adaptado f(x)"].values[0] = numAdaptado
        # mejor.index = 
    # input("en este punto ya EVALUO CUAL ES EL MAYOR CHECAR")
    
    print("\nEl nuevo mejor es:\n")
    print(mejor1)
    dic = tabla.to_dict("list")
    print("\nLa tabla con los individuos es:\n")
    # tabla.index = valoresLongitud
    print(tabla)
    print()
    lista = dic["Binarios"]
    return lista, tabla, mejor1

'''COMBINACION 2 C = Jerarquica + Cruce Uniforme'''
def elitista2C(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    tablaManual, _, = DecodificacionManuales(poblacion, longitud, rangoMin, rangoMax)
    tablaOrd = tablaManual.sort_values("Adaptado f(x)", ascending=False, ignore_index=True)
    # print("\n",tablaOrd)
    mejor = pd.DataFrame()
    fila = pd.Series(tablaOrd.iloc[0].to_dict())
    mejor = pd.concat([mejor, fila.to_frame().T], ignore_index=True)
    mejor.index = [1]
    print("\nEl individuo con mayor adaptacion es:\n")
    print(mejor)
    tablaNueva = tablaOrd.drop(index=0)
    print("\nLos individuos restantes son:\n")
    print(tablaNueva)
    _, tabla = mutacionUnifJerarElitista(tablaNueva, poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
    valoresIndi = []
    for x in range(len(tabla)):
        valoresIndi.append(x + 1)
    print("La tabla ordenada para evaluar es:\n")
    tabla = tabla.sort_values("Adaptado f(x)", ascending=False)
    tabla.index = valoresIndi
    print(tabla)
    if mejor.iloc[0].values[3] > tabla.iloc[0].values[1]:
        aux = tabla.iloc[0].values[0]
        tabla["Binarios"].values[0] = mejor["Binarios"].values[0]
        tabla["Adaptado f(x)"].values[0] = mejor["Adaptado f(x)"].values[0]
        numeroDecimal, numReal, numAdaptado = decoElitista(aux, rangoMin, rangoMax)
        mejor["Binarios"].values[0] = aux
        mejor["Decimal"].values[0] = numeroDecimal
        mejor["Reales"].values[0] = numReal
        mejor["Adaptado f(x)"].values[0] = numAdaptado
        # mejor.index = 
    
    print("\nEl nuevo mejor es:\n")
    print(mejor)
    # valoresLongitud = []
    # for x in range(len(tabla)):
    #     valoresLongitud.append(x + 1)
    dic = tabla.to_dict("list")
    print("\nLa tabla con los individuos es:\n")
    # tabla.index = valoresLongitud
    print(tabla)
    lista = dic["Binarios"]
    return lista, tabla, mejor

def elitista2Cauto(mejor1, listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce, tazaMutacion):
    _, tabla, = mutacionUnifAutoJerar(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce, tazaMutacion)

    print("La tabla ordenada para evaluar es:\n")
    tabla = tabla.sort_values("Adaptado f(x)", ascending=False)
    valoresIndi = []
    for x in range(len(tabla)):
        valoresIndi.append(x + 1)
    tabla.index = valoresIndi
    print(tabla)
    # input("en este punto ya se hizo S/C/M")
    if mejor1.iloc[0].values[3] > tabla.iloc[0].values[1]:
        aux = tabla.iloc[0].values[0]
        tabla["Binarios"].values[0] = mejor1["Binarios"].values[0]
        tabla["Adaptado f(x)"].values[0] = mejor1["Adaptado f(x)"].values[0]
        numeroDecimal, numReal, numAdaptado = decoElitista(aux, rangoMin, rangoMax)
        mejor1["Binarios"].values[0] = aux
        mejor1["Decimal"].values[0] = numeroDecimal
        mejor1["Reales"].values[0] = numReal
        mejor1["Adaptado f(x)"].values[0] = numAdaptado
        # mejor.index = 
    # input("en este punto ya EVALUO CUAL ES EL MAYOR CHECAR")
    
    print("\nEl nuevo mejor es:\n")
    print(mejor1)
    dic = tabla.to_dict("list")
    print("\nLa tabla con los individuos es:\n")
    # tabla.index = valoresLongitud
    print(tabla)
    print()
    lista = dic["Binarios"]
    return lista, tabla, mejor1

'''------------------------------------Opciones con 3: Elitista------------------------------------'''

'''COMBINACION 3 A = Torneo + Cruce de 1 punto'''
def elitista3A(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    tablaManual, _, = DecodificacionManuales(poblacion, longitud, rangoMin, rangoMax)
    tablaOrd = tablaManual.sort_values("Adaptado f(x)", ascending=False, ignore_index=True)
    # print("\n",tablaOrd)
    mejor = pd.DataFrame()
    fila = pd.Series(tablaOrd.iloc[0].to_dict())
    mejor = pd.concat([mejor, fila.to_frame().T], ignore_index=True)
    mejor.index = [1]
    print("\nEl individuo con mayor adaptacion es:\n")
    print(mejor)
    tablaNueva = tablaOrd.drop(index=0)
    print("\nLos individuos restantes son:\n")
    print(tablaNueva)
    _, tabla = mutacionTorneoElitista(tablaNueva, poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
    valoresIndi = []
    for x in range(len(tabla)):
        valoresIndi.append(x + 1)
    print("La tabla ordenada para evaluar es:\n")
    tabla = tabla.sort_values("Adaptado f(x)", ascending=False)
    tabla.index = valoresIndi
    print(tabla)
    if mejor.iloc[0].values[3] > tabla.iloc[0].values[1]:
        aux = tabla.iloc[0].values[0]
        tabla["Binarios"].values[0] = mejor["Binarios"].values[0]
        tabla["Adaptado f(x)"].values[0] = mejor["Adaptado f(x)"].values[0]
        numeroDecimal, numReal, numAdaptado = decoElitista(aux, rangoMin, rangoMax)
        mejor["Binarios"].values[0] = aux
        mejor["Decimal"].values[0] = numeroDecimal
        mejor["Reales"].values[0] = numReal
        mejor["Adaptado f(x)"].values[0] = numAdaptado
        # mejor.index = 
    
    print("\nEl nuevo mejor es:\n")
    print(mejor)
    # valoresLongitud = []
    # for x in range(len(tabla)):
    #     valoresLongitud.append(x + 1)
    dic = tabla.to_dict("list")
    print("\nLa tabla con los individuos es:\n")
    # tabla.index = valoresLongitud
    print(tabla)
    lista = dic["Binarios"]
    return lista, tabla, mejor

def elitista3Aauto(mejor1, listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce, tazaMutacion):
    _, tabla, = mutacionAutoTorneo(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce, tazaMutacion)

    print("La tabla ordenada para evaluar es:\n")
    tabla = tabla.sort_values("Adaptado f(x)", ascending=False)
    valoresIndi = []
    for x in range(len(tabla)):
        valoresIndi.append(x + 1)
    tabla.index = valoresIndi
    print(tabla)
    # input("en este punto ya se hizo S/C/M")
    if mejor1.iloc[0].values[3] > tabla.iloc[0].values[1]:
        aux = tabla.iloc[0].values[0]
        tabla["Binarios"].values[0] = mejor1["Binarios"].values[0]
        tabla["Adaptado f(x)"].values[0] = mejor1["Adaptado f(x)"].values[0]
        numeroDecimal, numReal, numAdaptado = decoElitista(aux, rangoMin, rangoMax)
        mejor1["Binarios"].values[0] = aux
        mejor1["Decimal"].values[0] = numeroDecimal
        mejor1["Reales"].values[0] = numReal
        mejor1["Adaptado f(x)"].values[0] = numAdaptado
        # mejor.index = 
    # input("en este punto ya EVALUO CUAL ES EL MAYOR CHECAR")
    
    print("\nEl nuevo mejor es:\n")
    print(mejor1)
    dic = tabla.to_dict("list")
    print("\nLa tabla con los individuos es:\n")
    # tabla.index = valoresLongitud
    print(tabla)
    print()
    lista = dic["Binarios"]
    return lista, tabla, mejor1

'''COMBINACION 3 B = Torneo + Cruce de 2 puntos'''
def elitista3B(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    tablaManual, _, = DecodificacionManuales(poblacion, longitud, rangoMin, rangoMax)
    tablaOrd = tablaManual.sort_values("Adaptado f(x)", ascending=False, ignore_index=True)
    # print("\n",tablaOrd)
    mejor = pd.DataFrame()
    fila = pd.Series(tablaOrd.iloc[0].to_dict())
    mejor = pd.concat([mejor, fila.to_frame().T], ignore_index=True)
    mejor.index = [1]
    print("\nEl individuo con mayor adaptacion es:\n")
    print(mejor)
    tablaNueva = tablaOrd.drop(index=0)
    print("\nLos individuos restantes son:\n")
    print(tablaNueva)
    _, tabla = mutacionPC2TorneoElitista(tablaNueva, poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
    valoresIndi = []
    for x in range(len(tabla)):
        valoresIndi.append(x + 1)
    print("La tabla ordenada para evaluar es:\n")
    tabla = tabla.sort_values("Adaptado f(x)", ascending=False)
    tabla.index = valoresIndi
    print(tabla)
    if mejor.iloc[0].values[3] > tabla.iloc[0].values[1]:
        aux = tabla.iloc[0].values[0]
        tabla["Binarios"].values[0] = mejor["Binarios"].values[0]
        tabla["Adaptado f(x)"].values[0] = mejor["Adaptado f(x)"].values[0]
        numeroDecimal, numReal, numAdaptado = decoElitista(aux, rangoMin, rangoMax)
        mejor["Binarios"].values[0] = aux
        mejor["Decimal"].values[0] = numeroDecimal
        mejor["Reales"].values[0] = numReal
        mejor["Adaptado f(x)"].values[0] = numAdaptado
        # mejor.index = 
    
    print("\nEl nuevo mejor es:\n")
    print(mejor)
    # valoresLongitud = []
    # for x in range(len(tabla)):
    #     valoresLongitud.append(x + 1)
    dic = tabla.to_dict("list")
    print("\nLa tabla con los individuos es:\n")
    # tabla.index = valoresLongitud
    print(tabla)
    lista = dic["Binarios"]
    return lista, tabla, mejor

def elitista3Bauto(mejor1, listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce, tazaMutacion):
    _, tabla, = mutacionPC2AutoTorneo(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce, tazaMutacion)

    print("La tabla ordenada para evaluar es:\n")
    tabla = tabla.sort_values("Adaptado f(x)", ascending=False)
    valoresIndi = []
    for x in range(len(tabla)):
        valoresIndi.append(x + 1)
    tabla.index = valoresIndi
    print(tabla)
    # input("en este punto ya se hizo S/C/M")
    if mejor1.iloc[0].values[3] > tabla.iloc[0].values[1]:
        aux = tabla.iloc[0].values[0]
        tabla["Binarios"].values[0] = mejor1["Binarios"].values[0]
        tabla["Adaptado f(x)"].values[0] = mejor1["Adaptado f(x)"].values[0]
        numeroDecimal, numReal, numAdaptado = decoElitista(aux, rangoMin, rangoMax)
        mejor1["Binarios"].values[0] = aux
        mejor1["Decimal"].values[0] = numeroDecimal
        mejor1["Reales"].values[0] = numReal
        mejor1["Adaptado f(x)"].values[0] = numAdaptado
        # mejor.index = 
    # input("en este punto ya EVALUO CUAL ES EL MAYOR CHECAR")
    
    print("\nEl nuevo mejor es:\n")
    print(mejor1)
    dic = tabla.to_dict("list")
    print("\nLa tabla con los individuos es:\n")
    # tabla.index = valoresLongitud
    print(tabla)
    print()
    lista = dic["Binarios"]
    return lista, tabla, mejor1

'''COMBINACION 3 C = Torneo + Cruce Uniforme'''
def elitista3C(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    tablaManual, _, = DecodificacionManuales(poblacion, longitud, rangoMin, rangoMax)
    tablaOrd = tablaManual.sort_values("Adaptado f(x)", ascending=False, ignore_index=True)
    # print("\n",tablaOrd)
    mejor = pd.DataFrame()
    fila = pd.Series(tablaOrd.iloc[0].to_dict())
    mejor = pd.concat([mejor, fila.to_frame().T], ignore_index=True)
    mejor.index = [1]
    print("\nEl individuo con mayor adaptacion es:\n")
    print(mejor)
    tablaNueva = tablaOrd.drop(index=0)
    print("\nLos individuos restantes son:\n")
    print(tablaNueva)
    _, tabla = mutacionUnifTorneoElitista(tablaNueva, poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
    valoresIndi = []
    for x in range(len(tabla)):
        valoresIndi.append(x + 1)
    print("La tabla ordenada para evaluar es:\n")
    tabla = tabla.sort_values("Adaptado f(x)", ascending=False)
    tabla.index = valoresIndi
    print(tabla)
    if mejor.iloc[0].values[3] > tabla.iloc[0].values[1]:
        aux = tabla.iloc[0].values[0]
        tabla["Binarios"].values[0] = mejor["Binarios"].values[0]
        tabla["Adaptado f(x)"].values[0] = mejor["Adaptado f(x)"].values[0]
        numeroDecimal, numReal, numAdaptado = decoElitista(aux, rangoMin, rangoMax)
        mejor["Binarios"].values[0] = aux
        mejor["Decimal"].values[0] = numeroDecimal
        mejor["Reales"].values[0] = numReal
        mejor["Adaptado f(x)"].values[0] = numAdaptado
        # mejor.index = 
    
    print("\nEl nuevo mejor es:\n")
    print(mejor)
    # valoresLongitud = []
    # for x in range(len(tabla)):
    #     valoresLongitud.append(x + 1)
    dic = tabla.to_dict("list")
    print("\nLa tabla con los individuos es:\n")
    # tabla.index = valoresLongitud
    print(tabla)
    lista = dic["Binarios"]
    return lista, tabla, mejor

def elitista3Cauto(mejor1, listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce, tazaMutacion):
    _, tabla, = mutacionUnifAutoTorneo(listaBin, poblacion, longitud, rangoMin, rangoMax, i, tazaCruce, tazaMutacion)

    print("La tabla ordenada para evaluar es:\n")
    tabla = tabla.sort_values("Adaptado f(x)", ascending=False)
    valoresIndi = []
    for x in range(len(tabla)):
        valoresIndi.append(x + 1)
    tabla.index = valoresIndi
    print(tabla)
    # input("en este punto ya se hizo S/C/M")
    if mejor1.iloc[0].values[3] > tabla.iloc[0].values[1]:
        aux = tabla.iloc[0].values[0]
        tabla["Binarios"].values[0] = mejor1["Binarios"].values[0]
        tabla["Adaptado f(x)"].values[0] = mejor1["Adaptado f(x)"].values[0]
        numeroDecimal, numReal, numAdaptado = decoElitista(aux, rangoMin, rangoMax)
        mejor1["Binarios"].values[0] = aux
        mejor1["Decimal"].values[0] = numeroDecimal
        mejor1["Reales"].values[0] = numReal
        mejor1["Adaptado f(x)"].values[0] = numAdaptado
        # mejor.index = 
    # input("en este punto ya EVALUO CUAL ES EL MAYOR CHECAR")
    
    print("\nEl nuevo mejor es:\n")
    print(mejor1)
    dic = tabla.to_dict("list")
    print("\nLa tabla con los individuos es:\n")
    # tabla.index = valoresLongitud
    print(tabla)
    print()
    lista = dic["Binarios"]
    return lista, tabla, mejor1
