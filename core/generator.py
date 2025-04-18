import random
import time
 
nose = [[6, 4, 1, 2, 7, 8, 9, 3, 5], [9, 8, 2, 5, 4, 6, 7, 1, 3], [4, 5, 7, 3, 8, 2, 1, 6, 9], [8, 9, 5, 6, 3, 4, 2, 7, 1], [7, 1, 9, 4, 6, 5, 3, 2, 8], [1, 7, 4, 8, 2, 3, 5, 9, 6], [3, 6, 8, 7, 1, 9, 4, 5, 2], [2, 3, 6, 9, 5, 1, 8, 4, 7], [5, 2, 3, 1, 9, 7, 6, 8, 4]]


def generaTablero():
    tablero = [[0 for _ in range(9)] for _ in range(9)]
    return tablero

def generaColumnas(longitud, matriz, posicion):
    Columna = []
    for i in range(longitud):
        Columna.append(matriz[i][posicion])
    return Columna

def generaCuadrante(matriz, fila, columna):
    Cuadrante = []
    if (fila >= 0 and fila <= 2):
        if  (columna >= 0 and columna <= 2):
            for i in range(3):
                for j in range(3):
                    Cuadrante.append(matriz[i][j])
        elif (columna >= 3 and columna <= 5):
            for i in range(3):
                for j in range(3):
                    Cuadrante.append(matriz[i][j+3])
        else:
            for i in range(3):
                for j in range(3):
                    Cuadrante.append(matriz[i][j+6])
    elif (fila >= 3 and fila <= 5):
        if  (columna >= 0 and columna <= 2):
            for i in range(3):
                for j in range(3):
                    Cuadrante.append(matriz[i+3][j])
        elif (columna >= 3 and columna <= 5):
            for i in range(3):
                for j in range(3):
                    Cuadrante.append(matriz[i+3][j+3])
        else:
            for i in range(3):
                for j in range(3):
                    Cuadrante.append(matriz[i+3][j+6])
    else:
        if  (columna >= 0 and columna <= 2):
            for i in range(3):
                for j in range(3):
                    Cuadrante.append(matriz[i+6][j])
        elif (columna >= 3 and columna <= 5):
            for i in range(3):
                for j in range(3):
                    Cuadrante.append(matriz[i+6][j+3])
        else:
            for i in range(3):
                for j in range(3):
                    Cuadrante.append(matriz[i+6][j+6])
    return Cuadrante

def generaNumero(min, max):
    numero = random.randint(min, max)

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
            for j in range(9):
                valido = False
                iteracion = 0
                while valido != True:
                    iteracion += 1
                    print("J vale: ", j)
                    print("LenTablero vale: ", len(Tablero))
                    currentColumna = generaColumnas(len(Tablero)-1, Tablero, j)
                    currentCuadrante = generaCuadrante(Tablero, i, j)
                    
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
                            fila = Tablero[i]
                            break
                    else:
                        print("Numero Valido\n Añadiendo")
                        valido = True
                        fila.append(numero)
                        continue
            if 0 in fila:
                print("Fila validada erroneamente")
                fila = []
                continue
            else:
                print("Se ve bien la fila")
                validatorNumber = True

        print("Fila Generada: ", fila)
        Tablero[i] = fila
        print("Nuevo Tablero: ", Tablero)
        print("Generado en: ", time.time()-TiempoI)
        #time.sleep(5)




LlenaTablero()
