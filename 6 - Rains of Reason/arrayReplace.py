# Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.

# Solution function
def solution(inputArray, elemToReplace, substitutionElem):

    # If the elem is in inputArray, replace
    output_array = []

    for i in inputArray:
        if not i == elemToReplace:
            output_array.append(i)
        else:
            output_array.append(substitutionElem)

    return output_array

