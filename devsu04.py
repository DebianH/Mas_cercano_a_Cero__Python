#Sumar 4 matrices
'''
Esta pregunta trataba de un terreno donde las hojas de un arbol las movia el viento esto equivale a
cada matriz y teneniamos que hacer una funcion que sume el numero de hojas.
'''

a = [[0,0,0,0],
     [0,0,2,0],
     [3,0,0,2],
     [0,4,4,0]]

b = [[0,0,0,0],
     [0,0,0,0],
     [8,0,0,2],
     [2,0,1,0]]

c = [[0,3,0,0],
     [0,0,0,0],
     [3,0,0,2],
     [0,2,7,0]]

d = [[0,0,0,0],
     [0,0,0,0],
     [2,0,1,2],
     [1,5,2,0]]

def sumaMatrices(m1,m2,m3,m4):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]): #comprobamos si las matrices son del mismo tamano

        m5 = []
        #creamos una matriz con las mismas dimenciones de m1
        for i in range(len(m1)):
            m5.append([])
            for j in range(len(m1[0])):
                m5[i].append(m1[i][j] + m2[i][j] + m3[i][j] + m4[i][j]) #colocamos el resultado sumado de las 4 matrices en la matriz m5
        return m5
    else:
        return None

#comprobamos la suma y una mejor manera de mostrar la matriz resultante
resultado = sumaMatrices(a,b,c,d)
if resultado == None:
    print("Intentalo de nuevo")
else:
    for fila in resultado:
        print("[", end=" ")
        for elemento in fila:
            print(elemento, end=" ")
        print("]")