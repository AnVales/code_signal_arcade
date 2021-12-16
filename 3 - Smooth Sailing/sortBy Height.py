# Some people are standing in a row in a park. 
# There are trees between them which cannot be moved. 
# Your task is to rearrange the people by their heights in a non-descending order without moving the trees. 
# People can be very tall!

a = [-1, 150, 190, 170, -1, -1, 160, 180]

a_sorted = sorted(a)
a_sorted = [i for i in a_sorted if i != -1]
print(a_sorted)

a_final = []
counter = 0

for i in range(len(a)):
    if a[i] == -1:
        a_final.append(a[i])
        counter = counter - 1

    else:
        a_final.append(a_sorted[i+counter])

print(a_final)