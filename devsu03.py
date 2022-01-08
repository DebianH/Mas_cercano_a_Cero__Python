"""
En este ejercicio nos pide que de un numero encontremos los multiplos que contiene y luego estos los sumemos
Los multiplos son 3 - 5 - 7
"""

def computing_digitos(n):
    c=0
    li = []
    for i in range(1,n+1):
        if i%3==0 or i%5==0 or i%7==0:
            li.append(i)
            c+=1
    print(li) # imprime los multiplos
    return sum(li) # suma los todos los multiplos que contiene n

print(computing_digitos(66)) # <- Test