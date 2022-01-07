# Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. 
# Since he likes to make things perfect, 
# he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. 
# He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

# Solution function
def makeArrayConsecutive2(statues):

    # Initialise variables and sort numbers
    statues.sort()
    statues_diff = []

    # Find the values missing
    for index, value in enumerate(statues):

        if index == 0:
            prev = value
    
        else: 
            statues_diff.append(value - prev)
            prev = value
        
    return sum(statues_diff) - len(statues_diff)
