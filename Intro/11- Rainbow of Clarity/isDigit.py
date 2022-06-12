# Determine if the given character is a digit or not.

import re

def solution(symbol):
    return bool(re.match('[0-9]', symbol))
