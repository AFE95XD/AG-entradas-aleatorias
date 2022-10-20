import math
from Generaciones import combi1a, combi1b, combi1c, combi2a, combi2b, combi2c
print('''
************************************************************
*    --------------------Bienvenido-------------------     *
*                                                          *
*    Escoja el tipo de Algoridmo Genetico.                 *
*                                                          *
*    -----------------Tipo de Algoritmo---------------     *
*                                                          *
*    1) Algoritmo Genetico Secuencial                      *
*    2) Algoritmo Genetico Elitista                        *
*                                                          *
************************************************************
''')
algoritmo = input("Ingrese el tipo de Algoritmo: ")

print('''
************************************************************
*    --------------------Bienvenido-------------------     *
*                                                          *
*    Escoja la configuracion del algoridmo genetico.       *
*                                                          *
*    ------------------Seleccion----------------------     *
*                                                          *
*    1) Seleccion o Ordenamamiento Ruleta                  *
*    2) Seleccion o Ordenamamiento Jerarquica              *
*                                                          *
*    ------------------Metodo de Cruce----------------     *
*                                                          *
*    a) Cruce de 1 punto                                   *
*    b) Cruce de 2 Puntos                                  *
*    c) Cruce Uniforme                                     *
*                                                          *
************************************************************
''')
seleccion = input("Ingrese el tipo de Seleccion: ")
metCruce = input("Ingrese el tipo de Cruce: ")
print()
poblacion = int(input("Por favor ingrese la poblacion: "))
presicion = float(input("Por favor ingresa la presicion: "))
rangoMin = int(input("Ingrese el rango minimo: "))
rangoMax = int(input("Ingrese el rango maximo: "))
tazaCruce = int(input("Ingrese la taza de cruce: "))
tazaMutacion = int(input("Ingrese la taza de mutacion: "))
longitud = round(math.log2(1+((rangoMax - rangoMin) / presicion)))

if algoritmo == "1":
    '''Primera Opcion'''
    if seleccion == "1" and metCruce == "a":
        combi1a(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
    elif seleccion == "1" and metCruce == "b":
        combi1b(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
    elif seleccion == "1" and metCruce == "c":
        combi1c(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
        '''Segunda Opcion'''
    elif seleccion == "2" and metCruce == "a":
        combi2a(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
    elif seleccion == "2" and metCruce == "b":
        combi2b(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
    elif seleccion == "2" and metCruce == "c":
        combi2c(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)

elif algoritmo == "2":
    '''Primera Opcion'''
    if seleccion == "1" and metCruce == "a":
        combi1a(poblacion, longitud, rangoMin, rangoMax)
    elif seleccion == "1" and metCruce == "b":
        combi1b(poblacion, longitud, rangoMin, rangoMax)
    elif seleccion == "1" and metCruce == "c":
        combi1c(poblacion, longitud, rangoMin, rangoMax)
        '''Segunda Opcion'''
    elif seleccion == "2" and metCruce == "a":
        combi2a(poblacion, longitud, rangoMin, rangoMax)
    elif seleccion == "2" and metCruce == "b":
        combi2b(poblacion, longitud, rangoMin, rangoMax)
    elif seleccion == "2" and metCruce == "c":
        combi2c(poblacion, longitud, rangoMin, rangoMax)