from core.generator import Generator
from core.sudoku import Sudoku
from core.validator import Validator


class main():

    
    def __init__(self):
        self.generator = Generator()
        self.validator = Validator()
        self.sudoku = Sudoku()
        

    def getSudoku(self):

        Matriz = self.generator.generaTablero()

        Tablero = self.sudoku.LlenarTablero(Matriz, self.generator.generaColumnas, self.generator.generaCuadrante, self.generator.generaNumero)


        print("es valido el tablero?")
        isValid = self.validator.validaTablero(Tablero ,self.generator.generaColumnas, self.generator.generaCuadrante)

        if isValid:
            print("Tablero Valido")
        else:
            print("Tablero Invalido")

        return Tablero, isValid


if __name__ == "__main__":
    app = main()
    app.getSudoku()