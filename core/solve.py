from core.sudoku import Sudoku
from core.generator import Generator
from core.validator import Validator

nose2= [
[3, 6, 2, 8, 7, 5, 4, 1, 0], 
[4, 9, 6, 1, 3, 8, 2, 7, 5], 
[6, 5, 8, 0, 9, 7, 4, 3, 1], 
[2, 7, 9, 5, 3, 4, 1, 6, 8], 
[0, 1, 9, 5, 4, 0, 6, 8, 0], 
[1, 3, 4, 5, 9, 6, 8, 2, 7], 
[6, 7, 1, 4, 5, 2, 8, 3, 9], 
[6, 3, 4, 7, 8, 9, 5, 2, 1], 
[6, 0, 4, 7, 9, 2, 3, 1, 0]
]


class solucionador():
    def __init__(self, Tablero):
        self.sudoku = Sudoku()
        self.generator = Generator()
        self.validator = Validator()
        self.board = Tablero
        self.newBoard = []
        self.NumberVoid = 0
        self.timesSeen = 0

    def resuelve(self):
        self.newBoard = self.board
        for i in range(len(self.newBoard)):
            fila = []
            fila.append(self.newBoard[i])
            for j in range(len(fila)):
                while True:
                    if fila[j] == 0:
                        numero = self.sudoku.LlenaNumero(i, j, fila, self.newBoard, self.generator.generaColumnas, self.generator.generaCuadrante, self.generator.generaNumero)
                        validFila = self.validator.validaFila(numero, fila)
                        validColumna = self.validator.validaColumna
                        validCuadrante = self.validator.validaCuadrante
            




solv = solucionador(nose2)
solv.resuelve()