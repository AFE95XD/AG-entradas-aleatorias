import pandas as pd
from Modulos.mutaciones.Mutacion import mutacion, mutacionAuto, mutacionJerar, mutacionAutoJerar
from Modulos.opBasicas.Decodificacion import DecodificacionAuto, funcionMatematica
from Modulos.mutaciones.MutacionPC2 import mutacionPC2, mutacionPC2Auto, mutacionPC2Jerar, mutacionPC2AutoJerar
from Modulos.mutaciones.MutacionUniforme import mutacionUnif, mutacionUnifAuto, mutacionUnifJerar, mutacionUnifAutoJerar

writer = pd.ExcelWriter("src/img/mejores.xlsx", engine='openpyxl')

'''------------------------------------Opciones con 1------------------------------------'''

'''COMBINACION 1 A = Ruleta + Cruce de 1 punto'''
def combi1a(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    listaBinarios, tabla = mutacion(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
    print('''
************************************************************
*    --------------------Tipo de Paro-----------------     *
*                                                          *
*    1) Generaciones                                       *
*    2) Convergencia                                       *
*                                                          *
*                                                          *
************************************************************
''')
    paro = input("Ingrese el tipo de Paro: ")

    if paro == "1":
        gen = int(input("Ingrese el numero de generaciones: "))
        print()
        x = 1
        while (x != gen):
            listaBin, tabla = mutacionAuto(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x, tazaCruce, tazaMutacion)
            listaBinarios = listaBin
            x += 1
        else:
            tablaManual, valoresLongitud = DecodificacionAuto(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x)
    elif paro == "2":
        porsentaje = int(input("Ingrese el porsentaje de convergencia: "))
        convergencia = round((porsentaje * poblacion) / 100)
        print()
        valMax = funcionMatematica(rangoMax)
        x = 1
        while not(len(tabla[tabla["Adaptado f(x)"] >= valMax]) >= convergencia):
            listaBin, tabla = mutacionAuto(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x, tazaCruce, tazaMutacion)
            listaBinarios = listaBin
            x += 1
        else:
            tablaManual, valoresLongitud = DecodificacionAuto(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x)
            print("\nLos mas mejores son:\n")
            print(tablaManual[tablaManual["Adaptado f(x)"] >= valMax])
            mejores = tablaManual[tablaManual["Adaptado f(x)"] >= valMax]
            mejores.to_excel(writer, sheet_name=f"Hoja{x+1}")
            writer.save()

'''COMBINACION 1 B = Ruleta + Cruce de 2 puntos'''
def combi1b(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    listaBinarios, tabla = mutacionPC2(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
    print('''
************************************************************
*    --------------------Tipo de Paro-----------------     *
*                                                          *
*    1) Generaciones                                       *
*    2) Convergencia                                       *
*                                                          *
*                                                          *
************************************************************
''')
    paro = input("Ingrese el tipo de Paro: ")

    if paro == "1":
        gen = int(input("Ingrese el numero de generaciones: "))
        print()
        x = 1
        while (x != gen):
            listaBin, tabla = mutacionPC2Auto(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x)
            listaBinarios = listaBin
            x += 1
        else:
            tablaManual, valoresLongitud = DecodificacionAuto(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x)
    elif paro == "2":
        porsentaje = int(input("Ingrese el porsentaje de convergencia: "))
        convergencia = round((porsentaje * poblacion) / 100)
        print()
        valMax = funcionMatematica(rangoMax)
        x = 1
        while not(len(tabla[tabla["Adaptado f(x)"] >= valMax]) >= convergencia):
            listaBin, tabla = mutacionPC2Auto(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x, tazaCruce, tazaMutacion)
            listaBinarios = listaBin
            x += 1
        else:
            tablaManual, valoresLongitud = DecodificacionAuto(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x)
            print("\nLos mas mejores son:\n")
            print(tablaManual[tablaManual["Adaptado f(x)"] >= valMax])
            mejores = tablaManual[tablaManual["Adaptado f(x)"] >= valMax]
            mejores.to_excel(writer, sheet_name=f"Hoja{x+1}")
            writer.save()

'''COMBINACION 1 C = Ruleta + Cruce Uniforme'''
def combi1c(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    listaBinarios = mutacionUnif(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
    print('''
************************************************************
*    --------------------Tipo de Paro-----------------     *
*                                                          *
*    1) Generaciones                                       *
*    2) Convergencia                                       *
*                                                          *
*                                                          *
************************************************************
''')
    paro = input("Ingrese el tipo de Paro: ")

    if paro == "1":
        gen = int(input("Ingrese el numero de generaciones: "))
        print()
        x = 1
        while (x != gen):
            listaBin, tabla = mutacionUnifAuto(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x, tazaCruce, tazaMutacion)
            listaBinarios = listaBin
            x += 1
        else:
            tablaManual, valoresLongitud = DecodificacionAuto(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x)
    elif paro == "2":
        porsentaje = int(input("Ingrese el porsentaje de convergencia: "))
        convergencia = round((porsentaje * poblacion) / 100)
        print()
        valMax = funcionMatematica(rangoMax)
        x = 1
        while not(len(tabla[tabla["Adaptado f(x)"] >= valMax]) >= convergencia):
            listaBin, tabla = mutacionUnifAuto(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x, tazaCruce, tazaMutacion)
            listaBinarios = listaBin
            x += 1
        else:
            tablaManual, valoresLongitud = DecodificacionAuto(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x)
            print("\nLos mas mejores son:\n")
            print(tablaManual[tablaManual["Adaptado f(x)"] >= valMax])
            mejores = tablaManual[tablaManual["Adaptado f(x)"] >= valMax]
            mejores.to_excel(writer, sheet_name=f"Hoja{x+1}")
            writer.save()


'''------------------------------------Opciones con 2------------------------------------'''

'''COMBINACION 2 A = Jerarquica + Cruce de 1 punto'''
def combi2a(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    listaBinarios = mutacionJerar(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
    print('''
************************************************************
*    --------------------Tipo de Paro-----------------     *
*                                                          *
*    1) Generaciones                                       *
*    2) Convergencia                                       *
*                                                          *
*                                                          *
************************************************************
''')
    paro = input("Ingrese el tipo de Paro: ")

    if paro == "1":
        gen = int(input("Ingrese el numero de generaciones: "))
        print()
        x = 1
        while (x != gen):
            listaBin, tabla= mutacionAutoJerar(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x, tazaCruce, tazaMutacion)
            listaBinarios = listaBin
            x += 1
        else:
            tablaManual, valoresLongitud = DecodificacionAuto(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x)
    elif paro == "2":
        porsentaje = int(input("Ingrese el porsentaje de convergencia: "))
        convergencia = round((porsentaje * poblacion) / 100)
        print()
        valMax = funcionMatematica(rangoMax)
        x = 1
        while not(len(tabla[tabla["Adaptado f(x)"] >= valMax]) >= convergencia):
            listaBin, tabla = mutacionAutoJerar(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x, tazaCruce, tazaMutacion)
            listaBinarios = listaBin
            x += 1
        else:
            tablaManual, valoresLongitud = DecodificacionAuto(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x)
            print("\nLos mas mejores son:\n")
            print(tablaManual[tablaManual["Adaptado f(x)"] >= valMax])
            mejores = tablaManual[tablaManual["Adaptado f(x)"] >= valMax]
            mejores.to_excel(writer, sheet_name=f"Hoja{x+1}")
            writer.save()

'''COMBINACION 2 B = Jerarquica + Cruce de 2 puntos'''
def combi2b(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    listaBinarios, tabla = mutacionPC2Jerar(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
    print('''
************************************************************
*    --------------------Tipo de Paro-----------------     *
*                                                          *
*    1) Generaciones                                       *
*    2) Convergencia                                       *
*                                                          *
*                                                          *
************************************************************
''')
    paro = input("Ingrese el tipo de Paro: ")

    if paro == "1":
        gen = int(input("Ingrese el numero de generaciones: "))
        print()
        x = 1
        while (x != gen):
            listaBin, tabla = mutacionPC2AutoJerar(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x, tazaCruce, tazaMutacion)
            listaBinarios = listaBin
            x += 1
        else:
            tablaManual, valoresLongitud = DecodificacionAuto(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x)
    elif paro == "2":
        porsentaje = int(input("Ingrese el porsentaje de convergencia: "))
        convergencia = round((porsentaje * poblacion) / 100)
        print()
        valMax = funcionMatematica(rangoMax)
        x = 1
        while not(len(tabla[tabla["Adaptado f(x)"] >= valMax]) >= convergencia):
            listaBin, tabla = mutacionPC2AutoJerar(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x, tazaCruce, tazaMutacion)
            listaBinarios = listaBin
            x += 1
        else:
            tablaManual, valoresLongitud = DecodificacionAuto(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x)
            print("\nLos mas mejores son:\n")
            print(tablaManual[tablaManual["Adaptado f(x)"] >= valMax])
            mejores = tablaManual[tablaManual["Adaptado f(x)"] >= valMax]
            mejores.to_excel(writer, sheet_name=f"Hoja{x+1}")
            writer.save()

'''COMBINACION 2 C = Jerarquica + Cruce Uniforme'''
def combi2c(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    listaBinarios, tabla = mutacionUnifJerar(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
    print('''
************************************************************
*    --------------------Tipo de Paro-----------------     *
*                                                          *
*    1) Generaciones                                       *
*    2) Convergencia                                       *
*                                                          *
*                                                          *
************************************************************
''')
    paro = input("Ingrese el tipo de Paro: ")

    if paro == "1":
        gen = int(input("Ingrese el numero de generaciones: "))
        print()
        x = 1
        while (x != gen):
            listaBin, tabla = mutacionUnifAutoJerar(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x, tazaCruce, tazaMutacion)
            listaBinarios = listaBin
            x += 1
        else:
            tablaManual, valoresLongitud = DecodificacionAuto(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x)
    elif paro == "2":
        porsentaje = int(input("Ingrese el porsentaje de convergencia: "))
        convergencia = round((porsentaje * poblacion) / 100)
        print()
        valMax = funcionMatematica(rangoMax)
        x = 1
        while not(len(tabla[tabla["Adaptado f(x)"] >= valMax]) >= convergencia):
            listaBin, tabla = mutacionUnifAutoJerar(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x, tazaCruce, tazaMutacion)
            listaBinarios = listaBin
            x += 1
        else:
            tablaManual, valoresLongitud = DecodificacionAuto(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x)
            print("\nLos mas mejores son:\n")
            print(tablaManual[tablaManual["Adaptado f(x)"] >= valMax])
            mejores = tablaManual[tablaManual["Adaptado f(x)"] >= valMax]
            mejores.to_excel(writer, sheet_name=f"Hoja1")
            writer.save()

