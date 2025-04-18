import random
import time

""" list = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], 
[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], 
[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
 """
list = [
[3, 6, 2, 8, 7, 5, 4, 1, 9], 
[3, 9, 6, 1, 3, 8, 2, 7, 5], 
[6, 5, 8, 2, 9, 7, 4, 3, 1], 
[2, 7, 9, 5, 3, 4, 1, 6, 8], 
[2, 1, 9, 5, 4, 7, 6, 8, 3], 
[1, 3, 4, 5, 9, 6, 8, 2, 7], 
[6, 7, 1, 4, 5, 2, 8, 3, 9], 
[6, 3, 4, 7, 8, 9, 5, 2, 1], 
[6, 5, 4, 7, 9, 2, 3, 1, 8]
]
 
tablero = [[random.randint(1, 9) for _ in range(9)] for _ in range(9)]
""" print("Su tablero es: ", tablero) """


def generaTablero():
    tablero = [[0 for _ in range(9)] for _ in range(9)]
    return tablero
    

def LlenaTablero():

    Tablero = generaTablero()

    print("Tablero Generado: ", Tablero)

    for i in range(9):

        digitos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        print("Generando fila numero: ", i + 1)
        print("Fila Original: ", Tablero[i])
        
        validatorNumber = False
            

        while validatorNumber != True:
            fila = []
            NumeroIntentados = []
            for j in range(9):
                valido = False
                NumeroIntentados = []
                iteracion = 0
                while valido != True:
                    iteracion += 1
                    currentColumna = []
                    for l in range(len(Tablero)):
                        currentColumna.append(Tablero[l][j])
                    print("Columna actual: ", currentColumna)
                    print("Fila Actual:   ", fila)
                    print("Determinando posicion: ", j+1, " de la lista: ", i+1)
                    
                    numero = random.randint(1, 9)
                    
                    if numero not in NumeroIntentados:
                        NumeroIntentados.append(numero)
                    print("Numero posible: ", numero)
        
                    if numero in fila or numero in currentColumna:
                        print("Numero no valido, ya esta")
                        if numero not in fila and numero in currentColumna and iteracion > 30:
                            print("Orden no valido\n Reseteando....")
                            fila = Tablero[i]
                            break
                    else:
                        print("Numero Valido\n Añadiendo")
                        valido = True
                        fila.append(numero)
                        continue
            if 0 in fila:
                print("Fila validada erroneamente")
                continue
            else:
                print("Se ve bien la fila")
                validatorNumber = True

        print("Fila Generada: ", fila)
        Tablero[i] = fila
        print("Nuevo Tablero: ", Tablero)
        #time.sleep(5)




def verificaTablero(lista):
    
    for i in range(len(lista)):
        currentLista = lista[i]

        print("------Lista en la que esta trabajando: ", currentLista, "-----------")
        
        for j in range(len(currentLista)):
            print("Lista Actual: ", currentLista)
            NumeroValido = False
            currentNumber = currentLista[j]
            iteraciones = 0
            

            print("Su Numero actual es: ", currentNumber)
            time.sleep(5)
            print("Lista orignal: ", tablero)
            print("Lista por el momento: ", lista)
            time.sleep(15)
            while NumeroValido != True:
                print("*********Analizando lista: ", j+1, "*****")
                iteraciones += 1
                IsColumna = False
                currentColumna = []
                esUnico = True




                for l in range(len(currentLista)):
                    currentColumna.append(lista[l][j])


                print("Fila actual: ", currentLista)
                print("Columna Actual: ", currentColumna)

                for k in range(len(currentLista)):
                    
                    if k == j:
                                continue
                    elif currentNumber == currentLista[k] or currentNumber == currentColumna[k]:
                        if currentNumber == currentColumna[k] and currentNumber != currentLista[k]:
                            IsColumna = True
                            break
                        print("El numero: ", currentNumber," ya se encuentra en la fila y/o columna")
                        esUnico = False
                        break
                        



                if esUnico:
                    if IsColumna:
                        numero = random.randint(0, 8)
                        while numero == j:
                            numero = random.randint(0, 8)
                        print("Numero: ", numero)
                        print("El numero: ", currentNumber," ya se encuentra en la columna")
                        print("Modificando posicion. \n Lista Anterior: ", currentLista)
                        currentLista.insert(numero, currentLista.pop(j))
                        print("Lista Nueva: ", currentLista)
                        currentNumber = currentLista[j]
                        print("Analizando ahora: ", currentNumber)
                    else:
                        print("Lista anterior: ", currentLista)
                        print("Reemplazando: ", currentLista[j], " por: ", currentNumber)
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
    
    listinha = verificaColumnas(Matriz)
    
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
                    verificaColumnas(listinha, currentNumber)
        print("Ya no se: ", lista)
        


    print("Lista final espero: ", lista)

    





#verificaColumnas(list)

                    

#verificaTablero(tablero)

LlenaTablero()