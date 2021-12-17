# Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

# Given two arrays a and b, check whether they are similar.

def solution(a, b):
    
    not_eq_num = 0
    not_eq_idx = []

    # Si son iguales
    if a==b:
        return True

    # Vemos cuantos ha diferentes
    else:
        for idx, val in enumerate(a):
            if not val == b[idx]:
                not_eq_num = not_eq_num + 1
                not_eq_idx.append(idx)
                
                # Si son mas de dos: no
                if not_eq_num > 2: 
                    return False
        
        # Si son dos y se pueden cambiar: si, sino: no
        if not_eq_num == 2 and a[not_eq_idx[0]]==b[not_eq_idx[1]] and a[not_eq_idx[1]]==b[not_eq_idx[0]]:
            return True
        else:
            return False

