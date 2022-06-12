# Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

# Solution function
def adjacentElementsProduct(inputArray):
    
    # Initialise variables
    max = - float("inf")
    ant = 0
    
    # Consecutive additions and return the greater
    for idx, i in enumerate(inputArray):
        
        if idx < 1:
            ant = i
            
        else:
            prod = ant * i
            
            if prod > max:
                max = prod
            
            ant = i
        
    return max