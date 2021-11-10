# Given a sequence of integers as an array, 
# determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

array_1 = [1, 2, 1, 2]

def almostIncreasingSequence(sequence):

    counter = 0
    for idx, val in enumerate(sequence):

        if idx == 0:
            prev = val

        else:
            if val > prev:
                prev = val

            else:
                counter = counter + 1
                print('counter', counter)
                print('val', val)
                prev = val

        if counter > 1:
            return False

        elif counter <= 1 and idx == len(sequence) - 1:
            return True

try_1 = almostIncreasingSequence(array_1)
print(try_1)

    