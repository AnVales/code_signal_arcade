# Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

def adjacentElementsProduct(inputArray):
    
    max = - float("inf")
    ant = 0
    
    for idx, i in enumerate(inputArray):
        
        if idx < 1:
            ant = i
            
        else:
            prod = ant * i
            
            if prod > max:
                max = prod
            
            ant = i
        
    return max