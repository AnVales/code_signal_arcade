lista = ['(perro)', '(gato)']
inputString = 'El (perro) y el (gato)'

import re

for i in lista:
    inputString = re.sub(i, i[1:-1][::-1], inputString)

print(inputString)