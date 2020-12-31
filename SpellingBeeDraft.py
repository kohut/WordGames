def SpellingBee(letters, key_letter):
    #Empty array to hold all the solutions
    solutions = []
    letters = frozenset(letters)

    # List of words
    f = open("scrabble_words.txt", "r")
    words = f.read().strip().split("\n")
    all_words = [word.lower().replace('\r', '') for word in words]
    f.close()

    ## Loop through the dictionary
    for word in all_words:
    ## Make sure word is long enough and the key letter is in the word
        if len(word) >= 4 and key_letter in word and letters >= set(word):
            solutions.append(word)
    ## Return the solution set

    solutions = sorted(solutions, key=len)
    return(solutions)

solutions = SpellingBee('xautcne', 'e')
print(solutions)
print(len(solutions))



