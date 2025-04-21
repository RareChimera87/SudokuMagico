from core.generator import Generator
from core.sudoku import Sudoku
from core.validator import Validator
from core.dificultad import dificultad
from core.solve import solucionador

from gui.pdfGen import Pdf
from gui.gui import Gui

tablero_dificil = [
    [0, 0, 0, 0, 0, 0, 9, 0, 7],
    [0, 0, 0, 4, 2, 0, 1, 0, 0],
    [0, 0, 2, 0, 0, 9, 0, 4, 0],
    [0, 0, 0, 2, 0, 4, 7, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 6, 0],
    [0, 0, 6, 1, 0, 7, 0, 0, 0],
    [0, 3, 0, 6, 0, 0, 2, 0, 0],
    [0, 0, 1, 0, 9, 2, 0, 0, 0],
    [2, 0, 9, 0, 0, 0, 0, 0, 0]
]

tablero_dificil2 = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]

tablero_ultra_dificil = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]

class main():

    
    def __init__(self):
        self.generator = Generator()
        self.validator = Validator()
        self.sudoku = Sudoku()
        self.dificultad = dificultad()
        self.nivel = 1
        self.solucionador = solucionador()
        self.pdfGen = Pdf()
        self.gui = Gui(self.Interfaz)
        self.valido = False
        self.board = []
        self.boardSolve = None
        self.resolver = False
        self.fileName = ""
        self.fileNameSolve = ""

    
    def getSudoku(self):

        Matriz = self.generator.generaTablero()

        self.board = self.sudoku.LlenarTablero(Matriz)
        


        print("es valido el tablero?")
        self.valido = self.validator.validaTablero(self.board )

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
        self.getSudoku()
        if resolver:
            self.Solucionador()



if __name__ == "__main__":
    main()


"""     respuesta = int(input("Quiere una archivo con la respuesta?\n1.Si\n2.No\nSu respuesta: "))
    if respuesta == 1:
        app.Solucionador() """