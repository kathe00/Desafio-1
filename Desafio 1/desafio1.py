# Uso de algoritmos DFS y BF (Best-First) para resolver Sudoku
# Grupo: Los Michis
# Integrantes: Carlos Núñez, Priscilla Riffo, Esteban Gonzáles y Katherine Sepúlveda

from re import T
from numpy.matrixlib.defmatrix import matrix
import numpy as np
from queue import PriorityQueue
from copy import deepcopy
from itertools import count

# estado: matriz de 9x9 y variable que se utilizará como marca para saber si el estado ya fue visitado o no
class State:
  def __init__(self, matrix, visited):
    self.matrix = matrix
    self.visited = visited

# se obtiene una instancia de sudoku a partir de un archivo txt y se crea un estado inicial
f = open('sudokus/s03b.txt', 'r') # CAMBIAR AQUÍ ARCHIVO

# se inicializa estado inicial
initial_state = State([], False)

# se lee línea por línea
for line in f:
    # se obtiene un arreglo de carácteres correspondientes a los dígitos
    numbers = line.split()

    # se convierte el arreglo de carácteres a un arreglo de enteros y se llena en la matriz del estado inicial
    map_of_numbers = map(int, numbers)
    array_of_numbers = list(map_of_numbers)
    initial_state.matrix.append(array_of_numbers)

# se cierra el archivo luego de leerlo completamente
f.close()

# acción: poner un número en la próxima casilla vacía
class Action:
  def __init__(self, i, j, number):
    self.i = i
    self.j = j
    self.number = number

# comprobar si el estado fue visitado o no
def visited(state):
    return state.visited

# marcar el estado indicando que se visitó
def visit(state):
    state.visited = True

# transición
def transition(state, action):
  state.matrix[action.i][action.j] = action.number

# estado final
def is_final_state(state):
    for i in range(9):
        for j in range(9):
            if state.matrix[i][j] == 0: return False
    return True

# revisar si el número candidato es único en la fila
def check_col(state, row, col, number):
    for i in range(9):
        if (i == row): continue
        if state.matrix[i][col] == number:
            return False
    return True

# revisar si el número candidato es único en la fila
def check_row(state, row, col, number):
    for j in range(9):
        if (j == col): continue
        if state.matrix[row][j] == number:
            return False
    return True

# orden sudoku
# [1][2][3]
# [4][5][6]
# [7][8][9]

# revisar si el número candidato es el único en el cuadrado de 3x3 correspondiente
def check_square(state, row, col, number):
    if(row>=0 and row<=2):
        if(col>=0  and col <=2):
            #Cuadrante 1
            for i in range(0,3):
                for j in range(0,3):
                    if (i != row) and (j != col):
                        if state.matrix[i][j] == number:
                            return False

        elif(col>=3 and col<=5):
            #Cuadrante 2
            for i in range(0,3):
                for j in range(3,6):
                    if (i != row) and (j != col):
                        if state.matrix[i][j] == number:
                            return False
                    
        elif(col>=6 and col <=8):
            #Cuadrante 3
            for i in range(0,3):
                for j in range(6,9):
                    if (i != row) and (j != col):
                        if state.matrix[i][j] == number:
                            return False
                    
    elif(row>=3 and row<=5):
        if(col>=0  and col <=2):
            #Cuadrante 4
            for i in range(3,6):
                for j in range(0,3):
                    if (i != row) and (j != col):
                        if state.matrix[i][j] == number:
                            return False
                    
        elif(col>=3 and col<=5):
            #Cuadrante 5
            for i in range(3,6):
                for j in range(3,6):
                    if (i != row) and (j != col):
                        if state.matrix[i][j] == number:
                            return False
                    
        elif(col>=6 and col <=8):
            #Cuadrante 6
            for i in range(3,6):
                for j in range(6,9):
                    if (i != row) and (j != col):
                        if state.matrix[i][j] == number:
                            return False
                    
    elif(row>=6 and row<=8):
        if(col>=0  and col <=2):
            #Cuadrante 7
            for i in range(6,9):
                for j in range(0,3):
                    if (i != row) and (j != col):
                        if state.matrix[i][j] == number:
                            return False
                    
        elif(col>=3 and col<=5):
            #Cuadrante 8
            for i in range(6,9):
                for j in range(3,6):
                    if (i != row) and (j != col):
                        if state.matrix[i][j] == number:
                            return False
                    
        elif(col>=6 and col <=8):
            #Cuadrante 9
            for i in range(6,9):
                for j in range(6,9):
                    if (i != row) and (j != col):
                        if state.matrix[i][j] == number:
                            return False
    return True
                    

# revisar si el número candidato es válido (en su fila, columna y cuadrado)
def number_is_valid(state, row, col, number):
    if check_row(state, row, col, number) and check_col(state, row, col, number) and check_square(state, row, col, number):
        return True
    return False

