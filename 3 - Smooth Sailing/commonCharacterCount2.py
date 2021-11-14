# Given two strings, find the number of common characters between them.

def solution(s1, s2):

    used_letters = []
    common_letters = 0

    for letter in s1:
        if letter in s2 and letter not in used_letters:
            used_letters.append(letter)
            if s1.count(letter) == s2.count(letter):
                common_letters = common_letters + s1.count(letter)
            elif s1.count(letter) < s2.count(letter):
                common_letters = common_letters + s1.count(letter)
            elif s1.count(letter) > s2.count(letter):
                common_letters = common_letters + s2.count(letter)

    return common_letters

