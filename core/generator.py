import random

""" list = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], 
[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], 
[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
 """
list = [
[3, 6, 2, 8, 7, 5, 4, 1, 9], 
[4, 9, 6, 1, 3, 8, 2, 7, 5], 
[6, 5, 8, 2, 9, 7, 4, 3, 1], 
[2, 7, 9, 5, 3, 4, 1, 6, 8], 
[2, 1, 9, 5, 4, 7, 6, 8, 3], 
[1, 3, 4, 5, 9, 6, 8, 2, 7], 
[6, 7, 1, 4, 5, 2, 8, 3, 9], 
[6, 3, 4, 7, 8, 9, 5, 2, 1], 
[6, 5, 4, 7, 9, 2, 3, 1, 8]
]
 
tablero = [[random.randint(1, 9) for _ in range(9)] for _ in range(9)]
print("Su tablero es: ", tablero)


def verificaTablero(lista):
    
    for i in range(len(lista)):
        currentLista = lista[i]
        NumbersTryed = []

        print("------Lista en la que esta trabajando: ", currentLista, "-----------")
        for j in range(len(currentLista)):
            print("Lista Actual: ", currentLista)
            NumeroValido = False
            currentNumber = currentLista[j]
            

            print("Su Numero actual es: ", currentNumber)
            while NumeroValido != True:
                currentColumna = []
                esUnico = True

                for l in range(len(currentLista)):
                    currentColumna.append(lista[l][j])


                print("Fila actual: ", currentLista)
                print("Columna Actual: ", currentColumna)

                for k in range(len(currentLista)):
                    
                    if k == j:
                        continue
                    elif currentNumber in NumbersTryed:
                        print("El numero: ", currentNumber, " ya se ha validado")
                        esUnico = False
                        break
                    elif currentNumber == currentLista[k] or currentNumber == 0:
                        print("El numero: ", currentNumber," ya se encuentra en la fila")
                        esUnico = False
                        break
                    """ elif currentNumber in currentColumna:
                        print("El numero: ", currentNumber," ya se encuentra en la columna")
                        esUnico = False
                        break """
                        



                if esUnico:
                    print("Lista anterior: ", currentLista)
                    print("Reemplazando: ", currentLista[j], " por: ", currentNumber)
                    NumbersTryed.append(currentNumber)

                    currentLista[j] = currentNumber
                    print("Lista modificada: ", currentLista)
                    NumeroValido = True


                else:
                    print("El numero: ", currentNumber, "No es valido")
                    currentNumber += 1
                    print("Nuevo numero: ", currentNumber)
                    if currentNumber > 9:
                        currentNumber = 1
                        print("Numero fuera de rango\n Nuevo numero: ", currentNumber)
            print("Su lista modificada es: ",currentLista)
    print("Su nuevo tablero es: ", lista)
    return lista 



def verificaColumnas(lista):
    print("Lista ingresada: ", lista)
    Matriz = []

    for j in range(len(lista)):
        currentLista = []
        for k in range(len(lista)):
            currentLista.append(lista[k][j])
        print("Nose: ", currentLista)
        Matriz.append(currentLista)

    print("Lista que mando: ", Matriz)
    
    listinha = verificaFilas(Matriz)
    
    print("Lista que devuelven: ", listinha)

    """  for j in range(len(lista)):
        currentLista = []
        for k in range(len(lista)):
            lista[k][j] = listinha[k][j]
            currentLista.append(lista[k][j])
        print("Nose: ", currentLista) """

    algo = 0

    while algo < 82:
        for i in range(len(listinha)):
            for j in range(len(listinha)):
                currentNumber = listinha[j][i]
                currentFila = lista[j]
                if currentNumber not in currentFila:
                    lista[k][i] = currentNumber
                    algo += 1
                else:
                    verificaFilas(listinha, currentNumber)
        print("Ya no se: ", lista)
        


    print("Lista final espero: ", lista)

    





#verificaColumnas(list)

                    

verificaTablero(tablero)