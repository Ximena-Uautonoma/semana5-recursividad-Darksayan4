"""
Ejercicio 1: Dado un número entero positivo N, retornar una lista con los números desde 1 hasta N.

Debe implementar dos funciones:
1. Una usando iteración (for o while)
2. Una usando recursividad
"""

def contar_ciclo(n):
    """
    Retorna una lista con los números desde 1 hasta n usando iteración.
    """
    numeros=[]
    for i in range(1,n+1):
        numeros.append(i)
    return numeros:
    print (contar_ciclo(4))


def contar_recursivo(n):
    """
    Retorna una lista con los números desde 1 hasta n usando recursividad.
    """
    if n == 1:
        return [1]
    else:
        return contar_recursivo(n-1)+[n] 
        #se crea una lista nueva para ir guardando los numeros en orden despues de que se cumple el if 
    print (contar_recursivo(4))
    #Preguntar a la profe como ejecutar el programa desde github
