# Given a sorted array of integers a, your task is to determine which element of a is closest to all other values of a. 
# In other words, find the element x in a, which minimizes the following sum:

# abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)

# (where abs denotes the absolute value)

# If there are several possible answers, output the smallest one.

a = [2, 4, 7]


menor_suma_valor = float("inf")
menor_suma_x = 0

for restando in a:
    suma_i = 0

    for value in a:
        suma_i = suma_i + abs(value - restando)

    if menor_suma_valor > suma_i:
        menor_suma_valor = suma_i
        menor_suma_x = restando
print(menor_suma_x, menor_suma_valor)

