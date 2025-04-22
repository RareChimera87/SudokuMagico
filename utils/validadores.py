

class Analiza:
    def __init__(self):
        pass

    def validaArrayIndividual(self, numero, array, posicion):
        if numero == array[posicion]:    
            return False
        else:
            return True
        
    def validaNumeroEnArray(self, numero, array):
        if numero in array:
            return False
        else:
            return True
    
    def find_empty(self, tablero, posiciones):
        for i in range(9):
            for j in range(9):
                if tablero[i][j] == 0:
                    posiciones[0] = i
                    posiciones[1] = j
                    return True
    
    def validaNombre(self, nombre, caracteresProhibidos):
        if not nombre.strip() or any(c in nombre for c in caracteresProhibidos):
            return False
        return True