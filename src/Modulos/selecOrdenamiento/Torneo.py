import random
import pandas as pd
from Modulos.opBasicas.Decodificacion import DecodificacionManuales, DecodificacionAuto

def torneo(poblacion, longitud, rangoMin, rangoMax):
    tablaManual, valoresLongitud = DecodificacionManuales(poblacion, longitud, rangoMin, rangoMax)
    numAl = []
    while len(numAl) < len(valoresLongitud):
        numero = random.randint(1,len(valoresLongitud))
        if numero in numAl:
            pass
        else:
            numAl.append(numero)

    nuevaTabla = pd.DataFrame()

    if len(numAl) % 2 == 0:
        print("-----------------------------Empieza Torneo-----------------------------")
        for i, j in zip(range(0,len(numAl)-1,2),range(1,len(numAl),2)):
            indi1 = tablaManual["Adaptado f(x)"].values[numAl[i]-1]
            indi2 = tablaManual["Adaptado f(x)"].values[numAl[j]-1]
            print(f"\nIndividuo {numAl[i]} con adaptacion = {indi1} VS Individuo {numAl[j]} con adaptacion = {indi2}")
            
            if indi1 > indi2:
                fila = pd.Series(tablaManual.iloc[numAl[i]-1].to_dict())
                nuevaTabla = pd.concat([nuevaTabla, fila.to_frame().T], ignore_index=True)
                print(f"\nEl ganador es el individuo {numAl[i]}")
                print("-------------------------------------------\n")
            else:
                fila = pd.Series(tablaManual.iloc[numAl[j]-1].to_dict())
                nuevaTabla = pd.concat([nuevaTabla, fila.to_frame().T], ignore_index=True)
                print(f"\nEl ganador es el individuo {numAl[j]}")
                print("-------------------------------------------\n")
    else:
        print("-----------------------------Empieza Torneo-----------------------------")
        for i, j in zip(range(0,len(numAl)-1,2),range(1,len(numAl),2)):
            indi1 = tablaManual["Adaptado f(x)"].values[numAl[i]-1]
            indi2 = tablaManual["Adaptado f(x)"].values[numAl[j]-1]
            print(f"\nIndividuo {numAl[i]} con adaptacion = {indi1} VS Individuo {numAl[j]} con adaptacion = {indi2}")
            
            if indi1 > indi2:
                fila = pd.Series(tablaManual.iloc[numAl[i]-1].to_dict())
                nuevaTabla = pd.concat([nuevaTabla, fila.to_frame().T], ignore_index=True)
                print(f"\nEl ganador es el individuo {numAl[i]}")
                print("-------------------------------------------\n")
            else:
                fila = pd.Series(tablaManual.iloc[numAl[j]-1].to_dict())
                nuevaTabla = pd.concat([nuevaTabla, fila.to_frame().T], ignore_index=True)
                print(f"\nEl ganador es el individuo {numAl[j]}")
                print("-------------------------------------------\n")
        
        ultimo = numAl[len(numAl)-1]
        print(f"El ultimo individuo es {ultimo} por lo tanto.\n")
        fila = pd.Series(tablaManual.iloc[ultimo-1].to_dict())
        nuevaTabla = pd.concat([nuevaTabla, fila.to_frame().T], ignore_index=True)
        print(f"\nEl ganador es el individuo {ultimo}")
        print("-------------------------------------------\n")
    
    valoresLongitud = []
    for x in range(len(nuevaTabla)):
        valoresLongitud.append(x + 1)
    nuevaTabla.index = valoresLongitud
    print("La Tabla Ordenada con Torneo es:\n")
    print(nuevaTabla)
    dic = nuevaTabla.to_dict("list")
    print("Agregando Individuos Faltantes")
    pobF = poblacion/2
    tablaManualF, _, = DecodificacionManuales(pobF, longitud, rangoMin, rangoMax)
    dicF = tablaManualF.to_dict("list")
    dicOrdFil = {
        "Binarios": dic["Binarios"] + dicF["Binarios"],
        "Adaptado f(x)": dic["Adaptado f(x)"] + dicF["Adaptado f(x)"]
    }
    tablaOrdenada = pd.DataFrame(dicOrdFil)
    valoresLongitud = []
    for x in range(len(tablaOrdenada)):
        valoresLongitud.append(x + 1)
    tablaOrdenada.index = valoresLongitud
    print("\nLa Tabla Ordenada con Torneo de Binarios y adaptados es:\n")
    print(tablaOrdenada)
    return tablaOrdenada, valoresLongitud

