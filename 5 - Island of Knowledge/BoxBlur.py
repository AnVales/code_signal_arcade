# Last night you partied a little too hard. 
# Now there's a black and white photo of you that's about to go viral! 
# You can't let this ruin your reputation, so you want to apply the box blur algorithm to the photo to hide its content.

# The pixels in the input image are represented as integers. 
# The algorithm distorts the input image in the following way: 
# Every pixel x in the output image has a value equal to the average value of the pixel values from the 3 × 3 square that has its center at x, 
# including x itself. 
# All the pixels on the border of x are then removed.

# Return the blurred image as an integer, with the fractions rounded down.

def solution(image):         

    # Import 
    import math
    import numpy as np

    # Prepare final matrix
    row = len(image)
    col = len(image[0])
    final_dim = [row-3+1, col-3+1]
    solution = []

    # Obtain the promedy of 3*3 matrix inside the image
    for i in range(len(image)):
        for j in range(len(image[0])):
            if j+1<len(image[0]) and j+2<len(image[0]) and i+1<len(image) and i+2<len(image):

                promedy = math.floor((image[i][j] + image[i][j+1] + image[i][j+2] + image[i+1][j] + image[i+1][j+1] + image[i+1][j+2] + image[i+2][j] + image[i+2][j+1] + image[i+2][j+2])/9)
                solution.append(promedy)

    return (np.resize(solution,final_dim))
