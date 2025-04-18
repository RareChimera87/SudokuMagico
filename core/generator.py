import random
import time

def generaTablero():
    tablero = [[0 for _ in range(9)] for _ in range(9)]
    return tablero

def generaColumnas(longitud, matriz, posicion):
    Columna = []
    for i in range(longitud):
        Columna.append(matriz[i][posicion])
    return Columna

def generaCuadrante(matriz, fila, columna, size):
    Cuadrante = []
    if (fila >= 0 and fila <= 2):
        if  (columna >= 0 and columna <= 2):
            for i in range(size):
                for j in range(size):
                    Cuadrante.append(matriz[i][j])
        elif (columna >= 3 and columna <= 5):
            for i in range(size):
                for j in range(size):
                    Cuadrante.append(matriz[i][j+3])
        else:
            for i in range(size):
                for j in range(size):
                    Cuadrante.append(matriz[i][j+6])
    elif (fila >= 3 and fila <= 5):
        if  (columna >= 0 and columna <= 2):
            for i in range(size):
                for j in range(size):
                    Cuadrante.append(matriz[i+3][j])
        elif (columna >= 3 and columna <= 5):
            for i in range(size):
                for j in range(size):
                    Cuadrante.append(matriz[i+3][j+3])
        else:
            for i in range(size):
                for j in range(size):
                    Cuadrante.append(matriz[i+3][j+6])
    else:
        if  (columna >= 0 and columna <= 2):
            for i in range(size):
                for j in range(size):
                    Cuadrante.append(matriz[i+6][j])
        elif (columna >= 3 and columna <= 5):
            for i in range(size):
                for j in range(size):
                    Cuadrante.append(matriz[i+6][j+3])
        else:
            for i in range(size):
                for j in range(size):
                    Cuadrante.append(matriz[i+6][j+6])
    return Cuadrante

def generaNumero(min, max):
    numero = random.randint(min, max)
    return numero

def validaNumero(Tablero, i, j, fila):
    valido = False
    iteracion = 0
    while valido != True:
        iteracion += 1
        print("J vale: ", j)
        print("LenTablero vale: ", len(Tablero))
        currentColumna = generaColumnas(len(Tablero)-1, Tablero, j)
        currentCuadrante = generaCuadrante(Tablero, i, j, 3)
        
        print("El cuadrante es: ", currentCuadrante)
        print("Columna actual: ", currentColumna)
        print("Fila Actual:   ", fila)
        print("Determinando posicion: ", j+1, " de la lista: ", i+1)
        
        numero = generaNumero(0, 9)
        print("Numero posible: ", numero)

        if numero in fila or numero in currentColumna or numero in currentCuadrante:
            print("Numero no valido, ya esta")
            if (numero not in fila and numero in currentColumna and iteracion > 33) or (numero not in fila and numero in currentCuadrante and iteracion > 33):
                print("Orden no valido\n Reseteando....")
                fila = []
                error = True
                return error
                
        else:
            print("Numero Valido\n Añadiendo")
            valido = True
            return numero

def validaTablero():
    tablero = LlenaTablero()
    print("**************Validando Tablero*******************")
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            numero = tablero[i][j]
            fila = tablero[i]
            currentColumna = generaColumnas(len(tablero), tablero, j)
            currentCuadrante = generaCuadrante(tablero, fila, )
            if numero in fila or numero in currentColumna or numero in currentCuadrante:
                    print("Numero no valido, ya esta")
                    if (numero not in fila and numero in currentColumna and iteracion > 33) or (numero not in fila and numero in currentCuadrante and iteracion > 33):
                        print("Orden no valido\n Reseteando....")
                        fila = []
                        error = True
                        return error
                        
            else:
                print("Numero Valido\n Añadiendo")
                valido = True
                return numero


def LlenaTablero():
    TiempoI = time.time()
    Tablero = generaTablero()

    print("Tablero Generado: ", Tablero)

    for i in range(9):

        print("Generando fila numero: ", i + 1)
        print("Fila Original: ", Tablero[i])
        
        validatorNumber = False
            

        while validatorNumber != True:
            fila = []
            error = False
            for j in range(9):
                numero = validaNumero(Tablero, i,j, fila)
                if type(numero) == bool:
                    fila = []
                    error = True
                    break
                else:
                    fila.append(numero)
                    continue
                
            if error:
                print("Fila validada erroneamente")
                fila = []
                error = False
                continue
            else:
                print("Se ve bien la fila")
                validatorNumber = True

        print("Fila Generada: ", fila)
        Tablero[i] = fila
        print("Nuevo Tablero: ", Tablero)

    print("\n\n\n------------------------------------------------------------------------")

    for i in range(9):
        print(Tablero[i])
        
    print("\n\n\n------------------------------------------------------------------------")


    print("Generado en: ", time.time()-TiempoI)
    return Tablero


