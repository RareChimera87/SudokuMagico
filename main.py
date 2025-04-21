from core.generator import Generator
from core.sudoku import Sudoku
from core.validator import Validator
from core.dificultad import dificultad
from core.solve import solucionador

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

class main():

    
    def __init__(self):
        self.generator = Generator()
        self.validator = Validator()
        self.sudoku = Sudoku()
        self.dificultad = dificultad()
        self.solucionador = solucionador()
        self.valido = False
        self.board = []
        self.boardSolve = None
    
    def getSudoku(self):

        Matriz = self.generator.generaTablero()

        self.board = self.sudoku.LlenarTablero(Matriz)
        
        print("Tablero generado: ")
        for i in range(len(self.board)):
            print(self.board[i])


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
            self.board = self.dificultad.modificaTablero(self.board)
            print("Tablero Modificado: ")
            for i in range(len(self.board)):
                print(self.board[i])
            self.Solucionador()
        else:
            print("El tablero no es valido")

    def Solucionador(self):
        print("==================================================================================")
        print("Solo es una prueba")
        if self.valido:
            self.boardSolve, val = self.solucionador.resuelve(tablero_dificil)
            if val:
                print("Tablero solcionado: ", tablero_dificil)
                return self.boardSolve
            else:
                print("El tablero no se pudo resolver")


        else:
            print("El tablero es invalido no se puede resolver")




if __name__ == "__main__":
    app = main()
    app.getSudoku()