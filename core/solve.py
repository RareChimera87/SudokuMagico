from core.sudoku import Sudoku
from core.validator import Validator
from core.generator import Generator
import copy
import time



class solucionador():
    def __init__(self):
        self.sudoku = Sudoku()
        self.validator = Validator()
        self.generator = Generator()
        self.board = []
        self.newBoard = []


    def gestionador(self, tablero):
        
        while True:
            try:
                #respuesta = int(input("Elija un metodo para resolver el sudoku:\n1.Aleatoriedad\n2.Bactracking\nRespuesta: "))
                respuesta = 2
                if  respuesta == 1:
                    print("Eligio Aleatoriedad")
                    ini = time.time()
                    self.resuelve(tablero)
                    print("Realizado en: ", time.time() - ini)
                    self.sudoku.printSudoku(self.newBoard)
                    return self.newBoard, True
                elif respuesta == 2:
                    print("Eligio Backtracking")
                    ini = time.time()
                    if(self.backtracking(tablero)):
                        print("Resuelto en: ", time.time() - ini)
                        self.sudoku.printSudoku(self.board)
                        return self.board, True
                    else:
                        print("Se ejecuto por: ", time.time() - ini)
                        print("No se pudo resolver")
                        return self.board, False
                else:
                    print("Elija una opcion valida.")
            except:
                print("Escriba un numero")

    def resuelve(self, tablero):
    
        self.board = tablero
        self.newBoard = copy.deepcopy(self.board)
        valide = False
        fall = []
        intentos = 0
        maxIntentos = 100

        while not valide and intentos <= maxIntentos:
            intentos += 1
            
            self.newBoard = copy.deepcopy(self.board)
            #print("Board: ", self.newBoard)
            for i in range(len(self.newBoard)):
                valid = False
                iteraciones = 0
                filaR = []
                while not valid:
                    filaR = copy.deepcopy(self.newBoard[i])
                    #print("Trabajando con: ", filaR)
                    errores = False
                    for j in range(len(filaR)):
                        posicion = (i, j)
                        if self.newBoard[i][j] == 0:
                            #print("newBoard: ", self.newBoard)
                            numero = self.sudoku.LlenaNumero(i, j, filaR, self.newBoard)
                            if numero:
                                #print("El numero para la posicion: ",posicion, " es: ", numero)
                                filaR[j] = numero
                            else: 
                                #print("Error en la posicion: ", posicion)
                                fall.append(posicion)
                                errores = True
                                valid = False
                    if errores:
                        valid = False
                        #print("Combinacion Invalida, reseteando fila\nAntigua: ", self.newBoard[i])
                        iteraciones += 1
                    else:
                        #print("Fila valida")
                        self.newBoard[i] = copy.deepcopy(filaR)
                        #print(self.newBoard[i])
                        valid = True
                    if iteraciones > 70:
                        valid = True
            print("Intento: ", intentos)
            if self.validator.validaTablero(self.newBoard):
                valide = True
                        
                
        #print("Fall: ", fall)
        return self.newBoard, True

    def backtracking(self, tablero):
        self.board = tablero
        posiciones = [0, 0]

        if not self.find_empty(tablero, posiciones):
            print("Fin Back")
            return True
            

        fila = posiciones[0]
        columna = posiciones[1]

        currentColumna = self.generator.generaColumnas(columna, self.board)
        currentCuadrante = self.generator.generaCuadrante(fila, columna, self.board)

        for n in range(1, 10):
            if (self.validaFila(n, self.board[fila]) and self.validaColumna(n, currentColumna) and self.validaCuadrante(n, currentCuadrante)):

                self.board[fila][columna] = n

                if(self.backtracking(self.board)):
                    return True
            
                self.board[fila][columna] = 0


        return False


    def find_empty(self, tablero, posiciones):
        for i in range(9):
            for j in range(9):
                if tablero[i][j] == 0:
                    posiciones[0] = i
                    posiciones[1] = j
                    return True

    def validaFila(self, numero, fila):
        if numero in fila:
            return False
        else:
            return True
    
    def validaColumna(self, numero, columna):
        if numero in columna:
            return False
        else:
            return True

    def validaCuadrante(self, numero, cuadrante):
        if numero in cuadrante:
            return False
        else:
            return True

