# lista = ['101011010', '101010100', '010110101',
#          '001101010', '011011010', '101010001', '011011101']


# def binarioDecimal(listaBin, poblacion, longitud):

#     listaStr = []
#     listaDecimales = []
#     listaBinarios = []
#     i = 1
#     while i <= int(poblacion):
#         if len(listaBin[i-1]) == longitud:
#             listaStr.append(listaBin[i-1])

#             listaBinarios.append(listaBin[i-1])

#             numero_decimal = int(listaStr[i-1], 2)
#             listaDecimales.append(numero_decimal)
#             print(
#                 f'El número en decimal de {listaStr[i-1]} es {numero_decimal}')
#             i += 1
#         else:
#             print("Debe ser de longitud", int(longitud), "intentalo de nuevo")
#     return listaDecimales, longitud, listaBinarios


# listaDecimales, longitud, listaBinarios = binarioDecimal(lista, 7, 9)

# print(listaDecimales)
# print(longitud)
# print(listaBinarios)

padre1 = "010010101101"
padre2 = "001010111010"
print('P1',padre1)
print('P2',padre2)
pcMax = 8
pcMin = 1

if pcMin != 1:
    print('entro al diferente')
    hijo1 = padre1[:-pcMax]
    hijo2 = padre2[:-pcMax]
    corteP1 = padre1[-pcMax:-(pcMin-1)]
    corteP2 = padre2[-pcMax:-(pcMin-1)]
    res1 = padre1[-(pcMin-1):]
    res2 = padre2[-(pcMin-1):]

    hijo1 = hijo1 + corteP2 + res1
    hijo2 = hijo2 + corteP1 + res2
else:
    hijo1 = padre1[:-pcMax]
    hijo2 = padre2[:-pcMax]
    corteP1 = padre1[-pcMax:]
    corteP2 = padre2[-pcMax:]

    hijo1 = hijo1 + corteP2
    hijo2 = hijo2 + corteP1

print(hijo1)
print(hijo2)
# corteP3 = padre2[-pcMax:]
# print(corteP3)

# from Modulos.selecOrdenamiento.Jerarquia import jer
# from Modulos.selecOrdenamiento.Ruleta import tablaOrdenadaManual
# jer()
# tablaOrdenadaManual(poblacion=13, longitud=9, rangoMin=1, rangoMax=9)

# from Modulos.selecOrdenamiento.Torneo import torneo

# from Modulos.selecOrdenamiento.Torneo import torneo

# torneo(13, 9, 1, 9)

# from Modulos.opBasicas.BinarioDecimal import binarioDecimal, binarioDecimalAuto

# lita=[1101111111001, 1010101010000, 1010100100111, 100100101001, 1000010011010, 1110111011011, 100111000, 110101111111, 1010100110001, 101110110000]
# listaDecimales, longitud, listaBinarios = binarioDecimalAuto(lita, 10, 13)
# print(listaDecimales, longitud, listaBinarios)

# print(listaBinarios[0])
# print(type(listaBinarios[0]))

# 010111010  186
# 100101001  297
# 001010101  85
# 000111001  57
# 110010101  405
# 110101010  426
# 000110110  54
# 000110101  53
# 011010101  213
# 101100001  353
# 001010101  85
# 001100010  98
# 001111001  121


# '''ELITISTA'''
# import pandas as pd
# from Modulos.opBasicas.Decodificacion import DecodificacionManuales
# from Modulos.selecOrdenamiento.Ruleta import elitistaRuleta

# tablaManual, _, = DecodificacionManuales(10,9,1,6)
# tablaOrd = tablaManual.sort_values("Adaptado f(x)", ascending=False, ignore_index=True)
# # print("\n",tablaOrd)
# mejor = pd.DataFrame()
# fila = pd.Series(tablaOrd.iloc[0].to_dict())
# mejor = pd.concat([mejor, fila.to_frame().T], ignore_index=True)
# mejor.index = [1]
# print("\nEl individuo con mayor adaptacion es:\n")
# print(mejor)
# tablaNueva = tablaOrd.drop(index=0)
# print("\nLos individuos restantes son:\n")
# print(tablaNueva)
# tablaOrdenada, valoresLongitud = elitistaRuleta(tablaNueva)
# print(type(tablaOrdenada))

