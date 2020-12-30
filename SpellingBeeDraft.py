
def SpellingBee(letters, key_letter):
    #Empty array to hold all the solutions
    solutions = []

    #Dictionary of all the words
    dictionary = open("/usr/share/dict/words", 'r')

    ## Loop through the dictionary
    for word in dictionary:

    ## Make sure the word has length >= 4
        if len(word) > 4:
            word = word.strip('\n')

    ## Make sure the key letter is in the word
        if key_letter in word:
        #Make sure each letter of the word is in the set "letters"
            # Assume the word is good
            letter_flag = True
            for letter in word:
                if letter not in letters:
                    # The word is not good
                    letter_flag = False
            #After looping through every letter, check flag
            if letter_flag:
                ## Append to the solution set
                solutions.append(word)

    ## Return the solution set
    return(solutions)

solutions = SpellingBee('acghlne', 'e')
print(solutions)
print(len(solutions))



