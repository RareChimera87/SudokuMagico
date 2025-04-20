import random


class Generator():
    def __init__(self):
        self.size = 9
        self.cuadrante_size = 3


    def generaTablero(self):
        return [[0 for _ in range(self.size)] for _ in range(self.size)]
    
    def generaColumnas(self, posicion, Tablero):
        Columna = []
        for i in range(self.size):
            Columna.append(Tablero[i][posicion])
        return Columna
    
    def generaCuadrante(self, fila, columna, Tablero):
        Cuadrante = []
        if (fila >= 0 and fila <= 2):
            if  (columna >= 0 and columna <= 2):
                for i in range(self.cuadrante_size):
                    for j in range(self.cuadrante_size):
                        Cuadrante.append(Tablero[i][j])
            elif (columna >= 3 and columna <= 5):
                for i in range(self.cuadrante_size):
                    for j in range(self.cuadrante_size):
                        Cuadrante.append(Tablero[i][j+3])
            else:
                for i in range(self.cuadrante_size):
                    for j in range(self.cuadrante_size):
                        Cuadrante.append(Tablero[i][j+6])
        elif (fila >= 3 and fila <= 5):
            if  (columna >= 0 and columna <= 2):
                for i in range(self.cuadrante_size):
                    for j in range(self.cuadrante_size):
                        Cuadrante.append(Tablero[i+3][j])
            elif (columna >= 3 and columna <= 5):
                for i in range(self.cuadrante_size):
                    for j in range(self.cuadrante_size):
                        Cuadrante.append(Tablero[i+3][j+3])
            else:
                for i in range(self.cuadrante_size):
                    for j in range(self.cuadrante_size):
                        Cuadrante.append(Tablero[i+3][j+6])
        else:
            if  (columna >= 0 and columna <= 2):
                for i in range(self.cuadrante_size):
                    for j in range(self.cuadrante_size):
                        Cuadrante.append(Tablero[i+6][j])
            elif (columna >= 3 and columna <= 5):
                for i in range(self.cuadrante_size):
                    for j in range(self.cuadrante_size):
                        Cuadrante.append(Tablero[i+6][j+3])
            else:
                for i in range(self.cuadrante_size):
                    for j in range(self.cuadrante_size):
                        Cuadrante.append(Tablero[i+6][j+6])
        return Cuadrante

    def generaNumero(self, min, max):
        numero = random.randint(min, max)
        return numero
