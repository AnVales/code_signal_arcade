# Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.

def solution(n):

    # Parameter initialization
    lst=[]
    n_del = 0

    # Search the lowest value and delete it
    for i in range(len(str(n))):
        
        if i!=len(str(n))-1:
            if str(n)[i] >= str(n)[i+1] or n_del != 0:
                lst.append(str(n)[i])

            else:
                n_del =+ 1

        elif i == len(str(n))-1 and n_del != 0:
            print(n_del)
            lst.append(str(n)[i])

    return int(''.join(lst))





