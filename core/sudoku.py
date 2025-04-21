import time
""" 
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
] """


class Sudoku:
    def __init__(self,):
        self.size = 9
        self.cuadrante_size = 3
        self.board = []

    

    def LlenarTablero(self, tableroVacio,generaColumnas, generaCuadrante, generaNumero):
        self.board = tableroVacio
        TiempoI = time.time()
        
        print("Tablero Generado: ", self.board)

        for i in range(self.size):
            print("Generando fila numero: ", i + 1)
            #print("Fila Original: ", self.board[i])
            
            validatorNumber = False
                

            while validatorNumber != True:
                fila = []
                error = False
                for j in range(9):
                    numero = self.LlenaNumero(i, j, fila, self.board, generaColumnas, generaCuadrante, generaNumero)
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

        print("Finalizado\nTablero generado: ")
        print("\n\n\n------------------------------------------------------------------------")
        for i in range(9):
            print(self.board[i])
        print("\n\n\n------------------------------------------------------------------------")

        print("Generado en: ", time.time()-TiempoI)
        return self.board
    
    def LlenaNumero(self, i, j, fila, tablero, generaColumnas, generaCuadrante, generaNumero):
        
        valido = False
        iteracion = 0
        while valido != True:
            iteracion += 1
            #print("J vale: ", j)
            #print("LenTablero vale: ", len(Tablero))
            currentColumna = generaColumnas(j, tablero)
            currentCuadrante = generaCuadrante(i, j, tablero)
            
            print("El cuadrante es: ", currentCuadrante)
            print("Columna actual: ", currentColumna)
            print("Fila Actual:   ", fila)
            #print("Determinando posicion: ", j+1, " de la lista: ", i+1)
            
            numero = generaNumero(1, 9)
            #print("Numero posible: ", numero)

            if numero in fila or numero in currentColumna or numero in currentCuadrante:
                #print("Numero no valido, ya esta")
                if (numero not in fila and numero in currentColumna and iteracion > 33) or (numero not in fila and numero in currentCuadrante and iteracion > 33):
                    #print("Orden no valido\n Reseteando....")
                    fila = []
                    return None
                    
            else:
                #print("Numero Valido\n Añadiendo")
                valido = True
                return numero

    




