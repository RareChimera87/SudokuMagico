import random

""" list = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], 
[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], 
[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
 """
tablero = [[random.randint(0, 9) for _ in range(9)] for _ in range(9)]
print("Su tablero es: ", tablero)


def verificaTablero(lista):
    
    
    
    for i in range(len(lista)):
        listaValida = []
        currentLista = lista[i]
        print("Lista en la que esta trabajando: ", currentLista)
        for j in range(len(currentLista)):
            NumeroValido = False
            currentNumber = currentLista[j]
            print("Su Numero actual es: ", currentNumber)
            while NumeroValido != True:
                l = 0
                for k in range(len(currentLista)):
                    if k == j:
                        l = l + 1
                        continue
                    if currentNumber != currentLista[k]:
                        if l == (len(currentLista) - 1):
                            listaValida.append(currentNumber)
                            print("Lista modificada: ", listaValida)
                            NumeroValido = True
                            break
                        l = l + 1
                        continue
                    else:
                        currentNumber = currentNumber + 1
                        l = 0
                        if currentNumber > 9:
                            currentNumber = 0
            print("Su lista modificada es: ",listaValida)
                    

        

                    

verificaTablero(tablero)