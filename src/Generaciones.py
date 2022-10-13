from Modulos.mutaciones.Mutacion import mutacion, mutacionAuto, mutacionJerar, mutacionAutoJerar
from Modulos.opBasicas.Decodificacion import DecodificacionAuto
from Modulos.mutaciones.MutacionPC2 import mutacionPC2, mutacionPC2Auto, mutacionPC2Jerar, mutacionPC2AutoJerar
from Modulos.mutaciones.MutacionUniforme import mutacionUnif, mutacionUnifAuto, mutacionUnifJerar, mutacionUnifAutoJerar

'''Opciones con 1'''
def combi1a(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion):
    listaBinarios = mutacion(poblacion, longitud, rangoMin, rangoMax, tazaCruce, tazaMutacion)
    gen = int(input("Ingrese el numero de generaciones: "))
    print()
    x = 1
    while (x != gen):
        listaBin = mutacionAuto(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x, tazaCruce, tazaMutacion)
        listaBinarios = listaBin
        x += 1
    else:
        tablaManual, valoresLongitud = DecodificacionAuto(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x, tazaCruce, tazaMutacion)

def combi1b(poblacion, longitud, rangoMin, rangoMax):
    listaBinarios = mutacionPC2(poblacion, longitud, rangoMin, rangoMax)
    gen = int(input("Ingrese el numero de generaciones: "))
    print()
    x = 1
    while (x != gen):
        listaBin = mutacionPC2Auto(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x)
        listaBinarios = listaBin
        x += 1
    else:
        tablaManual, valoresLongitud = DecodificacionAuto(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x)

def combi1c(poblacion, longitud, rangoMin, rangoMax):
    listaBinarios = mutacionUnif(poblacion, longitud, rangoMin, rangoMax)
    gen = int(input("Ingrese el numero de generaciones: "))
    print()
    x = 1
    while (x != gen):
        listaBin = mutacionUnifAuto(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x)
        listaBinarios = listaBin
        x += 1
    else:
        tablaManual, valoresLongitud = DecodificacionAuto(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x)

'''Opciones con 2'''
def combi2a(poblacion, longitud, rangoMin, rangoMax):
    listaBinarios = mutacionJerar(poblacion, longitud, rangoMin, rangoMax)
    gen = int(input("Ingrese el numero de generaciones: "))
    print()
    x = 1
    while (x != gen):
        listaBin = mutacionAutoJerar(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x)
        listaBinarios = listaBin
        x += 1
    else:
        tablaManual, valoresLongitud = DecodificacionAuto(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x)

def combi2b(poblacion, longitud, rangoMin, rangoMax):
    listaBinarios = mutacionPC2Jerar(poblacion, longitud, rangoMin, rangoMax)
    gen = int(input("Ingrese el numero de generaciones: "))
    print()
    x = 1
    while (x != gen):
        listaBin = mutacionPC2AutoJerar(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x)
        listaBinarios = listaBin
        x += 1
    else:
        tablaManual, valoresLongitud = DecodificacionAuto(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x)

def combi2c(poblacion, longitud, rangoMin, rangoMax):
    listaBinarios = mutacionUnifJerar(poblacion, longitud, rangoMin, rangoMax)
    gen = int(input("Ingrese el numero de generaciones: "))
    print()
    x = 1
    while (x != gen):
        listaBin = mutacionUnifAutoJerar(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x)
        listaBinarios = listaBin
        x += 1
    else:
        tablaManual, valoresLongitud = DecodificacionAuto(listaBinarios, poblacion, longitud, rangoMin, rangoMax, x)
