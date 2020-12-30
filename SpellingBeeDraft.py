import english_words
from english_words import english_words_lower_alpha_set as all_words

def SpellingBee(letters, key_letter):
    #Empty array to hold all the solutions
    solutions = []
    letters = frozenset(letters)
    ## Loop through the dictionary
    for word in all_words:
    ## Make sure word is long enough and the key letter is in the word
        if len(word) >= 4 and key_letter in word and letters >= set(word):
            solutions.append(word)
    ## Return the solution set
    return(solutions)

solutions = SpellingBee('trkacdp', 't')
print(solutions)
print(len(solutions))