def torneoAuto(listaBin, poblacion, longitud, rangoMin, rangoMax, i):
    tablaManual, valoresLongitud = DecodificacionAuto(listaBin, poblacion, longitud, rangoMin, rangoMax, i)
    numAl = []
    while len(numAl) < len(valoresLongitud):
        numero = random.randint(1,len(valoresLongitud))
        if numero in numAl:
            pass
        else:
            numAl.append(numero)

    nuevaTabla = pd.DataFrame()

    if len(numAl) % 2 == 0:
        print("-----------------------------Empieza Torneo-----------------------------")
        for i, j in zip(range(0,len(numAl)-1,2),range(1,len(numAl),2)):
            indi1 = tablaManual["Adaptado f(x)"].values[numAl[i]-1]
            indi2 = tablaManual["Adaptado f(x)"].values[numAl[j]-1]
            print(f"\nIndividuo {numAl[i]} con adaptacion = {indi1} VS Individuo {numAl[j]} con adaptacion = {indi2}")
            
            if indi1 > indi2:
                fila = pd.Series(tablaManual.iloc[numAl[i]-1].to_dict())
                nuevaTabla = pd.concat([nuevaTabla, fila.to_frame().T], ignore_index=True)
                print(f"\nEl ganador es el individuo {numAl[i]}")
                print("-------------------------------------------\n")
            else:
                fila = pd.Series(tablaManual.iloc[numAl[j]-1].to_dict())
                nuevaTabla = pd.concat([nuevaTabla, fila.to_frame().T], ignore_index=True)
                print(f"\nEl ganador es el individuo {numAl[j]}")
                print("-------------------------------------------\n")
    else:
        print("-----------------------------Empieza Torneo-----------------------------")
        for i, j in zip(range(0,len(numAl)-1,2),range(1,len(numAl),2)):
            indi1 = tablaManual["Adaptado f(x)"].values[numAl[i]-1]
            indi2 = tablaManual["Adaptado f(x)"].values[numAl[j]-1]
            print(f"\nIndividuo {numAl[i]} con adaptacion = {indi1} VS Individuo {numAl[j]} con adaptacion = {indi2}")
            
            if indi1 > indi2:
                fila = pd.Series(tablaManual.iloc[numAl[i]-1].to_dict())
                nuevaTabla = pd.concat([nuevaTabla, fila.to_frame().T], ignore_index=True)
                print(f"\nEl ganador es el individuo {numAl[i]}")
                print("-------------------------------------------\n")
            else:
                fila = pd.Series(tablaManual.iloc[numAl[j]-1].to_dict())
                nuevaTabla = pd.concat([nuevaTabla, fila.to_frame().T], ignore_index=True)
                print(f"\nEl ganador es el individuo {numAl[j]}")
                print("-------------------------------------------\n")
        ultimo = numAl[len(numAl)-1]
        print(f"El ultimo individuo es {ultimo} por lo tanto.\n")
        fila = pd.Series(tablaManual.iloc[ultimo-1].to_dict())
        nuevaTabla = pd.concat([nuevaTabla, fila.to_frame().T], ignore_index=True)
        print(f"\nEl ganador es el individuo {ultimo}")
        print("-------------------------------------------\n")
    
    valoresLongitud = []
    for x in range(len(nuevaTabla)):
        valoresLongitud.append(x + 1)
    nuevaTabla.index = valoresLongitud
    print("La Tabla Ordenada con Torneo es:\n")
    print(nuevaTabla)
    dic = nuevaTabla.to_dict("list")
    print("Agregando Individuos Faltantes")
    pobF = poblacion/2
    tablaManualF, _, = DecodificacionManuales(pobF, longitud, rangoMin, rangoMax)
    dicF = tablaManualF.to_dict("list")
    dicOrdFil = {
        "Binarios": dic["Binarios"] + dicF["Binarios"],
        "Adaptado f(x)": dic["Adaptado f(x)"] + dicF["Adaptado f(x)"]
    }
    tablaOrdenada = pd.DataFrame(dicOrdFil)
    valoresLongitud = []
    for x in range(len(tablaOrdenada)):
        valoresLongitud.append(x + 1)
    tablaOrdenada.index = valoresLongitud
    print("\nLa Tabla Ordenada con Torneo de Binarios y adaptados es:\n")
    print(tablaOrdenada)
    return tablaOrdenada, valoresLongitud

