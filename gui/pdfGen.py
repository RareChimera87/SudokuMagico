from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from utils.validadores import Analiza

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

class Pdf:
    def __init__(self):
        self.valida = Analiza()
        self.extension = '.pdf'
        self.canvas = canvas.Canvas('Sudoku.pdf')
        self.caracteresProhibidos = r'\/:*?"<>|'

    def Iniciador(self, tablero, nombre):
        while True:
            try:
                if not self.valida.validaNombre(nombre, self.caracteresProhibidos):
                    raise ValueError("Nombre inválido")
                break
            except:
                print("Escriba un nombre valido")
        nombre = nombre + self.extension
        self.canvas = canvas.Canvas(nombre)
        self.SudokuBoardGen(tablero)
        self.canvas.showPage()
        self.canvas.save()



    def SudokuBoardGen(self, numeros):
        width, height = letter  
        self.canvas.setFont("Helvetica", 20)
        
        x = 215
        y = 759 

        self.canvas.drawString(x, y, "Sudoku Generator")

        cell_size = 40
        tablero_size = cell_size * 9
        x_start = ((width - tablero_size) / 2) -10
        y_start = 700


        xlist = [x_start + i * cell_size for i in range(10)]
        ylist = [y_start - i * cell_size for i in range(10)]

        self.canvas.grid(xlist, ylist)

        self.canvas.setLineWidth(3)
        
        for i in range(0, 10, 3):  # cada 3 filas
            y = y_start - i * cell_size
            self.canvas.line(x_start, y, x_start + 9 * cell_size, y)

        for i in range(0, 10, 3):  # cada 3 columnas
            x = x_start + i * cell_size
            self.canvas.line(x, y_start, x, y_start - 9 * cell_size)

        xNumero = x_start+15
        yNumero = y_start-27
        for i in range(len(numeros)):
            for j in range(len(numeros[i])):
                if numeros[i][j] == 0:
                    self.canvas.drawString(xNumero, yNumero, "")
                    xNumero += cell_size
                else:
                    self.canvas.drawString(xNumero, yNumero, str(numeros[i][j]))
                    xNumero += cell_size
            xNumero = x_start+15
            yNumero -= cell_size

