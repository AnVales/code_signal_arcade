# Given a string, return its encoding defined as follows:

# First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
# for example, "aabbbc" is divided into ["aa", "bbb", "c"]

# Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
# for example, substring "bbb" is replaced by "3b"
# Finally, all the new strings are concatenated together in the same order and a new string is returned.

s = "abbcabb"

def solution(s):
    # Parameter initialization
    counter = 1
    final_list = []

    # Check if the previous and the current one are the same
    for i in range(len(s)):

        # There is no previuos
        if i == 0:
            prev_letter = s[i]
        
        else:
            # Same
            if prev_letter == s[i]:
                counter = counter + 1
                if i == len(s)-1:
                    final_list.append(str(counter))
                    final_list.append(prev_letter)

            # Different
            elif prev_letter != s[i]:

                # Almost two were the same
                if counter != 1:
                    final_list.append(str(counter))
                    counter = 1

                final_list.append(prev_letter)
                prev_letter = s[i]

                # The last letter is different
                if i == len(s)-1:
                    final_list.append(prev_letter)

    return("".join(final_list))

print(solution(s))