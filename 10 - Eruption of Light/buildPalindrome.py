# Given a string, 
# find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.

# Longest substring finder function at the end
def longestSubstringFinder(string1, string2):
    answer = ""

    # First string
    for i in range(len(string1)):
        match = ""
        last_i = 0
        # Second string
        for j in range(len(string2)):
            if (i + j < len(string1) and string1[i + j] == string2[j]):
                match += string2[j]
                last_i = i + j
            else:
                if (len(match) > len(answer) and last_i+1==len(string1)): answer = match
                match = ""
    return answer

# Solution function
def solution(st):

    # Reverse
    st_rev = st[::-1]

    # If st is palindrome
    if st_rev==st:
        return st

    # Find the longest substring finder function
    suf = longestSubstringFinder(st, st_rev)

    # Find the longest substring at the end
    import re
    pattern = '([a-z]+)'+suf
    m = re.search(pattern, st)
    return st+m.group(1)[::-1]






