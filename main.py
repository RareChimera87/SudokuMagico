from core.generator import Generator
from core.sudoku import Sudoku
from core.validator import Validator
from core.dificultad import dificultad


class main():

    
    def __init__(self):
        self.generator = Generator()
        self.validator = Validator()
        self.sudoku = Sudoku()
        self.dificultad = dificultad()
        self.valido = False
        self.board = []
        

    def getSudoku(self):

        Matriz = self.generator.generaTablero()

        self.board = self.sudoku.LlenarTablero(Matriz, self.generator.generaColumnas, self.generator.generaCuadrante, self.generator.generaNumero)


        print("es valido el tablero?")
        self.valido = self.validator.validaTablero(self.board ,self.generator.generaColumnas, self.generator.generaCuadrante)

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
        else:
            print("El tablero no es valido")


if __name__ == "__main__":
    app = main()
    app.getSudoku()