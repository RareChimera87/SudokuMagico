import random
import time

class Sudoku:
    def __init__(self):
        self.size = 9
        self.cuadrante_size = 3
        self.board = self.generaTablero()

    def generaTablero(self):
        return [[0 for _ in range(self.size)] for _ in range(self.size)]
    
    def printTablero(self):
        for i, fila in enumerate(self.board):
            print(fila)

if __name__ == "__main__":
    sudoku = Sudoku()
    sudoku.printTablero()