# An IP address is a numerical label assigned to each device (e.g., computer, printer) 
# participating in a computer network that uses the Internet Protocol for communication. 
# There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

# Given a string, find out if it satisfies the IPv4 address naming rules.

# IPv4 address:
# An identification number for devices connected to the internet. 
# An IPv4 addresses written in dotted quad notation consists of four 8-bit integers separated by periods.

# In other words, it's a string of four numbers each between 0 and 255 inclusive, with a "." character in between each number. 
# All numbers should be present without leading zeros.

def solution(inputString):

    # Regrex 
    import re
    pattern = '(\d+)\.(\d+)\.(\d+)\.(\d+)'
    pattern_0 = '0\d+'
    z = re.findall(pattern, inputString)

    # # Initialise variable
    fits = True 

    # Check address
    if re.fullmatch(pattern, inputString):
        z_list = list(z[0])
        for number in z_list:
            if int(number) < 0 or int(number) > 255 or re.fullmatch(pattern_0, number):
                fits = False

    else:
        fits = False

    return fits
