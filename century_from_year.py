# Given a year, return the century it is in. 
# The first century spans from the year 1 up to and including the year 100,
# the second - from the year 101 up to and including the year 200, etc.

def centuryFromYear(year):

    year_list = []
    century = 0

    for num in str(year):
        year_list.append(int(num))

    if 0 < len(year_list) <= 2:
        century = 1
        
    elif 2 < len(year_list) <= 3:
        if year_list[1] != 0 or year_list[2] != 0:
            century = year_list[0] + 1
        else:
            century = year_list[0]

    elif 3 < len(year_list) <= 4:
        if year_list[2] != 0 or year_list[3] != 0:
            century = year_list[0] * 10 + year_list[1] + 1
        else:
           century = year_list[0] * 10 + year_list[1]

    return century
