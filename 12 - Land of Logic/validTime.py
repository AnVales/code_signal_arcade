# Check if the given string is a correct time representation of the 24-hour clock.

import re

def solution(time):

    times = re.findall(r'[0-9]+', time)
    
    if not 0<=int(times[0])<=23 or not 0<=int(times[1])<60:
        return False
    
    return True
