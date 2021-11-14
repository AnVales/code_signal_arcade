# Given two strings, find the number of common characters between them.

def solution(s1, s2):

    # Contar letras por string y guardar en diccionario
    def make_dict(string):
        dict = {}

        for letter in string:
            if letter not in dict.keys():
                dict[letter] = string.count(letter)

        return dict
        
    # Hacer el diccionario
    dict_s1 = make_dict(s1)
    dict_s2 = make_dict(s2)
    
    # Obtener letras en común
    common_letters = 0

    for key in dict_s1:
        if key in dict_s2.keys():
            if dict_s1[key] == dict_s2[key]:
                common_letters = common_letters + dict_s1[key]
            elif dict_s1[key] < dict_s2[key]:
                common_letters = common_letters + dict_s1[key]
            elif dict_s1[key] > dict_s2[key]:
                common_letters = common_letters + dict_s2[key]

    return common_letters
    