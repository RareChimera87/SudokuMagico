from utils.generator import Generator

class Llenador:
    def __init__(self):
        self.generator = Generator()

    def LlenaNumero(self, i, j, fila, tablero, size):
        
        valido = False
        iteracion = 0
        while valido != True:
            iteracion += 1
            #print("J vale: ", j)
            #print("LenTablero vale: ", len(Tablero))
            currentColumna = self.generator.generaColumnas(j, tablero)
            currentCuadrante = self.generator.generaCuadrante(i, j, tablero)
            
            #print("El cuadrante es: ", currentCuadrante)
            #print("Columna actual: ", currentColumna)
            #print("Fila Actual:   ", fila)
            #print("Determinando posicion: ", j+1, " de la lista: ", i+1)
            
            numero = self.generator.generaNumero(1, size)
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