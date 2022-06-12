# You are given an array of desired filenames in the order of their creation. 
# Since two files cannot have equal names, 
# the one which comes later will have an addition to its name in a form of (k), 
# where k is the smallest positive integer such that the obtained name is not used yet.

# Return an array of names that will be given to the files.

def solution(names):

    # Initialize 
    names_final = []

    # Go through the initial list
    # If there is no identical one on the final list, it adds it
    for name in names:
        if not name in names_final: 
            names_final.append(name)

        # If it is already there, we look for the following: name(frec)
        # Frec = 1
        # As long as there is a match, adds 1 to the frequency
        # When there are no more matches, it appends it with the final frequency
        else:
            n = 1
            while "{0}({1})".format(name, n) in names_final:
                n = n + 1

            names_final.append(name+"("+str(n)+")")

    return (names_final)

