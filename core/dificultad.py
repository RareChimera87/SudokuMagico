from core.generator import Generator
from core.sudoku import Sudoku

nose = [
    [3, 6, 2, 8, 7, 5, 4, 1, 9], 
    [4, 9, 6, 1, 3, 8, 2, 7, 5], 
    [6, 5, 8, 2, 9, 7, 4, 3, 1], 
    [2, 7, 9, 5, 3, 4, 1, 6, 8], 
    [2, 1, 9, 5, 4, 7, 6, 8, 3], 
    [1, 3, 4, 5, 9, 6, 8, 2, 7], 
    [6, 7, 1, 4, 5, 2, 8, 3, 9], 
    [6, 3, 4, 7, 8, 9, 5, 2, 1], 
    [6, 5, 4, 7, 9, 2, 3, 1, 8]
]

class dificultad:
    def __init__(self):
        self.dificultad = 0
        self.elimnumbers = 0
        self.board = []

    def selelccionarDifucultad(self, nivel):
        while True:
            try:
                dificultad = int(nivel)
                if  1 <=  dificultad <= 5:
                    self.dificultad = dificultad
                    print("Dificultad asignada:", self.dificultad)
                    self.modificaNumsElim()
                    print("Numeros a eliminar: ", self.elimnumbers)
                    break
                else:
                    print("Elija un número dentro del rango 1-5.")
            except:
                print("Escriba un numero")

    def modificaNumsElim(self):
        if self.dificultad == 1:
            self.elimnumbers = 33

        elif self.dificultad == 2:
            self.elimnumbers = 42

        elif self.dificultad == 3:
            self.elimnumbers = 48

        elif self.dificultad == 4:
            self.elimnumbers = 53

        else:
            self.elimnumbers = 58

    def modificaTablero(self, Tablero, nivel):
        generador = Generator()
        self.board = Tablero
        min = 0
        max = len(self.board[min]) - 1
        self.selelccionarDifucultad(nivel)
        modificados = []
        for i in range(self.elimnumbers):
            while True:
                x = generador.generaNumero(min, max)
                y = generador.generaNumero(min, max)
                posicion = (x, y)
                if posicion not in modificados:
                    break
            #print(i)
            #print("Posicion:", posicion)
            #print("Valor: ", self.board[x][y])
            self.board[x][y] = 0
        
        Sudoku().printSudoku(self.board)
        return self.board
            
