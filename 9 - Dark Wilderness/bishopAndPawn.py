# Given the positions of a white bishop and a black pawn on the standard chess board, 
# determine whether the bishop can capture the pawn in one move.

# The bishop has no restrictions in distance for each move, 
# but is limited to diagonal movement. 
# Check out the example below to see how it can move:

# Make the string input into lists function
def make_list(string):
    list = []
    [list.append(letter) for letter in string]
    return list

# Solution function
def solution(bishop, pawn):

    # Letter array
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    number_int = list(range(1,len(letter)+1))
    number_str = [str(d) for d in number_int]

    # Make the list with the input info
    bishopList = make_list(bishop)
    pawnList = make_list(pawn)

    # Find the index
    bishopListIndex = [letter.index(bishopList[0]), number_str.index(bishopList[1])]
    pawnListIndex = [letter.index(pawnList[0]), number_str.index(pawnList[1])]

    # Check
    if abs(bishopListIndex[0]-pawnListIndex[0]) == abs(bishopListIndex[1]-pawnListIndex[1]):
        return(True)
    else:
        return(False)
