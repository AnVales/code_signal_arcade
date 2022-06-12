# Given an array of equal-length strings, 
# you'd like to know if it's possible to rearrange the order of the elements in such a way that 
# each consecutive pair of strings differ by exactly one character. Return true if it's possible, and false if not.

# Note: You're only rearranging the order of the strings, not the order of the letters within the strings!

# Find couple function  
def find_couple(word, inputArray, coupleArray):
    # Check with all the words in the list
    for possible_couple in inputArray:

        # There is no diff
        # If the word is not the one that we are searching and is not in the couple list
        if possible_couple!=word and possible_couple not in coupleArray:
            dif = 0
            for letter in range(len(word)):
                
                # There is a diff if a letter is diff
                if possible_couple[letter]!=word[letter]:
                    dif = dif + 1
                    
                # If the diff is 1 and we have check all the letters, this word is a couple, lets search again
                if dif == 1 and letter == len(word) - 1:
                    coupleArray.append(possible_couple)
                    find_couple(possible_couple, inputArray, coupleArray)

                # If at the end of the searchs we dont have a one letter different, coupleArray is initialise
                if dif != 1 and letter == len(word) - 1:
                    coupleArray = []

                # If we have the same number of str in the original and in the couple array, its possible
                if len(coupleArray) == len(inputArray):
                    return True

# Solution function
def solution(inputArray):
    # We traverse the array to put it into the match function
    for i in inputArray:
        coupleArray = [i]
        respuesta = find_couple(i, inputArray, coupleArray)
        # If the answer can be ordered, true
        if respuesta:
            return respuesta

    return False

