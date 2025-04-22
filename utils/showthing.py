
class Impresor:
    def printSudoku(self, tablero):
        print("\n\n\n------------------------------------------------------------------------")
        print("Tablero generado: ")
        for i in range(len(tablero)):
            print(tablero[i])
        print("\n\n\n------------------------------------------------------------------------")

