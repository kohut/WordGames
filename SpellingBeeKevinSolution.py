import english_words
from english_words import english_words_lower_alpha_set

def SpellingBeeKCP(letters, key_letter):
    solutions = []
    for word in english_words_lower_alpha_set:
        if len(word) >= 4 and key_letter in word and letters >= set(word):
            solutions.append(word)
    return solutions

letters = frozenset('trkacdp')
key_letter = 't'

print(SpellingBeeKCP(letters, key_letter))
print(len(SpellingBeeKCP(letters, key_letter)))

