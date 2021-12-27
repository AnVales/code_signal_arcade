# Recorrer el array dos veces
for word1_i in range(len(inputArray)):
    for word2_i in range(len(inputArray)):
        found_couple = []

        # Las palabras no son la misma
        if word1_i!=word2_i:
            # Miramos si difiere en 1 letra
            dif = 0
            for letter in range(len(inputArray[word1_i])):
                
                if inputArray[word1_i][letter] != inputArray[word2_i][letter]:
                    dif = dif + 1
                    

                if dif == 1 and letter == len(inputArray[word1_i]) - 1:
                    found_couple.append(inputArray[word1_i])
                    found_couple.append(inputArray[word2_i])

            print(found_couple)



def solution(inputArray):
    for i in inputArray:
        coupleArray = [i]
        respuesta = find_couple(i, inputArray, coupleArray)
        if respuesta:
            return respuesta
    return False