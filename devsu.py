"""
En este ejercicio, tienes que analizar los registros de temperatura para encontrar el más cercano a cero
"""

"""
Implementa compute_closest_to_zero(ts), función que toma un arreglo de temperaturas ts y devuelve la temperatura más cercana a 0.
"""
"""
Restricciones:
Si el arreglo está vacío, tu función debe devolver 0
0 ≤ ts tamaño ≤ 10000
Si dos temperaturas son igualmente cercanas a cero, debe ser devuelta la temperatura positiva.
Por ejemplo, si la entrada es -5 y 5, entonces se debe devolver 5.
El resultado es correcto con un conjunto de datos simple: {7 5 9 1 4} -> 1
Problem solving
+70pts
Funciona cuando solo está el -273
Problem solving
+20pts
Funciona cuando solo está el 5526
Problem solving
+20pts
Funciona cuando la entrada contienen solo números negativos: {-15 -7 -9 -14 -12} -> -7
Problem solving
+35pts
Funciona con dos temperaturas negativas que sean iguales: {-10 -10} -> -10
Problem solving
+35pts
La solución muestra 0 si no hay temperatura
Problem solving
+35pts
Cuando dos temperaturas son iguales de cercanas a 0, entonces gana la positiva: {15 -7 9 14 7 12} -> 7
Problem solving
+85pts
"""
def compute_closest_to_zero(ts):
    if len(ts) == 0:
        return 0

    closest = 0

    for index in range(len(ts)):
        if closest == 0:
            closest = ts[index]
        elif ts[index] > 0 and ts[index] <= abs(closest):
            closest = ts[index]
        elif ts[index] < 0 and - ts[index] < abs(closest):
            closest = ts[index]
        index += 1
    return closest

items = [-7,45,7] # <- Aqui deberias probar todas las opciones del testing que solicitan
print(compute_closest_to_zero(items))