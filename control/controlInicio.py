from core.generator import Generator
from core.sudoku import Sudoku
from core.validator import Validator
from core.dificultad import dificultad
from core.solve import solucionador
from control.sudokuLevel import GenYAssingSud

from gui.pdfGen import Pdf
from gui.gui import Gui


class Control:
    def __init__(self):
        self.validator = Validator()
        self.dificultad = dificultad()
        self.nivel = 1
        self.solucionador = solucionador()
        self.sudl = GenYAssingSud()
        self.pdfGen = Pdf()
        self.gui = Gui(self.Interfaz)
        self.valido = False
        self.board = []
        self.boardSolve = None
        self.resolver = False
        self.fileName = ""
        self.fileNameSolve = ""

                
    def Solucionador(self):
        if self.valido:
            self.boardSolve, val = self.solucionador.gestionador(self.board)
            if val:
                #print("Tablero solcionado: ", self.boardSolve)
                print("Vamos a verificarlo...")
                self.validator.validaTablero(self.boardSolve)
                self.pdfGen.Iniciador(self.boardSolve, self.fileNameSolve)
                return self.boardSolve
            else:
                print("El tablero no se pudo resolver")

        else:
            print("El tablero es invalido no se puede resolver")

    def Interfaz(self, nombre, nombreSol, resolver, dificultad):
        self.resolver = resolver
        self.fileName = nombre
        self.fileNameSolve = nombreSol
        self.nivel = dificultad
        self.board, self.valido = self.sudl.getSudoku(self.nivel, self.fileName)
        if resolver:
            self.Solucionador()

