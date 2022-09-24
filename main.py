import Libreria as lc    #Importamos la librería hecha previamente
import math
import matplotlib.pyplot as plt
from sys import stdin


'''EMPIEZA PROGRAMA SIMULACIÓN DE LO CLÁSICO A LO CUÁNTICO'''


#PRIMER EXPERIMENTO
def canicas(matriz,v_inicial):
    print("Experimentos Probabilistico con Canicas:")

    # MATRIZ DE PRUEBA
    print("Matriz asociada:")
    matriz = [[0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0],
              [0, 1, 0, 0, 0, 1]]

    for i in matriz:
        print(i)
    tics = 2
    X = [x[:] for x in matriz]

    for i in range(2, tics + 1):
        X = lc.multmatrices(X, matriz)  #Se usa la multiplicación de matrices

    print("Estado inicial:")
    v_inicial = [[3], [2], [5], [9], [0], [7]]

    print("Numero de tics:", tics)

    for i in v_inicial:
        print(v_inicial)

    posicion = lc.accionmatrizvector(X, v_inicial)  #Accion de matriz sobre vector

    print("Vector Final:")
    print(posicion)

#SEGUNDO EXPERIMENTO
def exp_2(matriz,v_inicial):
    print("Experimento Probabilistico con multiples rendijas")
    print("Matriz asociada:")
    matriz = [[0, 0, 0, 0, 0, 0, 0, 0],
              [1 / 2, 0, 0, 0, 0, 0, 0, 0],
              [1 / 2, 0, 0, 0, 0, 0, 0, 0],
              [0, 1 / 3, 0, 1, 0, 0, 0, 0],
              [0, 1 / 3, 0, 0, 1, 0, 0, 0],
              [0, 1 / 3, 1 / 3, 0, 0, 1, 0, 0],
              [0, 0, 1 / 3, 0, 0, 0, 1, 0],
              [0, 0, 1 / 3, 0, 0, 0, 0, 1]]

    for i in matriz:
        print(i)

    tics = 2
    X = [x[:] for x in matriz]

    for i in range(2, tics + 1):
        X = lc.multmatrices(X, matriz)

    print("Estado inicial:")
    v_inicial = [[1], [0], [0], [0], [0], [0], [0], [0]]

    print("Numero de tics:", tics)

    for i in v_inicial:
        print(i)
    posicion = lc.accionmatrizvector(X, v_inicial)

    print("Vector Final")
    print(posicion)
    lc.graficas(lc.n_tics(matriz), posicion)

#TERCER EXPERIMENTO
def exp_3(matriz,v_inicial):
    print("Experimento Cuantico con 2 rendijas")
    matriz = [[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
              [(1 / math.sqrt(2), 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
              [(1 / math.sqrt(2), 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
              [(0, 0), (-1 / math.sqrt(6), 1 / math.sqrt(6)), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
              [(0, 0), (-1 / math.sqrt(6), -1 / math.sqrt(6)), (0, 0), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0)],
              [(0, 0), (1 / math.sqrt(6), -1 / math.sqrt(6)), (-1 / math.sqrt(6), 1 / math.sqrt(6)), (0, 0), (0, 0),
               (1, 0), (0, 0), (0, 0)],
              [(0, 0), (0, 0), (-1 / math.sqrt(6), -1 / math.sqrt(6)), (0, 0), (0, 0), (0, 0), (1, 0), (0, 0)],
              [(0, 0), (0, 0), (1 / math.sqrt(6), -1 / math.sqrt(6)), (0, 0), (0, 0), (0, 0), (0, 0), (1, 0)]]
    print("Matriz Asociada: ")

    for i in matriz:
        print(i)
    tics = 3

    X = [x[:] for x in matriz]
    for i in range(2, tics + 1):
        X = lc.productomatricesComplex(X, matriz)
    print("Estado inicial: ")
    v_inicial = [[(1, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)]]

    print("Numero de tics:", tics)
    for i in v_inicial:
        print(i)
    posicion = lc.accmatriz_vectorcplx(X, v_inicial)

    print("Vector Final")
    probabilidades = []
    for i in range(len(posicion)):
        probabilidades += [(lc.modulocplx(posicion[i])) ** 2]
    for i in probabilidades:
        print(i)
    lc.graficas(lc.n_tics(matriz), probabilidades)

#4 Funcion graficas
def graficas(posicion, v):
    plt.bar(posicion, v, facecolor = "lime")
    plt.title("Gráfica de Probabilidades Finales")
    plt.xlabel("Posiciones")
    plt.ylabel("Probabilidad")
    plt.show()
    plt.savefig('Probabilidades.png')

#PRUEBAS

def main():
    matriz_1 = stdin.readline()
    v_inicial = stdin.readline()
    matriz_2 = stdin.readline()
    v_inicial2 = stdin.readline()
    matriz3 = stdin.readline()
    v_inicial3 = stdin.readline()
    canicas(matriz_1, v_inicial)
    exp_2(matriz_2, v_inicial2)
    exp_3(matriz3, v_inicial3)

main()