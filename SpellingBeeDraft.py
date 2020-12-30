import english_words
from english_words import english_words_lower_alpha_set as all_words

def SpellingBee(letters, key_letter):
    #Empty array to hold all the solutions
    solutions = []

    #Dictionary of all the words
    #dictionary = open("/usr/share/dict/words", 'r')

    ## Loop through the dictionary
    for word in all_words:

    ## Make sure word is long enough and the key letter is in the word
        if len(word) >= 4 and key_letter in word:
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

solutions = SpellingBee('trkacdp', 't')
print(solutions)
print(len(solutions))



