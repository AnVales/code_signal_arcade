# Given a string, your task is to replace each of its characters by the next one in the English alphabet; 
# i.e. replace a with b, replace b with c, etc (z would be replaced by a).

# Solution function
def solution(inputString):
    outputList = []

    # Alphabet list
    import string
    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)

    # Find the letter and replace with the next letter
    for letter in inputString:
        for index, alphabet in enumerate(alphabet_list):
            if letter == alphabet and index+1<len(alphabet_list):
                outputList.append(alphabet_list[index+1])
            elif letter == alphabet and not index+1<len(alphabet_list):
                outputList.append(alphabet_list[0])

    # Convert List to String Python
    outputString = ''.join(str(item) for item in outputList)

    return outputString