#busca la coordenada con más restricciones
def find_best_point(state):
    min = -1
    for i in range(9):
        for j in range(9):
            if state.matrix[i][j] == 0:#recorre el sudoku buscando espacios en blanco
                cant_restrictions = 0
                for x in range(1,10): #desde 1 al 9
                    if ((check_row(state, i, j, x) == False) or (check_col(state, i, j, x) == False) or (check_square(state, i, j, x) == False)): #si hay al menos una restriccion
                        cant_restrictions += 1
                if (min < cant_restrictions):
                    fila = i
                    columna = j
                    min = cant_restrictions
    return fila,columna

def get_valid_actions(state):
    valid_actions = [] #arreglo de posibles acciones
    i, j = find_best_point(state)#retorna la coordenada (i,j) donde hay más restricciones
    for number in range(1,10):  
        if number_is_valid(state, i, j, number):
            valid_actions.append(Action(i, j, number))
    return valid_actions

# comprobar si el estado es valido
def is_valid(state):
    for i in range(9):
        for j in range(9):
            if state.matrix[i][j] != 0:
                if 1 <= state.matrix[i][j] <= 9:
                    if not(check_row(state, i, j, state.matrix[i][j]) and check_col(state, i, j, state.matrix[i][j]) and check_square(state, i, j, state.matrix[i][j])):
                        return False
                else: return False
    return True

# Se imprime la matriz 
def print_matrix(state):
    for i in range(9):
        print("| " + str(state.matrix[i][0]) +" "+ str(state.matrix[i][1]) +" "+ str(state.matrix[i][2]) + " | "+ str(state.matrix[i][3]) +" "+ str(state.matrix[i][4]) +" "+ str(state.matrix[i][5]) + " | "  + str(state.matrix[i][6]) +" "+ str(state.matrix[i][7]) +" "+ str(state.matrix[i][8]) + " |")
        if (i == 2) or (i ==5): print("-------------------------")

# busqueda en profundidad
def dfs(initial_state):
    #inicializamos la pila con el estado inicial
    iters = 0
    stack = [deepcopy(initial_state)]
    while len(stack)>0:
        iters += 1 # se cuentan las iteraciones

        state = stack.pop() #tomamos el ultimo elemento de la pila

        if visited(state): continue #si ya se visito, se descarta
        # si no se visito, se visita (se marca)
        visit(state)

        # verificamos que sea un estado valido, si no, se descarta
        if is_valid(state) == False: continue 

        # si es final, es solución
        if is_final_state(state): return iters, state

        # si aún no se encuentra solución, se toman todas las acciones posibles de ese estado
        actions = get_valid_actions(state)
        # y se prueban
        for action in actions:
            new_state = deepcopy(state)
            new_state.visited = False
            transition(new_state, action)
            stack.append(new_state) #agrega al final de la pila

#función heurística
def heuristic_eval(state): #se cuenta y se retorna la cantidad de restricciones de un estado
    cant_restrictions = 0
    for i in range(9):
        for j in range(9):
            if state.matrix[i][j] == 0:#recorre el sudoku buscando espacios en blanco
                for x in range(1,10): #desde 1 al 9
                    if ((check_row(state, i, j, x) == False) or (check_col(state, i, j, x) == False) or (check_square(state, i, j, x) == False)): #si hay al menos una restriccion
                        cant_restrictions += 1
    return cant_restrictions

#best first con heuristica de restricciones
def best_first(initial_state, heuristic_eval):
    unique = count()    
    #se inicializa la cola con prioridad con el estado inicial
    q = PriorityQueue()
    q.put( (-1,0, deepcopy(initial_state)) )
    iters = 0
    while not q.empty():
        iters += 1
        elem = q.get()
        state = elem[2] #retorna y elimina el primer elemento

        if is_final_state(state): return iters, state 

        actions = get_valid_actions(state)

        for action in actions:
            new_state = deepcopy(state) #ojo que debemos copiar el estado antes de modificarlo!
            transition(new_state, action)
            q.put((heuristic_eval(new_state), next(unique), new_state)) #agrega al la cola

# solución con el algoritmo dfs
iters, st_dfs = dfs(initial_state)
# Comprobamos que se haya encontrado un estado
if(st_dfs):
    print("Estado final encontrado con DFS.")
    print("Iteraciones: ", iters)
    print_matrix(st_dfs)
else:
    print("No se encontró ninguna solución.")

print("\n")

# solución con el algoritmo bfs
iters, st_bf = best_first(initial_state, heuristic_eval)
if(st_bf):
    print("Estado final encontrado con BF.")
    print("Iteraciones: ", iters)
    print_matrix(st_bf)
else:
    print("No se encontró ninguna solución.")