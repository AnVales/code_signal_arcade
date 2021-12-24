# Check if all digits of the given integer are even.

# def solution(n):

n = 642386
even = True

for digit in str(n):
    if  not int(digit) % 2 == 0:
        even = False

print(even)