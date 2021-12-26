# Given a sequence of integers as an array, 
# determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

def almostIncreasingSequence(sequence):

    counter = 0
    
    # If sort
    if isSorted(sequence):
        return True
        
    # Add to counter
    for i in range(1,len(sequence)):
        if sequence[i]<=sequence[i-1]:
            counter = counter + 1
        if counter >= 2:
            return False
            
    
    # Check 
    if i-2 >= 0 and i+1 < len(sequence) and sequence[i] <= sequence[i-2] and sequence[i+1] <= sequence[i-1]:
        return False 
    return True
  
  
    # Sort function
def isSorted(sequence):
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            return False
    return True
        


    
