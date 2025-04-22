
from utils.generator import Generator
from utils.validadores import Analiza


class Validator():
    def __init__(self):
        self.board = []
        self.tablero_valido = False
        self.generator = Generator()
        self.analiza = Analiza()
        self.results = []

    @property
    def size(self):
        return len(self.board)

    
    def validaTablero(self, tablero):
        self.board = tablero
        #print("Tablero: ", self.board)
        #print("Tamaño: ", self.size)
        fallas = []
        #Valido = True
        print("**************Validando Tablero*******************")

        self.recorreYvalida(fallas)
        
        print("--------------------------------------")
        print("Resultados globales del tablero: ")
        for i in range(self.size):
            #time.sleep(1)
            print("Fila: ", i, ": ", self.results[i])
            
        if not fallas:
            print("Su Tablero es valido, felicidades")
            print("fallas: ", fallas)
            self.tablero_valido = True
            
        else:
            print("Su tablero es invalido")
            print("Se encontraron errores en las posiciones: ", fallas)
        print("--------------------------------------")
        return self.tablero_valido
    

    def recorreYvalida(self, fallas):
        for i in range(self.size):
            Estado = True
            fila = self.board[i]
            #print("Analizando fila: ", i, ": ", fila)
            for j in range(self.size):
                numero = self.board[i][j]
                
                #print("Analizando posicion: (", i, ", ", j, "): ", numero)
                currentColumna = self.generator.generaColumnas(j, self.board)
                #print("Analizando columna: ", j, ": ", currentColumna)
                currentCuadrante = self.generator.generaCuadrante(i, j, self.board)
                #print("Cuadrante: ", currentCuadrante)
                if numero in currentCuadrante:
                    index = currentCuadrante.index(numero)
                    currentCuadrante[index] = 0
                #print(currentCuadrante)
                for k in range(self.size):
                    if k != j:
                        EstadoF = self.analiza.validaArrayIndividual(numero, fila, k)
                        if Estado == False:
                            #print("False: ", Estado)
                            self.whereFalla(numero, fallas, i, j)
                            print("+El numero: ", numero, " esta en fila de la posicion: (", i, ", ", k, ") ")
                            continue
                        else:
                            Estado = EstadoF
                            #print("Nose: ", Estado)
                    if k != i:
                        EstadoC = self.analiza.validaArrayIndividual(numero, currentColumna, k)
                        if Estado == False:
                            #print("False: ", Estado)
                            self.whereFalla(numero, fallas, i, j)
                            print("-El numero: ", numero, " esta en columna de la posicion: (", i, ", ", k, ") ")
                            continue
                        else:
                            Estado = EstadoC
                            #print("Nose: ", Estado)
                    if True:
                        EstadoCT = self.analiza.validaArrayIndividual(numero, currentCuadrante, k)
                        if Estado == False:
                            #print("False: ", Estado)
                            self.whereFalla(numero, fallas, i, j)
                            print("*El numero: ", numero, " esta en su cuadrante")
                            continue
                        else:
                            Estado = EstadoCT
                            #print("Nose: ", Estado)

            #print("\n**********************")
            if Estado:
                #print("Resultado de la fila: ", i, ": ✅")
                self.results.append("✅")
            else:
                #print("Resultado de la fila: ", i, ": ❌")
                self.results.append("❌")
            #print("\n**********************")
        
        
     

    
    def whereFalla(self, numero, fallas, i, j):
        posicion = (i, j)
        if posicion not in fallas:
            fallas.append(posicion)
        print("La posicion: (", i, ", ", j, "): ", numero, " ya se encuentra ")


        
