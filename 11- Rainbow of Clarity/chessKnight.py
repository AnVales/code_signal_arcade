# Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

# The knight can move to a square that is two squares horizontally and one square vertically, 
# or two squares vertically and one square horizontally away from it. 
# The complete move therefore looks like the letter L. 
# Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.

def solution(cell):

    # Column/ Row and change the letter to index
    lst = [ord(cell[0]) - 96, int(cell[1])]

    # Possible new positions
    mov_letter = [1,-1,1,-1,2,-2,2,-2]
    mov_number = [2,2,-2,-2,1,1,-1,-1]

    valid = 0
    for i in range(int(len(mov_letter))):
        if 0<lst[0]+mov_letter[i]<=8 and 0<lst[1]+mov_number[i]<=8:
            valid += 1
 
    return(valid)
