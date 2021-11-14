# Ticket numbers usually consist of an even number of digits. 
# A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

# Given a ticket number n, determine if it's lucky or not.

def solution(n):
    first = 0
    second = 0

    n = str(n)

    for i in range(len(str(n))):
        if i > (len(str(n))-1)/2:
            first = first + int(n[i])
        elif i < (len(str(n))-1)/2:
            second = second + int(n[i])

    return first==second
    
