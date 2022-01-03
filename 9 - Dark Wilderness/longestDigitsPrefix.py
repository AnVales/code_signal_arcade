# Given a string, output its longest prefix which contains only digits.

inputString = "123aa1"

import re

output = re.findall('\d*', inputString)

len= 0
index = 0
