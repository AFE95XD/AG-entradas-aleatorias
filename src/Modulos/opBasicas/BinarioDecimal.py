import random

def binarioDecimal(poblacion, longitud):
    print()
    binStri = ""
    listaBinarios = []
    listaDecimales = []

    for x in range(int(poblacion)):
        for y in range(int(longitud)):
            numero = str(random.randint(0, 1))
            binStri += numero 

        listaBinarios.append(binStri)
        
        numero_decimal = int(binStri, 2)
        listaDecimales.append(numero_decimal)

        print(f'El número en decimal de {binStri} es {numero_decimal}')
        binStri = ""
    return listaDecimales, longitud, listaBinarios


def binarioDecimalAuto(listaBin, poblacion, longitud):
    listaStr = []
    listaDecimales = []
    listaBinarios = []
    i = 1
    while i <= int(poblacion):
        if len(listaBin[i-1]) == longitud:
            listaStr.append(listaBin[i-1])

            listaBinarios.append(listaBin[i-1])

            numero_decimal = int(listaStr[i-1], 2)
            listaDecimales.append(numero_decimal)
            print(
                f'El número en decimal de {listaStr[i-1]} es {numero_decimal}')
            i += 1
        else:
            print("Debe ser de longitud", int(longitud), "intentalo de nuevo")
    return listaDecimales, longitud, listaBinarios
