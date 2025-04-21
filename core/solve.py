from core.sudoku import Sudoku
from core.validator import Validator
import copy



class solucionador():
    def __init__(self):
        self.sudoku = Sudoku()
        self.validator = Validator()
        self.board = []
        self.newBoard = []

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
            print("Board: ", self.newBoard)
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
                        print("Combinacion Invalida, reseteando fila\nAntigua: ", self.newBoard[i])
                        iteraciones += 1
                    else:
                        print("Fila valida")
                        self.newBoard[i] = copy.deepcopy(filaR)
                        print(self.newBoard[i])
                        valid = True
                    if iteraciones > 70:
                        valid = True
            print("Intento: ", intentos)
            if self.validator.validaTablero(self.newBoard):
                valide = True
                        
                
        #print("Fall: ", fall)
        print("----------------------------------")
        for i in range(len(self.newBoard)):
            print(self.newBoard[i])
        print("----------------------------------")
        return self.newBoard, True



            

