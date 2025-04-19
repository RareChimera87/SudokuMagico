import random
import time

#Recuerda lo de probar reemplazar el len por self.size


class Sudoku:
    def __init__(self):
        self.size = 9
        self.cuadrante_size = 3
        self.board = self.generaTablero()

    def generaTablero(self):
        return [[0 for _ in range(self.size)] for _ in range(self.size)]
    
    def generaColumnas(self, posicion):
        Columna = []
        for i in range(len(self.board)):
            Columna.append(self.board[i][posicion])
        return Columna
    
    def generaCuadrante(self, fila, columna):
        Cuadrante = []
        if (fila >= 0 and fila <= 2):
            if  (columna >= 0 and columna <= 2):
                for i in range(self.cuadrante_size):
                    for j in range(self.cuadrante_size):
                        Cuadrante.append(self.board[i][j])
            elif (columna >= 3 and columna <= 5):
                for i in range(self.cuadrante_size):
                    for j in range(self.cuadrante_size):
                        Cuadrante.append(self.board[i][j+3])
            else:
                for i in range(self.cuadrante_size):
                    for j in range(self.cuadrante_size):
                        Cuadrante.append(self.board[i][j+6])
        elif (fila >= 3 and fila <= 5):
            if  (columna >= 0 and columna <= 2):
                for i in range(self.cuadrante_size):
                    for j in range(self.cuadrante_size):
                        Cuadrante.append(self.board[i+3][j])
            elif (columna >= 3 and columna <= 5):
                for i in range(self.cuadrante_size):
                    for j in range(self.cuadrante_size):
                        Cuadrante.append(self.board[i+3][j+3])
            else:
                for i in range(self.cuadrante_size):
                    for j in range(self.cuadrante_size):
                        Cuadrante.append(self.board[i+3][j+6])
        else:
            if  (columna >= 0 and columna <= 2):
                for i in range(self.cuadrante_size):
                    for j in range(self.cuadrante_size):
                        Cuadrante.append(self.board[i+6][j])
            elif (columna >= 3 and columna <= 5):
                for i in range(self.cuadrante_size):
                    for j in range(self.cuadrante_size):
                        Cuadrante.append(self.board[i+6][j+3])
            else:
                for i in range(self.cuadrante_size):
                    for j in range(self.cuadrante_size):
                        Cuadrante.append(self.board[i+6][j+6])
        return Cuadrante

    def generaNumero(self, min, max):
        numero = random.randint(min, max)
        return numero
    
    def validaNumero(self, i, j, fila):
        valido = False
        iteracion = 0
        while valido != True:
            iteracion += 1
            #print("J vale: ", j)
            #print("LenTablero vale: ", len(Tablero))
            currentColumna = self.generaColumnas(j)
            currentCuadrante = self.generaCuadrante(i, j, )
            
            #print("El cuadrante es: ", currentCuadrante)
            #print("Columna actual: ", currentColumna)
            #print("Fila Actual:   ", fila)
            #print("Determinando posicion: ", j+1, " de la lista: ", i+1)
            
            numero = self.generaNumero(1, 9)
            #print("Numero posible: ", numero)

            if numero in fila or numero in currentColumna or numero in currentCuadrante:
                #print("Numero no valido, ya esta")
                if (numero not in fila and numero in currentColumna and iteracion > 33) or (numero not in fila and numero in currentCuadrante and iteracion > 33):
                    #print("Orden no valido\n Reseteando....")
                    fila = []
                    return None
                    
            else:
                #print("Numero Valido\n Añadiendo")
                valido = True
                return numero

    def LlenarTablero(self):
        TiempoI = time.time()
        
        print("Tablero Generado: ", self.board)

        for i in range(9):
            print("Generando fila numero: ", i + 1)
            print("Fila Original: ", self.board[i])
            
            validatorNumber = False
                

            while validatorNumber != True:
                fila = []
                error = False
                for j in range(9):
                    numero = self.validaNumero(i, j, fila)
                    if type(numero) == bool:
                        fila = []
                        error = True
                        break
                    else:
                        fila.append(numero)
                        continue
                if numero is None:
                    #print("Fila validada erroneamente")
                    fila = []
                    error = False
                    continue
                else:
                    #print("Se ve bien la fila")
                    validatorNumber = True
            print("Fila Generada: ", fila)
            self.board[i] = fila
            print("Nuevo Tablero: ", self.board)

        print("\n\n\n------------------------------------------------------------------------")
        for i in range(9):
            print(self.board[i])
        print("\n\n\n------------------------------------------------------------------------")

        print("Generado en: ", time.time()-TiempoI)
        return self.board
    
    def validaTablero(self,):
        results = []
        fallas = []
        Valido = True
        print("**************Validando Tablero*******************")
        for i in range(len(self.board)):
            fila = self.board[i]
            print("Analizando fila: ", i, ": ", fila)
            for j in range(len(self.board)):
                Estado = True
                posicion = None
                numero = self.board[i][j]
                
                print("Analizando posicion: (", i, ", ", j, "): ", numero)
                currentColumna = self.generaColumnas(j)
                print("Analizando columna: ", j, ": ", currentColumna)
                currentCuadrante = self.generaCuadrante(self.board, i, j, 3)
                print("Cuadrante: ", currentCuadrante)
                if numero in currentCuadrante:
                    index = currentCuadrante.index(numero)
                    currentCuadrante[index] = 0
                print(currentCuadrante)
                for k in range(len(self.board)):
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
        for i in range(len(self.board)):
            time.sleep(3)
            print("Fila: ", i, ": ", results[i])
            
        if Valido:
            print("Su Tablero es valido, felicidades")
            print("fallas: ", fallas)
        else:
            print("Su tablero es invalido")
            print("Se encontraron errores en las posiciones: ", fallas)
        print("--------------------------------------")