'''------------------------Elitista------------------------'''
def torneoElitista(tablaManual, poblacion, longitud, rangoMin, rangoMax):
    valoresLongitud = []
    for x in range(len(tablaManual)):
        valoresLongitud.append(x + 1)

    numAl = []
    while len(numAl) < len(valoresLongitud):
        numero = random.randint(1,len(valoresLongitud))
        if numero in numAl:
            pass
        else:
            numAl.append(numero)

    nuevaTabla = pd.DataFrame()

    if len(numAl) % 2 == 0:
        print("-----------------------------Empieza Torneo-----------------------------")
        for i, j in zip(range(0,len(numAl)-1,2),range(1,len(numAl),2)):
            indi1 = tablaManual["Adaptado f(x)"].values[numAl[i]-1]
            indi2 = tablaManual["Adaptado f(x)"].values[numAl[j]-1]
            print(f"\nIndividuo {numAl[i]} con adaptacion = {indi1} VS Individuo {numAl[j]} con adaptacion = {indi2}")
            
            if indi1 > indi2:
                fila = pd.Series(tablaManual.iloc[numAl[i]-1].to_dict())
                nuevaTabla = pd.concat([nuevaTabla, fila.to_frame().T], ignore_index=True)
                print(f"\nEl ganador es el individuo {numAl[i]}")
                print("-------------------------------------------\n")
            else:
                fila = pd.Series(tablaManual.iloc[numAl[j]-1].to_dict())
                nuevaTabla = pd.concat([nuevaTabla, fila.to_frame().T], ignore_index=True)
                print(f"\nEl ganador es el individuo {numAl[j]}")
                print("-------------------------------------------\n")
    else:
        print("-----------------------------Empieza Torneo-----------------------------")
        for i, j in zip(range(0,len(numAl)-1,2),range(1,len(numAl),2)):
            indi1 = tablaManual["Adaptado f(x)"].values[numAl[i]-1]
            indi2 = tablaManual["Adaptado f(x)"].values[numAl[j]-1]
            print(f"\nIndividuo {numAl[i]} con adaptacion = {indi1} VS Individuo {numAl[j]} con adaptacion = {indi2}")
            
            if indi1 > indi2:
                fila = pd.Series(tablaManual.iloc[numAl[i]-1].to_dict())
                nuevaTabla = pd.concat([nuevaTabla, fila.to_frame().T], ignore_index=True)
                print(f"\nEl ganador es el individuo {numAl[i]}")
                print("-------------------------------------------\n")
            else:
                fila = pd.Series(tablaManual.iloc[numAl[j]-1].to_dict())
                nuevaTabla = pd.concat([nuevaTabla, fila.to_frame().T], ignore_index=True)
                print(f"\nEl ganador es el individuo {numAl[j]}")
                print("-------------------------------------------\n")
        
        ultimo = numAl[len(numAl)-1]
        print(f"El ultimo individuo es {ultimo} por lo tanto.\n")
        fila = pd.Series(tablaManual.iloc[ultimo-1].to_dict())
        nuevaTabla = pd.concat([nuevaTabla, fila.to_frame().T], ignore_index=True)
        print(f"\nEl ganador es el individuo {ultimo}")
        print("-------------------------------------------\n")
    
    valoresLongitud = []
    for x in range(len(nuevaTabla)):
        valoresLongitud.append(x + 1)
    nuevaTabla.index = valoresLongitud
    print("La Tabla Ordenada con Torneo es:\n")
    print(nuevaTabla)
    dic = nuevaTabla.to_dict("list")
    print("Agregando Individuos Faltantes")
    pobF = poblacion/2
    tablaManualF, _, = DecodificacionManuales(pobF, longitud, rangoMin, rangoMax)
    dicF = tablaManualF.to_dict("list")
    dicOrdFil = {
        "Binarios": dic["Binarios"] + dicF["Binarios"],
        "Adaptado f(x)": dic["Adaptado f(x)"] + dicF["Adaptado f(x)"]
    }
    tablaOrdenada = pd.DataFrame(dicOrdFil)
    valoresLongitud = []
    for x in range(len(tablaOrdenada)):
        valoresLongitud.append(x + 1)
    tablaOrdenada.index = valoresLongitud
    print("\nLa Tabla Ordenada con Torneo de Binarios y adaptados es:\n")
    print(tablaOrdenada)
    return tablaOrdenada, valoresLongitud


