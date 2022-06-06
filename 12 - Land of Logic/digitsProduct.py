# Given an integer product, 
# find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. 
# If there is no such integer, return -1 instead.

def solution(n):

    numeros = []

    # If the number is 0, as the result must me bigger than 0, the result is 10
    if n == 0:
        return (10)

    # If the number is bigger than 0 but less than 10, the result is the number itself    
    elif 0<n<10:
        return (n)

    # In another case, the number is divided by numbers less than 10 until it cannot be divided any more    
    else:
        for i in range(9,1,-1):
            while n%i==0:
                numeros.append(i)
                n = n / i

    # If it is a prime number or multiple of one, returns -1
    # If it is not a prime number, the divisors are returned from smallest to largest in a single value.

    multiplicacion = 1
    for i in numeros:
        multiplicacion = multiplicacion * i

    if 1 != int(n):
        return (-1)
    else:
        inv = numeros[::-1]
        return int("".join([str(elem) for elem in inv]))