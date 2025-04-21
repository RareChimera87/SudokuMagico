
from core.generator import Generator
from core.sudoku import Sudoku

al = [[7, 3, 1, 4, 8, 6, 2, 5, 9], [9, 6, 2, 1, 7, 5, 4, 8, 3], [5, 8, 4, 9, 3, 2, 6, 7, 1], [6, 4, 5, 8, 1, 9, 3, 2, 7], [2, 7, 9, 5, 4, 3, 1, 6, 8], [8, 1, 3, 6, 2, 7, 9, 4, 5], [3, 5, 8, 2, 9, 4, 7, 1, 6], [1, 2, 7, 3, 6, 8, 5, 9, 4], [4, 9, 6, 7, 5, 1, 8, 3, 2]]

class Validator():
    def __init__(self):
        self.board = []
        self.tablero_valido = False
        self.generator = Generator()

    @property
    def size(self):
        return len(self.board)

    
    def validaTablero(self, tablero):
        self.board = tablero
        #print("Tablero: ", self.board)
        #print("Tamaño: ", self.size)
        results = []
        fallas = []
        Valido = True
        print("**************Validando Tablero*******************")
        for i in range(self.size):
            Estado = True
            fila = self.board[i]
            #print("Analizando fila: ", i, ": ", fila)
            for j in range(self.size):
                numero = self.board[i][j]
                
                #print("Analizando posicion: (", i, ", ", j, "): ", numero)
                currentColumna = self.generator.generaColumnas(j, self.board)
                #print("Analizando columna: ", j, ": ", currentColumna)
                currentCuadrante = self.generator.generaCuadrante(i, j, self.board)
                #print("Cuadrante: ", currentCuadrante)
                if numero in currentCuadrante:
                    index = currentCuadrante.index(numero)
                    currentCuadrante[index] = 0
                #print(currentCuadrante)
                for k in range(self.size):
                    if k != j:
                        EstadoF = self.validaFila(numero, fila, fallas, i, j ,k)
                        if Estado == False:
                            #print("False: ", Estado)
                            continue
                        else:
                            Estado = EstadoF
                            #print("Nose: ", Estado)
                    if k != i:
                        EstadoC = self.validaColumna(numero, currentColumna, fallas, i, j ,k)
                        if Estado == False:
                            #print("False: ", Estado)
                            continue
                        else:
                            Estado = EstadoC
                            #print("Nose: ", Estado)
                    if True:
                        EstadoCT = self.validaCuadrante(numero, currentCuadrante, fallas, i, j ,k)
                        if Estado == False:
                            #print("False: ", Estado)
                            continue
                        else:
                            Estado = EstadoCT
                            #print("Nose: ", Estado)

            #print("\n**********************")
            if Estado:
                #print("Resultado de la fila: ", i, ": ✅")
                results.append("✅")
            else:
                #print("Resultado de la fila: ", i, ": ❌")
                results.append("❌")
            #print("\n**********************")
        print("--------------------------------------")
        print("Resultados globales del tablero: ")
        for i in range(self.size):
            #time.sleep(1)
            print("Fila: ", i, ": ", results[i])
            
        if not fallas:
            print("Su Tablero es valido, felicidades")
            print("fallas: ", fallas)
            self.tablero_valido = True
            
        else:
            print("Su tablero es invalido")
            print("Se encontraron errores en las posiciones: ", fallas)
        print("--------------------------------------")
        return self.tablero_valido

    def validaFila(self, numero, fila, fallas, i, j ,k):
        if numero == fila[k]:
            posicion = (i, j)
            if posicion not in fallas:
                fallas.append(posicion)

                print("La posicion: (", i, ", ", j, "): ", numero, " ya se encuentra ")
                print("+El numero: ", numero, " esta en fila de la posicion: (", i, ", ", k, ") ")
                return False
            else:

                print("La posicion: (", i, ", ", j, "): ", numero, " ya se encuentra ")
                print("+El numero: ", numero, " esta en fila de la posicion: (", i, ", ", k, ") ")
                return False
        else:
            return True
        
    def validaColumna(self, numero, currentColumna, fallas, i, j, k):
        if numero == currentColumna[k]:
            posicion = (i, j)
            if posicion not in fallas:
                fallas.append(posicion)

                print("La posicion: (", i, ", ", j, "): ", numero, " ya se encuentra ")
                print("-El numero: ", numero, " esta en columna de la posicion: (", i, ", ", k, ") ")
                return False
            else:

                print("La posicion: (", i, ", ", j, "): ", numero, " ya se encuentra ")
                print("-El numero: ", numero, " esta en columna de la posicion: (", i, ", ", k, ") ")
                return False
        else:
            return True
    def validaCuadrante(self, numero, currentCuadrante, fallas,i, j, k):
        if numero == currentCuadrante[k]:  
            posicion = (i, j)
            if posicion not in fallas:
                fallas.append(posicion)

                print("La posicion: (", i, ", ", j, "): ", numero, " ya se encuentra ")
                print("*El numero: ", numero, " esta en su cuadrante")
                if 0 in currentCuadrante:
                    index = currentCuadrante.index(0)
                    currentCuadrante[index] = numero
                print(currentCuadrante)
                return False
            else:

                print("La posicion: (", i, ", ", j, "): ", numero, " ya se encuentra ")
                print("*El numero: ", numero, " esta en su cuadrante")
                if 0 in currentCuadrante:
                    index = currentCuadrante.index(0)
                    currentCuadrante[index] = numero
                print(currentCuadrante)
                return False
        else:
            return True
        
