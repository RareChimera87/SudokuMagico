import random
import time

nose = [
[3, 6, 2, 8, 7, 5, 4, 1, 9], 
[4, 9, 6, 1, 3, 8, 2, 7, 5], 
[6, 5, 8, 2, 9, 7, 4, 3, 1], 
[2, 7, 9, 5, 3, 4, 1, 6, 8], 
[2, 1, 9, 5, 4, 7, 6, 8, 3], 
[1, 3, 4, 5, 9, 6, 8, 2, 7], 
[6, 7, 1, 4, 5, 2, 8, 3, 9], 
[6, 3, 4, 7, 8, 9, 5, 2, 1], 
[6, 5, 4, 7, 9, 2, 3, 1, 8]
]


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
        #print("J vale: ", j)
        #print("LenTablero vale: ", len(Tablero))
        currentColumna = generaColumnas(len(Tablero)-1, Tablero, j)
        currentCuadrante = generaCuadrante(Tablero, i, j, 3)
        
        #print("El cuadrante es: ", currentCuadrante)
        #print("Columna actual: ", currentColumna)
        #print("Fila Actual:   ", fila)
        #print("Determinando posicion: ", j+1, " de la lista: ", i+1)
        
        numero = generaNumero(0, 9)
        #print("Numero posible: ", numero)

        if numero in fila or numero in currentColumna or numero in currentCuadrante:
            #print("Numero no valido, ya esta")
            if (numero not in fila and numero in currentColumna and iteracion > 33) or (numero not in fila and numero in currentCuadrante and iteracion > 33):
                #print("Orden no valido\n Reseteando....")
                fila = []
                error = True
                return error
                
        else:
            #print("Numero Valido\n Añadiendo")
            valido = True
            return numero

def validaTablero():
    results = []
    tablero = LlenaTablero()
    fallas = []
    Valido = True
    print("**************Validando Tablero*******************")
    for i in range(len(tablero)):
        fila = tablero[i]
        print("Analizando fila: ", i, ": ", fila)
        for j in range(len(tablero)):
            Estado = True
            posicion = None
            numero = tablero[i][j]
            
            print("Analizando posicion: (", i, ", ", j, "): ", numero)
            currentColumna = generaColumnas(len(tablero), tablero, j)
            print("Analizando columna: ", j, ": ", currentColumna)
            currentCuadrante = generaCuadrante(tablero, i, j, 3)
            print("Cuadrante: ", currentCuadrante)
            if numero in currentCuadrante:
                index = currentCuadrante.index(numero)
                currentCuadrante[index] = 0
            print(currentCuadrante)
            for k in range(len(tablero)):
                if k != j:
                    if numero == fila[k]:
                        posicion = (i, j)
                        if posicion not in fallas:
                            fallas.append(posicion)
                            Estado = False
                            Valido = False
                            print("La posicion: (", i, ", ", j, "): ", numero, " ya se encuentra ")
                            print("+El numero: ", numero, " esta en fila de la posicion: (", i, ", ", k, ") ")
                        else:
                            Estado = False
                            Valido = False
                            print("La posicion: (", i, ", ", j, "): ", numero, " ya se encuentra ")
                            print("+El numero: ", numero, " esta en fila de la posicion: (", i, ", ", k, ") ")
                if k != i:
                    if numero == currentColumna[k]:
                        posicion = (i, j)
                        if posicion not in fallas:
                            fallas.append(posicion)
                            Estado = False
                            Valido = False
                            print("La posicion: (", i, ", ", j, "): ", numero, " ya se encuentra ")
                            print("-El numero: ", numero, " esta en columna de la posicion: (", i, ", ", k, ") ")
                        else:
                            Estado = False
                            Valido = False
                            print("La posicion: (", i, ", ", j, "): ", numero, " ya se encuentra ")
                            print("-El numero: ", numero, " esta en columna de la posicion: (", i, ", ", k, ") ")
                if numero == currentCuadrante[k]:  
                    posicion = (i, j)
                    if posicion not in fallas:
                        fallas.append(posicion)
                        Estado = False
                        Valido = False
                        print("La posicion: (", i, ", ", j, "): ", numero, " ya se encuentra ")
                        print("*El numero: ", numero, " esta en su cuadrante")
                        if 0 in currentCuadrante:
                            index = currentCuadrante.index(0)
                            currentCuadrante[index] = numero
                        print(currentCuadrante)
                    else:
                        Estado = False
                        Valido = False
                        print("La posicion: (", i, ", ", j, "): ", numero, " ya se encuentra ")
                        print("*El numero: ", numero, " esta en su cuadrante")
                        if 0 in currentCuadrante:
                            index = currentCuadrante.index(0)
                            currentCuadrante[index] = numero
                        print(currentCuadrante)

        print("**********************")
        if Estado:
            print("Resultado de la fila: ", i, ": ✅")
            results.append("✅")
        else:
            print("Resultado de la fila: ", i, ": ❌")
            results.append("❌")
        print("**********************")
    print("--------------------------------------")
    print("Resultados globales del tablero: ")
    for i in range(len(tablero)):
        time.sleep(3)
        print("Fila: ", i, ": ", results[i])
        
    if Valido:
        print("Su Tablero es valido, felicidades")
        print("fallas: ", fallas)
    else:
        print("Su tablero es invalido")
        print("Se encontraron errores en las posiciones: ", fallas)
    print("--------------------------------------")



def LlenaTablero():
    TiempoI = time.time()
    Tablero = generaTablero()

    print("Tablero Generado: ", Tablero)

    for i in range(9):

        #print("Generando fila numero: ", i + 1)
        #print("Fila Original: ", Tablero[i])
        
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
                #print("Fila validada erroneamente")
                fila = []
                error = False
                continue
            else:
                #print("Se ve bien la fila")
                validatorNumber = True

        #print("Fila Generada: ", fila)
        Tablero[i] = fila
        #print("Nuevo Tablero: ", Tablero)

    print("\n\n\n------------------------------------------------------------------------")

    for i in range(9):
        print(Tablero[i])
        
    print("\n\n\n------------------------------------------------------------------------")


    print("Generado en: ", time.time()-TiempoI)
    return Tablero
