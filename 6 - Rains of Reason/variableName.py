# Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

# Check if the given string is a correct variable name.

def solution(name):

    # Make a list of characters
    name_list = []

    for chr in name:
        name_list.append(chr)

    # Search a pattern
    import re
    a = re.findall('[a-z]|[A-Z]', name)
    b = re.findall('[0-9]', name)
    c = re.findall('\_',name)

    # check if any character does not correspond to what is required
    if b:
        if name_list[0] == b[0]:
            return False

    for chr in name_list:

        if not chr in a and not chr in b and not chr in c:
            return False
        
    return True


    