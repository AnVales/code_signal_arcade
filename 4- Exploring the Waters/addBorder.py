# Given a rectangular matrix of characters, add a border of asterisks(*) to it.

def solution(picture):
    picture_complete = []
    border = ''

    for col in range(len(picture[0])+2):
        border = border + '*'

    picture_complete.append(border)

    for row in range(len(picture)):
        picture_complete.append("*"+picture[row]+"*")

    picture_complete.append(border)

    return picture_complete



