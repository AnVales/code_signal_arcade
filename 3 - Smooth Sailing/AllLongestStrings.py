# Given an array of strings, return another array containing all of its longest strings.

# Solution function
def allLongestStrings(inputArray):

    # Initialise variable
    prev_word_count = - float("inf")

    # Chech the length of each word, save the word if its longer than the perv or has the same length
    for word in inputArray:

        if len(word) > prev_word_count:
            outputArray = []
            outputArray.append(word)
            prev_word_count = len(word)

        elif len(word) == prev_word_count:
            outputArray.append(word)

    return outputArray


