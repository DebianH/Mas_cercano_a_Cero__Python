"""
En este ejercicio nos pide crear una funcion que solo permita un maximo de 2 digitos
es decir 110 | 33222 son VALIDOS pero 567 NO ES VALIDO es porque tiene tres diferentes digitos
"""

def duoDigitos(numero):

    #nu = list(map(int, str(numero))) #convert number to list
    #nu = [int(x) for x in str(numero)] #otra forma de convertir numero a lista
    nu =[]
    for h in str(numero):
        if h == "-":
            #nu.append(h) agregamos el elemento y luego lo eliminamos NO tiene sentido mejor utilizamos un pass
            #nu.remove(h) asi controlamos los numero negativos
            pass
        else:
            nu.append(h)

    new = dict(zip(nu,map(lambda x: nu.count(x),nu))) #contar cuantas veces se repite un numero
    print(new)

    if len(new) > 2:
        print("n")
    else:
        print("y")


#Test
duoDigitos(11110)
duoDigitos(567)
duoDigitos(-227)