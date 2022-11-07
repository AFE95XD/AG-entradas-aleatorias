from Generaciones import combi1a, combi1b, combi1c, combi2a, combi2b, combi2c, combi3a, combi3b, combi3c, combi21a, combi21b, combi21c, combi22a, combi22b, combi22c, combi23a, combi23b, combi23c
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
*    3) Seleccion o Ordenamamiento Torneo                  *
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
# presicion = float(input("Por favor ingresa la presicion: "))
rangoMin = int(input("Ingrese el rango minimo: "))
rangoMax = int(input("Ingrese el rango maximo: "))
tazaCruce = int(input("Ingrese la taza de cruce: "))
tazaMutacion = int(input("Ingrese la taza de mutacion: "))
# longitud = round(math.log2(1+((rangoMax - rangoMin) / presicion)))
longitud = int(input("por favor ingresa la longitud: "))
# print(longitud)
# print(type(longitud))
# input()

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
        '''Tercera Opcion'''
    elif seleccion == "3" and metCruce == "a":
        combi3a(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
    elif seleccion == "3" and metCruce == "b":
        combi3b(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
    elif seleccion == "3" and metCruce == "c":
        combi3c(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)

elif algoritmo == "2":
    '''Primera Opcion'''
    if seleccion == "1" and metCruce == "a":
        combi21a(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
    elif seleccion == "1" and metCruce == "b":
        combi21b(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
    elif seleccion == "1" and metCruce == "c":
        combi21c(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
        '''Segunda Opcion'''
    elif seleccion == "2" and metCruce == "a":
        combi22a(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
    elif seleccion == "2" and metCruce == "b":
        combi22b(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
    elif seleccion == "2" and metCruce == "c":
        combi22c(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
        '''Tercera Opcion'''
    elif seleccion == "3" and metCruce == "a":
        combi23a(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
    elif seleccion == "3" and metCruce == "b":
        combi23b(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
    elif seleccion == "3" and metCruce == "c":
        combi23c(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)