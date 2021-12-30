# Given array of integers, find the maximal possible sum of some of its k consecutive elements.

def solution(inputArray, k):
    # Sumamos el primer conjunto
    add_i = 0
    for i in range(k):
        add_i = add_i + inputArray[i]

    # Solo guardamos el mayor numero
    max_val = add_i

    # Ahora vamos a sumar el siguiente y restar el anterior
    for i in range(len(inputArray)-k):
        add_i = - inputArray[i] + add_i + inputArray[i+k]

        if max_val < add_i:
            max_val = add_i

    return max_val
    