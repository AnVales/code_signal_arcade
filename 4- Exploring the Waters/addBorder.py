# Given a rectangular matrix of characters, add a border of asterisks(*) to it.

# Solution function
def solution(picture):

    # Initialise variables
    picture_complete = []
    border = ''

    # First and last rows with *
    for col in range(len(picture[0])+2):
        border = border + '*'

    picture_complete.append(border)

    # First and last columns with *
    for row in range(len(picture)):
        picture_complete.append("*"+picture[row]+"*")

    picture_complete.append(border)

    return picture_complete



