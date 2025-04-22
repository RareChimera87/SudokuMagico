import time

from utils.generator import Generator
from utils.llena import Llenador
from utils.showthing import Impresor


class Sudoku:
    def __init__(self,):
        self.size = 9
        self.cuadrante_size = 3
        self.board = []
        self.generator = Generator()
        self.llenador = Llenador()
        self.imprime = Impresor()

    

    def LlenarTablero(self, tableroVacio):
        self.board = tableroVacio
        TiempoI = time.time()
        
        self.imprime.printSudoku(self.board)

        for i in range(self.size):
            #print("Generando fila numero: ", i + 1)
            #print("Fila Original: ", self.board[i])
            
            validatorNumber = False
                

            while validatorNumber != True:
                fila = []
                error = False
                for j in range(9):
                    numero = self.llenador.LlenaNumero(i, j, fila, self.board, self.size)
                    #print("numero: ", numero)
                    if numero is None:
                        fila = []
                        error = True
                        break
                    else:
                        fila.append(numero)
                        continue
                if error:
                    #print("Fila validada erroneamente")
                    fila = []
                    error = False
                    continue
                else:
                    #print("Se ve bien la fila")
                    validatorNumber = True
            #print("Fila Generada: ", fila)
            self.board[i] = fila
            #print("Nuevo Tablero: ", self.board)

        print("Finalizado")
        self.imprime.printSudoku(self.board)
        print("Generado en: ", time.time()-TiempoI)
        return self.board
    
         



