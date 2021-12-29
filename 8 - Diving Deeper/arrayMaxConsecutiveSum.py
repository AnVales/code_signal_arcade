# Given array of integers, find the maximal possible sum of some of its k consecutive elements.

# Funcion suma
def add(num, add_i):
    return num + add_i

# Funcion suma los numeros 
def each_add(array, idx, k, add_i):
    add_i = add(array[idx], add_i)

    # Si aun no ha sumado todos los numeros, sigue sumando
    if k != 0:
        k = k - 1
        idx = idx - 1
        add_i = each_add(array, idx, k, add_i)

    return add_i

# Funcion solucion, da la mayor suma de un numero de numeros k consecutivos de un array 
def solution(inputArray, k):
    max_ad = -float('inf')

    # Recorre el array desde el indice k-1
    for idx in range(k-1, len(inputArray)):
        # La suma de cada conjunto inicial
        add_i = 0
        # La suma de cada conjunto final
        add_i = each_add(inputArray, idx, k-1, add_i)
        print(add_i)
       
        # Si la nueva suma es mayor que la mayor suma anterior, reemplaza
        if max_ad < add_i:
            max_ad = add_i

    return max_ad
