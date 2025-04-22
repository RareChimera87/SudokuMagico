from utils.generator import Generator
from core.sudoku import Sudoku
from core.validator import Validator
from core.dificultad import dificultad
from gui.pdfGen import Pdf


class GenYAssingSud():
    def __init__(self):
        self.board = []
        self.valido = False
        self.generator = Generator()
        self.sudoku = Sudoku()
        self.validator = Validator()
        self.dificultad = dificultad()
        self.pdfGen = Pdf()
        self.fileName = ""
        self.nivel = 1

    def getSudoku(self, nivel, fileName):
        self.fileName = fileName
        self.nivel = nivel

        Matriz = self.generator.generaTablero()

        self.board = self.sudoku.LlenarTablero(Matriz)
        


        print("es valido el tablero?")
        self.valido = self.validator.validaTablero(self.board)

        if self.valido:
            print("Tablero Valido")
            self.AsignarDificultad()
            
        else:
            print("Tablero Invalido")

        return self.board, self.valido
    
    def AsignarDificultad(self):
        if self.valido:
            print("Asignando dificultad...")
            self.board = self.dificultad.modificaTablero(self.board, self.nivel)
            self.pdfGen.Iniciador(self.board, self.fileName)
            print()
            print()

        else:
            print("El tablero no es valido")

