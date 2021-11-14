# Given an array of strings, return another array containing all of its longest strings.

inputArray = ['aba', 'aa', 'aba']

def allLongestStrings(inputArray):

    prev_word_count = - float("inf")

    for word in inputArray:

        if len(word) > prev_word_count:
            outputArray = []
            outputArray.append(word)
            prev_word_count = len(word)

        elif len(word) == prev_word_count:
            outputArray.append(word)

    return outputArray

print(allLongestStrings(inputArray))

