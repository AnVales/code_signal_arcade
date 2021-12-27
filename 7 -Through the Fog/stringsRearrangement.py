# Given an array of equal-length strings, 
# you'd like to know if it's possible to rearrange the order of the elements in such a way that 
# each consecutive pair of strings differ by exactly one character. Return true if it's possible, and false if not.

# Note: You're only rearranging the order of the strings, not the order of the letters within the strings!

inputArray = ["aba", "aab", "aaa"]

def find_couple(word, inputArray, coupleArray):
    # Comprobamos con cada palabra de la lista
    for possible_couple in inputArray:

        # Si la palabra no es la que estamos usando en la busqueda y no esta en la lista de parejas, a priori no hay diferencias
        if possible_couple!=word and possible_couple not in coupleArray:
            dif = 0
            for letter in range(len(word)):
                
                # Si las letras son diferentes, hay diferencias
                if possible_couple[letter]!=word[letter]:
                    dif = dif + 1
                    
                # Si la diferencia es 1 y ya hemos mirado todas las letras nos quedamos con esa palabra como pareja, volvemos a buscar
                if dif == 1 and letter == len(word) - 1:
                    coupleArray.append(possible_couple)
                    find_couple(possible_couple, inputArray, coupleArray)

                # Si al final de las busquedas no tenemos una diferencia de 1 letra, se inicializa coupleArray
                if dif != 1 and letter == len(word) - 1:
                    coupleArray = []

                # Si llevamos ya el mismo numero de strings en la original que en el emparejado pues ya estaria y se puede
                if len(coupleArray) == len(inputArray):
                    return True

# La funcion final que llama a la otra
def solution(inputArray):
    # Recorremos el array para meterlo en la funcion de buscar parejas
    for i in inputArray:
        coupleArray = [i]
        respuesta = find_couple(i, inputArray, coupleArray)
        # Si la respuesta es que se puede ordenar, true
        if respuesta:
            return respuesta
    # Si no devolvemos true, pues da false
    return False

print(solution(inputArray))